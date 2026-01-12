import datetime

class Journal:
    def __init__(self):
        self.filename = "journal.txt"

    def add_entry(self):
        print()
        print("enter your journal entry:")
        text = input()
        time = datetime.datetime.now()

        with open(self.filename, "a") as file:
            file.write("[" + str(time) + "]\n")
            file.write(text + "\n\n")

        print()
        print("entry added successfully!")
        print()

    def view_entries(self):
        try:
            with open(self.filename, "r") as file:
                data = file.read()

            if data == "":
                print()
                print("no journal entries found . start by adding a new entry!")
                print()
            else:
                print()
                print("your journal entries:")
                print("---------------------------------")
                print(data)

        except FileNotFoundError:
            print()
            print("error:- the journal file does not exist . please add a new entry first .")
            print()

    def search_entry(self):
        print()
        key = input("enter a keyword or date to search : ")

        try:
            with open(self.filename, "r") as file:
                lines = file.readlines()

            found = False
            print()
            print("matching entries:")
            print("--------------------------------------")

            for line in lines:
                if key.lower() in line.lower():
                    print(line, end="")
                    found = True

            if not found:
                print(f"no entries were found for the keyword : {key}")

            print()

        except FileNotFoundError:
            print()
            print("no journal entries found . start by adding a new entry!")
            print()

    def delete_entries(self):
        print()
        ans = input("are you sure you want to delete all entries ? (yes/no) : ")

        if ans == "yes":
            try:
                open(self.filename, "w").close()
                print()
                print("all journal entries have been deleted.")
                print()
            except FileNotFoundError:
                print()
                print("no journal entries to delete.")
                print()
        else:
            print()
            print("delete cancelled")
            print()

# OBJECT CREATED
journal = Journal()

print("welcome to personal journal manager!")
print("please select an option:")
print()

while True:
    print("1. add a new entry")
    print("2. view all entries")
    print("3. search for an entry")
    print("4. delete all entries")
    print("5. exit")
    print()

    ch = input("user input:\n")

    if ch == "1":
        journal.add_entry()
    elif ch == "2":
        journal.view_entries()
    elif ch == "3":
        journal.search_entry()
    elif ch == "4":
        journal.delete_entries()
    elif ch == "5":
        print()
        print("thank you for using personal journal manager . goodbye!")
        print()
        break
    else:
        print()
        print("invalid option . please select a valid option from the menu .")
        print()
