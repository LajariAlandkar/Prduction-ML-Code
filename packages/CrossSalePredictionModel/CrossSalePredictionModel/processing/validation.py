import numpy as np
from CrossSalePredictionModel.config import config

def removing_negatives(ip, feature_set):
    df = ip.copy()
    if (df[feature_set] <= 0).any().any():
       vars_with_neg_values =  feature_set[
           (df[feature_set] <= 0).any()]
       df = df[df[vars_with_neg_values]>0]
       
    return df

def validate_inputs(input_data):
    """ Validating input"""
    validated_data = input_data.copy()
    
    validated_data = removing_negatives(validated_data, config.TRANSFORM_FEATURES)
    validated_data = removing_negatives(validated_data, config.BINN_FEATURES)

    return validated_data
        

