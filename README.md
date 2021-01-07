
# Index of Jupyter (IPython) Notebooks

Instead of providing a sophisticated definition of Data Science, We run with this definition for now(by J. Kolter at CMU): 

> Data science = statistics + data collection + data preprocessing + machine learning + visualization + business insights + scientific hypotheses + big data + (etc)

Process of data science is something as follows: 

![alt text](data_science_process.png "Logo Title Text 1")

Data Science has been around for a while. Even big data has been around for a while(Hubble has been sending us image data and Scientists at CERN have been collecting Tera Bytes to uncover the secrets of the universe). Business recently realised that they can making use of the user data and event data to make data-informed decisions which replaces thd gut instinct, loudest voice, and best argument methods. THe insights agther throught the process can be used ro insights that help improve existing processes and drive out operations cost. It also bit of an art, that requires learning 'how to be smart with data' and create value from data. 


### Topics: 

Notebooks for data science practice - inspired by peter norvig's [pytudes project](https://github.com/norvig/pytudes#pytudes-index-of-jupyter-ipython-notebooks) and Project's by folks like: [Donne_Martin](https://github.com/donnemartin/data-science-ipython-notebooks), [Dfriends](https://dfrieds.com/), [Chris_albon](https://chrisalbon.com/).  

- Data Wrangling  
- Basic Statistics
- Machine Learning
- NLP with Deep Learning
- Data Engineering with Spark 



## Descriptive Analytics 

Descriptive Analytics is aimed at Describing the dataset at hand, Discovering insigths and Acting on those insights. It requires finding meaningful patterns, trends and exceptions that are easy to see and interpret for decision makers. It answers real business questions 


| Notebook                 | Notebooks | Blog |
|--------------------------|-----------|------|
| data types Tutorial      |           |      |
| Data Wrangling with Unix |           | post |
| Numpy Basics Tutorial    | DN        | post |
| Pandas Tutorial          | DN        |      |
| Seaborn                  |           |      |
| Matplotlib               |           |      |
| statsmodels              |           |      |

### Useful Guides:

- Data Formats should be easy for computers to parse, people to read and widely used by systems in production. Here is a guide for [Common Data Types and Formats](https://github.com/asjad99/datascience-GYM/blob/master/Data_Munging/2.%20data_types_formats.ipynb)
- [Reproducability in Data Science] https://maxmasnick.com/media/slides/data-analysis-reproducibility/data-analysis-reproducibility.pdf
- The computations we perform must be reproducible and tweakable. Data Pipelines need to be documented. Here is a guide by Jeff lean on [how to share data with a statistician](https://github.com/asjad99/datascience-GYM/blob/master/Data_Munging/3.%20Data_Cleaning.ipynb)
- Creating a data driven organization: https://learning.oreilly.com/library/view/data-driven/9781491925454/
- Managing teams: https://www.oreilly.com/library/view/managing-data-science/9781838826321/

#### Interesting case studies: 

Its good to see some data science projects. In each project, the author had a question they wanted to answer and used data to answer that question. They explored, visualized, and analysed the data. Then, they wrote blog posts to communicate their findings. Take a look to learn more about the topics listed and to see how others work through the data science project process and communicate their results!

- https://pennmusa.github.io/MUSA_801.io/project_5/index.html
- https://sharlagelfand.netlify.app/posts/tidying-toronto-open-data/
- https://masalmon.eu/2017/11/16/wheretoliveus/
- http://varianceexplained.org/r/trump-tweets/

----------------------------------------------------------------------------------------------------------------


## Predictive Analytics with Machine Learning 

According to J. Kolter at CMU:  

> for many data science problems, simple machine learning algorithms suffice to attain sufficiently good performance (by whatever metric you want to define performance, but I simply mean that they effectively solve the problem). The numbers here are all just examples (specifically the solvable/unsolvable ratio), but the point it gets at is important. There are many data science problems one would like to be able to solve, but in a large number of these cases, there is simply no way to solve the problem given the available data. For the set of problems that are solvable with some kind of machine learning, the vast majority will be solvable at least to a level of sufficient performance, using relatively simple models. The 5% of remaining problems is an important one, because they often consist of the most “interesting” problems from a research standpoint (think problems like speech recognition, natural language understanding, computer vision), but they are often not indicative of the types of problems one encounters in “most” data science applications.


![alt text](ml_problems.png "Logo Title Text 1")


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
- Debugging ML Systems 
- Feature Engineering 
- Challenges in Production: https://blog.acolyer.org/2019/10/07/150-successful-machine-learning-models/


## Deep Learning and NLP: 


-- retrieving relevant code given a natural language query: 


#### Cool Applications: 

- Deep learning to translate between programming languages https://ai.facebook.com/blog/deep-learning-to-translate-between-programming-languages/


----------------------------------------------------------------------------------------------------------------

## Predictive Analytics with Reinforcement Learning 

#### Basic Theory: 
  - 3 pillers of reinforcement learning 
  - Exploration vs Exploitation 
  - RL in the Real World: Challenges and Opportunities 
  - Counterfactual Policy Evaluation 
  - Math of RL 

#### Case Study: 
  - Supporting Knowledge Instensive Processes in Clincial Settings 

------------------------------------------------------------------------------------------------------------------------

## Useful Data Algorithms for Building Data Products 

A data product provides actionable information without exposing decision makers to the underlying
data or analytics. Examples include: Movie Recommendations, Production Process Improvements, Targeted Advertising etc.

### Data Mining Algorithms 

| Algorithm                | Notebooks | Description |   |   |
|--------------------------|-----------|-------------|---|---|
| Assoicative Rule Mining  |           |             |   |   |
| Alpha Miner              |           |             |   |   |
| Flexible Heuristic Miner |           |             |   |   |

###  Matrix Algorithms 

| Latent Semantic Indexing                      | [Code] <https://gist.github.com/asjad99/e87a695df10b0859ee943b8e661f0fc3> |
|-----------------------------------------------|-------------------------------------------------------------------------------------------|
| Principal Component Analysis (PCA)            |                                                                                           |
| Probabilistic Latent Semantic Indexing (PLSA) |                                                                                           |
| Latent Dirchlet Allocation (LDA)              |                                                                                           |
| Logistic Matrix Factorization                 |                                                                                           |
| Restricted Boltzmann Machines                 |                                                                                           |
| Collaborative Filtering                       |                                                                                           |
| Compressive sensing                           |                                                                                           |
| Linear and convex programming                 |                                                                                           |

### Graph algorithms




https://blog.fastforwardlabs.com/2020/01/29/a-symbiotic-relationship-knowledge-graphs-machine-learning.html

### Classic AI algorithms







## Math Topics
Data science rests on a foundation of
mathematics, particularly statistics and linear algebra. It is important to
understand this material on an intuitive level: why these concepts were
developed, how they are useful, and when they work best. e.g develop statistical reasoning is a core goal. 

Linear Algebra
Sets
Graph Theory
Probability
