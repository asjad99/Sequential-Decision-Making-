
## Introduction: 

Data Science has been around for a while. Even big data has been around for a while(Hubble has been sending us image data and Scientists at 
CERN have been collecting Tera Bytes to uncover the secrets of the universe). Business recently realised that can extract value out of the 
data they collect(e.g user data and event data) to make data-informed decisions which replaces the old model of going with the gut instinct, 
loudest voice, and best argument methods. The insights gathered through this process can help improve existing processes and lower operations cost. 
Learning 'how to be smart with data' is also bit of an art, that requires curosity, creativity and attention to detail and so on. 
All of this requires experience and practice.  

Instead of providing a sophisticated definition of Data Science, We run with this definition for now(by J. Kolter at CMU): 

> Data science = statistics + data collection + data preprocessing + machine learning + visualization + business insights + scientific hypotheses + big data + (etc)

----------------------------------------------------------------------------------------------------------------


#### Experiment LifeCyle - An Iterative Process: 
Data Science analytics are a lot like broccoli – fractal in nature in
both time and construction. Early versions of an analytic follow the
same development process as later versions. At any given iteration, the
analytic itself is a collection of smaller analytics that often decompose
into yet smaller analytics. This is described as follows: 

![alt text](data_science_process.png "Logo Title Text 1")

Decomposing the problem into manageable pieces is the frist step
in the analytic selection process. Achieving a desired analytic action
often requires combining multiple analytic techniques into a holistic,
end-to-end solution. Engineering the complete solution requires that
the problem be decomposed into progressively smaller sub-problems.
Fractal Analytic Model embodies this approach. At any given
stage, the analytic itself is a collection of smaller computations that
decompose into yet smaller computations. When the problem is
decomposed far enough, only a single analytic technique is needed
to achieve the analytic goal. Problem decomposition creates multiple
sub-problems, each with their own goals, data, computations, and
actions.

  Set up the infrastructure, aggregate and prepare the data, and
incorporate domain expert knowledge. Try di$erent analytic
techniques and models on subsets of the data. Evaluate the models,
refine, evaluate again, and select a model. Do something with your
models and results – deploy the models to inform, inspire action, and
act. Evaluate the business results to improve the overall product.

references: 
  - Data Science Field guide - Booz Allen Hamilton
  - https://dfrieds.com/articles/recipe-great-data-science-work.html
  

----------------------------------------------------------------------------------------------------------------

## Topics: 

- Data Munging (Data Acquistion and pre-processing) 
- Data Engineering (Large Scale Data Processing) 
- Descriptive Analytics (Data Wrangling and Basic Statistics to summarize data)
- Preditive Analytics with Machine Learning 
- Prescriptive Analytics 
- Data Engineering with Spark 

----------------------------------------------------------------------------------------------------------------

## Data Engineering 

Most data science activities starts with acquiring the relevent data. We then prepare the acquired data for analysis, usually by 
setting up the infrastructure, performs various aggregates and incorporating domain expert knowledge.  


#### Data Munging 

