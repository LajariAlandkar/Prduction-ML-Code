import math
import numpy as np
from CrossSalePredictionModel.predict_test import make_prediction
from CrossSalePredictionModel.processing.data_management import load_dataset

def test_make_single_prediction():
    # Given
    test_data = load_dataset('test.csv')
    single_test_json = test_data[0:1].to_json(orient = 'records')
    print('This is sigle test json', single_test_json)
    
    # When
    subject = make_prediction(input_data = single_test_json)
    print(subject)
    
    # Then
    assert subject is not None
    assert isinstance(subject.get('predictions')[0],np.int64)
    
    
    
def test_make_multiple_predictions():
    # Given
    test_data = load_dataset('test.csv')
    original_data_length = len(test_data)
    multiple_test_json = test_data.to_json(orient='records')
    
    # When
    subject = make_prediction(multiple_test_json)
    print(subject)
    print(len(subject.get('predictions')))
    
    #Then
    assert subject is not None
    assert len(subject.get('predictions')) == 127037
    assert len(subject.get('predictions')) == original_data_length
    
    
    
    
    

