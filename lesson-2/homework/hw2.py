##1. Age calculator

# Ask for  name
name = input("Enter your name: ")

# Ask for birth
birth_year = int(input("Enter your year of birth: "))

current_year = 2025

age = current_year - birth_year

# Display the result
print(f"Hello {name}, you are {age} years old.")



##2. Extract Car Names
txt = 'LMaasleitbtui'

txt[1::2]  ##Malibu
txt[::2]    ##Lasetti

#3. Extract Car names
txt = 'MsaatmiazD'

txt[::2]   #Matiz

txt[9:0:-2]



#4.Extract residence area.
txt = "I'am John. I am from London"

txt[21:27:1]



#5. Reverse String
user_string= input('Enter string:')
reversed_string = user_string[::-1]
print('Reversed string:', reversed_string)


#6. Count Vowels
user_string= input("enter a string: ")

vowels='AaOoUuIieE'
vowel_count = sum(1 for char in user_string if char in vowels)

print("Nemer of vowels:", vowel_count)


#7. Find Maximum Value

user_input = input("Enter a list of numbers separated by spaces: ")


numbers = list(map(int, user_input.split()))

max_value = max(numbers)

print(f"The maximum value is: {max_value}")


#8. Check Palindrome

word=input("Enter a word:")
is_palindrome = word == word[::-1]

print(f"The word '{word}' is a palindrome: {is_palindrome}")




#9. Extract Email Domain
email = input("Enter your email address: ")

domain = email.split('@')[-1]

print(f"The domain is: {domain}")



#10. Generate Random Password
import random
import string

# Define the characters to use in the password
characters = string.ascii_letters + string.digits + string.punctuation

# Generate a random password of length 8
password = ''.join(random.choice(characters) for _ in range(8))

# Print the generated password
print(f"Generated password: {password}")


