import joblib
import pandas as pd

def encodeData(df):
    scaler = joblib.load('./helper/scaler.pkl')
    label_encoder = joblib.load('./helper/label_encoders.pkl')

    df.drop(columns = ['Name'], inplace = True)

    df['Age'] = scaler.transform(df[['Age']])

    for column, encoder in label_encoder.items():
        df[column] = encoder.transform(df[column])
    
    X = df.values
    return X