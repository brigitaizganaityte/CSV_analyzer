import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data2.csv")

print(df.head())

#main statistic of the file
#describe - only describes numerical columns
print("Statistics: ")
print(df.describe())

#missing values in each column
print("Missing values:")
print(df.isnull().sum())

#creating diagram - products vs amount
plt.figure(figsize=(8, 5))
plt.bar(df["Product"], df["Amount"], color='skyblue')
plt.xlabel("Product")
plt.ylabel("Amount")
plt.title("Amount of products that were sold")
plt.xticks(rotation=45)
plt.show()