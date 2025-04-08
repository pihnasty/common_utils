import pandas as pd


def write_csv(df: pd.DataFrame, file_path: str):
    with open(file_path, mode='w', newline='') as file:
        df.to_csv(file, sep=';', decimal=',', index=False)
