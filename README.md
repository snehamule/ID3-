        
# ID3 Decision Tree - Machine Learning 

This project is implementaion of decision tree using ID3 algorithm. Decision tree builds classification or regression models in the form of a tree structure. Decision tree break datset to subset until leaf node(decision) remains. Attribute selection is based on entropy. Entropy can be defined as impurity in the attributes. <br />
This project uses ID3 algorithm , ID3 algorithm is greedy algorithm with no backtrackin. Id3 uses Information gain and Entropy to decide which attribute to select next.

Entropy:

> Entropy = - p(a)*log(p(a)) - p(b)*log(p(b))<br />
s – The current (data) set for which entropy is being calculated <br />
x– Set of classes in s<br />
p(x) – The probability of the number of elements in class 'x' to the number of elements in set S<br />



## Technology / libraries used: <br />
Python, Scikit learn, Panda, Numpy

## Setup required:<br />
python version: 3 or greater<br />
Libraries : ScikitLearn, Panda,Numpy


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
* Install Numpy : pip install numpy<br />
* Install  Panada : pip install pandas<br />
* Install  Scikitlearn: pip install scipy, scikit-learn<br />

**For windows operating system**<br />
* Install numpy : pip install numpy<br />
* Install pandas : python -m pip install pandas<br />
* Install  Scikitlearn: pip install -U scikit-learn<br />


## Dataset Download :<br />
This recommendation system use  Book-Crossing Dataset.
Download Adult Dataset from UCI dataset [Adult UCI dataset](https://archive.ics.uci.edu/ml/datasets/adult).  

## Run program : <br />
1. Download code from git  using  git clone .
2. Place downloaded dataset files in the same folder
3. For Process the Data run command 
```
	python process_data.py
```	
4. To run backpropogation algorithm, run command 
```
	python backPropogation_algorithm py
```
5. To run same program using scikit learn :
```
     python scitkit_learn_backpropogation_algo.py

```

