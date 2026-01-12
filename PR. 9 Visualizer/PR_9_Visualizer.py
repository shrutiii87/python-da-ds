import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class SalesDataAnalyzer:

    def __init__(self):
        self.data = None
        self.current_plot = None

    def __del__(self):
        pass

    #LOAD DATA 
    def load_dataset(self):
        print("\n== Load Dataset ==")
        path = input("Enter the path of the dataset (CSV file): ")
        try:
            self.data = pd.read_csv(path)
            print("Dataset loaded successfully!")
        except Exception as e:
            print("Error loading file:", e)

    #EXPLORE DATA
    def explore_data(self):
        if self.data is None:
            print("Load a dataset first!")
            return
        while True:
            print("\n== Explore Data ==")
            print("1. Display the first 5 rows")
            print("2. Display the last 5 rows")
            print("3. Display column names")
            print("4. Display data types")
            print("5. Display basic info")
            print("6. Back")

            choice = input("Enter your choice: ")

            if choice == "1":
                print(self.data.head())
            elif choice == "2":
                print(self.data.tail())
            elif choice == "3":
                print(self.data.columns)
            elif choice == "4":
                print(self.data.dtypes)
            elif choice == "5":
                self.data.info()
            elif choice == "6":
                break
            else:
                print("Invalid choice")

    #HANDLE MISSING DATA
    def handle_missing_data(self):
        if self.data is None:
            print("Load a dataset first!")
            return
        while True:
            print("\n== Handle Missing Data ==")
            print("1. Display rows with missing values")
            print("2. Fill missing values with mean")
            print("3. Drop rows with missing values")
            print("4. Replace missing values with a specific value")
            print("5. Back")

            choice = input("Enter your choice: ")

            if choice == "1":
                missing = self.data[self.data.isnull().any(axis=1)]
                if missing.empty:
                    print("No missing values found in the dataset!")
                else:
                    print(missing)

            elif choice == "2":
                self.data.fillna(self.data.mean(numeric_only=True), inplace=True)
                print("Missing values filled with mean")

            elif choice == "3":
                self.data.dropna(inplace=True)
                print("Rows with missing values dropped")

            elif choice == "4":
                value = input("Enter value to replace missing values: ")
                try:
                    value = float(value)
                except:
                    pass
                self.data.fillna(value, inplace=True)
                print("Missing values replaced")

            elif choice == "5":
                break
            else:
                print("Invalid choice")

    #DESCRIPTIVE STATS
    def descriptive_stats(self):
        if self.data is None:
            print("Load a dataset first!")
            return
        print("\n== Descriptive Statistics ==")
        print(self.data.describe())
        print("\nStandard Deviation:\n", self.data.std(numeric_only=True))
        print("\nVariance:\n", self.data.var(numeric_only=True))
        print("\nQuantiles:\n", self.data.quantile(numeric_only=True))

    #DATAFRAME OPERATIONS
    def dataframe_operations(self):
        if self.data is None:
            print("Load a dataset first!")
            return
        while True:
            print("\n== DataFrame Operations ==")
            print("1. Perform mathematical operations")
            print("2. Combine Multiple DataFrames")
            print("3. Split DataFrames")
            print("4. Back")

            choice = input("Enter your choice: ")

            #Mathematical Operations
            if choice == "1":
                col = input("Enter numeric column name: ")
                if col in self.data.columns and np.issubdtype(self.data[col].dtype, np.number):
                    print("Sum:", self.data[col].sum())
                    print("Mean:", self.data[col].mean())
                    print("Max:", self.data[col].max())
                    print("Min:", self.data[col].min())
                else:
                    print("Column not found or not numeric!")

            #Combine DataFrames
            elif choice == "2":
                path = input("Enter second CSV file path: ")
                try:
                    df2 = pd.read_csv(path)
                    combined = pd.merge(self.data, df2, left_on='Product', right_on='product_name', how='outer')
                    print("Combined DataFrame:")
                    print(combined.head())
                except Exception as e:
                     print("Error combining DataFrames:", e)


            #Split DataFrame
            elif choice == "3":
                try:
                    ratio = float(input("Enter split ratio (e.g. 0.7): "))
                    split_index = int(len(self.data) * ratio)
                    df1 = self.data.iloc[:split_index]
                    df2 = self.data.iloc[split_index:]
                    print("First Split:")
                    print(df1.head())
                    print("\nSecond Split:")
                    print(df2.head())
                except:
                    print("Invalid ratio")

            elif choice == "4":
                break
            else:
                print("Invalid choice")

    #VISUALIZATION
    def visualize_data(self):
        if self.data is None:
            print("Load a dataset first!")
            return
        while True:
            print("\n== Data Visualization ==")
            print("1. Bar Plot")
            print("2. Line Plot")
            print("3. Scatter Plot")
            print("4. Pie Chart")
            print("5. Histogram")
            print("6. Stack Plot")
            print("7. Heatmap (Seaborn)")
            print("8. Back")

            choice = input("Enter your choice: ")

            if choice == "1":
                plt.bar(self.data.iloc[:, 1], self.data.iloc[:, 3])
                plt.title("Bar Plot")
                self.current_plot = plt.gcf()
                plt.show()

            elif choice == "2":
                plt.plot(self.data.iloc[:, 0], self.data.iloc[:, 3])
                plt.title("Line Plot")
                self.current_plot = plt.gcf()
                plt.show()

            elif choice == "3":
                x = input("Enter x-axis column name: ")
                y = input("Enter y-axis column name: ")
                plt.scatter(self.data[x], self.data[y])
                plt.title("Scatter Plot")
                self.current_plot = plt.gcf()
                plt.show()

            elif choice == "4":
                self.data.groupby(self.data.columns[2])[self.data.columns[3]].sum().plot.pie(autopct="%1.1f%%")
                plt.title("Pie Chart")
                self.current_plot = plt.gcf()
                plt.show()

            elif choice == "5":
                self.data.iloc[:, 3].hist()
                plt.title("Histogram")
                self.current_plot = plt.gcf()
                plt.show()

            elif choice == "6":
                plt.stackplot(self.data.index, self.data.iloc[:, 3])
                plt.title("Stack Plot")
                self.current_plot = plt.gcf()
                plt.show()

            elif choice == "7":
                sns.heatmap(self.data.corr(numeric_only=True), annot=True)
                plt.title("Heatmap")
                self.current_plot = plt.gcf()
                plt.show()

            elif choice == "8":
                break

            else:
                print("Invalid choice")

    #SAVE PLOT
    def save_visualization(self):
        if self.current_plot is None:
            print("No plot generated yet to save!")
            return
        filename = input("Enter file name to save the plot (e.g., plot.png): ")
        try:
            self.current_plot.savefig(filename)
            print(f"Visualization saved as {filename} successfully!")
        except:
            print("Error saving the plot!")


#MAIN MENU
analyzer = SalesDataAnalyzer()

while True:
    print("\n========== Data Analysis & Visualization Program ==========")
    print("Please select an option:")
    print("1. Load Dataset")
    print("2. Explore Data")
    print("3. Perform DataFrame Operations")
    print("4. Handle Missing Data")
    print("5. Generate Descriptive Statistics")
    print("6. Data Visualization")
    print("7. Save Visualization")
    print("8. Exit")
    print("===========================================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        analyzer.load_dataset()
    elif choice == "2":
        analyzer.explore_data()
    elif choice == "3":
        analyzer.dataframe_operations()
    elif choice == "4":
        analyzer.handle_missing_data()
    elif choice == "5":
        analyzer.descriptive_stats()
    elif choice == "6":
        analyzer.visualize_data()
    elif choice == "7":
        analyzer.save_visualization()
    elif choice == "8":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice")
