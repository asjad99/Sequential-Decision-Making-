### Topics: 

- Introduction
- Process Mining in Practice 
- Resources 


### Introduction 


> There have long been a few fundamental challenges associated with business process management. But a relatively new and innovative technology, process mining, has the capability to revitalize process management in firms where it has lain fallow for years. One problem involves the creation of “current state” processes — a description of how a business process is being performed today. In business process reengineering, organizations are primarily interested in an improved “to be” process, so often they have little interest in exploring “as is,” or how the process is currently performed. The other general problem with process management is the lack of connections between business processes and an organization’s enterprise information systems. Enter process mining. Process mining software can help organizations easily capture information from enterprise transaction systems and provides detailed — and data-driven — information about how key processes are performing. It creates event logs as work is done: an order is received, a product is delivered, a payment is made. The logs make visible how computer-mediated work is really happening, including who did it, how long it takes, and how it departs from the average. 

Process analytics create key performance indicators for the process, which enables a company to focus on the priority steps to improve -

Reference:  What Process Mining Is, and Why Companies Should Do It by Thomas H. Davenport and Andrew Spanyi


### Read More: 
- [Process Analytics: A Survey] ()
- [Introduction to Business Process Analytics](https://asjadkhan.ghost.io/business-process-analytics/)
- [Improving Process Efficiency with Process Mining](https://asjadkhan.ghost.io/improving-process-efficincy-with-process-mining/)
- [Case Study: Improving treatment careflow with Process Mining]()

https://medium.com/@c3_62722/process-mining-with-python-tutorial-a-healthcare-application-part-1-ae02027a050
http://fundamentals-of-bpm.org/wp-content/uploads/2013/02/EMIT_2013-La-Rosa-Part-1.pdf 


--------


### Practical Process Analytics: 





## Step 1: Process Mining in Practice 

## Exploratory Data Analysis + Analysis of specific process domain problems* *  



we  look at the topics most relvant to practiionars (process analysts). i.e how do process analysts conduct a process mining projects: 




There is a paper that surveys and describes how practitionars conduct a process mining project: 

 - **paper**:  Mining Process Mining Practices: An Exploratory Characterization of Information Needs in Process Analytics

   

* First, process models are used to visualize the **topology of the process or the control-flow**, respectively. In this regard, the frequency of activities and their connections is displayed as well. Second, meta-information primarily regarding activity and case attributes is captured in tables. Third, the major category of information needs is related to understanding the distribution of cases, activities, execution patterns, and durations, and is visualized using bar charts, tables or other techniques. Fourth, analysts also investigate the correlation between a broad range of attributes including execution patterns, items, durations, time points and organizational entities. This type of information is displayed in tables, dotted charts or other types of general-purpose techniques. 

* Commonly, those high-level domain problems are too complex to be straightforwardly answered by applying a single analysis technique, and thus analysts divide them into more fine-grain questions, leading to lower-level information needs that can be satisfied through the application of analysis techniques

* its an iterative process: A large share of the information needs also emerged during familiarization and discovery

* **where do analysts spend most of their time?** 

  - there are four main types of analysis. First, process models are used to **visualize the topology of the process or the control-flow**, respectively. In this regard, the frequency of activities and their connections is displayed as well. Second, meta-information primarily regarding activity and case attributes is captured in tables. Third, the major category of information needs is related to understanding the distribution of cases, activities, execution patterns, and durations, and is visualized using bar charts, tables or other techniques. Fourth, analysts also investigate the correlation between a broad range of attributes including execution patterns, items, durations, time points and organizational entities. This type of information is displayed in tables, dotted charts or other types of general-purpose techniques.

* Output: discovery of  ** the Process Model**? 

  

  * In our study, we observed that the most frequently examined problems are those referring to the analysis of perspectives other than the control-flow perspective,* ***especially the case perspective****. In this regard, our analysis revealed that the problems are largely explored via* ***visualization techniques*** *not specific to process mining, pointing to areas that might benefit more sophisticated analytical support. Additionally, the data revealed that discovery is a domain problem that organizations need to explore. Moreover, discovery is also often analyzed as part of the familiarization with the data in order to establish a basic understanding of the underlying process.*  

  

  ![img](https://paper-attachments.dropbox.com/s_80A4D8B925EDA83588B1B9ACF6AEBD5C0637E16F315242A68155EF30342E80A3_1600911484105_Screen+Shot+2020-09-24+at+11.37.54+am.png) 

  

  In the first edition in 2011, **discovery was the dominating domain problem**; it also was the problem that the analysts focused on the most in 2012, although the other **domain problems** started to receive increased attention. In the remaining editions the **case perspective** is the most frequently investigated problem. In this regard, 2018 is an exception where many information needs arose during familiarization and the case perspective ranked second. On average, the case perspective was the most important problem. A large share of the information needs also emerged during familiarization and discovery. Moreover, while conformance checking, prediction, and drift detection only played minor roles, the time and organizational perspectives were moderately important.

  

  | **Task**                                | **Task details**                                             |
  | --------------------------------------- | ------------------------------------------------------------ |
  | **domain problems**                     | This set included the problems of process discovery where a process model describing the control flow is inferred from the data and of conformance checking which deals with verifying that the behavior in the event log adheres to a set of business rules, e.g., defined as a process model. While these two use cases focus on the control-flow perspective, there are three enhancement use cases which refer to other perspectives. |
  | **time perspective**                    | deal with understanding the performance of the process such as throughput times, working times or waiting times. <br> The *time perspective* is concerned with the timing and frequency of events. In most event logs, events have a timestamp (#*time*(e)). The granularity of these timestamps may vary. In some logs only date information is given, e.g., “30-12-2010”. Other event logs have timestamps with millisecond precision. The presence of timestamps enables the discovery of bottlenecks, the analysis of service levels, the monitoring of resource utilization, and the prediction of remaining processing times of running cases. |
  | **organizational perspective**          | focuses on the utilization of resources and their dependencies.  Organizational mining focuses on the *organizational perspective* [130, 159]. Start- ing point for organizational mining is typically the #*resource*(e) attribute present in most event logs.By analyzing an event log as shown in Table 9.3 it is possible to analyze the relation between resources and activities. Table 9.4 shows the mean number of times a resource performs an activity per case. <br/>**Social Network Analysis**<br/>Sociometry*, also referred to as sociography, refers to methods that present data on interpersonal relationships in graph or matrix form. <br/> **Discovering Organizational Structures** <br/>**Analyzing Resource Behavior** |
  | **case prespective** or decision mining | case perspective deals with the influence of other process attributes, e.g., related to the customer, on the behavior comprehending the influences of attributes on the process behavior <br>Section 9.5 showed how to use attributes in the log for decision mining. This shows which data is relevant and should be included in the model. |
  | **prediction problems**                 | where analysts aimed to create models that can forecast the development of process instances |
  | **drift detection** or Deviant analysis | aims to recognize points in time at which the underlying behavior of a process changed and to provide details regarding this change |
  | **familiarization**                     | is an activity that helps experts to understand basic characteristics of the business process and the event data |

  

  ## Step 2: Combine the analysis to get an Integrated Model (or an Enriched Model)  



Using organizational prespective, case prespective, and time prescpective to get a **integrated model** which provides a holistic view see figure below   

<img src="/Users/asjad/Desktop/Screen Shot 2021-02-02 at 12.21.42 pm.png" alt="Screen Shot 2021-02-02 at 12.21.42 pm" style="zoom:25%;" />

control-flow model can be extended with additional perspectives extracted from the event log to ob- tain a fully integrated model covering all relevant aspects of the process at hand. 

TODO: link it to business process life-cycle 

The topics we covered were the ones with 3-4 good papers available 



## Step 3: **use simulations/what if analysis to improve performance:**  



Enrich the process model - Such an integrated model can be used for “what if” analysis using simulation.



- Marlon Dumas: 
- Automated Process Improvement: 
- Causal Analysis 





















## Resources: 

See paper: Process Diagnostics: a Method Based on Process Mining
Mining Process Mining Practices: An Exploratory Characterization of Information Needs in Process Analytics
book chapter -  Chapter 9,13,14 of by van der alst 
book chapter  by marlon dumas 


### Books 

- Process Mining: Data Science in Action Book by Wil van der Aalst
- Process Mining in Action Principles, Use Cases and Outlook
- Fundamentals of Business Process Management.
- https://www.futurelearn.com/courses/business-process-management


###  Courses: 
- Marlon Dumas: http://fundamentals-of-bpm.org/supplementary-material/lectures/ 
- Jan Mendling: https://www.youtube.com/watch?v=vpAxkG_W1_w&list=PL9iw99lS3Prj5VoC4Bwhmj9Wawd2r-Vtt 


###  Key People:


|                              | Research Interests                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Chiara di Francescomarino | Current research interests include, besides business process modeling, collaborative modelling and the evaluation of tools and techniques for its support, process mining(specifically discovery and predictive monitoring) and verification.<br><br><br>- Semantic annotation of business processes and automated reasoning capabilities they can provide on process models such as constraint verification, crosscutting concern mining and process aspectization.<br>- Methodologies and tools for supporting domain experts and technicians in the(collaborative) design of models integrating procedural and declarative knowledge.<br>- Reverse engineering of understandable business process models from existing systems.<br>- Empirical evaluations with human subjects in both academic and industrial settings.<br>- Monitoring of incomplete logs and predictive monitoring.<br>- Process and data mining and verification. |
| Marlon Dumas              | I conduct research in the field of information systems engineering. The problems I examine generally revolve around the following question: How to build and maintain information systems that are aligned with business operations? My efforts are currently focused on two approaches:<br><br><br>- Business Process Management: analysing and building software systems starting from models of how an organisation works, also called business process models<br>- Service-Oriented Computing: analysing and building software systems based on the metaphor of "software as a service", usually on top of Web technology.                                                                                                                                                                                                                                                                                                           |
| Josep Carmona                | My research interests include process and data science, formal methods, business intelligence and business process management.<br><br>I am member of the IEEE Task Force on Process Mining. I have an industrial collaboration with Naturgy, and currently I am promoting different research projects in the field of process mining and modeling.<br><br>Book on Conformance checking.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Claudio Di Ciccio            | My re­search in­terests in­clude pro­cess min­ing, de­clar­at­ive pro­cess mod­el­ling, and blockchains. I have pub­lished more than 60 re­search pa­pers, among oth­ers in In­form­a­tion Sys­tems, De­cision Sup­port Sys­tems, ACM Trans­ac­tions on Man­age­ment In­form­a­tion Sys­tems, and IEEE In­ter­net Com­put­ing.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Jan Mendling                 | His research interests include various topics in the area of business process management and information systems.<br><br><br>Research Interests<br>- Business Process Modeling<br>- Business Process Management<br>- Process Mining<br>- Information Systems<br>- Enterprise Architecture                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Hajo Reijers                 | My research and teaching focus on business process management, data analytics, and enterprise information systems.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Matthias Weidlich            | My research focuses on specific types of information systems, those that are process-oriented and those that are event-driven. Such systems represent general-purpose technology with applications in diverse domains, reaching from health care through logistics to e-commerce. I am interested in formal methods for the specification and verification of information systems, their analysis based on log data, and techniques that optimise their run-time behaviour. Specifically, I explore scenarios where process-oriented and event-based systems come together: where processes generate events or event processing technology supports the execution of a process.                                                                                                                                                                                                                                                          |
| Manfred Reichert             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Matthias Weske               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Amin Beheshti                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Boualem Benatallah           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |


