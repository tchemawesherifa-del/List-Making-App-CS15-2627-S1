
# List Making App

todo_list = []
completed_list = []

previous_todo = []
previous_completed = []
has_undo = False

while True:
    print("\n===== TO-DO LIST APP =====")
    print("1. Add an Item")
    print("2. Remove an Item")
    print("3. Display a List")  
    print("4. Undo Previous Change")
    print("5. Replace an Item")
    print("6. Check Off an Item")
    print("7. Exit")

    choice = input("Choose an option (1-7): ")

    # Add an item
    if choice == "1":
        item = input("Enter the item you want to add: ")

        if item.strip() == "":
            print("You cannot add an empty item.")

        else:
            previous_todo = todo_list.copy()
            previous_completed = completed_list.copy()
            has_undo = True

            todo_list.append(item)
            print("Item added!")

    # Remove an item
    elif choice == "2":
        if len(todo_list) == 0:
            print("Your to-do list is empty.")

        else:
            print("\nYour To-Do List:")
            for i in range(len(todo_list)):
                print(i, "-", todo_list[i])

            try:
                index = int(input("Enter the index of the item to remove: "))

                if index < 0 or index >= len(todo_list):
                    print("Invalid index. Try again.")

                else:
                    previous_todo = todo_list.copy()
                    previous_completed = completed_list.copy()
                    has_undo = True

                    removed_item = todo_list.pop(index)
                    print(removed_item, "was removed!")

            except ValueError:
                print("Please enter a number.")

    # Display a list
    elif choice == "3":
        print("\n1. View To-Do List")
        print("2. View Completed List")

        view_choice = input("Which list would you like to see? ")

        if view_choice == "1":
            print("\n--- TO-DO LIST ---")

            if len(todo_list) == 0:
                print("No unfinished items.")

            else:
                for i in range(len(todo_list)):
                    print(i, "-", todo_list[i])

        elif view_choice == "2":
            print("\n--- COMPLETED LIST ---")

            if len(completed_list) == 0:
                print("No completed items.")

            else:
                for i in range(len(completed_list)):
                    print(i, "-", completed_list[i])

        else:
            print("Invalid choice.")

    # Undo the previous change
    elif choice == "4":
        if has_undo:
            todo_list = previous_todo.copy()
            completed_list = previous_completed.copy()

            has_undo = False
            print("Your previous change has been undone!")

        else:
            print("There is nothing to undo.")

    # Replace an item
    elif choice == "5":
        if len(todo_list) == 0:
            print("Your to-do list is empty.")

        else:
            print("\nYour To-Do List:")
            for i in range(len(todo_list)):
                print(i, "-", todo_list[i])

            try:
                index = int(input("Enter the index of the item to replace: "))

                if index < 0 or index >= len(todo_list):
                    print("Invalid index. Try again.")

                else:
                    new_item = input("Enter the new item: ")

                    if new_item.strip() == "":
                        print("You cannot enter an empty item.")

                    else:
                        previous_todo = todo_list.copy()
                        previous_completed = completed_list.copy()
                        has_undo = True

                        todo_list[index] = new_item
                        print("Item replaced!")

            except ValueError:
                print("Please enter a number.")

    # Check off an item
    elif choice == "6":
        if len(todo_list) == 0:
            print("Your to-do list is empty.")

        else:
            print("\nYour To-Do List:")
            for i in range(len(todo_list)):
                print(i, "-", todo_list[i])

            try:
                index = int(input("Enter the index of the item to complete: "))

                if index < 0 or index >= len(todo_list):
                    print("Invalid index. Try again.")

                else:
                    previous_todo = todo_list.copy()
                    previous_completed = completed_list.copy()
                    has_undo = True

                    finished_item = todo_list.pop(index)
                    completed_list.append(finished_item)

                    print(f"'{finished_item}' has been completed!")

            except ValueError:
                print("Please enter a number.")

    # Exit
    elif choice == "7":
        print("Thanks for using the To-Do List App!")
        break

    else:
        print("Invalid menu choice. Please choose 1-7.")
