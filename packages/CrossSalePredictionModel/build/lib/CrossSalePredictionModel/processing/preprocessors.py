import pandas as pd
import numpy as np

from sklearn.base import BaseEstimator, TransformerMixin


class LabelEncodeFeatures(BaseEstimator, TransformerMixin):
    
    def __init__(self, variables = None):
        self.vd_dict = {'Yes':1, 'No':0}
        self.va_dict = {'< 1 Year':1,'1-2 Year':2,'> 2 Years':3}
        self.g_dict = {'Male':1,'Female':0}
        
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables
    
    def fit(self, X,y=None):
        return self
    
    def transform(self,X):
        X = X.copy()
        for f in self.variables:
            if f == 'Vehicle_Damage':
                X[f] = X[f].replace(self.vd_dict)
            elif f == 'Vehicle_Age':
                X[f] = X[f].replace(self.va_dict)
            elif f == 'Gender':
                X[f] = X[f].replace(self.g_dict)                
        return X
    
        
class BinningAge(BaseEstimator,TransformerMixin):
    
    def __init__(self, variables=None):
        if len(variables) == 1:
            self.variables = variables[0]
        else:
            self.variables = variables
        
            
    def fit(self, X, y = None):
        return self
    
    def transform(self, X):
        X = X.copy()
        X[self.variables] = pd.cut(X[self.variables],[0,15,30,45,60,75,90,105],labels=[1,2,3,4,5,6,7], include_lowest = True)
        
        return X
    
        
class FrequencyEncodeFeatures(BaseEstimator, TransformerMixin):
    def __init__(self, variables=None):
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables
            
    def fit(self, X, y=None):
        self.encode_dict = {}
        for f in self.variables:
            dict_map =  dict(zip(X[f].value_counts(ascending = False),range(1,X[f].nunique()+1)))
            self.encode_dict[f] = dict_map
            
        return self
    
    def transform(self,X):
        X = X.copy()
        for f in self.variables:
            X[f] = X[f].replace(self.encode_dict[f])
        
        return X
    
        

class DropUnecessaryFeatures(BaseEstimator, TransformerMixin):

    def __init__(self, variables_to_drop=None):
        
        self.variables = variables_to_drop

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # encode labels
        X = X.copy()
        X = X.drop(self.variables, axis=1)

        return X
    






