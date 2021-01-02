import pandas as pd

from CrossSalePredictionModel.processing.data_management import load_pipeline
from CrossSalePredictionModel.processing.validation import validate_inputs
from CrossSalePredictionModel import __version__ as _version
from CrossSalePredictionModel.config import config
import logging

_logger = logging.getLogger(__name__)


pipeline_file_name = f"{config.PIPELINE_NAME}_{_version}.pkl"
_resp_pipe = load_pipeline(file_name = pipeline_file_name)




def make_prediction(input_data):
    # make prediction on test data using trained classifier
    data = pd.read_json(input_data)
    validated_data = validate_inputs(data)
    prediction = _resp_pipe.predict(validated_data)
    response = {"predictions":prediction}
    
    _logger.info(f"Making Prediction with model version: {_version}"
                 f"Inputs: {validated_data} "
                 f"Predictions: {response}")
    
    
    return response


