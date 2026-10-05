"""
TASK 2 - Exploratory Data Analysis
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/books_scraped_sample.csv")

print("Shape:", df.shape)
print("\nData types:")
print(df.dtypes)
print("\nMissing values:")
print(df.isna().sum())
print("\nDescriptive statistics:")
print(df.describe(include="all"))

print("\nMost expensive books:")
print(df.nlargest(10, "price_gbp")[["title", "price_gbp"]])

print("\nPrice-band counts:")
print(df["price_band"].value_counts().sort_index())

# Basic hypothesis:
# H0: the mean sample price is £30 or less.
# H1: the mean sample price is greater than £30.
# The sample mean is compared with £30 descriptively.
mean_price = df["price_gbp"].mean()
print(f"\nSample mean price: £{mean_price:.2f}")
print("Descriptive conclusion:", "above £30" if mean_price > 30 else "£30 or below")

# IQR anomaly check
q1 = df["price_gbp"].quantile(0.25)
q3 = df["price_gbp"].quantile(0.75)
iqr = q3 - q1
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr
outliers = df[(df["price_gbp"] < lower) | (df["price_gbp"] > upper)]
print("\nIQR bounds:", lower, upper)
print("Potential outliers:")
print(outliers[["title", "price_gbp"]])
