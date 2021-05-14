# Trends forecast

The aim of this project is to:
1. Use Google trends API to collect trend
2. Build a forecasting model on the direction of trends based on API request


## Data sources:

- from gtrends API

## Setting

First create a dedicated virtual environment:

First create a dedicated virtual environment and activate it with python:

```bash
 python3 -m venv venv/ 
source venv/bin/activate 
```

Activate your venv in jupyter notebook

```bash
pip install ipykernel
python -m ipykernel install --user --name $1 --display-name "Python $PROJECT_NAME"
pip install -U jupyter
```

#### Install all requirements
```bash
pip install -r requirements.txt
```
## Folder structure :

Customer segmentation has the following structure:

```
GOOGLE_TRENDS_FORECASTING/

├── bin/
│   ├──model.pickle  
├── data/
│   ├──keywords_gtrends.txt  
├── outputs/
│   ├──gtrends_colected.csv 
├── notebooks/
│   ├──dataprep.ipynb
│   ├──forecasting_prophet.ipynb
│   ├──forecasting_catboost.ipynb
├── src/
│   ├──collector.py
│   ├──config.py
│   ├──utils.py
│   ├──main.py
├── tests/
│   ├──tests.ipynb
