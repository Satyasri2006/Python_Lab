#4.1
#ii.
import pandas as pd
data=[10,20,30,40,50]
series=pd.Series(data)
python_list=series.tolist()
print("Converted Python List:")
print(python_list)
print("Type of Object:")
print(type(python_list))
