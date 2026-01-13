import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#CLASS DEFINITION 
class LibraryDashboard:

    def __init__(self):
        self.df = None

    # 1.Load and Validate Data
    def load_data(self, file_path):
        try:
            if not file_path.endswith('.csv'):
                raise ValueError("Only CSV files are allowed")

            self.df = pd.read_csv(file_path)
            print("CSV file loaded successfully!\n")

            self.df.dropna(inplace=True)
            self.df['Date'] = pd.to_datetime(self.df['Date'])
            self.df = self.df[self.df['Borrowing Duration (Days)'] > 0]

            print("Data cleaned and validated successfully!\n")

        except Exception as e:
            print("Error:", e)

    # 2.Calculate Statistics
    def calculate_statistics(self):
        print("-----Library statistics-----\n")

        duration_array = np.array(self.df['Borrowing Duration (Days)'])

        most_borrowed = self.df['Book Title'].value_counts().idxmax()
        print("Most Borrowed Book:", most_borrowed)

        print("Average Borrowing Duration:", round(np.mean(duration_array), 2), "days")
        print("Borrowing Duration Standard Deviation:", round(np.std(duration_array), 2))

        busiest_day = self.df['Date'].dt.day_name().value_counts().idxmax()
        print("Busiest Day:", busiest_day)
        print()

    # 3.Filter Transactions
    def filter_transactions(self, genre=None, min_days=None):
        filtered_df = self.df

        if genre:
            filtered_df = filtered_df[filtered_df['Genre'] == genre]

        if min_days:
            filtered_df = filtered_df[filtered_df['Borrowing Duration (Days)'] >= min_days]

        print("-----Filtered Transactions (Preview)-----\n")
        print(filtered_df.head())
        print()

        return filtered_df

    # 4. Generate Summary Report
    def generate_report(self):
        print("-----Summary report-----\n")
        print("Total Transactions:", len(self.df))
        print("Unique Users:", self.df['User ID'].nunique())
        print("Unique Books:", self.df['Book Title'].nunique())
        print("Available Genres:", self.df['Genre'].unique())
        print()

    # 5.Data Visualizations
    def visualize_data(self):

        plt.figure()
        self.df['Book Title'].value_counts().head(5).plot(kind='bar')
        plt.title('Top 5 Most Borrowed Books')
        plt.xlabel('Book Title')
        plt.ylabel('Borrow Count')
        plt.show()

        plt.figure()
        self.df.set_index('Date').resample('ME').size().plot()
        plt.title('Monthly Borrowing Trend')
        plt.xlabel('Month')
        plt.ylabel('Number of Borrowings')
        plt.show()

        plt.figure()
        self.df['Genre'].value_counts().plot(kind='pie', autopct='%1.1f%%')
        plt.title('Books Borrowed by Genre')
        plt.ylabel('')
        plt.show()

        heatmap_df = self.df.copy()
        heatmap_df['Day'] = heatmap_df['Date'].dt.day_name()

        pivot_table = pd.pivot_table(
            heatmap_df,
            values='Borrowing Duration (Days)',
            index='Day',
            columns='Genre',
            aggfunc='mean',
            fill_value=0
        )

        plt.figure()
        sns.heatmap(pivot_table, annot=True)
        plt.title('Borrowing Activity Heatmap (Day vs Duration)')
        plt.show()

#MAIN EXECUTION
if __name__ == "__main__":

    dashboard = LibraryDashboard()

    while True:
        print("\n------E-LIBRARY DATA INSIGHTS DASHBOARD------")
        print()
        print("1. Load and Validate Data")
        print("2. Calculate Statistics")
        print("3. Filter Transactions")
        print("4. Generate Summary Report")
        print("5. Data Visualizations")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")
        print()

        if choice == '1':
            file_path = input("Enter CSV file name:-")
            print()
            dashboard.load_data(file_path)

        elif choice == '2':
            if dashboard.df is not None:
                dashboard.calculate_statistics()
            else:
                print("Please load data first!")

        elif choice == '3':
            if dashboard.df is not None:
                genre = None
                min_days = None
                dashboard.filter_transactions(genre=genre, min_days=min_days)
            else:
                print("Please load data first!")

        elif choice == '4':
            if dashboard.df is not None:
                dashboard.generate_report()
            else:
                print("Please load data first!")

        elif choice == '5':
            if dashboard.df is None:
                print("Please load data first!")
                continue

            while True:
                print("\n--- DATA VISUALIZATION MENU ---")
                print("1. Bar Chart: Top 5 Most Borrowed Books")
                print("2. Line Graph: Monthly Borrowing Trend")
                print("3. Pie Chart: Genre Distribution")
                print("4. Heatmap: Borrowing Activity")
                print("5. Back to Main Menu")

                vis_choice = input("Enter your choice (1-5): ")

                if vis_choice == '1':
                    plt.figure()
                    dashboard.df['Book Title'].value_counts().head(5).plot(kind='bar')
                    plt.title('Top 5 Most Borrowed Books')
                    plt.xlabel('Book Title')
                    plt.ylabel('Borrow Count')
                    plt.show()

                elif vis_choice == '2':
                    plt.figure()
                    dashboard.df.set_index('Date').resample('ME').size().plot()
                    plt.title('Monthly Borrowing Trend')
                    plt.xlabel('Month')
                    plt.ylabel('Borrowings')
                    plt.show()

                elif vis_choice == '3':
                    plt.figure()
                    dashboard.df['Genre'].value_counts().plot(kind='pie', autopct='%1.1f%%')
                    plt.title('Genre Distribution')
                    plt.ylabel('')
                    plt.show()

                elif vis_choice == '4':
                    heatmap_df = dashboard.df.copy()
                    heatmap_df['Day'] = heatmap_df['Date'].dt.day_name()

                    pivot = pd.pivot_table(
                        heatmap_df,
                        values='Borrowing Duration (Days)',
                        index='Day',
                        columns='Genre',
                        aggfunc='mean',
                        fill_value=0
                    )

                    plt.figure()
                    sns.heatmap(pivot, annot=True)
                    plt.title('Borrowing Activity Heatmap')
                    plt.show()

                elif vis_choice == '5':
                    break

                else:
                    print("Invalid visualization choice!")

        elif choice == '6':
            print("Exiting Dashboard. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")
