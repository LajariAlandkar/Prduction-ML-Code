
from pathlib import Path

from setuptools import find_packages, setup


# Package meta-data.
NAME = 'CrossSalePredictionModel'
DESCRIPTION = 'Train and deploy classification model.'
URL = 'https://github.com/LajariAlandkar/CrossSalePredictionModel.git'
AUTHOR = 'Lajari'
REQUIRES_PYTHON = '>=3.6.0'


# packages required for this module has been extracted from requirements.txt file
def list_reqs(fname='requirements.txt'):
    with open(fname) as fd:
        return fd.read().splitlines()


# Load the package's version
ROOT_DIR = Path(__file__).resolve().parent
PACKAGE_DIR = ROOT_DIR / NAME
about = {}
with open(PACKAGE_DIR / 'VERSION') as f:
    _version = f.read().strip()
    about['__version__'] = _version


# Where the magic happens:
setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    author=AUTHOR,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=('tests',)),
    install_requires=list_reqs(),
    extras_require={},
    license='MIT',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
        ]

)