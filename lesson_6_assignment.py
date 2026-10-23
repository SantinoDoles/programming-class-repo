def main():
    student_information = {}
    student_information["John Smith"] = {
        "ID": 1001,
        "GPA": 3.5,
        "Credits": 45,
        "Grades": ["A", "B", "A", "B"]
    }
    
    student_information["Jane Doe"] = {
        "ID": 1002,
        "GPA": 3.8,
        "Credits": 60,
        "Grades": ["A", "A", "B", "A"]
    }

    print("Student Information Dictionary:")
    print(student_information)
    print("\nStudent Names:")

    for name in student_information:
        print(name)

    print("\nAccessing Student Information:")
    print("Name\tID\tGPA\tCredits\tGrades")

    for name, info in student_information.items():
       print(f"{name}\t{info['ID']}\t{info['GPA']}\t{info['Credits']}\t{info['Grades']}")

    print("\nRemoving a Student:")
    student_information.pop("John Smith")
    print(student_information)

    print("\nAccessing GPA Information:")

    for name, info in student_information.items():
        gpa = info.get("GPA")
        print(f"{name}: {gpa}")

    print("\nClearing Student Registry:")
    student_information.clear()
    print(student_information)
    print("\nCompleted by, Santino Doles")
   

if __name__ == "__main__":
    main()
