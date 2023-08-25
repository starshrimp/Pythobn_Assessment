import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/stawiskm/pythoncourse/teacher/Code_Examples/Day%204/Data/cardio.csv')

print(data.dtypes)
print(data.head(10))