print("Welcome to the Student Data Organizer!")
student = []

while True:
    print()
    print("===== Main Menu =====")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")
    print()

    option = input("Enter your choice: ")

    if option == "1":
        print()
        print("Enter student details:")
        id = input("Student ID: ")
        fullname = input("Name: ")

        while True:
            age = input("Age: ")
            if age.isdigit():
                break
            print("Invalid age! Enter a number.")

        grade = input("Grade: ")
        birthdate = input("Date of Birth: ")
        choose_subjects = input("Subjects: ")

        newstudent = {
            "id": id,
            "name": fullname,
            "age": age,
            "grade": grade,
            "dob": birthdate,
            "subjects": choose_subjects
        }

        student.append(newstudent)
        print("Student added successfully!")

    elif option == "2":
        print()
        print("===== Student Records =====")
        if not student:
            print("No students found.")
        else:
            for info in student:
                print("ID:", info["id"],
                      "| Name:", info["name"],
                      "| Age:", info["age"],
                      "| Grade:", info["grade"],
                      "| DOB:", info["dob"],
                      "| Subjects:", info["subjects"])

    elif option == "3":
        print()
        idupdate = input("Enter Student ID to update: ")
        foundstu = False

        for info in student:
            if info["id"] == idupdate:
                print()
                print("Enter new details :")

                updatename = input(f"Name ({info['name']}): ")
                updateage = input(f"Age ({info['age']}): ")
                updategrade = input(f"Grade ({info['grade']}): ")
                updatedob = input(f"DOB ({info['dob']}): ")
                updatesubjects = input("Subjects (comma-separated): ")

                if updatename:
                    info["name"] = updatename
                if updateage:
                    info["age"] = updateage
                if updategrade:
                    info["grade"] = updategrade
                if updatedob:
                    info["dob"] = updatedob
                if updatesubjects:
                    info["subjects"] = updatesubjects

                print("Student updated successfully!")
                foundstu = True
                break

        if not foundstu:
            print("Student not found.")

    elif option == "4":
        print()
        delete = input("Enter Student ID to delete: ")
        removed = False

        for info in student:
            if info["id"] == delete:
                student.remove(info)
                print("Student deleted successfully!")
                removed = True
                break

        if not removed:
            print("Student not found.")

    elif option == "5":
        print()
        print("--- Subjects Offered ---")
        
        if not student:
            print("No subjects available.")
        else:
            subjects = set()
            for s in student:
                subjects.add(s["subjects"])   
            
            for sub in subjects:
                print(sub)

    elif option == "6":
        print()
        print("Thank you for using the Student Data Organizer! Goodbye!")
        break

    else:
        print("Invalid choice! Try again.")
