while True:
    print("Welcome to the Pattern Generator and Number Analyzer!")
    print()
    print("Select an option:")
    print()
    print("1. Generate a pattern")
    print("2. Analyze a range of numbers")
    print("3. EXIT")
    print()
    choose = int(input("Enter your choice: "))

    if choose == 1:
        rows = int(input("Enter the number of rows for the pattern: "))
        print()
        print("Pattern:")
        for i in range(1, rows + 1):
            print("*" * i)

    elif choose== 2:
        start = int(input("Enter the start of the range: "))
        ending = int(input("Enter the end of the range: "))
        sum = 0
        print()
        for a in range(start, ending + 1):
            if a % 2 == 0:
                print("Number",a," is Even")
            else:
                print("number",a," is odd")
            sum += a
        print()
        print("Sum of all numbers from",start,"to",ending,"is",sum)

    elif choose == 3:
        print()
        print("Exiting the program. Goodbye!")
        break
    else:
        print()
        print("Invalid choice! Please enter 1, 2, or 3.")
