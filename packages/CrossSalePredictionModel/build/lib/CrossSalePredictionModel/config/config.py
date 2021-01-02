import pathlib
import CrossSalePredictionModel


PACKAGE_ROOT = pathlib.Path(CrossSalePredictionModel.__file__).resolve().parent
TRAINED_MODEL_DIR = PACKAGE_ROOT / "trained_models"
DATASET_DIR = PACKAGE_ROOT / "dataset"


# Train and Test source files

TRAIN_FILE = 'train.csv'
TEST_FILE = 'test.csv'
PIPELINE_NAME = 'classification_model'


TARGET = 'Response'

# input Variable
FEATURES = [
    'id', 
    'Gender', 
    'Age', 
    'Driving_License', 
    'Region_Code',
    'Previously_Insured', 
    'Vehicle_Age', 
    'Vehicle_Damage', 
    'Annual_Premium',
    'Policy_Sales_Channel', 
    'Vintage']


# Features to drop
DROP_FEATURES = ['id', 'Driving_License', 'Vintage']

# Features to label encode
LABEL_ENCODE_FEATURES = ['Gender','Vehicle_Age','Vehicle_Damage']

# Features to frequency encode
FREQ_ENCODE_FEATURES = ['Policy_Sales_Channel', 'Region_Code']

# Binning Features
BINN_FEATURES = ['Age']

# Features to transform
TRANSFORM_FEATURES = ['Annual_Premium']

# Model parameters decided through experimentation during research
MODEL_PARAMS = {'random_state':3,'criterion': 'entropy', 'min_samples_leaf': 3, 'min_samples_split': 2}

