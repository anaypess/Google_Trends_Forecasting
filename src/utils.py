####### 
import datetime

def parse_raw_trend(raw_trend_df):
    ### Clean pytrends API raw output
    trend_result = raw_trend_df.copy()
    trend_result.reset_index(inplace = True)
    trend_result.columns = ['date', 'unscaled', 'monthly', 'isPartial', 'scale', 'key']
    trend_result = trend_result[['date', 'unscaled']]
    trend_result.dropna(inplace = True)
    
    return trend_result

def store_dataframe_to_csv(df, csv_name):
    path = "../outputs/" + csv_name + "_" + str(datetime.datetime.now()).replace(" ", "") + ".csv"
    df.to_csv(path, index = False)

