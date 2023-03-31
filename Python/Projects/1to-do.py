# To-Do List App: Create a command-line application that allows users to create, read, update, and delete to-do list items.
#You can use Python's built-in input() function to take user input and store data in a text file or a database.

def show_list():
    with open("todo.txt", "r") as file:
        for line in file:
            print(line.strip())

def add_item():
    item = input("Enter a new to-do list item: ")
    with open("todo.txt", "a") as file:
        file.write(item + "\n")
    print("Item added to the list.")

def delete_item():
    item = input("Enter the item you want to delete: ")
    with open("todo.txt", "r") as file:
        lines = file.readlines()
    with open("todo.txt", "w") as file:
        for line in lines:
            if line.strip() != item:
                file.write(line)
    print("Item removed from the list.")

def update_item():
    item = input("Enter the item you want to update: ")
    new_item = input("Enter the new value for the item: ")
    with open("todo.txt", "r") as file:
        lines = file.readlines()
    with open("todo.txt", "w") as file:
        for line in lines:
            if line.strip() == item:
                file.write(new_item + "\n")
            else:
                file.write(line)
    print("Item updated.")

while True:
    print("To-Do List")
    print("1. Show list")
    print("2. Add item")
    print("3. Delete item")
    print("4. Update item")
    print("5. Quit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        show_list()
    elif choice == "2":
        add_item()
    elif choice == "3":
        delete_item()
    elif choice == "4":
        update_item()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Try again.")
