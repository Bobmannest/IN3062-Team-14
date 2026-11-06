import os
import pandas as pd

path = "."

filename_read = os.path.join(path, "anime-dataset-2026.csv")
df = pd.read_csv(filename_read)
print(df.columns.tolist(), "\n")
print(df['Image URL'][0], "\n")
print(df[0:-1])