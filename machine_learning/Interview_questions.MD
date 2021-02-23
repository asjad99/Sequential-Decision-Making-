Interview Questions: 


* Explain generalisation and what is regularization?  

#-------------------------------------------------------------------------------


* And how to avoid overfitting training data? 


#-------------------------------------------------------------------------------

## If your model performs great on the training set but generalizes poorly, what happening? Can you give possible solutions? 

If the training error is low (i.e your model makes a few mistakes on the training set but the generalization error is high, it means that your model is overfitting the training data). 

We can fix this by : a) Selecting a more a powerful model, with more parameters. b) feed better features to the learning algorithm c) Reduce teh constraints on the model (e.g reduce the regularization hyperparemeter)

#-------------------------------------------------------------------------------
## what is teh difference between parameter and hyperparemeter of a model?

there are bells and whites you can tweak to control teh regualization. the expressive power of the model which allows it to fit the model. 

A hyperparemeter is a parameter of a learning algorithm (not of the model)

It is set prior to training and remains constant during training. 

Parameters are something the algorithm tunes using an optimizaiton technique. 

#-------------------------------------------------------------------------------

#### what is the purpose of validation set?


#-------------------------------------------------------------------------------


## How to Estiamte bias and Variance?**

Bias: 



Variance: 


#-------------------------------------------------------------------------------
## what is the free lunch theorem? 

Well if we make no assumptions about the data(e.g linear model assumpts that the data is fundamentally linear), then there is no reason to prefer one model over any other. 

#-------------------------------------------------------------------------------

## Explain the ROC curve ? ROC (how to determine optimal threshold)? 

During training we try to evaluate the performance by plotting its “learning curve” which shows the error rate(measured on test set) as a function of training examples. A good learning algorithm achieves an error rate of (almost) zero as you show it more and more examples. The rate at which the curve approaches zeros depends on how difficult the learning task is.





#----------------#----------------#----------------#----------------#----------------#----------------#----------------#----------------

#### Feature Engineering
* Explain a Feature selection/extraction techniques? 
* Explain dimensionality reduction and explain PCA? 



#----------------#----------------#----------------#----------------#----------------#----------------#----------------#----------------


Explain the working of the following core ML algorithms? 
	- K-Nearnet Neighbours 
	- Linear and Logistic regression
	- Support Vector Machines (SVMs)
	- Decision Trees and Random forests 
	- Neural Networks 
### Linear regression





#----------------#----------------#----------------#----------------#----------------#----------------#----------------#----------------


#### Probability: 
	* Explain Skewness of distribution
	* Explain Central limit theorem   

#### Statistics: 
	* variance in probability (basically summing random variables with constants out front, and finding the overall variance).
	* Mean, Min, Max
	* Standard deviation measures how dispersed the values are
	* 25%, 50%, 75% rows show corresponding percentiles: a percentile indicates the value below which a given percentage of obeservations in a group of observations fall 
	

#----------------#----------------#----------------#----------------#----------------#----------------#----------------#----------------
 
 ###Case Study : 