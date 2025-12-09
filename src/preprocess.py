import pandas as pd

def load_and_clean(path="data/sample_user_data.csv"):
    df = pd.read_csv(path)
    df.dropna(inplace=True)
    return df
