#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Stefan Hiemer
"""

# this is just a module to allow you to write out your results and read them 
# again
from json import dump,load

import numpy as np
from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt 


from sklearn.preprocessing import StandardScaler,PolynomialFeatures
from sklearn.linear_model import LinearRegression,Ridge,Lasso
from sklearn.feature_selection import SelectFromModel
from sklearn.model_selection import GridSearchCV,train_test_split 
from sklearn.tree import DecisionTreeRegressor 
from sklearn.ensemble import AdaBoostRegressor,GradientBoostingRegressor,\
                             RandomForestRegressor
from sklearn.kernel_ridge import KernelRidge

if __name__ == "__main__":
    
    pass
    
    