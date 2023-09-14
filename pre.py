import pandas as pd

df = pd.read_csv('myntra.csv')

def  preprocess():
    global df
    df = df.groupby('Category').sum()['DiscountPrice (in Rs)']

    return df