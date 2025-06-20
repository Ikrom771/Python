# %%
##1.Given a string txt, insert an underscore (_) after every third character. 
# If a character is a vowel or already has an underscore after it, 
# shift the underscore placement to the next character. 
# No underscore should be added at the end

txt = input("Enter a string: ")
vowels = 'aeiouAEIOU'
result = ''
i = 0
count = 0

while i < len(txt):
    result += txt[i]
    count += 1

    if count == 3:
        next_pos = i + 1
        if txt[i] in vowels or (next_pos < len(txt) and txt[next_pos] == '_'):
            # Shift underscore forward
            j = next_pos
            while j < len(txt) and (txt[j] in vowels or txt[j] == '_'):
                result += txt[j]
                i += 1
                j += 1
            if j < len(txt) and txt[j] not in vowels and txt[j] != '_':
                result += '_'
        else:
            if i + 1 < len(txt):
                result += '_'
        count = 0
    i += 1

# Remove trailing underscore if any
if result.endswith('_'):
    result = result[:-1]

print(result)



# %%
##2.The provided code stub reads an integer, n, from STDIN. 
# For all non-negative integers i where 0 <= i < n, print i^2.

n=int(input("input positive number:"))

if n < 0 or n > 20:
    print("❌ Input must be between 0 and 20")
else:
    for i in range(n):
        print(i * i)
          



# %%
##3.
# Exercise 1: Print first 10 natural numbers using a while loop

for i in range(1,11):
    print(i)

# %%
#Exercise 2: Print the following pattern
n=int(input("enter natural number"))
for i in range(n):
    for j in range(i):
        print(j+1,end=' ')
    print()

# %%
#Exercise 3: Calculate sum of all numbers from 1 to a given number
n=int(input("enter natural number"))
sum=0
for i in range(1,n+1):
    sum+=i
    
print(sum)

# %%
#Exercise 4: Print multiplication table of a given number
n=int(input("enter natural number"))

for i in range(1,11):
    print(i*n)


# %%
#Exercise 5: Display numbers from a list using a loop
numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    if num > 500:
        break
    if num > 150:
        continue  
    if num % 5 == 0 and num >= 75:
        print(num)

# %%
#Exercise 6: Count the total number of digits in a number
n=int(input("enter natural number"))

while n>0:
    n=n//10
    count+=1
print(count)

# %%
#Exercise 7: Print reverse number pattern
n=int(input("enter natural number"))

for i in range(n):
    for j in range(n-i, 0, -1):
        print(j,end=' ')
    print()  ##new line

# %%
#Exercise 8: Print list in reverse order using a loop
list1 = [10, 20, 30, 40, 50]

for i in range(len(list1)-1, -1, -1):
    print(list1[i])

# %%
#Exercise 9: Display numbers from -10 to -1 using a for loop

for i in range(-10,0):
    print(i)

# %%
#Exercise 10: Display message “Done” after successful loop execution
n= int(input("Input a number"))
for i in range(n):
    print(i)
print("Done!")

# %%
#Exercise 11: Print all prime numbers within a range

for num in range(2, 40):  # Start from 2 (1 is not prime)
    is_prime = True
    for i in range(2, int(num**0.5) + 1):  # Check up to √num
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)

# %%
n1, n2 = 0, 1  # first two Fibonacci numbers
count = 0

while count < 10:
    print(n1)
    nth = n1 + n2  # next term
    n1 = n2        # shift: first becomes second
    n2 = nth       # next becomes second
    count += 1

# %%
#Exercise 13: Find the factorial of a given number
n= int(input("Input a number"))
i=1
fac=1
while i<=n:
    fac*=i
    i+=1
print(fac)


# %%
#4.Return the elements that are not common between two lists. 
# The order of elements does not matter.

list1 = input("Enter list one (comma-separated): ").split(',')
list2 = input("Enter list two (comma-separated): ").split(',')

result = []

for i in list1:
    if i not in list2:
        result.append(i)

for j in list2:
    if j not in list1:
        result.append(j)

print(result)





