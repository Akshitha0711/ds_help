import pandas as pd
import numpy as np

def column_detector(df):
    column_types = {}
    for col in df.columns:
        dtype = df[col].dtype
        unique_count = df[col].nunique()
        
        if unique_count < 20:
            column_types[col] = 'categorical'
        elif dtype in ['float64', 'int64']:
            column_types[col] = 'numerical'
        elif dtype in ['object']:
            column_types[col] = 'categorical/text'
    
    return column_types


df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': ['apple', 'banana', 'apple', 'orange', 'banana'],
    'C': [0.1, 0.2, 0.3, 0.4, 0.5]
})

print(column_detector(df))