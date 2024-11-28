#https://colab.research.google.com/drive/1Tt_Z9bsdUbjvaJjTkeTWj9BUvq3aq9CK?usp=sharing


import pandas as pd


file_path = 'iris.csv' 
data = pd.read_csv(file_path)

print("Podgląd danych za pomocą head():")
print(data.head())  # Wyświetla pierwsze 5 wierszy

print("\nPodgląd danych za pomocą tail():")
print(data.tail())  # Wyświetla ostatnie 5 wierszy

print("\nOpis statystyczny danych za pomocą describe():")
print(data.describe())  # Statystyki opisowe dla kolumn numerycznych

numeric_columns = data.select_dtypes(include='number')

mean_values = numeric_columns.mean()
median_values = numeric_columns.median()

print("\nŚrednie wartości dla kolumn numerycznych:")
print(mean_values)

print("\nMedianowe wartości dla kolumn numerycznych:")
print(median_values)

threshold = float(input("\nPodaj wartość progu dla petallength (≥): "))

filtered_data = data[data['petallength'] >= threshold]

print("\nPodgląd przefiltrowanych danych (pierwsze 5 wierszy):")
print(filtered_data.head())


