import json
import os
import shutil

def load_data(file_path):
    if not os.path.exists(file_path):
        return []
    with open(file_path, 'r') as f:
        return json.load(f)

def save_data(file_path, backup_path, data):
    if os.path.exists(file_path):
        shutil.copy(file_path, backup_path)
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

def show_restaurant_card(res, index):
    print(f"\n--- Restaurant #{index} ---")
    for key, value in res.items():
        print(f"{key}: {value}")

def new_data_entry_process(paragraph, itemId):
    return {
        "name": paragraph[:20],
        "location": "Unknown",
        "cuisine": "Unknown",
        "rating": 0,
        "description": paragraph,
        "id": itemId
    }

def manage_restaurants(file_path, backup_path):
    while True:
        data = load_data(file_path)

        print(f"\nRecords: {len(data)}")
        print("1. Browse")
        print("2. View")
        print("3. Add")
        print("4. Edit")
        print("5. Delete")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            for i, res in enumerate(data):
                print(f"{i}: {res.get('name')}")

        elif choice == '2':
            index = input("Index: ")
            if index.isdigit() and int(index) < len(data):
                show_restaurant_card(data[int(index)], int(index))
            else:
                print("Invalid index")

        elif choice == '3':
            confirm = input("Type 'yes' to continue: ")
            if confirm != 'yes':
                continue
            paragraph = input("Enter description: ")
            itemId = 100000 + len(data)
            data.append(new_data_entry_process(paragraph, itemId))
            save_data(file_path, backup_path, data)

        elif choice == '4':
            confirm = input("Type 'yes' to continue: ")
            if confirm != 'yes':
                continue
            index = input("Index: ")
            if index.isdigit() and int(index) < len(data):
                record = data[int(index)]
                for key in record:
                    new_val = input(f"{key} ({record[key]}): ")
                    if new_val:
                        record[key] = new_val
                save_data(file_path, backup_path, data)

        elif choice == '5':
            confirm = input("Type 'yes' to continue: ")
            if confirm != 'yes':
                continue
            index = input("Index: ")
            if index.isdigit() and int(index) < len(data):
                data.pop(int(index))
                save_data(file_path, backup_path, data)

        elif choice == '6':
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    manage_restaurants(
        'structured_restaurant_data.json',
        'structured_restaurant_data.json.bak'
    )
