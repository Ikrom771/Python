# %%
class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = False  # False = incomplete, True = complete

    def mark_complete(self):
        self.status = True

class ToDoList:
    def __init__(self):
        self.task_list=[]
    
    def add_task(self, task):
        self.task_list.append(task)

    def list_all_tasks(self):
        for index, task in enumerate(self.task_list):
            status= "done" if task.status else "Pending"
            print(f"{index + 1}. {task.title} - {status}")

    def list_incomplete_tasks(self):
        for index, task in enumerate(self.task_list):
            if not task.status:
                print(f"{index + 1}. {task.title} (Due: {task.due_date})")

    def mark_task_complete(self, index):
        if 0 <= index < len(self.task_list):
            self.task_list[index].mark_complete()
            print("Task marked as complete.")
        else:
            print("Invalid index.")


def main():
    todo = ToDoList()

    while True:
        print("\n--- ToDo List Menu ---")
        print("1. Add Task")
        print("2. List All Tasks")
        print("3. List Incomplete Tasks")
        print("4. Mark Task as Complete")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Title: ")
            description = input("Description: ")
            due_date = input("Due Date: ")
            task = Task(title, description, due_date)
            todo.add_task(task)
            print("Task added.")

        elif choice == "2":
            todo.list_all_tasks()

        elif choice == "3":
            todo.list_incomplete_tasks()

        elif choice == "4":
            todo.list_all_tasks()
            index = int(input("Enter task number to mark complete: ")) - 1
            todo.mark_task_complete(index)

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice.")
if __name__ == "__main__":
    main()



# %%
#blog
class Post:
    def __init__(self, title, content, author):
        self.title= title
        self.content= content
        self.author= author


class Blog:
    def __init__(self):
        self.posts=[]

 
    def add_post(self, post):
        self.posts.append(post)

    def list_all_posts(self):
        if not self.posts:
            print("No posts yet")
            return
        for i , post in enumerate(self.posts):
            print(f"{i+1}.{post.title} by {post.author}")
    
    def show_posts_by_author(self, author_name):
        found=False
        for post in self.posts:
            if post.author==author_name:
                print(f"Title: {post.title}\nContent: {post.content}\n-- ")
                found=True
            if not found:
                print("No posts found for this author")



#main program
def main():
    blog=Blog()


    while True:
       print("\n--- Blog Menu ---")
       print("1. Add Post")
       print("2. List All Posts")
       print("3. Show Posts by Author")
       print("4. Exit")

       choice1= input("Enter your choice: ")

       if choice1=="1":
              title = input("Title: ")
              content = input("Content: ")
              author = input("Author: ")
              post=Post(title, content, author)
              blog.add_post(post)
              print("Post added")

       elif choice1=="2":
             blog.list_all_posts()
        
       elif choice1=="3":
            author_name= input("Enter authoe name: ")
            blog.show_posts_by_author(author_name)

       elif choice1=="4":
            print("exiting...")
            break
       
       else:
            print("Invalid choice.")

if __name__=="__main__":
     main()

# %%
class Account:
    def __init__(self, acc_number, holder_name, balance=0):
        self.acc_number = acc_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Amount must be positive.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds.")

    def check_balance(self):
        print(f"Account Balance: {self.balance}")


class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def find_account(self, acc_number):
        for acc in self.accounts:
            if acc.acc_number == acc_number:
                return acc
        return None


def main():
    bank = Bank()

    while True:
        print("\n--- Bank Menu ---")
        print("1. Add Account")
        print("2. Check Balance")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            acc_number = input("Enter Account Number: ")
            holder_name = input("Enter Account Holder Name: ")
            account = Account(acc_number, holder_name)
            bank.add_account(account)
            print("Account created successfully.")

        elif choice == "2":
            acc_number = input("Enter Account Number: ")
            acc = bank.find_account(acc_number)
            if acc:
                acc.check_balance()
            else:
                print("Account not found.")

        elif choice == "3":
            acc_number = input("Enter Account Number: ")
            acc = bank.find_account(acc_number)
            if acc:
                amount = float(input("Enter deposit amount: "))
                acc.deposit(amount)
            else:
                print("Account not found.")

        elif choice == "4":
            acc_number = input("Enter Account Number: ")
            acc = bank.find_account(acc_number)
            if acc:
                amount = float(input("Enter withdrawal amount: "))
                acc.withdraw(amount)
            else:
                print("Account not found.")

        elif choice == "5":
            print("Exiting Banking System...")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()



