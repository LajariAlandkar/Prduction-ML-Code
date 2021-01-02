
from CrossSalePredictionModel.config import config
from CrossSalePredictionModel.processing.data_management import load_dataset, save_pipeline
from CrossSalePredictionModel import pipeline
from sklearn.model_selection import train_test_split
from CrossSalePredictionModel import __version__ as _version
import logging

_logger = logging.getLogger('CrossSalePredictionModel')
 
 
def run_training():
    "Train the model"
    
    
    # read training data
    data = load_dataset(config.TRAIN_FILE)
    
    # Divide into train and test
    xtrain, xtest, ytrain, ytest = train_test_split(
        data[config.FEATURES],
        data[config.TARGET],
        test_size=0.1,
        random_state = 3)
    
    pipeline.response_pipe.fit(xtrain[config.FEATURES], ytrain)
    
    # Save trained pipline 
    _logger.info(f"saving model version: {_version}")
    save_pipeline(pipeline_to_persist=pipeline.response_pipe)
    
     

if __name__ == '__main__':
    run_training()
    
     
 


