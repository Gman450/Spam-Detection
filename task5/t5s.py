import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pylab import show
from numpy import loadtxt

def sigmoid(z):  
    return 1 / (1 + np.exp(-z))

def cost(theta, X, y):  
    theta = np.matrix(theta)
    X = np.matrix(X)
    y = np.matrix(y)
    first = np.multiply(-y, np.log(sigmoid(X * theta.T)))
    second = np.multiply((1 - y), np.log(1 - sigmoid(X * theta.T)))
    return np.sum(first - second) / (len(X))

def gradient(theta, X, y):  
    theta = np.matrix(theta)
    X = np.matrix(X)
    y = np.matrix(y)

    parameters = int(theta.ravel().shape[1])
    grad = np.zeros(parameters)

    error = sigmoid(X * theta.T) - y

    for i in range(parameters):
        term = np.multiply(error, X[:,i])
        grad[i] = np.sum(term) / len(X)

    return grad

def predict(theta, X):  
    probability = sigmoid(X * theta.T)
    return [1 if x >= 0.5 else 0 for x in probability]
  
#load the dataset
data = pd.read_csv('ex2data1.txt', header=None, names=['Exam 1', 'Exam 2', 'Admitted'])
data.head()
#load complete

#visualized dataset plot
positive = data[data['Admitted'].isin([1])]  
negative = data[data['Admitted'].isin([0])]
fig, ax = plt.subplots(figsize=(12,8))  
ax.scatter(positive['Exam 1'], positive['Exam 2'], s=50, c='b', marker='o', label='Admitted')  
ax.scatter(negative['Exam 1'], negative['Exam 2'], s=50, c='r', marker='x', label='Not Admitted')  
ax.legend()  
ax.set_xlabel('Exam 1 Score')  
ax.set_ylabel('Exam 2 Score')  
show()
#finished visualization

#sigmoid function display
"""nums = np.arange(-10, 10, step=1)
fig, ax = plt.subplots(figsize=(12,8))  
ax.plot(nums, sigmoid(nums), 'r') 
show()"""
#sigmoid display ends

#testing out cost function
data.insert(0, 'Ones', 1)
cols=data.shape[1]
X = data.iloc[:,0:cols-1]  
y = data.iloc[:,cols-1:cols]
X = np.array(X.values)  
y = np.array(y.values)  
theta = np.zeros(3) 
print X.shape
print y.shape
print theta.shape
print "Cost=",cost(theta, X, y)
#finished testing cost function - working properly

#testing out gradient function
import scipy.optimize as opt  
result = opt.fmin_tnc(func=cost, x0=theta, fprime=gradient, args=(X, y))  
print "Gradient=",cost(result[0], X, y)
#finished testing gradient function - working properly

#testing out accuracy function
theta_min = np.matrix(result[0])  
predictions = predict(theta_min, X)  
correct = [1 if ((a == 1 and b == 1) or (a == 0 and b == 0)) else 0 for (a, b) in zip(predictions, y)]  
accuracy = (sum(map(int, correct)) % len(correct))  
print 'accuracy = {0}%'.format(accuracy)  
#finished testing - working properly

