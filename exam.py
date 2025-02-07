
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt


file_name = "files\\cap_rooms.csv"

""" get the file path """
def get_file_path(file_name):
    script_dir = Path(__file__).parent
    file_path = script_dir / file_name
    print(file_path)
    return file_path

""" get the largest value from group dataset by passing nth, column"""
def larget_value(grp, n, colname):
    return grp.nlargest(n, colname).iloc[-1]

"""read the csv and stored data into variable dataframe and return"""
def read_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e :
        print(e)
        return None

"""filter the 3 top rooms in dataframe variable based on the ptype, reviews"""
def filterTopRooms(df):
    print("Top Rooms")
    return df.groupby('PType').apply(lambda x: larget_value(x, 2, "Reviews"))
    
    

""" find the costliest and cheapest rooms in the dataframe based on the city"""
def cheapestRooms(df):
    cheapest_rooms = df.loc[df.groupby('City')['PPN'].idxmin()]
    costliest_rooms = df.loc[df.groupby('City')['PPN'].idxmax()]
    return cheapest_rooms, costliest_rooms

""" show the plot graph based on the PPN and Number of Beds """
def PPNWithRooms(df):
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Beds'], df['PPN'], color='blue', alpha=0.5)
    plt.title('Relationship between Price Per Night (PPN) and Number of Beds')
    plt.xlabel('Number of Beds')
    plt.ylabel('Price Per Night (PPN)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

""" show the menu to select the option for which type of report"""
def showMenu():
    print("\nMenu:")
    print("1. Top rooms")
    print("2. cheapest Room")
    print("3. PPNWithRooms")
    print("5. Exit")

""" Main function"""
def main():
    file_path = get_file_path(file_name)
    df = read_csv(file_path) 
    while True:
        showMenu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            result = filterTopRooms(df)
            print(result)
        elif choice == '2':
            maxprice, minprice = cheapestRooms(df)
            print('max price', maxprice)
            print('min price', minprice)
        elif choice == '3':
            PPNWithRooms(df)
        elif choice == '4':
            print("Exiting the menu. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.") 

if __name__ == "__main__":
    main()
