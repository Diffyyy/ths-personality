from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd

class CustomScaler(BaseEstimator, TransformerMixin):
    def __init__(self, data_range):
        self.data_range = data_range
        self.min_val = data_range[0]
        self.max_val = data_range[1]
        
    def fit(self,X,y=None):
        return self

    def transform(self,X,y=None):
        X = pd.DataFrame(X).copy()
        X = (X - self.min_val) /(self.max_val - self.min_val)
        return X