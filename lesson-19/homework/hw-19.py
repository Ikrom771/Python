# %% [markdown]
# Homework Assignment 1: Analyzing Sales Data
# 
# You are given a dataset containing sales data for an e-commerce website. The dataset (task\sales_data.csv) has the following columns:
# 
#    Date: Date of the sale.
#    Product: Name of the product sold.
#     Category: Category to which the product belongs.
#     Quantity: Number of units sold.
#     Price: Price per unit.
# 
# 
# 
# Tasks:
# 
# Group the data by the Category column and calculate the following aggregate statistics for each category:
# --Total quantity sold.
# --Average price per unit.
# --Maximum quantity sold in a single transaction.
# Identify the top-selling product in each category based on the total quantity sold.
# Find the date on which the highest total sales (quantity * price) occurred.

# %%
import pandas as pd
sales_data = pd.read_csv('sales_data.csv')



# %%
print("Total quantity sold by category:")
print(sales_data.groupby('Category')['Quantity'].sum())

# %%
print("Average price per unit by category:")
print(sales_data.groupby('Category')['Price'].mean())

# %%
print("Maximum quantity sold in a single transaction by category:")
print(sales_data.groupby('Category')['Quantity'].max())

# %%
print('Top selling product in each category based on total quantity sold:')
print(sales_data.groupby('Category').apply(lambda x: x.loc[x['Quantity'].idxmax(), 'Product']))

# %%

sales_data['Total_Sales']=sales_data['Quantity']*sales_data['Price']
max_sales_idx = sales_data['Total_Sales'].idxmax()
print("Date with highest total sales:")
print(sales_data.loc[max_sales_idx, 'Date'])

# %% [markdown]
# # Homework Assignment 2: Examining Customer Orders
# 
# You have a dataset (task\customer_orders.csv) containing information about customer orders. The dataset has the following columns:
# 
# OrderID: Unique identifier for each order.
# CustomerID: Unique identifier for each customer.
# Product: Name of the product ordered.
# Quantity: Number of units ordered.
# Price: Price per unit.
# 
# 
# ** Tasks:**
# 
# Group the data by CustomerID and filter out customers who have made less than 20 orders.
# Identify customers who have ordered products with an average price per unit greater than $120.
# Find the total quantity and total price for each product ordered, and filter out products that have a total quantity less than 5 units.

# %%
cus_orders=pd.read_csv('customer_orders.csv')
cus_orders.head()

# %%
print("customers with less than 20 orders:")
print(cus_orders.groupby('CustomerID').filter(lambda x: x['OrderID'].count() < 20))

# %%
print('Customers who ordered products with an average price per unit greater than $120:')
print(cus_orders.groupby('CustomerID').filter(lambda x:(x['Price'].mean() > 120)))

# %%
print("Products with total quantity and price, filtered by quantity<5 ")
product_data= sales_data.groupby('Product').agg({'Quantity': 'sum', 'Price': 'sum'})
print(product_data[product_data['Quantity']>5])

# %% [markdown]
# # Homework Assignment 3: Population Salary Analysis
# 
# "task\population.db" sqlite database has population table.
# "task\population salary analysis.xlsx" file defines Salary Band categories.
# Read the data from population table and calculate following measures:
# Percentage of population for each salary category;
# Average salary in each salary category;
# Median salary in each salary category;
# Number of population in each salary category;
# Calculate the same measures in each State
# Note: Use SQL only to select data from database. All the other calculations should be done in python.

# %%
import pandas as pd
import sqlite3 
import numpy as np


# %%
db_path= 'population.db'
conn= sqlite3.connect(db_path)
query= 'SELECT * FROM population'

# %%
df2=pd.read_sql_query(query, conn)
print(df2.head())
print(df2.describe())
conn.close()

# %%
salary_bands = [
    ("till $200,000", 0, 200_000),
    ("$200,001 - $400,000", 200_001, 400_000),
    ("$400,001 - $600,000", 400_001, 600_000),
    ("$600,001 - $800,000", 600_001, 800_000),
    ("$800,001 - $1,000,000", 800_001, 1_000_000),
    ("$1,000,001 - $1,200,000", 1_000_001, 1_200_000),
    ("$1,200,001 - $1,400,000", 1_200_001, 1_400_000),
    ("$1,400,001 - $1,600,000", 1_400_001, 1_600_000),
    ("$1,600,001 - $1,800,000", 1_600_001, 1_800_000),
    ("$1,800,001 and over", 1_800_001, float("inf"))
]

def get_salary_band(sal):
    for band, low, high in salary_bands:
        if low <= sal <= high:
            return band
    return "Undefined"

df2['SalaryCategory'] = df2['salary'].apply(get_salary_band)


# %%
total_pop = len(df2)
overall = (
    df2.groupby('SalaryCategory')['salary']
    .agg(count='count', average='mean', median='median')
    .reset_index()
)
overall['percentage'] = round(overall['count'] / total_pop * 100, 2)
overall['average'] = round(overall['average'], 2)
overall['median'] = round(overall['median'], 2)

print("\nOverall by Salary Category:\n", overall)

# %%
total_population = len(df2)
print(f"Total population: {total_population}")



# %%
by_state = (
    df2.groupby(['state'])['salary']
    .agg(count='count', average='mean', median='median')
    
)
by_state['percentage'] = by_state.groupby('state')['count'].apply(lambda x: round(x / x.sum() * 100, 2))
by_state['average'] = round(by_state['average'], 2)
by_state['median'] = round(by_state['median'], 2)

print("\nBy State and Salary Category:\n", by_state)


