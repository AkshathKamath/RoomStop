import json
import pandas as pd

def returnData(df, indexes):
    df = df.iloc[indexes][:]

    return df.to_json(orient = "records")