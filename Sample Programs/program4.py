import pandas as pd


df = pd.read_csv('sampledata.csv')

print(df['Age'].duplicated().sum())

count = df['Age'].drop_duplicates().duplicated().sum()
print(count)
print(df.isna().sum())

numeric_cols = df.select_dtypes(include=['int','float'])

category_col = df.select_dtypes(exclude=['int','float'])

numeric_cols.fillna(0, inplace=True)

print(numeric_cols.isna().sum())
b=numeric_cols['Age'].mean()

numeric_cols['Age'].fillna(b)