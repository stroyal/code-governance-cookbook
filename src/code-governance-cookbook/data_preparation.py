import pandas as pd

def load_data(filename: str) -> pd.DataFrame:
    """
    Load the data from the given filename
    """
    # Load the data
    data = pd.read_csv(filename)
    return data

def clean_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the data
    """
    # Drop missing values
    data = data.dropna()
    return data