#mathOpertaions
def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide (a,b):
    if b==0:
         raise ValueError("cannot divide by zero")
    return a/b

if __name__=="__main__":
    print(add(5, 3))       # Output: 8
    print(subtract(5, 3))  # Output: 2
    print(multiply(5, 3))  # Output: 15
    print(divide(6, 2))    # Output: 3.0


#stringutils

def reverse_string(text):
       """Return the reversed string."""
       if not isinstance(text, str):
           raise TypeError("Input must be a string")
       return text[::-1]

def count_vowels(text):
       """Count vowels (a, e, i, o, u) in the string, case-insensitive."""
       if not isinstance(text, str):
           raise TypeError("Input must be a string")
       vowels = "aeiou"
       return sum(1 for char in text.lower() if char in vowels)
if __name__ == "__main__":
       # Test the functions
       print(reverse_string("hello"))      # Output: olleh
       print(count_vowels("hello"))        # Output: 2
       print(count_vowels("PYTHON"))       # Output: 1
       print(reverse_string(" asdasd"))           # Output: ""

#geometry package
import math

def calculate_area(radius):
       """Calculate the area of a circle given its radius."""
       if not isinstance(radius, (int, float)):
           raise TypeError("Radius must be a number")
       if radius < 0:
           raise ValueError("Radius cannot be negative")
       return math.pi * radius ** 2

def calculate_circumference(radius):
       """Calculate the circumference of a circle given its radius."""
       if not isinstance(radius, (int, float)):
           raise TypeError("Radius must be a number")
       if radius < 0:
           raise ValueError("Radius cannot be negative")
       return 2 * math.pi * radius

if __name__ == "__main__":
       # Test the functions
       print(calculate_area(5))         # Output: 78.53981633974483
       print(calculate_circumference(5))  # Output: 31.41592653589793


from .circle import calculate_area, calculate_circumference



#test
import math_operations
import string_utils
from geometry import calculate_area, calculate_circumference
from file_operations import read_file, write_file

def main():
       # Test math_operations
       print("Testing math_operations:")
       print(f"Add: {math_operations.add(10, 5)}")          # Output: 15
       print(f"Subtract: {math_operations.subtract(10, 5)}")  # Output: 5
       print(f"Multiply: {math_operations.multiply(10, 5)}")  # Output: 50
       try:
           print(f"Divide: {math_operations.divide(10, 2)}")  # Output: 5.0
           print(f"Divide by zero: {math_operations.divide(10, 0)}")
       except ValueError as e:
           print(f"Error: {e}")

       # Test string_utils
       print("\nTesting string_utils:")
       print(f"Reverse 'hello': {string_utils.reverse_string('hello')}")  # Output: olleh
       print(f"Vowels in 'hello': {string_utils.count_vowels('hello')}")  # Output: 2
       try:
           string_utils.reverse_string(123)  # Should raise TypeError
       except TypeError as e:
           print(f"Error: {e}")

       # Test geometry
       print("\nTesting geometry:")
       print(f"Area of circle (r=5): {calculate_area(5)}")          # Output: 78.53981633974483
       print(f"Circumference (r=5): {calculate_circumference(5)}")  # Output: 31.41592653589793
       try:
           calculate_area(-1)  # Should raise ValueError
       except ValueError as e:
           print(f"Error: {e}")

       # Test file_operations
       print("\nTesting file_operations:")
       try:
           write_file("test.txt", "This is a test file.\nHello, world!")
           content = read_file("test.txt")
           print(f"File content:\n{content}")
       except Exception as e:
           print(f"Error: {e}")

if __name__ == "__main__":
       main()

