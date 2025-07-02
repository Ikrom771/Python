# %%
#1.
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

# Example
c = Circle(5)
print("Area:", c.area())
print("Perimeter:", c.perimeter())


# %%
#2.
from datetime import datetime

class Person:
    def __init__(self, name, country, birth_date):  # birth_date in 'YYYY-MM-DD'
        self.name = name
        self.country = country
        self.birth_date = datetime.strptime(birth_date, '%Y-%m-%d')

    def age(self):
        today = datetime.today()
        return today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))

# Example
p = Person("Ikrom", "Uzbekistan", "1993-06-29")
print("Name:", p.name)
print("Age:", p.age())


# %%
#3.
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"

# Example
calc = Calculator()
print("Add:", calc.multiply(10, 5))
print("Divide:", calc.divide(10, 0))


# %%
#4.
import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

# Example
s = Circle(7)
print("Square Area:", s.area())
print("Square Perimeter:", s.perimeter())


# %%
#5.
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        def _insert(node, value):
            if not node:
                return Node(value)
            if value < node.value:
                node.left = _insert(node.left, value)
            else:
                node.right = _insert(node.right, value)
            return node

        self.root = _insert(self.root, value)

    def search(self, value):
        def _search(node, value):
            if not node:
                return False
            if value == node.value:
                return True
            elif value < node.value:
                return _search(node.left, value)
            else:
                return _search(node.right, value)

        return _search(self.root, value)

# Example
bst = BST()
bst.insert(10)
bst.insert(5)
print("Found 5?", bst.search(5))


# %%
#6.
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        return "Stack is empty"

# Example
s = Stack()
s.push(1)
s.push(4)
s.push(9)
print(s.pop())  # 2


# %%
#7.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next

# Example
ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.display()


# %%
#8.
class Cart:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price):
        self.items[name] = self.items.get(name, 0) + price

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]

    def total(self):
        return sum(self.items.values())

# Example
c = Cart()
c.add_item("Book", 15)
c.add_item("Pen", 2)
c.remove_item("Pen")
print("Total:", c.total())


# %%
#9.
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        return "Empty"

    def display(self):
        print("Stack:", self.stack)

# Example
s = Stack()
s.push(3)
s.push(5)

s.display()


# %%
#10.
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        return "Queue is empty"

# Example
q = Queue()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())  # 1


# %%
class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, balance=0):
        self.accounts[name] = balance

    def deposit(self, name, amount):
        if name in self.accounts:
            self.accounts[name] += amount

    def withdraw(self, name, amount):
        if name in self.accounts and self.accounts[name] >= amount:
            self.accounts[name] -= amount
        else:
            return "Insufficient funds"

    def check_balance(self, name):
        return self.accounts.get(name, "Account not found")

# Example
b = Bank()
b.create_account("Ikrom", 1000)
b.deposit("Ikrom", 500)
print("Balance:", b.check_balance("Ikrom"))



