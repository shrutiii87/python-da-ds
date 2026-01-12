def data_analyzer():
    data = []  

    while True:
        
        print("\nWelcome to the Data Analyzer Program!")
        print("Main Menu:")
        print("1. Input Data")
        print("2. Display Data Summary")
        print("3. Calculate Factorial")
        print("4. Filter Data by Threshold")
        print("5. Sort Data")
        print("6. Display Dataset Statistics")
        print("7. Exit Program")
        
        choice = input("Enter your choice (1-7): ")

#choice 1 :- input data
        if choice == '1':
            def input_data():
                data_input = input("Enter data for a 1D array (separated by spaces): ") 
                data = list(map(int, data_input.split()))  
                print("Data has been stored successfully!")
                return data
            
            data = input_data()

#choice 2 :- Display Data Summary
        elif choice == '2':
            def display_data(data):
             
                total_ele = len(data)  
                min_val = min(data) 
                max_val = max(data)  
                sum_val = sum(data)
                avg_val = sum_val / total_ele 
                return total_ele, min_val, max_val, sum_val, avg_val

            total_ele, min_val, max_val, sum_val, avg_val = display_data(data)
            print("\nData Summary:")
            print("-Total elements: ", total_ele)
            print("-Minimum value: ", min_val)
            print("-Maximum value: ", max_val)
            print("-Sum of all values: ", sum_val)
            print("-Average value: ", avg_val)

# choice 3 :- calculate the factorial
        elif choice == '3':
            def factorial(n):
                """ use recursion to calculate factorial:-
     -this is how it works :-
     for an example:-
     Factorial of n (n!) = n × (n-1) × (n-2) × ... × 1
     Example Calculation: 5! = 5 × 4 × 3 × 2 × 1 = 120 """
               
                if n == 0 or n == 1:
                    return 1
                else:
                    return n * factorial(n - 1)

            num = int(input("Enter a number to calculate its factorial: "))
            fact_result = factorial(num) 
            print("The factorial of", num, "is:", fact_result)
            print(factorial.__doc__)
        
#choice 4 :- Filter Data by Threshold
        elif choice == '4':
            def filter_data(data, threshold):

                return list(filter(lambda x: x >= threshold, data))

            threshold = int(input("Enter a threshold value: "))
            filtered_data = filter_data(data, threshold)  
            print("Filtered data (values >= ", threshold, "): ", filtered_data)

#  choice :- 5 Sort Data
        elif choice == '5':
            def sort_data(data,order='asc'):
                return sorted(data) if order == 'asc' else sorted(data,reverse=True)
            print("choose sorting option:-")
            print("1. Ascending order :-")
            print("2. Descending order :-")
            order= input("enter your choice :-")
            if order =='1':
                sort_data = sort_data(data,'asc')
                print("sorted data in Ascending order :-",sort_data)
            elif order =='2':
                sort_data = sort_data(data,'desc')
                print("sorted data in Descending order :-",sort_data)
            else:
                print("please enter a valid choice !")

#choice :- 6 Display Dataset Statistics
        elif choice == '6':
            def maximum():
                """ this step calculates :-maximum , minimum , sum , average .
                - by using functions and loops .- use of global keyword also """
                m=data[0]
                for choice in data:
                    if choice > m:
                        m=choice
                print("maximum value :-",m)
            maximum()
            

            def minimum():
                mi=data[0]
                for choice in data:
                    if choice < mi:
                        mi=choice
                print("Minimum value :-",mi)
            minimum()

            def sum_values():
                global total
                total = 0
                for choice in data:
                    total = total + choice
                print("sum of all values :-",total)
            sum_values()

            def average():
                count=0
                for choice in data:
                    count+=1
                avg = total/count
                print("avergae of values",avg)
            average()
            print(maximum.__doc__)

# choice :- 7 Exit Program
        elif choice == '7':
            print("Thank you for using the Data Analyzer and transformer program. Goodbye!")
            break  
        else:
            print("Invalid choice. Please select a valid option (1-7).") 
            
data_analyzer()