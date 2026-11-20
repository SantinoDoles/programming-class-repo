def main():
    print("Welcome to the String Replacement Tool!")
    main_string = get_string("Enter the string to search through: ")
    substring = get_string("Enter the string to search for: ")
    index = find_substring(main_string, substring)

    if index != -1:
        main_string = replace_substring(main_string, substring)

    print("Thank you for using our program!")
    print("Completed by, Santino Doles")

def get_string(prompt):
    user_input = input(prompt)
    return user_input

def find_substring(main_string, substring):
    index = main_string.find(substring)

    if index == -1:
        print("Substring not found.")
    else:
        print("Substring found at index:", index)

    return index

def replace_substring(main_string, substring):
    choice = input("Would you like to replace the substring? (yes/no) ")
    while choice != "yes" and choice != "no":
        choice = input("Please enter yes or no: ")
    if choice == "yes":
        new_substring = input("Enter the replacement string: ")
        main_string = main_string.replace(substring, new_substring)
        print("Updated string:", main_string)
        return main_string
    else:
        print("No replacement was made.")
        return main_string

       

main()