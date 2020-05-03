import plot_functions.chapter_two_plots as c2
import pandas as pd
import numpy as np
import os

DATA_DIR = r"C:\project_data\ISLR"

df = pd.read_csv(os.path.join(DATA_DIR, "Advertising.csv"), )
df = df.iloc[:, 1:]
print(df)
print(df.info())
print(df.describe())

print(df.TV.plot())
