import pandas as pd
import numpy as np
from pytrends.request import TrendReq
from pytrends.dailydata import get_daily_data
import time 
import config
import utils

def run_collector():
    pytrends = TrendReq()
    trends_result = []

    for keyword in config.KEYWORDS:
       # time.sleep(120)
        for geo_code in config.GEO_CODES:
            try :
                raw_trend_df = get_daily_data( keyword, config.START_YEAR,
                 config.START_MONTH, config.END_YEAR, config.END_MONTH, 
                 geo = geo_code)

                parsed_trend =  utils.parse_raw_trend(raw_trend_df)
                parsed_trend["Keyword"] = keyword
                parsed_trend["State"] = geo_code

                trends_result.append(parsed_trend)

            except Exception as error:
                print("Could not access "+ keyword + "_" + geo_code)
                print(error)

    trends_result_df = pd.concat(trends_result)
    
    utils.store_dataframe_to_csv(trends_result_df, "trends_result")

