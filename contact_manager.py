def create_csv_file():
    with open("contacts.csv", "w", newline="") as file:
        file.write("Name,Phone,Email\n")
        print("Contact CSV file created successfully!")

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email: ")
    with open("contacts.csv", "a", newline="") as file:
        file.write(f"{name},{phone},{email}\n")
        print("Contact added successfully!")

def view_contacts():
    print("\nContacts Information:")
    with open("contacts.csv", "r", newline="") as file:
        contacts = file.readlines()
        for contact in contacts:
            print(contact.strip().replace(",", " | "))

def edit_contact():
    view_contacts()
    with open("contacts.csv", "r", newline="") as file:
        contacts = file.readlines()
        name_to_edit = input("Enter the name of the contact to edit: ")
        found = False 
        for index in range(1, len(contacts)):
            contact = contacts[index]
            fields = contact.strip().split(",")
            if fields[0] == name_to_edit:
                found = True
                new_phone = input("Enter new phone number: ")
                new_email = input("Enter new email address: ")
                fields[1] = new_phone
                fields[2] = new_email
                updated_contact = ",".join(fields) + "\n"
                contacts[index] = updated_contact
                break
    with open("contacts.csv", "w", newline="") as file:
        file.writelines(contacts)
    if found:
        print("Contact updated successfully!")
    if not found:
        print("Contact not found. Please try again.")



def main():
    while True:
        print("Welcome to the Contact Manager App")
        print("1 - Create a new contact CSV file")
        print("2 - Add a new contact")
        print("3 - View all contacts")
        print("4 - Modify an existing contact")
        print("5 - Exit")
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            print("Creating a new contact CSV file...")
            create_csv_file()
        elif choice == "2":
            print("Adding a new contact...")
            add_contact()
        elif choice == "3":
            print("Viewing all contacts...")
            view_contacts()
        elif choice == "4":
            print("Modifying an existing contact...")
            edit_contact()
        elif choice == "5":
            print("Exiting...")
            break 
        else:
            print("Invalid option. Please try again.")

main()
print("Completed by, Santino Doles")