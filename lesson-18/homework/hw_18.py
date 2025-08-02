# %% [markdown]
# Homework 2:
# Find all questions that were created before 2014
# Find all questions with a score more than 50
# Find all questions with a score between 50 and 100
# Find all questions answered by Scott Boston
# Find all questions answered by the following 5 users
# Find all questions that were created between March, 2014 and October 2014 that were answered by Unutbu and have score less than 5.
# Find all questions that have score between 5 and 10 or have a view count of greater than 10,000
# Find all questions that are not answered by Scott Boston

# %%
import pandas as pd
df = pd.read_csv('tackoverflow_qa.csv')

df.head()

# %%
print('Questions created before 2014:')
print(df[df['creationdate'] < '2014-01-01'])

# %%
print('Questions with a score more than 50:')
print(df[df['score']>50])

# %%
print('Questions with score btw 50 and 100:\n')
print(df[df['score'].between(50, 100)])
#print(df[(df['score']>=50) & (df['score']<=100)])

# %%
print('Question answeres by Scott Boston:\n')
print(df[df['ans_name'] == 'Scott Boston'])

# %%
print('questions answered by the following 5 users')
print(df[df['ans_name'].isin(['Scott Boston', 'John Smith', 'Jane Doe', 'Alice Johnson', 'Bob Brown'])])

# %%
print('questions that were created between March, 2014 and October 2014 that were answered by Unutbu and have score less than 5.')
print(df[(df['creationdate'].between('2014-03-01', '2014-10-31')) & (df['ans_name'] == 'Unutbu') & (df['score'] < 5)])

# %%
print('Questions that have score between 5 and 10 or have a view count of greater than 10,000:')
print(df[(df['score'].between(5, 10)) | (df['viewcount'] > 10000)])

# %%
print('Questions not answered by Scott Boston:')
print(df[df['ans_name'] != 'Scott Boston'])

# %% [markdown]
# --Homework2
# 1.  Select Female Passengers in Class 1 with Ages between 20 and 30: Extract a DataFrame containing female passengers in Class 1 with ages between 20 and 30.
# 
# 2. Filter Passengers Who Paid More than $100: Create a DataFrame with passengers who paid a fare greater than $100.
# 
# Select Passengers Who Survived and Were Alone: Filter passengers who survived and were traveling alone (no siblings, spouses, parents, or children).
# 
# Filter Passengers Embarked from 'C' and Paid More Than $50: Create a DataFrame with passengers who embarked from 'C' and paid more than $50.
# 
# Select Passengers with Siblings or Spouses and Parents or Children: Extract passengers who had both siblings or spouses aboard and parents or children aboard.
# 
# Filter Passengers Aged 15 or Younger Who Didn't Survive: Create a DataFrame with passengers aged 15 or younger who did not survive.
# 
# Select Passengers with Cabins and Fare Greater Than $200: Extract passengers with known cabin numbers and a fare greater than $200.
# 
# Filter Passengers with Odd-Numbered Passenger IDs: Create a DataFrame with passengers whose PassengerId is an odd number.
# 
# Select Passengers with Unique Ticket Numbers: Extract a DataFrame with passengers having unique ticket numbers.
# 
# Filter Passengers with 'Miss' in Their Name and Were in Class 1: Create a DataFrame with female passengers having 'Miss' in their name and were in Class 1.

# %%
import pandas as pd
df2=pd.read_csv('titanic.csv')
df2.reset_index(drop=True, inplace=True)
df2.head()
df2.describe()

# %%


# %%

print('Female Passengers in Class 1 with Ages between 20 and 30:\n')
print(df2[(df2['Sex']=='female') & (df2['Pclass']==1) & (df2['Age'].between(20, 30))])

# %%
print(' Passengers Who Paid More than $100:\n')
print(df2[df2['Fare']>100])

# %%
print('Passengers Who Survived and Were Alone:\n')
print(df2[(df2['Survived']==0) & (df2['SibSp']==0) & (df2['Parch']==0)])

# %%
print('Passengers Embarked from "C" and Paid More Than $50:\n')
print(df2[(df2['Embarked']=='C') & (df2['Fare']>50)])

# %%
print('Passengers with Siblings or Spouses and Parents or Children:\n')
print(df2[(df2['SibSp'] > 0) & (df2['Parch']>0)])

# %%
print("Passengers Aged 15 or Younger Who Didn't Survive:\n" )
print(df2[(df2['Age']<=15) & (df2['Survived']==1)])

# %%
print('Passengers with Cabins and Fare Greater Than $200:\n')
print(df2[(df2['Cabin'].notnull()) & (df2['Fare']>200)])

# %%
print('Passengers with Odd-Numbered Passenger IDs:\n')
print(df2[df2['PassengerId'] % 2 == 1])

# %%
print("Passengers with Unique Ticket Numbers: \n")
print(df2[df2['Ticket'].duplicated(keep=False) == False])

# %%
print("Passengers with 'Miss' in Their Name and Were in Class 1:\n")
print(df2[(df2['Name'].str.contains('Miss')) & (df2['Pclass']==1)])


