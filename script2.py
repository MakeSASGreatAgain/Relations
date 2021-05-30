import pandas as pd

path = 'data.htm'
with open(path) as f:
    data = pd.read_html(f)
data = data[0]

table1 = data[0:8][[7, 8]].dropna().drop([0, 1])

data1 = data.fillna(0)
data1 = data1[9:][0]
names = data1.drop_duplicates().drop([11, 12])
table2 = data[9:].dropna()
table2[0] = names.values