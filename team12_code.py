# -*- coding: utf-8 -*-
"""team12_code.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1V-A2lzwD5pyZlo1jyWgOOvqBRnYT0Xtd
"""

import numpy as np
import matplotlib.pyplot as plt
import math


#this function plots the graph of the given function as well as the points that the algorithm went through
#it accepts the array of x and y values for each iteration of the algorithm
#It also accepts the count variable which keeps track of number of iteratins algorithm went through
#for graphing used examples from https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/
#for setting a limit used https://www.geeksforgeeks.org/how-to-set-the-x-and-the-y-limit-in-matplotlib-with-python/ 
def plot(x_values, y_values, count):
    print("Number of Iterations:", len(x_values))
    print("The minimum of the function is:",y_values[len(y_values)-1], "and occurs at x =",x_values[len(x_values)-1])
    x = np.arange(-5, 5, 0.01)
    y = np.sin(x) - np.cos(x)
    #plotting the graph of the original function
    plt.plot(x, y) 
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('f(x) = sinx - cosx')
    plt.xlim(-6, 6) 
    #plotting the point the algorithm went through on the graph
    plt.scatter(x_values, y_values) 
    plt.show()
    

#this function defines the original function. 
#It accepts x value and calculates function at that point
def funct(x):
    return math.sin(x)-math.cos(x)

#this function defines the derivative of the original function. 
#It accepts x value and calculates derivative at that point
def deriv_funct(x):
    return math.cos(x)+ math.sin(x)
   
#This function defines the Gradient Descent Algorithm
#It acccepts paramenter count, x value, step size, and the max number of iterations for the algorithm
def GDA(count, x, step, num_interations):
    x_values = [x] #creating array for all the x values is initializes and the value of xinit is appended
    y = funct(x) #calculating the function value at xinit
    y_values = [y] #creating array for all of the y values anf appending f(xinit)
    
    
    #the while loop runs while count does not exceed the max number of iterations
    while count <= num_interations :
        f1 = funct(x) #determining the value of the function at x prev
        x = x - step * deriv_funct(x) #calculating x next
        count=count+1

        #for the case when initial point is greater than 3pi/4 and x next goes beyond the determined limits
        if x >= 5:
            x = 5.0 #the function minimum value is assigned to x=5
            f2=funct(x) #function is calculated at x=5 for local min
            x_values.append(x)
            y_values.append(f2)
 
            plot(x_values, y_values, count)
            print(x_values)
            print(y_values)    
            break
        
        #for the case when initial point is less than -5pi/4 and x next goes beyond the determined limits
        if x <= -5:
            x = -5.0 #the function minimum value isassigned to x=-5 
            f2 = funct(x) #function is calculated at x=-5 for local min
            x_values.append(x)
            y_values.append(f2) 
            
            plot(x_values, y_values, count)
            print(x_values)
            print(y_values)
            break
        
        f2 = funct(x) #determining the value of f at x next
        
        #for the case when x initial is within -5pi/4 to 3pi/4 and the algorithm will reach the global minimum
        #when f(x_next) is greater than or equal to f(x_prev) or when the algortihm reaches the maximum number of iterations
        if f2>=f1 or count==num_iterations:
            plot(x_values, y_values, count)
            print(x_values)
            print(y_values)
            break
            
        #if none of those cases happen, the values of xnext and function at xnext are apppended to the array
        
        x_values.append(x)
        y_values.append(f2)

count = 0 #thisvariable counts the number of iterations that algorithm goes through
x_init = 2 #this values sets the initial value for x
step = 0.01 #this values sets the stuep size for the function
num_iterations = 50 #this value sets the max number of iterations

GDA(count, x_init, step, num_iterations)

count = 0 #thisvariable counts the number of iterations that algorithm goes through
x_init = 2 #this values sets the initial value for x
step = 0.1 #this values sets the stuep size for the function
num_iterations = 50 #this value sets the max number of iterations

GDA(count, x_init, step, num_iterations)

count = 0 #thisvariable counts the number of iterations that algorithm goes through
x_init = 2 #this values sets the initial value for x
step = 0.01 #this values sets the stuep size for the function
num_iterations = 500 #this value sets the max number of iterations

GDA(count, x_init, step, num_iterations)

count = 0 #thisvariable counts the number of iterations that algorithm goes through
x_init = 3 #this values sets the initial value for x
step = 0.05 #this values sets the stuep size for the function
num_iterations = 500 #this value sets the max number of iterations

GDA(count, x_init, step, num_iterations)