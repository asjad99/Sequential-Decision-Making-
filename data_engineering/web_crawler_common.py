import httplib2
from logging import info, basicConfig, DEBUG
from urllib2 import HTTPError, urlopen
import urllib2
from urlparse import urlparse
from lxml.html import parse, fromstring, tostring
import Queue
import json
import sys
import logging
from datetime import datetime
import os
import errno

CATEGORIES_MISMATCH = "SwlException - Mismatch in number of categories"

class IndexableQueue(Queue.Queue):
  def __getitem__(self, index):
    with self.mutex:
      return self.queue[index]

class SWLLogger:

    LEVELS = { 'debug':logging.DEBUG,
      'info':logging.INFO,
      'warning':logging.WARNING,
      'error':logging.ERROR,
      'critical':logging.CRITICAL,
      }
    
    def __init__(self, 
                 _logger_name='defaultLogger', 
                 _console_level='debug', 
                 _log_to_disk=False, 
                 _disk_level='critical', 
                 _file_location='log/' + datetime.now().strftime('crawl.%m.%d.%Y.log'),
                 _console_formatter='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                 _disk_formatter='%(asctime)s %(name)-12s %(levelname)-8s %(message)s'):
    
      self.logger = logging.getLogger(_logger_name)
      self.logger.setLevel(logging.DEBUG)
        
      if _console_level != None:  
        self.console_level = self.LEVELS.get(_console_level, logging.NOTSET)
        ch = logging.StreamHandler()
        ch.setLevel(self.console_level)
        chf = logging.Formatter(_console_formatter)
        ch.setFormatter(chf)
        self.logger.addHandler(ch)
        
      if _disk_level != None and _log_to_disk == True:
        file_level = self.LEVELS.get(_disk_level, logging.NOTSET)
        fh = logging.FileHandler(_file_location, mode='a')
        fh.setLevel(file_level)
        fhf = logging.Formatter()
        fh.setFormatter(fhf)
        self.logger.addHandler(fh) 
    
    def logdebug(self, msg):
      self.logger.debug (msg)
    
    def loginfo(self, msg):
      self.logger.info (msg)
    
    def logwarn(self, msg):
      self.logger.warn (msg)
    
    def logerror(self, msg):
      self.logger.error (msg)

    def logcritical(self, msg):
      self.logger.critical (msg)  
    
class StatsManager:

  def __init__(self, name):
    now_category = 0
    category_count = 0
    current_page = 0
    total_pages = 0

  def SetLatestStats(self, _now_category, _category_count, _current_page, _total_pages):
    self.now_category = _now_category
    self.category_count = _category_count
    self.current_page = _current_page
    self.total_pages = _total_pages
  
  def PrintLatestStats(self):
    return "Category " + str(self.now_category) + "/" + str(self.category_count) + " : Page " + str(self.current_page) + "/" + str(self.total_pages)

  def GetCurrentPage(self):
    return self.current_page

class DiskIOManager:
  
  @staticmethod
  def DumpThisItem(data):
    print json.dumps(data) 
    sys.stdout.write(",")
  
      
class NetworkIOManager:

  h2 = httplib2.Http()
  
  @staticmethod  
  def cleanURL(self, serverRoot, url):
    o = urlparse(url)
   
    netloc = "?"
    scheme = "http"
    
    if o.netloc == "":
      netloc = serverRoot
    else:
      netloc = o.netloc
    
    if o.scheme == "":
      scheme = "http"
    
    clean_url = scheme + "://" + netloc + o.path
    return clean_url
  
  def itExists(self, url):
    #debug ("CONFIRMING")
    res = self.h2.request(url, 'HEAD')
    #debug (res[0].status)
    if res[0].status == 200:
      return True
    else:
      return False
 
  @staticmethod
  def itExists2(url):
    try:
      res = urlopen(url)
      return True
    except urllib2.URLError, e:
      return False 
 
  @staticmethod
  def completeURL(server_root, path):
    if server_root != None:
      if path.find("../") != -1:
        path = path[2:]
        info ("path = " + path)
        #raise SystemExit
      return server_root + path
    else:
      return path
  
  @staticmethod  
  def read_link(link, server_root=None):
    try:
      info ("read_link - link = " + link)
      #raise SystemExit
      url_parsed = urlparse(link)
      url = ""
      if url_parsed.netloc == "":
        url = NetworkIOManager.completeURL(server_root, link)
      else:
        url = link
      
      info ("------------------------")
      info ("read url = " + url)
      return parse(urlopen(url)).getroot()
      #b = br.open(url)
      #return fromstring(b)
      #return parse(url).getroot()
      
      #response = br.open(link)
      #body = response.read()
      #print(body)
      #raise SystemExit
      #return fromstring(body)
      
    except (HTTPError, IOError) as e:
      #info ("Caught " + str(e.code) + " for url = " + url)
      #print ("read_link - " + str(e))
      #print "read_link - " + str(e.status))
      return None
      
class CommonConfig:
   
  categoriesQ = IndexableQueue()
  itemsQ = Queue.Queue()
  nwio = NetworkIOManager
  
  nwio = NetworkIOManager()
  sm = StatsManager("")
  
  #these should bhere - not sure of best way to do it
  #def __init__(self):
    
      
class SwlException(Exception):
    pass