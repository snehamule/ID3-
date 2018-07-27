        
# ID3 Decision Tree - Machine Learning 

This project is implementaion of decision tree using ID3 algorithm. Decision tree builds classification or regression models in the form of a tree structure. Decision tree break datset to subset until leaf node(decision) remains. Attribute selection is based on entropy. Entropy can be defined as impurity in the attributes. <br />
This project uses ID3 algorithm , ID3 algorithm is greedy algorithm with no backtrackin. Id3 uses Information gain and Entropy to decide which attribute to select next.

Entropy:

> Entropy = - p(a)*log(p(a)) - p(b)*log(p(b))<br />
s – The current (data) set for which entropy is being calculated <br />
x– Set of classes in s<br />
p(x) – The probability of the number of elements in class 'x' to the number of elements in set S<br />



## Technology / libraries used: <br />
Python, Numpy

## Setup required:<br />
python version: 3 or greater<br />



## Install python <br />
If python is not installed then need to install python:<br />
<br />
**For  osx operating system (mac)**<br />
	python get-pip.py 

**For windows operating system**<br />
	refer steps from [windows python installation steps](https://docs.python.org/3/using/windows.html).
	

## Check python version:
python -version


## Install Libraries<br /> 

**For  osx operating system (mac)**<br />
* Install Numpy : pip install numpy<br /

**For windows operating system**<br />
* Install numpy : pip install numpy<br />


## Dataset Download :<br />
This recommendation system use  Book-Crossing Dataset.
Download Credit card approval dataset from UCI dataset [Credit card approval](http://archive.ics.uci.edu/ml/datasets/credit+approval).  

## Run program : <br />
1. Download code from git  using  git clone .
2. Place downloaded dataset files in the same folder
3. For Process the Data run command 
```
	python process_data.py
```	
4. To run backpropogation algorithm, run command 
```
	python test.py  
```

