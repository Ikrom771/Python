# %% [markdown]
# Homework 1:
# 
# import pandas as pd
# 
# data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [25, 30, 35, 40], 'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']} df = pd.DataFrame(data)
# 
# Rename column names using function. "First Name" --> "first_name", "Age" --> "age
# Print the first 3 rows of the DataFrame
# Find the mean age of the individuals
# Select and print only the 'Name' and 'City' columns
# Add a new column 'Salary' with random salary values
# Display summary statistics of the DataFrame

# %%
import pandas as pd

data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'], 
'Age': [25, 30, 35, 40], 
'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
} 
df = pd.DataFrame(data)

print(df.head())  # Display the first few rows of the DataFrame


# %%
df.rename(columns={'First Name': 'first_name', 'Age': 'age'}, inplace=True)
print(df)

# %%
print(df.head(3))  # Display the first three rows of the DataFrame

# %%
print(df['age'].mean())  # Calculate the mean of the 'age' column  

# %%
print(df[['first_name','City']])

# %%
import random

# Create a list of 4 random salaries between 50000 and 100000
salaries = [random.randint(50000, 100000) for _ in range(len(df))]

# Add it to the DataFrame
df['salary'] = salaries
print(df)


# %%
print(df.describe())  # Display summary statistics of the DataFrame

# %% [markdown]
# Homework 2:
# 
# Create a DataFrame named sales_and_expenses with columns 'Month', 'Sales', and 'Expenses', representing monthly sales and expenses data. Use below table.
# Month	Sales	Expenses
# Jan	5000	3000
# Feb	6000	3500
# Mar	7500	4000
# Apr	8000	4500
# ---Calculate and display the maximum sales and expenses.
# ---Calculate and display the minimum sales and expenses.
# ---Calculate and display the average sales and expenses.

# %%
sales_and_expenses = {'Month': ['January', 'February', 'March', 'April'],
'Sales': [5000 , 6000, 7500, 8000],
'Expenses': [3000, 3500, 4000, 4500]
}

df=pd.DataFrame(sales_and_expenses)
print(df)

# %%
print("Maximum sales and expenses:")
print(df[['Sales', 'Expenses']].max())  # Maximum sales and expenses
print("Minimum sales and expenses:")
print(df[['Sales', 'Expenses']].min())  # Minimum sales and expenses
print("Average sales and expenses:")
print(df[['Sales', 'Expenses']].mean())  # Average sales and expenses
print("Total sales and expenses:")
print(df[['Sales', 'Expenses']].sum())  # Total sales and expenses

# %% [markdown]
# Homework 3:
# 
# Create a DataFrame named expenses with columns 'Category', 'January', 'February', 'March', and 'April', representing monthly expenses for different categories. Use below table.
# Category	January	February	March	April
# Rent	1200	1300	1400	1500
# Utilities	200	220	240	250
# Groceries	300	320	330	350
# Entertainment	150	160	170	180
# --Calculate and display the maximum expense for each category.
# --Calculate and display the minimum expense for each category.
# --Calculate and display the average expense for each category.
# --In this task, use .set_index method to make Category column as index.
# 
# Try this code, learn it and use it in the task.
# 
# expenses.set_index('Category')

# %%

expenses={'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
     'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
     }


df_expenses = pd.DataFrame(expenses)
df_expenses = df_expenses.set_index('Category')
print(df_expenses)

# %%
print("Maximum expense for each category:")
print(df_expenses.max(axis=1))  # Maximum expense for each category
print("Minimum expense for each category:")
print(df_expenses.min(axis=1))  # Minimum expense for each category   
print("Average expense for each category:")  
print(df_expenses.mean(axis=1))  # Average expense for each category

# %%



