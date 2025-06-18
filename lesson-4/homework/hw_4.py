# %%
#1.Write a Python script to sort (ascending and descending) a dictionary by value.
# Sample dictionary
data = {'apple': 50, 'banana': 20, 'cherry': 30, 'date': 40}

# Sort dictionary by value in ascending order
asc_sorted = dict(sorted(data.items(), key=lambda item: item[1]))
print("Ascending:", asc_sorted)

# Sort dictionary by value in descending order
desc_sorted = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))
print("Descending:", desc_sorted)



# %%
#2.Write a Python script to add a key to a dictionary.

data2={0: 10, 1: 20}


data2[2]=30 

print(data2)

# %%
#3.Write a Python script to concatenate the following dictionaries to create a new one.

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

merged=dic1|dic2|dic3
print(merged)

# %%
#4.Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).

n=int(input("Enter Number:"))

dict_sq={x:x*x for x in range(1, n+1)}

print(dict_sq)

# %%
#5.Write a Python script to print a dictionary where the keys are numbers
#  between 1 and 15 (both included) and the values are the square of the keys.

dict_sq2={x:x*x for x in range(1, 16)}

print(dict_sq2)


# %%
#6.Write a Python program to create a set.
set_1={'one', 'two', 'three'}

print(set_1)

# %%
#7. Write a Python program to iterate over sets.
iter_set={1,3,5,8}

for item in iter_set:
    print(item)



# %%
#8.Write a Python program to add member(s) to a set.

iter_set={1,3,5,8}
iter_set.add(9)
print(iter_set)

# %%
#9.Write a Python program to remove item(s) from a given set.

iter_set={1,3,5,8}
iter_set.remove(3)
print(iter_set)

# %%
#10.Write a Python program to remove an item from a set if it is present in the set.

iter_set={1,3,5,8}
item=6
if item in iter_set:
    iter_set.remove(item)
print(iter_set)





