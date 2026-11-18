
# HELENE THE QUEEN'S TO-DO LIST APP <3

todo_list = []
completed_list = []

old_todo = []
old_completed = []
has_undo = False

while True:
    print("\n------ HELENE THE QUEEN'S TO-DO LIST APP ------")
    print("1. Add an Item")
    print("2. Remove an Item")
    print("3. Display a List")
    print("4. Undo Previous Change")
    print("5. Replace an Item")
    print("6. Check Off an Item")
    print("7. Exit")

    choice = input("What would you like to do? <3  ")

    # Add an item
    if choice == "1":
        item = input("What item do you want to add? ")

        if item.strip() == "":
            print("You can't add an empty item!")

        else:
            old_todo = todo_list.copy()
            old_completed = completed_list.copy()
            has_undo = True

            todo_list.append(item)
            print("Item added!")

    # Remove an item
    elif choice == "2":
        if len(todo_list) == 0:
            print("Your to-do list is empty!!! >: ")

        else:
            print("\nYour To-Do List:")

            for i in range(len(todo_list)):
                print(i, todo_list[i])

            try:
                index = int(input("Enter the index of the item you want to remove: "))

                if index >= 0 and index < len(todo_list):
                    old_todo = todo_list.copy()
                    old_completed = completed_list.copy()
                    has_undo = True

                    todo_list.pop(index)
                    print("Item removed!")

                else:
                    print("That index doesn't exist! >:")

            except ValueError:
                print("Please enter a number!")

    # Display a list
    elif choice == "3":
        print("\n1. View To-Do List")
        print("2. View Completed List")

        view_choice = input("Which list would you like to seeeeeeeeee? ")

        if view_choice == "1":
            print("\n--- TO-DO LIST ---")

            if len(todo_list) == 0:
                print("Your list is empty!")

            else:
                for i in range(len(todo_list)):
                    print(i, todo_list[i])

        elif view_choice == "2":
            print("\n--- COMPLETED LIST ---")

            if len(completed_list) == 0:
                print("You haven't completed anything yet!")

            else:
                for i in range(len(completed_list)):
                    print(i, completed_list[i])

        else:
            print("Invalid choice!")

    # Undo previous change
    elif choice == "4":
        if has_undo:
            todo_list = old_todo.copy()
            completed_list = old_completed.copy()

            has_undo = False
            print("Your last change has been undone <: ")

        else:
            print("There is nothing to undo!")

    # Replace an item
    elif choice == "5":
        if len(todo_list) == 0:
            print("Your to-do list is empty!!! >: ")

        else:
            print("\nYour To-Do List:")

            for i in range(len(todo_list)):
                print(i, todo_list[i])

            try:
                index = int(input("Enter the index of the item you want to replace: "))

                if index >= 0 and index < len(todo_list):
                    new_item = input("What do you want to replace it with? ")

                    if new_item.strip() == "":
                        print("You can't enter an empty item!")

                    else:
                        old_todo = todo_list.copy()
                        old_completed = completed_list.copy()
                        has_undo = True

                        todo_list[index] = new_item
                        print("Item replaced!")

                else:
                    print("That index doesn't exist!")

            except ValueError:
                print("Please enter a number!")

    # Check off an item
    elif choice == "6":
        if len(todo_list) == 0:
            print("Your to-do list is empty!!! >: ")

        else:
            print("\nYour To-Do List:")

            for i in range(len(todo_list)):
                print(i, todo_list[i])

            try:
                index = int(input("Enter the index of the item you completed: "))

                if index >= 0 and index < len(todo_list):
                    old_todo = todo_list.copy()
                    old_completed = completed_list.copy()
                    has_undo = True

                    finished_item = todo_list.pop(index)
                    completed_list.append(finished_item)

                    print("YAY! You completed:", finished_item)

                else:
                    print("That index doesn't exist silly !")

            except ValueError:
                print("Please enter a number!")

    # Exit
    elif choice == "7":
        print("Thanks for using the Queeeeeeeen's To-Do List App! oki baiiii <3")
        break

    else:
        print("Invalid choice. Please try again! >: ")
