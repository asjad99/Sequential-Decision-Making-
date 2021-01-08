#-----------------------------------------
import mechanize
from lxml.cssselect import CSSSelector
import httplib2
import sys
import Queue

#import common
#reload(common)
from common import crawlerCommon
import itertools
import argparse

#----------------------------------------------------------------------------------
# Crawler config params for Anneklein

class AnnekleinConfig:

    brand_name = "Anne Klein"

    def __init__(self, _sale):
        self.swl = crawlerCommon.SWLLogger('anneklein', 'debug', True, 'info')
        self.sale_items_only = _sale


    categoriesQ = crawlerCommon.IndexableQueue()
    itemsQ = Queue.Queue()
  
    nwio = crawlerCommon.NetworkIOManager()
    sm = crawlerCommon.StatsManager("")


    ############################
    #FetchCategories
    ############################
    
    def FetchCategories(self, page_url, mapping_list, css_selector, sex):

        self.swl.logdebug("FetchCategories - Entered function")
        self.swl.loginfo("reading " + page_url)
        h = crawlerCommon.NetworkIOManager.read_link(page_url, None)

        anchor_tags_in_submenu = css_selector(h) 
        self.swl.loginfo("item count = " + str(len(anchor_tags_in_submenu)))
        anchors_list = []
        
        for item in anchor_tags_in_submenu:
            self.swl.loginfo("item = " + str(item))
            if isinstance(item.text, str):
                self.swl.loginfo(item.text.strip().rstrip())
                anchor_text = item.text_content().strip().rstrip()
                anchor_url = item.get("href")
                anchors_list.append({"anchor_text":anchor_text, 
                                     "anchor_url": anchor_url})

            
        self.swl.logdebug("len(anchors_list) = " + str(len(anchors_list)))
        for anchor in anchors_list:
            self.swl.logdebug(anchor["anchor_text"])

        found_items_counter = 0;
        list_items_found = []
        
        for anchor in anchors_list:    
            for k, v in mapping_list.iteritems():
                titles_only = []

                for entry in v:
                    titles_only.append(entry["title"])
                       
                if anchor["anchor_text"] in titles_only:
                    subcategory = ""

                    for entry in v:
                        if entry["title"] == anchor["anchor_text"]:
                            subcategory = entry["subcategory"]
                            
                    self.swl.loginfo("Found *" + k + "* for " + anchor["anchor_text"])
                
                    self.categoriesQ.put({"sex":sex,
                       "category_url": anchor["anchor_url"],
                       "category_title":k,
                       "subcategory": subcategory
                      })

                    list_items_found.append(anchor["anchor_text"])
                    found_items_counter += 1
                    self.swl.loginfo(found_items_counter)

        total_items_to_find = 0
        list_items_to_find = []
        
        for k, v in mapping_list.iteritems():
            total_items_to_find += len(v)
            list_items_to_find.append(v)

        list_items_to_find = list(itertools.chain(*list_items_to_find))  
        self.swl.loginfo("Found " + str(found_items_counter) + "/" + str(total_items_to_find) + " items")

        if (found_items_counter != total_items_to_find):
            self.swl.logcritical("Category items missing") 
            raise crawlerCommon.SwlException(crawlerCommon.CATEGORIES_MISMATCH)
    
        self.swl.loginfo("") #newline

    
    #women only here
    category_pages_women = []

    #Menu : Main categies that dont have any subcategories
    women_category_mapping1 = {
                            "Tops": (),
                                          
                            "Bottoms": (),
                            
                            "Outerwear": ({"title" : "Jackets & Outerwear",
                                           "subcategory" : ""},),
    
                            "Footwear": (),
                            
                            "Accessories":(),
                            
                            "Other": ({"title" : "New Arrivals",
                                       "subcategory" : ""},
                                      {"title" : "Leo Legacy",
                                       "subcategory" : ""},
                                       {"title" : "Suiting",
                                        "subcategory" : ""},)
                                                                
                          }
  
  
    category_pages_women.append({
                "mapping": women_category_mapping1,
                "page_url":"http://www.anneklein.com/Dresses/90263425,default,sc.html",
                "css_selector":CSSSelector("div #navlist li a"),
                "listing_type":"regular"
              })


    #Menu : Shoes
    women_category_mapping2 = {
                            "Tops": (),
                                          
                            "Bottoms": (),
                            
                            "Outerwear": (),
    
                            "Footwear": ({"title" : "New Arrivals",
                                          "subcategory" : "shoes"},
                                         {"title" : "Pumps & Heels",
                                          "subcategory" : "shoes"},
                                         {"title" : "Sandals",
                                          "subcategory" : "shoes"},
                                         {"title" : "Flats",
                                          "subcategory" : "shoes"}),
                            
                            "Accessories":(),
                            
                            "Other": ()
                                                                
                          }
  
  
    category_pages_women.append({
                "mapping": women_category_mapping2,
                "page_url":"http://www.anneklein.com/womens-shoes/90263428,default,sc.html",
                "css_selector":CSSSelector("li.other ul li a"),
                "listing_type":"regular"
              })


    #Menu : Handbags
    women_category_mapping3 = {
                            "Tops": (),
                                          
                            "Bottoms": (),
                            
                            "Outerwear": (),
    
                            "Footwear": (),
                            
                            "Accessories":({"title" : "Satchels",
                                            "subcategory" : "handbags"},
                                           {"title" : "Totes",
                                            "subcategory" : "handbags"},
                                           {"title" : "Shoulder",
                                            "subcategory" : "handbags"},
                                           {"title" : "Cosmetic Cases",
                                            "subcategory" : "handbags"},
                                           {"title" : "Wallets",
                                            "subcategory" : "handbags"}),
                            
                            "Other": ()
                                                                
                          }
  
  
    category_pages_women.append({
                "mapping": women_category_mapping3,
                "page_url":"http://www.anneklein.com/Handbags/90263432,default,sc.html",
                "css_selector":CSSSelector("li.other ul li a"),
                "listing_type":"regular"
              })
    

    #Menu : Watches
    women_category_mapping4 = {
                            "Tops": (),
                                          
                            "Bottoms": (),
                            
                            "Outerwear": (),
    
                            "Footwear": (),
                            
                            "Accessories":({"title" : "Leather",
                                            "subcategory" : "watch"},
                                           {"title" : "Color",
                                            "subcategory" : "watch"},
                                           {"title" : "Ceramic",
                                            "subcategory" : "watch"},
                                           {"title" : "Metals",
                                            "subcategory" : "watch"},
                                           {"title" : "Diamonds & Crystals",
                                            "subcategory" : "watch"},
                                           {"title" : "Tortoise & Horn",
                                            "subcategory" : "watch"},
                                           ),
                            
                            "Other": ()
                                                                
                          }
  
  
    category_pages_women.append({
                "mapping": women_category_mapping4,
                "page_url":"http://www.anneklein.com/womens-watches/90263431,default,sc.html",
                "css_selector":CSSSelector("li.other ul li a"),
                "listing_type":"regular"
              })

    
    #Menu : Jewelry
    women_category_mapping5 = {
                            "Tops": (),
                                          
                            "Bottoms": (),
                            
                            "Outerwear": (),
    
                            "Footwear": (),
                            
                            "Accessories":({"title" : "Bracelets",
                                            "subcategory" : "jewelry"},
                                           {"title" : "Necklaces",
                                            "subcategory" : "jewelry"},
                                           {"title" : "Earrings",
                                            "subcategory" : "jewelry"}),
                            
                            "Other": ()
                                                                
                          }
  
  
    category_pages_women.append({
                "mapping": women_category_mapping5,
                "page_url":"http://www.anneklein.com/Jewelry/90263434,default,sc.html",
                "css_selector":CSSSelector("li.other ul li a"),
                "listing_type":"regular"
              })


    #Menu : Dresses
    women_category_mapping6 = {
                            "Tops": (),
                                          
                            "Bottoms": (),
                            
                            "Outerwear": (),
    
                            "Footwear": (),
                            
                            "Accessories":(),
                            
                            "Other": ({"title" : "Work",
                                       "subcategory" : "dresses"},
                                      {"title" : "Casual",
                                       "subcategory" : "dresses"},
                                      {"title" : "Evening",
                                       "subcategory" : "dresses"})
                                                                
                          }
  
  
    category_pages_women.append({
                "mapping": women_category_mapping6,
                "page_url":"http://www.anneklein.com/Dresses/90263425,default,sc.html",
                "css_selector":CSSSelector("li.other ul li a"),
                "listing_type":"regular"
              })


    #Menu : Tops
    women_category_mapping7 = {
                            "Tops": ({"title" : "Blouses & Shirts",
                                       "subcategory" : "tops"},
                                     {"title" : "Knits & Tees",
                                       "subcategory" : "tops"},
                                     {"title" : "Sweaters",
                                       "subcategory" : "tops"}),
                                          
                            "Bottoms": (),
                            
                            "Outerwear": (),
    
                            "Footwear": (),
                            
                            "Accessories":(),
                            
                            "Other": ()
                                                                
                          }
  
  
    category_pages_women.append({
                "mapping": women_category_mapping7,
                "page_url":"http://www.anneklein.com/Tops/90263441,default,sc.html",
                "css_selector":CSSSelector("li.other ul li a"),
                "listing_type":"regular"
              })


    #Menu : Bottoms
    women_category_mapping8 = {
                            "Tops": (),
                                          
                            "Bottoms": ({"title" : "Pants",
                                         "subcategory" : ""},
                                        {"title" : "Jeans",
                                         "subcategory" : ""},
                                        {"title" : "Skirts",
                                         "subcategory" : ""}),
                            
                            "Outerwear": (),
    
                            "Footwear": (),
                            
                            "Accessories":(),
                            
                            "Other": ()
                                                                
                          }
  
  
    category_pages_women.append({
                "mapping": women_category_mapping8,
                "page_url":"http://www.anneklein.com/Bottoms/90263442,default,sc.html",
                "css_selector":CSSSelector("li.other ul li a"),
                "listing_type":"regular"
              })

    
    #Menu : Sale
    women_category_mapping9 = {
                            "Tops": ({"title" : "Tops",
                                      "subcategory" : ""},
                                     ),
                                          
                            "Bottoms": ({"title" : "Bottoms",
                                         "subcategory" : ""},),
                            
                            "Outerwear": ({"title" : "Jackets & Blazers",
                                           "subcategory" : ""},
                                          {"title" : "Outerwear",
                                           "subcategory" : ""},
                                          ),
    
                            "Footwear": ({"title" : "Shoes",
                                          "subcategory" : ""},),
                            
                            "Accessories":({"title" : "Jewelry",
                                            "subcategory" : ""},
                                           {"title" : "Handbags",
                                            "subcategory" : ""},),
                            
                            "Other": ({"title" : "Dresses",
                                       "subcategory" : ""},
                                      {"title" : "Suiting",
                                       "subcategory" : ""},)
                                                                
                          }
  
  
    category_pages_women.append({
                "mapping": women_category_mapping9,
                "page_url":"http://www.anneklein.com/Sale/90275671,default,sc.html",
                "css_selector":CSSSelector("li.other ul li a"),
                "listing_type":"sale"
              })

    
    server_root = "http://www.anneklein.com"
    swllist = {
    "root": {"title":"Anneklein",
             "url": server_root
             },
    "sex":[
            {"title":"women", 
            "categories":category_pages_women
            }
            ]
      }


    ############################
    #fetchItemsQueue
    ############################
 
    css_selector_string_for_item_box = CSSSelector("div.contentProduct")
    def fetchItemsQueue(self, h):
        if h == None:
            return None
        
        return self.css_selector_string_for_item_box(h)


    ############################
    #findNextPageURL
    ############################

    def findNextPageURL(self, h, page_num):
        return None


    ############################
    #findTotalPages
    ############################
    
    def findTotalPages(self, h):
        return 1


    ############################
    #fetchItemURL
    ############################
    
    css_selector_string_for_item_url = CSSSelector("a")
    def fetchItemURL(self, h):
        if h == None:
            return None
        
        temp = self.css_selector_string_for_item_url(h)
        server_root = "anneklein.com"   #Don't write 'http://' here; its appended in cleanURL
        
        if len(temp) == 0:
            return "?"
        else:    
            item_url = self.nwio.cleanURL(self, server_root, temp[0].get("href"))
      
        return item_url


    ############################
    #fetchItemImageURL
    ############################

    css_selector_string_for_item_image_url = CSSSelector("meta[property='og:image']")
    def fetchItemImageURL(self, h):
        if h == None:
            return None
        
        image_url = "?"
        temp = self.css_selector_string_for_item_image_url(h)
        server_root = "www.katespade.com"  #Don't write 'http://' here; its appended in cleanURL
        
        if len(temp) > 0:
            image_url = self.nwio.cleanURL(self, server_root, temp[0].get("content"))
            
        return image_url


    ############################
    #fetchItemTitle
    ############################

    css_selector_string_for_item_title = CSSSelector("h1.pNameHOne")
    def fetchItemTitle(self, h):
        if h == None:
            return None
        
        temp = self.css_selector_string_for_item_title(h)

        if len(temp) == 0:
            return "?"
        else:
            return temp[0].text.strip()



    ############################
    #fetchItemPrice
    ############################

    css_selector_string_for_item_regular_price = CSSSelector("span.productListPrice.noSalePrices")  
    css_selector_string_for_item_regular_onSale_previous = CSSSelector("span.productSalePrice.SalePrices")
    css_selector_string_for_item_regular_onSale_current = CSSSelector("span.productListPrice.SalePrices.ListSalePrices")

    def fetchItemPrice(self, h):
        item_price = ""
        item_sale_price = ""
        price_array = []

        _item_regular_price = self.css_selector_string_for_item_regular_price(h)
        _item_regular_price_onsale_prev = self.css_selector_string_for_item_regular_onSale_previous(h)
        _item_regular_price_onsale_current = self.css_selector_string_for_item_regular_onSale_current(h)
        if _item_regular_price != None and len(_item_regular_price) > 0: 
            price_array.append(_item_regular_price[0].text.strip().lstrip()) 
        elif _item_regular_price_onsale_prev != None and len(_item_regular_price_onsale_prev) > 0: 
            price_reg = _item_regular_price_onsale_prev[0].text.strip().lstrip()
            price_reg = price_reg.split(" ")
            price_array.append(price_reg[1])
        else:
            price_array.append("N/A") 
        if _item_regular_price_onsale_current != None and len(_item_regular_price_onsale_current) > 0: 
            price_sale = _item_regular_price_onsale_current[0].text.strip().lstrip()
            price_sale = price_sale.split(" ")
            price_array.append(price_sale[1])

        if len(price_array) > 1:
            item_price = price_array[1]
            item_sale_price = price_array[0]
        else: 
            item_price = price_array[0]

          
        return {"price" : item_price , "sale_price" : item_sale_price}


    ############################
    #fetchItemDetails
    ############################

    css_selector_string_for_item_details1 = CSSSelector("div #descriptionHolder")
    def fetchItemDetails(self, h):
        if h == None:
            return None
        
        item_details = ""
        temp1 = self.css_selector_string_for_item_details1(h)
    
        if len(temp1) > 0:
            item_details = temp1[0].text_content().strip().replace("\n\n\n", " ")
            
        return item_details


    ############################
    #fetchItemInfo
    ############################
    
    def fetchItemInfo(self, item_box):
        
        item_url = self.fetchItemURL(item_box)
        self.swl.loginfo("item_url = " + item_url)

        if item_url == None:
            self.swl.logwarn("ITEM MISSING, SKIPPING")
            return None

        h = self.nwio.read_link(item_url)
        item_image_url = self.fetchItemImageURL(h)
        item_title = self.fetchItemTitle(h)
        item_price_dict = self.fetchItemPrice(item_box) #Note: Passing item_box so that price is read from product's listing page and not details' page
        item_details = self.fetchItemDetails(h)
        brand = self.brand_name

        item = {"item_url":item_url,
                "image_url" : item_image_url,
                "title" : item_title,
                "price" : item_price_dict["price"],
                "sale_price" : item_price_dict["sale_price"],
                "brand" : brand,
                "details" : item_details}

        return item


    ############################
    #PopulateItemsList
    ############################

    def PopulateItemsList(self, items_boxes_list, current_sex, current_category, subcategory):
        self.swl.loginfo("Items found on this page = " + str(len(items_boxes_list)))
    
        item_counter = 0
        total_items = str(len(items_boxes_list))
        for item_box in items_boxes_list:

            self.swl.loginfo(self.sm.PrintLatestStats())
            info_dict = self.fetchItemInfo(item_box)
      
            if info_dict == None:
                continue
      
            item = {"url" : info_dict["item_url"],
                    "image" : info_dict["image_url"],
                    "title" : info_dict["title"],
                    "subcategory": subcategory,
                    "price" : info_dict["price"],
                    "sale_price" : info_dict["sale_price"],
                    "brand" : info_dict["brand"],
                    "category" : current_category,
                    "sex" : current_sex,
                    "details" : info_dict["details"]}
              
            crawlerCommon.DiskIOManager.DumpThisItem(item)
      
            item_counter += 1        
            self.swl.loginfo("Fetched item # " + str(item_counter) + "/" + total_items)


    ############################
    #crawl
    ############################
      
    def crawl(self):
        sys.stdout.write("[")
        
        for sex in self.swllist["sex"]:
            self.swl.logdebug(sex["title"])
            categories_list = sex["categories"]

            for category in categories_list:
                category_page_url = category["page_url"]
                category_mapping_list = category["mapping"]
                css_selector = category["css_selector"]

                if self.sale_items_only == True:
                    if category["listing_type"] == "sale":
                        self.swl.loginfo(category_page_url)
                        self.FetchCategories(category_page_url, category_mapping_list, css_selector, sex["title"])
                else:
                    self.swl.loginfo(category_page_url)
                    self.FetchCategories(category_page_url, category_mapping_list, css_selector, sex["title"])
                                         
            category_count = str(self.categoriesQ.qsize())
            self.swl.loginfo("category_count = " + category_count)

        for i in range(self.categoriesQ.qsize()):
            now_category = i+1   
            
            category = self.categoriesQ[i]
            current_page_url = category["category_url"]
            category_title = category["category_title"]
            category_sex = category["sex"]
            subcategory = category['subcategory']
 
            self.swl.loginfo("NOW ON CATEGORY " + str(now_category) + " Category Title = " + category_title)
            
            self.swl.loginfo("current_page_url = " + current_page_url)
            h = self.nwio.read_link(current_page_url, self.server_root)
            
            current_page = 1
            total_pages = 1
            
            item_boxes_list = self.fetchItemsQueue(h)
            
            number_of_items_per_page = len(item_boxes_list)
            self.swl.logdebug("len(item_boxes_list) = " + str(number_of_items_per_page))
            
            total_pages = self.findTotalPages(h)
            self.swl.loginfo("total_pages = " + str(total_pages))
            
            self.sm.SetLatestStats(now_category, category_count, str(current_page), str(total_pages))
            self.swl.loginfo(self.sm.PrintLatestStats())
            
            self.PopulateItemsList(item_boxes_list, category_sex, category_title, subcategory) #This will get all items from a category


        sys.stdout.write("]")
    
#---------------------------------------------------------------------------------------  
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--sale", help="optional argument to crawl only sale items - no option means all categories will be crawled",
                    action="store_true")
                    
    args = parser.parse_args()
    if args.sale:
        print "Fetching sale items only"

    b = AnnekleinConfig(args.sale)
    b.crawl()
