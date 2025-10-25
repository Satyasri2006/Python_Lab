#4.2
#iv.
import numpy as np
import pandas as pd
data = {
	'Name': ['Alice', 'Bob', 'Charlie'],
	'Age': [25, 30, 27],
	'City': ['New York', 'London', 'Paris']
}
df=pd.DataFrame(data)
column_list=df.columns.tolist()
print("List of column headers:")
print(column_list)
