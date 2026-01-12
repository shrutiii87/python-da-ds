import datetime
import time
import math
import random
import uuid
import string

def datetime_opt():
    while True:
        print()
        print("Datetime & Time Operations:")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates/times")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")
        
        option = input("Enter your choice: ")

        try:
            if option == "1":
                now = datetime.datetime.now()
                print()
                print("Current Date and Time:", now.strftime("%Y-%m-%d %H:%M:%S"))
                print("================================")
                continue

            elif option == "2":
                print()
                d1 = input("Enter the first date (YYYY-MM-DD): ")
                d2 = input("Enter the second date (YYYY-MM-DD): ")
                date1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
                date2 = datetime.datetime.strptime(d2, "%Y-%m-%d")
                diff = abs((date2 - date1).days)
                print("Difference:", diff, "days")
                print("================================")
                continue

            elif option == "3":
                print()
                fmt = input("Enter format (e.g. %d-%m-%Y): ")
                print("Formatted Date:", datetime.datetime.now().strftime(fmt))
                print("================================")
                continue

            elif option == "4":
                print()
                input("Press Enter to start stopwatch")
                start = time.time()
                input("Press Enter to stop")
                end = time.time()
                print("Elapsed time:", round(end - start, 2), "seconds")
                print("================================")
                continue

            elif option == "5":
                print()
                sec = int(input("Enter seconds: "))
                while sec > 0:
                    print(sec)
                    time.sleep(1)
                    sec -= 1
                print("Time's up!")
                print("================================")
                continue

            elif option == "6":
                break
            else:
                print("Invalid Choice\n")

        except Exception as e:
            print("Error:", e)


def math_opt():
    while True:
        print()
        print("Mathematical Operations:")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Back to Main Menu")

        option = input("Enter your choice: ")

        try:
            if option == "1":
                n = int(input("Enter a number: "))
                print("Factorial:", math.factorial(n))
                print("================================")
                continue

            elif option == "2":
                p = float(input("Enter Principal amount: "))
                r = float(input("Enter Rate of intrest (%): "))
                t = float(input("Enter Time (in years): "))
                ci = p * (1 + r / 100) ** t
                print("Compound Interest:", round(ci, 2))
                print("================================")
                continue

            elif option == "3":
                angle = float(input("Enter angle in degrees: "))
                rad = math.radians(angle)
                print("sin:", math.sin(rad))
                print("cos:", math.cos(rad))
                print("tan:", math.tan(rad))
                print("================================")
                continue

            elif option == "4":
                r = float(input("Radius: "))
                print("Area:", math.pi * r * r)
                print("================================")
                continue

            elif option == "5":
                break
            else:
                print("Invalid choice")

        except Exception as e:
            print("Error:", e)


def random_opt():
    while True:
        print()
        print("Random Data Generation:")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Back to Main Menu")

        option = input("Enter your choice: ")

        try:
            if option == "1":
                print("Random Number:", random.randint(1, 100))
                print("================================")
                continue

            elif option == "2":
                n = int(input("Enter List size: "))
                print("Random List:", [random.randint(1, 50) for _ in range(n)])
                print("================================")
                continue

            elif option == "3":
                length = int(input("Enter Password length: "))
                chars = string.ascii_letters + string.digits + "@#$!"
                password = "".join(random.choice(chars) for _ in range(length))
                print("Generated Password:", password)
                print("================================")
                continue

            elif option == "4":
                otp = random.randint(100000, 999999)
                print("Generated OTP:", otp)
                print("================================")
                continue

            elif option == "5":
                break
            else:
                print("Invalid choice")

        except Exception as e:
            print("Error:", e)


def uuid_opt():
    print()
    print("Generated Unique Identifiers :")
    print("Generated UUID :-",uuid.uuid4())
    print("================================")

def file_opt():
    while True:
        print()
        print("File Operations (Custom Module):")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to Main Menu")

        option = input("Enter your choice: ")

        try:
            if option == "1":
                name = input("Enter File name: ")
                open(name, "w").close()
                print("File created successfully!")
                print("================================")
                continue

            elif option == "2":
                name = input("Enter File name: ")
                data = input("Enter data to write : ")
                with open(name, "w") as f:
                    f.write(data)
                print("Data Written successfully")
                print("================================")
                continue

            elif option == "3":
                name = input("Enter File name: ")
                with open(name, "r") as f:
                    print("\nFile Content:\n", f.read())
                print("================================")
                continue

            elif option == "4":
                name = input("Enter File name: ")
                data = input("Enter the data: ")
                with open(name, "a") as f:
                    f.write("\n"+data)
                print("Appended")
                print("================================")
                continue

            elif option == "5":
                break
            else:
                print("Invalid choice")

        except Exception as e:
            print("Error:", e)

def explore_opt():
    print()
    print("Explore Module Attributes (dir()):")
    try:
        mod = input("Enter module name to explore: ")
        module = __import__(mod)
        print("Available Attributes in math module :\n", dir(module))
        print("================================")
    except Exception as e:
        print("Error:", e)

def main():
    print()
    print("==============================")
    print("Welcome to Multi-Utility Toolkit")
    print("==============================")

    while True:
        print("Choose an option:")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")
        print("==============================")

        option = input("Enter your choice: ")

        if option == "1":
            datetime_opt()
        elif option == "2":
            math_opt()
        elif option == "3":
            random_opt()
        elif option == "4":
            uuid_opt()
        elif option == "5":
            file_opt()
        elif option == "6":
            explore_opt()
        elif option == "7":
            print("==============================")
            print("Thank you for using the Toolkit!")
            print("==============================")
            break
        else:
            print("Invalid choice")
        

if __name__ == "__main__":
    main()
