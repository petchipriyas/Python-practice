import copy

try:
    # Get number of students
    n = int(input("Enter number of students: "))

    if n <= 0:
        raise ValueError("Number of students must be greater than 0.")

    # Lists
    names = []
    roll_numbers = []
    marks = []          # Nested list

    # Input student details
    for i in range(n):
        print(f"\nEnter details for Student {i + 1}")

        name = input("Enter Name: ").strip()

        if not name:
            raise ValueError("Name cannot be empty.")

        roll = int(input("Enter Roll Number: "))

        subject_marks = []

        for j in range(3):
            mark = int(input(f"Enter mark for Subject {j + 1}: "))

            if mark < 0 or mark > 100:
                raise ValueError("Marks must be between 0 and 100.")

            subject_marks.append(mark)

        names.append(name)
        roll_numbers.append(roll)
        marks.append(subject_marks)

    # --------------------------------
    # Dictionary using zip()
    # --------------------------------
    student_dict = dict(zip(roll_numbers, names))

    print("\n--- Student Dictionary ---")
    print(student_dict)

    # --------------------------------
    # String Operations
    # --------------------------------

    # Convert names to uppercase
    uppercase_names = [name.upper() for name in names]

    print("\n--- Names in Uppercase ---")
    print(uppercase_names)

    # Names longer than 5 characters
    long_names = [name for name in names if len(name) > 5]

    print("\n--- Names Longer Than 5 Characters ---")
    print(long_names)

    # Count names starting with A
    count_A = sum(1 for name in names if name.upper().startswith("A"))

    print("\n--- Names Starting With A ---")
    print(count_A)

    # --------------------------------
    # List Comprehension
    # --------------------------------

    # Students whose average marks > 75
    high_average_students = [
        names[i]
        for i in range(n)
        if sum(marks[i]) / len(marks[i]) > 75
    ]

    print("\n--- Students With Average > 75 ---")
    print(high_average_students)

    # Even roll numbers
    even_roll_numbers = [
        roll for roll in roll_numbers
        if roll % 2 == 0
    ]

    print("\n--- Even Roll Numbers ---")
    print(even_roll_numbers)

    # --------------------------------
    # Tuple
    # --------------------------------

    first_student_marks = tuple(marks[0])

    print("\n--- First Student Marks as Tuple ---")
    print(first_student_marks)

    # --------------------------------
    # Set
    # --------------------------------

    unique_marks = {
        mark
        for student_marks in marks
        for mark in student_marks
    }

    print("\n--- Unique Marks ---")
    print(unique_marks)

    # --------------------------------
    # Shallow Copy and Deep Copy
    # --------------------------------

    shallow_marks = copy.copy(marks)
    deep_marks = copy.deepcopy(marks)

    # Modify original nested list
    marks[0][0] = 99

    print("\n--- After Modifying Original Marks ---")

    print("Original Marks:")
    print(marks)

    print("\nShallow Copy:")
    print(shallow_marks)

    print("\nDeep Copy:")
    print(deep_marks)


# --------------------------------
# Error Handling
# --------------------------------

except ValueError as e:
    print("\nInvalid input:", e)

except TypeError as e:
    print("\nType error:", e)

except Exception as e:
    print("\nUnexpected error:", e)