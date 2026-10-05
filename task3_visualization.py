"""
TASK 3 - Data Visualization
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/books_scraped_sample.csv")

# 1. Price distribution
plt.figure(figsize=(10,6))
plt.hist(df["price_gbp"], bins=6)
plt.title("Distribution of Book Prices")
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")
plt.tight_layout()
plt.show()

# 2. Highest prices
top10 = df.nlargest(10, "price_gbp").sort_values("price_gbp")
plt.figure(figsize=(10,6))
plt.barh(top10["title"], top10["price_gbp"])
plt.title("10 Highest-Priced Books")
plt.xlabel("Price (£)")
plt.tight_layout()
plt.show()

# 3. Price bands
df["price_band"] = pd.cut(
    df["price_gbp"],
    bins=[0,20,40,60],
    labels=["£0–£20","£20–£40","£40–£60"],
    include_lowest=True
)
counts = df["price_band"].value_counts().sort_index()
plt.figure(figsize=(8,5))
plt.bar(counts.index.astype(str), counts.values)
plt.title("Books by Price Band")
plt.xlabel("Price Band")
plt.ylabel("Number of Books")
plt.tight_layout()
plt.show()

# 4. Listing order
plt.figure(figsize=(10,5))
plt.plot(range(1, len(df)+1), df["price_gbp"], marker="o")
plt.title("Book Price by Scraped Listing Order")
plt.xlabel("Listing Order")
plt.ylabel("Price (£)")
plt.tight_layout()
plt.show()
