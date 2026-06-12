import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 


# Read CSV and skip problematic rows
df = pd.read_csv('sampledata.csv', on_bad_lines='skip')

df.groupby('')
#num_data = df.select_dtypes(include=['int','float'])
#sns.heatmap(num_data.corr(), annot=True)

#plt.scatter(num_data['Age'], num_data['Salary'])
#plt.show()


# salaries = [100,200,300,400,32423434]
# #sns.boxplot(y=salaries)

# sns.boxplot(data=df, x='Deparntment', y='Salary')
# plt.show()

