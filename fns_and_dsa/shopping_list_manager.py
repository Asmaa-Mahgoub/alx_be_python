
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(shopping_list)
            else:
                print("Item name cannot be empty.")
        elif choice == '2':

            # Prompt for and remove an item
            remove_item = input("Please enter an item to be removed: ")
            if remove_item:
                    shopping_list.remove(remove_item)
                    print(shopping_list)
            
            else:
                    print("No Item is removed.")

        elif choice == '3':
            if shopping_list:
                print(shopping_list)
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()