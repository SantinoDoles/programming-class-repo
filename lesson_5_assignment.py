import random
def main():
    grades = []

    while True:
        grade = int(input("Enter a grade (-1 to stop): "))
        if grade == -1:
            break
        grades.append(grade)
    print("Grades entered:", grades)
    print("\nRemoving the lowest grade:")

    if grades:
        lowest_grade = min(grades)
        lowest_index = grades.index(lowest_grade)
        grades.pop(lowest_index)

    print("Grades after removal:", grades)
    print("\nRemoving a random grade:")

    if grades:
        random_grade = random.choice(grades)
        grades.remove(random_grade)

    print("Grades after random removal:", grades)
    print("\nEditing a grade:")

    for index, grade in enumerate(grades, start=1):
        print(index, grade)
    if grades:
        while True:
            choice = int(input("Which grade number would you like to edit? "))

            if 1 <= choice <= len(grades):
                break
            print("Invalid grade number. Try again.")
        new_grade = int(input("Enter the new grade: "))
        grades[choice - 1] = new_grade

        print("Updated grades:", grades)
    print("\nSorting and reversing the grades:")

    grades.sort()
    grades.reverse()

    print("Sorted and reversed grades:", grades)
    print("\nCalculating grade total and average:")

    total = sum(grades)
    print("Total grades:", total)

    if grades:
        average = total / len(grades)
        print("Average grade:", average)
    print("\nCompleted by, Santino Doles")
if __name__ == "__main__":
    main()
