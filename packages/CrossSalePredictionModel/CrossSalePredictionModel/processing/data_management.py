import pandas as pd
import joblib
import logging

from CrossSalePredictionModel.config import config
from CrossSalePredictionModel import __version__ as _version

_logger = logging.getLogger(__name__)

def load_dataset(file_name):
    """load data"""
    data = pd.read_csv(f"{config.DATASET_DIR}/{file_name}")
    return data

def save_pipeline(pipeline_to_persist):
    """Persist the pipeline"""
    
    save_file_name = f"{config.PIPELINE_NAME}_{_version}.pkl"
    save_path = config.TRAINED_MODEL_DIR / save_file_name
    
    remove_old_pipeline(files_to_keep=save_file_name)
    joblib.dump(pipeline_to_persist, save_path)
    _logger.info(f"saved pipeline: {save_file_name}")

    
def load_pipeline(file_name):
    """load a persisted pipeline"""
    
    file_path = config.TRAINED_MODEL_DIR / file_name
    saved_pipeline = joblib.load(file_path)
    return saved_pipeline


def remove_old_pipeline(files_to_keep):
    
    for model_file in config.TRAINED_MODEL_DIR.iterdir():
        if model_file.name not in [files_to_keep, "__init__.py"]:
            model_file.unlink()
    