| Notebook                 | Description | Code | Blog |
|--------------------------|-----------|------|-------|
| Data Wrangling with Unix | Learn various command line utlities and how they can be used to clean and compute basic statistics          | post |         |
| Web Data Collection      | Learn to collect data available on web (APIs or web scrapping)          | [Notebook](https://github.com/asjad99/datascience-GYM/tree/master/data_engineering)          |      |
| Numpy Basics Tutorial    | Learn the basics of the library that underpins scientific computing          |Notebook        | Notes |
| Pandas Tutorial          |           |Notebook        |      |

### Useful Guides: 

- Guide for [Common Data Types and Formats](https://github.com/asjad99/datascience-GYM/blob/master/Data_Munging/2.%20data_types_formats.ipynb)
- Guide by Jeff lean on [how to share data with a statistician](https://github.com/asjad99/datascience-GYM/blob/master/Data_Munging/3.%20Data_Cleaning.ipynb)

------------------------------------------

### Data Engineering 

### Data Models

| Algorithm           | Notes     | 
|---------------------|-----------|
| Relational Data     |           |
| Document Model      |           |
| Graph Model         |           |

### Large-Scale Processing 

| Notebook                 | Description | Code | Blog | 
|--------------------------|-------------|------|------|
| Speeding up Numpy        | Learn how to get optimal performance out of NumPY | | [Notes](https://asjadkhan.ghost.io/speeding-up-numpy/)          |
| Spark Tutorial           | Learn large scale Data Engineering with Spark          |     | [Notes](https://asjadkhan.ghost.io/ghost/#/editor/post/5f39c86010c8da00398dc9ce)     |
| Topic Modeling in Spark  | LSI Modeling in Spark to Extract document topics | [Python_code](https://gist.github.com/asjad99/e87a695df10b0859ee943b8e661f0fc3)  | |



----------------------------------------------------------------------------------------------------------------

## Descriptive Analytics 

Descriptive Analytics is aimed at answering real busiessn questions. Describing the dataset at hand, Discovering insigths and Acting on those insights. 
It requires finding meaningful patterns, trends and exceptions that are easy to see and interpret for decision makers. 


| Notebook                 | Notebooks | Blog |
|--------------------------|-----------|------|
| Seaborn                  |           |      |
| Matplotlib               |           |      |
| statsmodels              |           |      |

### Useful Guides:

Data Formats should be easy for computers to parse, people to read and widely used by systems in production. 
The computations we perform must be reproducible and tweakable. Data Pipelines need to be documented. 

- [Reproducability in Data Science](https://maxmasnick.com/media/slides/data-analysis-reproducibility/data-analysis-reproducibility.pdf)
- [Creating a data driven organization](https://www.oreilly.com/library/view/creating-a-data-driven/9781492049227/ch04.html)
- [Managing Data Science Teams and Projects](https://www.oreilly.com/library/view/managing-data-science/9781838826321/)

#### Interesting case studies: 

Context, inferences and models are created by humans and carry with them biases and assumptions. Blindly trusting your analyses is a dangerous thing
that can lead to erroneous conclusions. We should try to clearly communite our findings by describing: 

- What problem are we trying to solve and why its intresting? 
- Document your assumptions and make sure they have not introduced bias in your work.
- Does the approach taken and answers make sense? (we should be Be skeptical of surprise findings and make sure the analysis address the
original intent)

The goal of your analysis is to tell an actionable story. Its good to see some data science projects and learn from them. In each project, the author had a question they wanted to answer and used data to answer that question. They explored, visualized, and analysed the data. Then, they wrote blog posts to communicate their findings. Take a look to learn more about the topics listed and to see how others work through the data science project process and communicate their results!

- https://pennmusa.github.io/MUSA_801.io/project_5/index.html
- https://sharlagelfand.netlify.app/posts/tidying-toronto-open-data/
- https://masalmon.eu/2017/11/16/wheretoliveus/
- http://varianceexplained.org/r/trump-tweets/

----------------------------------------------------------------------------------------------------------------


## Predictive Analytics with Machine Learning 

Machine Learning  Utilizes past observation data to predict future observations. e.g Can we predict which products
that certain customer groups are more likely to purchase? 

In terms of impact most of AI technologies currently being deployed are still falling under this machine learning. 

According to andrew Ng: 

> Almost all of AI’s recent progress is through one type, in which some input data (A) is used to quickly generate some simple response (B). Being able to 
input A and output B will transform many industries. The technical term for building this A→B software is supervised learning. These A→B systems have been
improving rapidly, and the best ones today are built with a technology called deep learning or deep neural networks, which were loosely inspired by the brain. 

According to J. Kolter at CMU:  

> for many data science problems, simple machine learning algorithms suffice to attain sufficiently good performance (by whatever metric you want to define performance, but I simply mean that they effectively solve the problem). The numbers here are all just examples (specifically the solvable/unsolvable ratio), but the point it gets at is important. There are many data science problems one would like to be able to solve, but in a large number of these cases, there is simply no way to solve the problem given the available data. For the set of problems that are solvable with some kind of machine learning, the vast majority will be solvable at least to a level of sufficient performance, using relatively simple models. The 5% of remaining problems is an important one, because they often consist of the most “interesting” problems from a research standpoint (think problems like speech recognition, natural language understanding, computer vision), but they are often not indicative of the types of problems one encounters in “most” data science applications.


![alt text](ml_problems.png "Logo Title Text 1")


The ultiamte goal of Machine learning is to be able to generatize to new unseen data. i.e predicting
behavior under new conditions. we study Problems like: Regression, Clustering, Classication, Recommendation. 


| Algorithm           | Notebooks | Description |
|---------------------|-----------|-------------|
| Linear Regression   |           |             |
| Logistic Regression |           |             |
| SVMs                |           |             |
| XGboost             |           |             |
| Clustering          |           |             |




#### Cool ML Applications: 

- The Case for Learned Index Structures 
- [Machine Learning in Compilers: Past, Present and Future] (https://research.fb.com/wp-content/uploads/2020/09/Machine-Learning-in-Compilers-Past-Present-and-Future.pdf)
- [Using machine learning for code recommendation](https://ai.facebook.com/blog/aroma-ml-for-code-recommendation/)
- [Learn to rank](https://medium.com/@nikhilbd/intuitive-explanation-of-learning-to-rank-and-ranknet-lambdarank-and-lambdamart-fe1e17fac418
https://arxiv.org/pdf/1812.00073.pdf)



#### Useful Guides: 

- Understanding Generalizations in Machine Learning 
- Why is ML hard http://ai.stanford.edu/~zayd/why-is-machine-learning-hard.html 
- Debugging ML Systems (Machine learning Yearning by Andrew Ng)
- Feature Engineering and dimensionality reduction
- Challenges in Deploying Machine Learning: a Survey of Case Studies
- Challenges in Production: https://blog.acolyer.org/2019/10/07/150-successful-machine-learning-models/


----------------------------------------------------------------------------------------------------------------


## Deep Learning and NLP: 


-- retrieving relevant code given a natural language query: 


#### Cool Applications: 

- Deep learning to translate between programming languages https://ai.facebook.com/blog/deep-learning-to-translate-between-programming-languages/


----------------------------------------------------------------------------------------------------------------

## Predictive Analytics with Reinforcement Learning 

We can model many problems as a Markov Decision Process or POMDP. We define a reward function that captures out goals and we then find a policy that maximuses the sum of future rewards.
This is similar to Operations Research techniques focused on selecting the best element from a set of available alternatives to maximize a utility function. 

#### Basic Theory: 
  - 3 pillers of reinforcement learning 
  - Exploration vs Exploitation 
  - RL in the Real World: Challenges and Opportunities 
  - Counterfactual Policy Evaluation 
  - Math of RL 

#### Case Study: 
  - Supporting Knowledge Instensive Processes in Clincial Settings 

------------------------------------------------------------------------------------------------------------------------


## Math Topics
Data science rests on a foundation of
mathematics, particularly statistics and linear algebra. It is important to
understand this material on an intuitive level: why these concepts were
developed, how they are useful, and when they work best. e.g develop statistical reasoning is a core goal. 

- Linear Algebra
- Sets
- Graph Theory
- Probability



--------------------------------------------------------------------
--------------------------------------------------------------------


“Standard Human Condition is miscognition, ignorance and Stupidity” - Charlie Munger 

inspired by peter norvig's [pytudes project](https://github.com/norvig/pytudes#pytudes-index-of-jupyter-ipython-notebooks) and Project's by folks like: [Donne_Martin](https://github.com/donnemartin/data-science-ipython-notebooks), [Dfriends](https://dfrieds.com/), [Chris_albon](https://chrisalbon.com/).  
