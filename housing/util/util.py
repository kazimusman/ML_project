# read yaml file function 

# util is kind of helper function, so we are going to create few functions inside util and we 
# will use these function whenever they are required 

import yaml
from housing.exception import HousingException
import os,sys

# Where we are going to use this read_yaml_file function? we will use in configuration.py file 

def read_yaml_file(file_path:str)->dict:
    """
    Reads a YAML file and returns the contents as a dictionary.
    file_path: str
    """
    try:
        with open(file_path, 'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise HousingException(e,sys) from e 