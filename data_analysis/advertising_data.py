import os

import pandas as pd
from utilities.config import DATA_DIR

df = pd.read_csv(os.path.join(DATA_DIR, "Advertising.csv"), )
df = df.iloc[:, 1:]
print(df)
print(df.info())
print(df.describe())

print(df.TV.plot())
