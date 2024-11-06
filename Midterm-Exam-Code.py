Data = []

def display_data(data):
    if not data:
        print("No data available.")
    else:
        print("Data:", data)

def add_single_entry(data):
    entry = input("Enter a single data entry: ")
    data.append(entry)
    print(f"'{entry}' added.")

def add_multiple_entries(data):
    entries = input("Enter multiple data entries (separate by commas): ").split(',')
    entries = [entry.strip() for entry in entries]  # Remove extra spaces around entries
    data.extend(entries)
    print(f"{len(entries)} entries added.")

def delete_data(data):
    display_data(data)
    entry = input("Enter the data entry to delete: ")
    if entry in data:
        data.remove(entry)
        print(f"'{entry}' deleted.")
    else:
        print("Data entry not found.")

def update_data(data):
    display_data(data)
    old_entry = input("Enter the data entry to update: ")
    if old_entry in data:
        new_entry = input(f"Enter the new value for '{old_entry}': ")
        index = data.index(old_entry)
        data[index] = new_entry
        print(f"'{old_entry}' updated to '{new_entry}'.")
    else:
        print("Data entry not found.")

def reverse_data(data):
    data.reverse()
    print("Data reversed.")

def main():
    data = []  # Initialize an empty list to store data
    while True:
        print("\nChoose an action:")
        print("1. Add a single data entry")
        print("2. Add multiple data entries")
        print("3. Display data")
        print("4. Delete data entry")
        print("5. Update data entry")
        print("6. Reverse the data")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            add_single_entry(data)
        elif choice == '2':
            add_multiple_entries(data)
        elif choice == '3':
            display_data(data)
        elif choice == '4':
            delete_data(data)
        elif choice == '5':
            update_data(data)
        elif choice == '6':
            reverse_data(data)
        elif choice == '7':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
