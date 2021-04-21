# Trends forecast

The aim of this project is to use forecasting models based on google trends information


## Data sources:

- from gtrends API

## Setting

First create a dedicated conda environment:

```bash
conda create -y -n trends_forecast python=3.6
conda insall -n trends_forecast pip
conda activate trends_forecast
conda install -c anaconda ipykernel
python -m ipykernel install --user --name=trends_forecast
```

Install all the requirements:

```bash
pip install -r requirements.txt
```

## Folder structure :

Customer segmentation has the following structure:

```
TRENDS_FORECAST/
├── bin/
│   ├──  
├── data/
│   ├── 

