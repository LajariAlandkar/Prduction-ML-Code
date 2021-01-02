from flask import Blueprint, request, jsonify

from api.config import get_logger
from api.validation import validate_inputs
from CrossSalePredictionModel.predict_test import make_prediction
from api import __version__ as api_version
from CrossSalePredictionModel import __version__ as _version

_logger = get_logger(__name__)

print(__name__)
prediction_app = Blueprint('prediction_App', __name__)


@prediction_app.route('/health',methods=['GET'])
def health():
    if request.method == 'GET':
        _logger.info('health status OK')
        return 'ok'


@prediction_app.route('/version', methods=['GET'])
def version():
    if request.method == 'GET':
        return jsonify({'model_version': _version,
                        'api_version': api_version})



@prediction_app.route('/v1/predict/classification', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Extract post data from request body as json
        json_data = request.get_json()
        _logger.debug(f'Inputs: {json_data}')
        
        # Validate the input using marshmallow Schema
        input_data, errors = validate_inputs(input_data=json_data)
        
        # Model Prediction
        result = make_prediction(input_data=input_data)
        _logger.debug(f'Outputs: {result}')
        
        # Return the response as json        
        predictions = result.get('predictions').tolist()
        version = result.get('version')
        
        return jsonify({'predictions': predictions,
                        'version': version,
                        'errors': errors})
    
    
   
    









