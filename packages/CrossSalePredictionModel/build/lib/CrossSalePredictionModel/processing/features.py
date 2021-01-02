import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from CrossSalePredictionModel.processing.errors import InvalidModelInputError

class LogTransformer(BaseEstimator, TransformerMixin):

    def __init__(self, variables=None):
        if len(variables) == 1:
            self.variables = variables[0]
        else:
            self.variables = variables

    def fit(self, X, y=None):
        # to accomodate the pipeline
        return self

    def transform(self, X):
        X = X.copy()
        
        if not (X[self.variables] > 0).all().all():
            vars = self.variables[(X[self.variables]<=0).any()]
            raise InvalidModelInputError(
                f"Variable contain zero or negative values,"
                f"can't apply log for vars: {vars}"
                )
            
        X[self.variables] = np.log(X[self.variables])

        return X
    
    