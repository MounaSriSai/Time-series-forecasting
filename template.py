import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = "timeseries_forecasting"

list_of_files = [
    f"src/{project_name}/__init__.py",
    
    # Pipeline modules
    f"src/{project_name}/pipeline/__init__.py",
    # Utilities
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    
    # Config
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    
    # Root-level files
    "config/config.yaml",
    "params.yaml",
    "app.py",    # For deployment (Streamlit/FastAPI)
    "main.py",   # Entry point for training
    "requirements.txt",
    "setup.py",
    "research/experiments.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")
