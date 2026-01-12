import numpy as np

class DataAnalytics:

    def __init__(self):
        self.array = None   

    # ENCAPSULATION (PRIVATE METHOD) 
    def __check_array_exists(self):
        if self.array is None:
            raise ValueError("Array not created yet.")
        
    # CLASS METHOD
    @classmethod
    def create_with_array(cls, elements, shape=None):
        obj = cls()
        if shape:
            obj.array = np.array(elements).reshape(shape)
        else:
            obj.array = np.array(elements)
        return obj
      
    # ARRAY CREATION 
    def create_array(self):
        while True:
            try:
                print("\nSelect the type of array to create:")
                print("1. 1D Array")
                print("2. 2D Array")
                print("3. 3D Array")
                print("4. Go Back")
                choice = int(input("Enter your choice: "))

                if choice == 1:
                    n = int(input("Enter number of elements: "))
                    elements = list(map(int, input(f"Enter {n} elements separated by space: ").split()))
                    if len(elements) != n:
                        raise ValueError(f"You must enter exactly {n} elements.")
                    self.array = np.array(elements)

                elif choice == 2:
                    r = int(input("Enter number of rows: "))
                    c = int(input("Enter number of columns: "))
                    elements = list(map(int, input(f"Enter {r*c} elements separated by space: ").split()))
                    if len(elements) != r * c:
                        raise ValueError(f"You must enter exactly {r*c} elements.")
                    self.array = np.array(elements).reshape(r, c)

                elif choice == 3:
                    x = int(input("Enter dimension 1 size: "))
                    y = int(input("Enter dimension 2 size: "))
                    z = int(input("Enter dimension 3 size: "))
                    elements = list(map(int, input(f"Enter {x*y*z} elements separated by space: ").split()))
                    if len(elements) != x*y*z:
                        raise ValueError(f"You must enter exactly {x*y*z} elements.")
                    self.array = np.array(elements).reshape(x, y, z)

                elif choice == 4:
                    return

                else:
                    print("Invalid choice!")
                    continue

                print("\nArray created successfully:")
                print(self.array)
                self.index_slice_menu()
                break

            except ValueError as ve:
                print("Error:", ve)

    # INDEXING AND SLICING 
    def index_slice_menu(self):
        try:
            self.__check_array_exists()
        except ValueError as e:
            print(e)
            return

        while True:
            try:
                print("\nChoose an operation:")
                print("1. Indexing")
                print("2. Slicing")
                print("3. Go Back")
                ch = int(input("Enter your choice: "))

                if ch == 1:
                    print("\nArray:")
                    print(self.array)
                    idx = input("Enter index (comma separated for multi-dim, e.g., 0,1,2): ")
                    index_tuple = tuple(map(int, idx.split(',')))
                    print("\nIndexed Value:")
                    print(self.array[index_tuple])

                elif ch == 2:
                    print("\nArray:")
                    print(self.array)
                    if self.array.ndim == 1:
                        r = input("Enter the range (start:end): ")
                        rs, re = map(int, r.split(":"))
                        print("\nSliced Array:")
                        print(self.array[rs:re])
                    elif self.array.ndim == 2:
                        r = input("Enter row range (start:end): ")
                        c = input("Enter column range (start:end): ")
                        rs, re = map(int, r.split(":"))
                        cs, ce = map(int, c.split(":"))
                        print("\nSliced Array:")
                        print(self.array[rs:re, cs:ce])
                    else:
                        r = input("Enter first dimension range (start:end): ")
                        s = input("Enter second dimension range (start:end): ")
                        t = input("Enter third dimension range (start:end): ")
                        r1, r2 = map(int, r.split(":"))
                        s1, s2 = map(int, s.split(":"))
                        t1, t2 = map(int, t.split(":"))
                        print("\nSliced Array:")
                        print(self.array[r1:r2, s1:s2, t1:t2])

                elif ch == 3:
                    return
                else:
                    print("Invalid choice!")

            except (ValueError, IndexError):
                print("Error: Invalid input format.")

    # MATHEMATICAL OPERATIONS
    def mathematical_operations(self):
        try:
            self.__check_array_exists()
        except ValueError as e:
            print(e)
            return

        while True:
            try:
                print("\nMathematical Operations:")
                print("1. Addition")
                print("2. Subtraction")
                print("3. Multiplication")
                print("4. Division")
                print("5. Go Back")
                ch = int(input("Enter your choice: "))
                if ch == 5:
                    return

                elements = list(map(int, input(f"Enter {self.array.size} elements separated by space: ").split()))
                if len(elements) != self.array.size:
                    print(f"Error: You must enter exactly {self.array.size} elements.")
                    continue

                second_array = np.array(elements).reshape(self.array.shape)

                print("\nOriginal Array:")
                print(self.array)
                print("\nSecond Array:")
                print(second_array)

                if ch == 1:
                    print("\nResult of Addition:")
                    print(self.array + second_array)
                elif ch == 2:
                    print("\nResult of Subtraction:")
                    print(self.array - second_array)
                elif ch == 3:
                    print("\nResult of Multiplication:")
                    print(self.array * second_array)
                elif ch == 4:
                    if np.any(second_array == 0):
                        print("Error: Division by zero is not allowed.")
                        continue
                    print("\nResult of Division:")
                    print(self.array / second_array)
                else:
                    print("Invalid choice!")
                    continue
                break

            except ValueError:
                print("Error: Invalid input.")

    # COMBINE OR SPLIT
    def combine_split(self):
        try:
            self.__check_array_exists()
        except ValueError as e:
            print(e)
            return

        while True:
            try:
                print("\nCombine or Split Arrays:")
                print("1. Combine Arrays")
                print("2. Split Array")
                print("3. Go Back")
                ch = int(input("Enter your choice: "))
                if ch == 3:
                    return

                if ch == 1:
                    elements = list(map(int, input(f"Enter {self.array.size} elements to combine: ").split()))
                    second_array = np.array(elements).reshape(self.array.shape)

                    print("\nOriginal Array:")
                    print(self.array)
                    print("\nSecond Array:")
                    print(second_array)

                    if self.array.ndim == 1:
                        print("\nCombined Array:")
                        print(np.concatenate((self.array, second_array)))
                    elif self.array.ndim == 2:
                        print("\nCombined Array:")
                        print(np.vstack((self.array, second_array)))
                    else:
                        print("\nCombined Array:")
                        print(np.concatenate((self.array, second_array), axis=0))

                elif ch == 2:
                    parts = int(input("Enter number of parts to split: "))
                    print("\nSplit Arrays:")
                    for arr in np.array_split(self.array, parts):
                        print(arr)
                else:
                    print("Invalid choice!")
                break

            except ValueError:
                print("Error: Invalid input.")

    # SEARCH, SORT, FILTER 
    def search_sort_filter(self):
        try:
            self.__check_array_exists()
        except ValueError as e:
            print(e)
            return

        while True:
            try:
                print("\nSearch, Sort, and Filter:")
                print("1. Search a value")
                print("2. Sort the array")
                print("3. Filter values")
                print("4. Go Back")
                ch = int(input("Enter your choice: "))
                if ch == 4:
                    return

                if ch == 1:
                    val = int(input("Enter value to search: "))
                    print("\nValue found at index:")
                    print(np.where(self.array == val))
                elif ch == 2:
                    print("\nSorted Array:")
                    print(np.sort(self.array, axis=None))
                elif ch == 3:
                    val = int(input("Enter minimum value to filter: "))
                    print("\nFiltered Array:")
                    print(self.array[self.array > val])
                else:
                    print("Invalid choice!")
                break

            except ValueError:
                print("Error: Invalid input.")

    # AGGREGATES AND STATISTICS
    def aggregates_statistics(self):
        try:
            self.__check_array_exists()
        except ValueError as e:
            print(e)
            return

        while True:
            try:
                print("\nAggregates and Statistics:")
                print("1. Sum")
                print("2. Mean")
                print("3. Median")
                print("4. Standard Deviation")
                print("5. Variance")
                print("6. Go Back")
                ch = int(input("Enter your choice: "))
                if ch == 6:
                    return

                print("\nOriginal Array:")
                print(self.array)

                if ch == 1:
                    print("Sum:", np.sum(self.array))
                elif ch == 2:
                    print("Mean:", np.mean(self.array))
                elif ch == 3:
                    print("Median:", np.median(self.array))
                elif ch == 4:
                    print("Standard Deviation:", np.std(self.array))
                elif ch == 5:
                    print("Variance:", np.var(self.array))
                else:
                    print("Invalid choice!")
                break

            except ValueError:
                print("Error: Invalid input.")


# MAIN MENU 
def main():
    analyzer = DataAnalytics()
    print("Welcome to the NumPy Analyzer!")
    print("---------------------------------------")

    while True:
        try:
            print("\nChoose an option:")
            print("1. Create a Numpy Array")
            print("2. Perform Mathematical Operations")
            print("3. Combine or Split Arrays")
            print("4. Search, Sort, or Filter Arrays")
            print("5. Compute Aggregates and Statistics")
            print("6. Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                analyzer.create_array()
            elif choice == 2:
                analyzer.mathematical_operations()
            elif choice == 3:
                analyzer.combine_split()
            elif choice == 4:
                analyzer.search_sort_filter()
            elif choice == 5:
                analyzer.aggregates_statistics()
            elif choice == 6:
                print("\nThank you for using the NumPy Analyzer! Goodbye!")
                break
            else:
                print("Invalid menu choice.")

        except ValueError:
            print("Error: Please enter a number.")


main()
