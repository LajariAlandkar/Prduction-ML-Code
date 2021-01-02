from CrossSalePredictionModel.config import config as model_config
from CrossSalePredictionModel.processing.data_management import load_dataset
from CrossSalePredictionModel import __version__ as _version
from api import __version__ as api_version

import json


def test_health_endpoint_returns_200(flask_test_client):
    # When
    response = flask_test_client.get('/health')

    # Then
    assert response.status_code == 200
    
    
    
def test_version_endpoint_returns_version(flask_test_client): 
    # When
    response = flask_test_client.get('/version')
    
    # Then
    assert response.status_code == 200
    response_json = json.loads(response.data)
    print(response_json)
    assert response_json['model_version'] == _version
    assert response_json['api_version'] == api_version


def test_prediction_endpoint_returns_prediction(flask_test_client):
    # Given
    test_data = load_dataset(file_name = model_config.TEST_FILE)
    post_json = test_data[0:1].to_json(orient='records')
    
    # When
    response =flask_test_client.post('/v1/predict/classification', json = json.loads(post_json))
    
    #THEN
    assert response.status_code == 200
    response_json = json.loads(response.data)
    prediction = response_json['predictions']
    response_version = response_json['version']
    assert response_version == _version

    

    
    

    
    





