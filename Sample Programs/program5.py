import pandas as pd
import matplotlib.pyplot as plt

# Read CSV and skip problematic rows
df = pd.read_csv('sampledata.csv', on_bad_lines='skip')

# Select numeric columns
numeric_data = df.select_dtypes(include=['number'])

# Histograms for numeric columns
for column in numeric_data.columns:
    plt.figure(figsize=(6, 4))
    plt.title(f"Histogram of {column}")
    plt.hist(numeric_data[column].dropna(), edgecolor='black')
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.show()

# Select text columns
text_data = df.select_dtypes(include=['object'])

print("Text Columns:", text_data.columns.tolist())

# Bar charts for text columns
for column in text_data.columns:
    data = text_data[column].value_counts().head(10)

    plt.figure(figsize=(8, 5))
    plt.title(f"Bar Chart of {column}")
    plt.bar(data.index, data.values)
    plt.xlabel(column)
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()