
my_list = []
old_list = []
has_undo = False

while True:
    print("\n------ HELENE THE QUEEN'S LIST APP ------")
    print("1. Add an Item")
    print("2. Remove an Item")
    print("3. Display the List")
    print("4. Undo Previous Change")
    print("5. Exit")

    choice = input("What would you like to do? <3  ")

    if choice == "1":
        item = input("What item do you want to add? ")

        if item.strip() == "":
            print("You can't add an empty item!")

        else:
            old_list = my_list.copy()
            my_list.append(item)
            has_undo = True

            print("Item added!")

    elif choice == "2":
        if len(my_list) == 0:
            print("Your list is empty!!! >: ")

        else:
            print("\nHere is your list:")

            for i in range(len(my_list)):
                print(i, my_list[i])

            try:
                index = int(input("Enter the index of the item you want to remove: "))

                if index >= 0 and index < len(my_list):
                    old_list = my_list.copy()
                    my_list.pop(index)
                    has_undo = True

                    print("Item removed!")

                else:
                    print("That index doesn't exist!")

            except ValueError:
                print("Please enter a number!")

    elif choice == "3":
        if len(my_list) == 0:
            print("Your list is empty!")

        else:
            print("\nYour List:")

            for item in my_list:
                print(item)

    elif choice == "4":
        if has_undo:
            my_list = old_list.copy()
            has_undo = False

            print("Your last change has been undone  yay <: ")

        else:
            print("There is nothing to undo!")

    elif choice == "5":
        print("Thanks for using Helene the Queen's List App!")
        break

    else:
        print("Invalid choice. Please try again >: !!")
