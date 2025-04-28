import sqlite3

def display_entries(cursor):
    cursor.execute('SELECT * FROM PhoneBook')
    rows = cursor.fetchall()
    print("ID | Name | PhoneNumber")
    print("-----------------------")
    for row in rows:
        print(f"{row[0]} | {row[1]} | {row[2]}")

connection = sqlite3.connect('phonebook.db')
cursor = connection.cursor()

while True:
    print("\nPhone Book Manager")
    print("1. View entries")
    print("2. Update an entry")
    print("3. Delete an entry")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        display_entries(cursor)
    elif choice == '2':
        id_to_update = input("Enter the ID of the entry to update: ")
        new_name = input("Enter the new name: ")
        new_phone = input("Enter the new phone number: ")
        cursor.execute('UPDATE PhoneBook SET Name = ?, PhoneNumber = ? WHERE ID = ?', (new_name, new_phone, id_to_update))
        connection.commit()
        print("Entry updated.")
    elif choice == '3':
        id_to_delete = input("Enter the ID of the entry to delete: ")
        cursor.execute('DELETE FROM PhoneBook WHERE ID = ?', (id_to_delete,))
        connection.commit()
        print("Entry deleted.")
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")

connection.close()
