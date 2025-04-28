import sqlite3

def add_entry(name, phone_number):
    cursor.execute('INSERT INTO Entries (Name, PhoneNumber) VALUES (?, ?)', (name, phone_number))
    connection.commit()
    print(f"Entry added: {name} - {phone_number}")

def look_up_entry(name):
    cursor.execute('SELECT PhoneNumber FROM Entries WHERE Name = ?', (name,))
    result = cursor.fetchone()
    if result:
        print(f"{name}'s phone number is: {result[0]}")
    else:
        print(f"No entry found for {name}.")

def update_entry(name, new_phone_number):
    cursor.execute('UPDATE Entries SET PhoneNumber = ? WHERE Name = ?', (new_phone_number, name))
    if cursor.rowcount > 0:
        connection.commit()
        print(f"Updated {name}'s phone number to: {new_phone_number}")
    else:
        print(f"No entry found for {name}.")

def delete_entry(name):
    cursor.execute('DELETE FROM Entries WHERE Name = ?', (name,))
    if cursor.rowcount > 0:
        connection.commit()
        print(f"Deleted entry for {name}.")
    else:
        print(f"No entry found for {name}.")

def display_all_entries():
    cursor.execute('SELECT * FROM Entries')
    rows = cursor.fetchall()
    print("\nPhone Book:")
    print("Name | PhoneNumber")
    print("------------------")
    for row in rows:
        print(f"{row[0]} | {row[1]}")

# Main program
connection = sqlite3.connect('phonebook.db')
cursor = connection.cursor()

while True:
    print("\nPhone Book Menu")
    print("1. Add an entry")
    print("2. Look up a phone number")
    print("3. Update a phone number")
    print("4. Delete an entry")
    print("5. Display all entries")
    print("6. Exit")

    choice = input("Enter your choice: ")
    if choice == '1':
        name = input("Enter name: ")
        phone_number = input("Enter phone number: ")
        add_entry(name, phone_number)
    elif choice == '2':
        name = input("Enter name: ")
        look_up_entry(name)
    elif choice == '3':
        name = input("Enter name: ")
        new_phone_number = input("Enter new phone number: ")
        update_entry(name, new_phone_number)
    elif choice == '4':
        name = input("Enter name: ")
        delete_entry(name)
    elif choice == '5':
        display_all_entries()
    elif choice == '6':
        break
    else:
        print("Invalid choice. Please try again.")

connection.close()
