# %%
#1.Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.

try:
    x=9/0
except ZeroDivisionError:
    print("can't divide by zero")


# %%
#2.Write a Python program that prompts the user to input an integer and raises a
#  ValueError exception if the input is not a valid integer.

try:
    integ=int(input("input an integer"))
except ValueError:
    print("Not an integer")

# %%
#3.Write a Python program that opens a file and handles a 
# FileNotFoundError exception if the file does not exist.
try:
    with open("nonexist.txt", "r") as f:
        data = f.read()
except FileNotFoundError:
    print("File not found.")



# %%
#4.Write a Python program that prompts the user to 
# input two numbers and raises a TypeError exception if the inputs are not numerical.
try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
except ValueError:
    raise TypeError("Inputs must be numerical.")


# %%
#5.
try:
    with open("example.txt", "r") as f:
        print(f.read())
except PermissionError:
    print("Permission denied.")

# %%
#6.Write a Python program that executes an operation on a 
# list and handles an IndexError exception if the index is out of range.
list = [1,2,3]
try:
    print(list[6])
except IndexError:
    print("Index out of range.")


# %%
#7.Write a Python program that prompts the user to input a number 
# and handles a KeyboardInterrupt exception if the user cancels the input.
try:
    n = input("Enter a number: ")
except KeyboardInterrupt:
    print("cancelled by user")


# %%
#8.Write a Python program that executes division and handles 
# an ArithmeticError exception if there is an arithmetic error.


try:
    x = 10 / 0
except ArithmeticError:
    print("Arithmetic error occurred.")

# %%
#9.Write a Python program that opens a file and handles a 
# UnicodeDecodeError exception if there is an encoding issue.

try:
    with open("example9.txt", "r", encoding="ascii") as f:
        print(f.read())
except UnicodeDecodeError:
    print("Unicode decoding error.")

# %%
#10.Write a Python program that executes a list operation and
#  handles an AttributeError exception if the attribute does not exist.
try:
    n = 5
    n.append(1)
except AttributeError:
    print("Attribute does not exist.")


# %% [markdown]
# --File I/O exercises

# %%
#1.
with open("test1.txt", "r") as f:
    print(f.read)

# %%
#2.
n = 4
with open("test1.txt", "r") as f:
    for i in range(n):
        print(f.readline(), end="")

# %%
#3.
with open("test1.txt", "a") as f:
    f.write("\nAppended line.")
with open("test1.txt", "r") as f:
    print(f.read())

# %%
#4.
n = 4
with open("test1.txt", "r") as f:
    lines = f.readlines()
    for line in lines[-n:]:
        print(line.strip())

# %%
#5.
with open("test1.txt", "r") as f:
    lines = f.readlines()

# %%
#6.
with open("test.txt", "r") as f:
    data = f.read()

# %%
#7.
with open("test.txt", "r") as f:
    array = [line.strip() for line in f]


# %%
#8.
with open("test1.txt", "r") as f:
    words = f.read().split()
    max_len = max(len(word) for word in words)
    longest = [word for word in words if len(word) == max_len]
    print(longest)

# %%
#9.
with open("test1.txt", "r") as f:
    print(sum(1 for _ in f))

# %%
#10.
from collections import Counter
with open("test1.txt", "r") as f:
    counts = Counter(f.read().split())
    print(counts)

# %%
# 11. File size
import os
size = os.path.getsize("test1.txt")
print(size)

# %%
# 12. Write list to file
items = ['apple', 'banana', 'cherry']
with open("fruits.txt", "w") as f:
    for item in items:
        f.write(item + "\n")

# %%
#13
with open("test1.txt", "r") as f1, open("copy.txt", "w") as f2:
    f2.write(f1.read())

# %%
# 14. Combine lines from two files
with open("copy.txt") as f1, open("test1.txt") as f2, open("example1.txt", "w") as out:
    for l1, l2 in zip(f1, f2):
        out.write(l1.strip() + " " + l2)

# %%
# 15. Read random line
import random
with open("test1.txt", "r") as f:
    lines = f.readlines()
    print(random.choice(lines))

# %%
# 16. Check if file is closed
f = open("test1.txt")
print(f.closed)
f.close()
print(f.closed)

# %%
# 17. Remove newline characters
with open("test1.txt", "r") as f:
    text = f.read().replace("\n", "")

# %%
#18.
with open("test1.txt") as f:
    text = f.read().replace(",", " ")
    print(len(text.split()))


# %%
# 19. Extract characters from files
chars = []
for name in ["test1.txt", "fruits.txt"]:
    with open(name) as f:
        chars.extend(list(f.read()))

# %%
#20.
import string
for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", "w") as f:
        f.write(letter)

# %%
#21.
letters = string.ascii_lowercase
num_per_line = 5
with open("letters.txt", "w") as f:
    for i in range(0, len(letters), num_per_line):
        f.write(letters[i:i+num_per_line] + "\n")


