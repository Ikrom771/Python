# %%
#1.def is_leap(year): """ Determines whether a given year is a leap year.

year_inp=int(input("Enter year:"))

is_leap= (year_inp %4==0 and year_inp %100==0) or (year_inp % 4==0)
print(is_leap)


# %% [markdown]
# #2.Given an integer, n, perform the following conditional actions:
# 
# --If n is odd, print Weird\n
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird

# %%
n= int(input("Enter an integer"))  # input an integer

if n < 1 or n > 100:
    print("Input must be between 1 and 100.")

elif n%2 !=0:
    print("weird")
elif(n%2==0 and n in range(2,5)):
    print("Not weird")
elif(n%2==0 and n in range(6,20)):
    print("weird")
elif(n%2==0 and n>20):
    print("Not weird")

# %%
#3. with If-else

a = int(input("Enter a: "))
b = int(input("Enter b: "))

# Ensure a is less than or equal to b
if a > b:
    a, b = b, a

evens = [x for x in range(a, b + 1) if x % 2 == 0]
print(evens)

# %%
#3. without if-else
a = int(input("Enter a: "))
b = int(input("Enter b: "))

# Using min() and max() to avoid if-else
evens = [x for x in range(min(a, b), max(a, b) + 1) if x % 2 == 0]
print(evens)

# %%




