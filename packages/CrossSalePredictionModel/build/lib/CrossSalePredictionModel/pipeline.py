from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier
from CrossSalePredictionModel.config import config
from CrossSalePredictionModel.processing import preprocessors as pp
from CrossSalePredictionModel.processing import features


response_pipe = Pipeline(
    [
     ('label_encoder',
      pp.LabelEncodeFeatures(variables = config.LABEL_ENCODE_FEATURES)),
     ('binning_age', 
      pp.BinningAge(variables = config.BINN_FEATURES)),
     ('freq_encode_feature', 
      pp.FrequencyEncodeFeatures(variables = config.FREQ_ENCODE_FEATURES)),
     ('log_transform',
      features.LogTransformer(variables = config.TRANSFORM_FEATURES)),
     ('drop_cols',
      pp.DropUnecessaryFeatures(variables_to_drop = config.DROP_FEATURES)),
      ('tree_model', 
      DecisionTreeClassifier(**config.MODEL_PARAMS))
     ]
    )




