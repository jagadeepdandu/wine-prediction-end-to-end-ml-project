import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "winequality"


list_of_files = [
    rf"src\{project_name}\__init__.py",
    rf"src{project_name}\components\__init.py",
    rf"src{project_name}\utils\__init__.py",
    rf"src{project_name}\utils\common.py",
    rf"src{project_name}\config\__init.py",
    rf"src{project_name}\config\configuration.py",
    rf"src{project_name}\pipeline\__init__.py",
    rf"src{project_name}\entity\__init__.py",
    rf"src{project_name}\entity\config_entity.py",
    rf"src{project_name}\constants\__init.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "requirements.txt",
    "setup.py",
    "research\\trails.ipynb",
    "templates\index.html"





]



for filepath in list_of_files:
    filepath = Path(filepath)

    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass 
            logging.info(f"creating empty file: {filepath}")

    else :
        logging.info(f"{filename} is already exists")

