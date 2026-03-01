import pandas as pd
from scipy.io import arff

data, meta = arff.loadarff('dataset.arff')
df = pd.DataFrame(data)

for col in df.select_dtypes([object]):
    df[col] = df[col].str.decode('utf-8')

df.to_csv('dataset.csv', index=False)

print("Conversion successful! dataset.csv created.")