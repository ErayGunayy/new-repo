import pandas as pd


df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=['A', 'B', 'C'])

df2 = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=['D', 'E', 'F'])


print(pd.concat([df, df2],axis=1))  # Output: True