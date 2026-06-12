
import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv('sampledata.csv', on_bad_lines='skip')

s= df.groupby('Deparntment')['Salary'].max()
print(s)

x=s.keys().to_list()
y=s.values.tolist()

plt.bar(x,y)
plt.show()