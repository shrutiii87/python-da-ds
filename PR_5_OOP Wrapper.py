class Person:

    def __init__(self, name="Unknown", age=0):     # Method Overloading 
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

class Employee(Person):
       
    def __init__(self, name="Unknown", age=0, emp_id="N/A", salary=0.0):
        super().__init__(name, age)
        self.__employee_id = emp_id     # Encapsulation
        self.__salary = salary

    def get_employee_id(self):
        return self.__employee_id

    def set_employee_id(self, emp_id):
        self.__employee_id = emp_id
                                           #Getter and setter
    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    def display(self):                                         
        super().display()                                  # Overriding
        print("Employee ID:", self.__employee_id)
        print("Salary:", self.__salary)


class Manager(Employee):
   
    def __init__(self, name="Unknown", age=0, emp_id="N/A", salary=0.0, department="Not Assigned"):
        super().__init__(name, age, emp_id, salary)
        self.department = department

    def display(self):                                            # Overriding
        super().display()
        print("Department:", self.department)

                          #PROGRAM
person_obj = None
employee_obj = None
manager_obj = None

print("---python OOP project: Employee Management system---")
print()
while True:

    print("Choose an operation:")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Show Details")
    print("5. Exit")

    print()
    choice = input("Enter your choice: ")
    print()

    # PERSON
    if choice == "1":
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        person_obj = Person(name, age)
        print()
        print(f"Person created with name:-{name} and age:-{age}")
        print()
        print("-----choose another option-----")
        print()

    # EMPLOYEE
    elif choice == "2":
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        emp_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))
        employee_obj = Employee(name, age, emp_id, salary)
        print()
        print(f"Employee created with name:-{name}, age:-{age}, ID:-{emp_id}, salary:-{salary}")
        print()
        print("-----choose another option-----")
        print()

    # MANAGER
    elif choice == "3":
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        emp_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))
        dept = input("Enter Department: ")
        manager_obj = Manager(name, age, emp_id, salary, dept)
        print()
        print(f"Manager created with name:-{name}, age:-{age}, ID:-{emp_id}, salary:-{salary}, department:-{dept}")
        print()
        print("-----choose another option-----")
        print()

    # DETAILS
    elif choice == "4":
        print("Choose details to show:")
        print("1. Person")
        print("2. Employee")
        print("3. Manager")
        option = input("Enter your choice: ")
        print()

        if option == "1" and person_obj:
            issubclass(Employee, Person)
            print("Person details:")
            person_obj.display()

        elif option == "2" and employee_obj:
            issubclass(Employee, Person)
            print("Employee details:")
            employee_obj.display()

        elif option == "3" and manager_obj:
            issubclass(Manager, Employee)
            issubclass(Manager, Person)
            print("Manager details:")
            manager_obj.display()

        else:
            print("No data found!")

        print()
        print("-----choose another option-----")
        print()

    # EXIT
    elif choice == "5":
        print("Exiting the system. All resources have been freed.")
        print()
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Try again.")
