import pandas as pd
import matplotlib.pyplot as plt
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def validate_filename(filename):   
    if not filename.endswith('.csv'):
        name, ext = os.path.splitext(filename)
    return f"{filename}.csv" if ext != ".csv" else filename
    
def load_csv_file():
    filename = input("Please provide file name that should be analyzed: ")
    filename = validate_filename(filename)
    
    try:
        df = pd.read_csv(filename)
        return df
    except FileNotFoundError:
        print("File was not found. Please check if it is in the same directory as the program.")
    except pd.errors.EmptyDataError:
        print("File is empty.")
    except pd.errors.ParserError:
        print("Error while reading the file. Please check file format. It should be csv.")
    except Exception as e:
        print(f"Error: {e}")
    return None
    
def visualize_data(df):
    print("Vizualization of products vs amount")
    plt.figure(figsize=(8, 5))
    plt.bar(df["Product"], df["Amount"], color='skyblue')
    plt.xlabel("Product")
    plt.ylabel("Amount")
    plt.title("Amount of products that were sold")
    plt.xticks(rotation=45)
    plt.show()
    
def export_data(df):
    attempts = 0 #number that will be allowed to insert input. After that will be coming back to additional choices.
    while attempts<3:        
        data_to_export = input("What data would you like to include into export? \n 1: main information of the file \n 2: statistics \n 3: missing values (of each column) \n 4: correlation \n Please input numbers seperated by comma: ")
        selected = set(data_to_export.replace(' ', '').split(','))
        valid_choices = {'1', '2', '3', '4'}
        
        if selected.issubset(valid_choices):
                     selected_data = []                      
                     if '1' in data_to_export:
                        selected_data.append("Main information: ")
                        selected_data.append(str(df.info()))
                     if '2' in data_to_export:
                        selected_data.append("Statistics: ")
                        selected_data.append(df.describe())
                     if '3' in data_to_export:
                        selected_data.append("Missing values: ")
                        selected_data.append(df.isnull().sum())
                     if '4' in data_to_export:
                        selected_data.append("Correlation: ")
                        selected_data.append(df.corr(numeric_only=True))
                     file_name_of_exp = input("Please provide filename to export to: ")
                     file_name_of_exp = validate_filename(file_name_of_exp)
                     with open(file_name_of_exp, 'w') as f:
                        for item in selected_data:
                            f.write(str(item) + "\n")
                     print(f"Exported results to {file_name_of_exp}")
                     break 
        else:
            clear_screen()
            attempts += 1
            invalid_choices = sorted(selected - valid_choices)
            print(f"Incorrect choice: {', '.join(map(str, invalid_choices))} - there is no such choice. Try again.")
            if attempts==3:
                print("You have reached your attempt limit.")
        
    

def main():
    df = load_csv_file()
    if df is None:
        return
    print("ANALYSIS OF THE FILE")

    #information about data in the file
    print("Main information: ")
    print(df.info())
    
    #first 5 lines
    print("First 5 lines in the file: ")
    print(df.head())

    #main statistic of the file
    #describe - only describes numerical columns
    print("Statistics: ")
    print(df.describe())

    while True:
    #Additional choices
        print("Additional analysis options: ")
        print("1: Show columns")
        print("2: Correlation")
        print("3: Show missing values in columns")
        print("4: Export results to csv")
        print("5: Visualization of products vs amount")
        print("6: End")
        
        add_choices = input("Please select option: ").strip()
        
        clear_screen()
        
        if add_choices == "1":
             print("Columns in data: ")
             print(df.columns)
        elif add_choices == "2":
             print("Correlation: ")
             print(df.corr(numeric_only=True))          
        elif add_choices == "3":
             print("Missing values:")
             print(df.isnull().sum())
        elif add_choices == "4":
            export_data(df)
        elif add_choices == "5":
            visualize_data(df)
        elif add_choices == "6":
             print("END")
             break
        else:
             print("Incorrect choice")
         
        contin = input("Would you like to proceed? (Y/N): ").strip().lower()
        if contin != "y":
            print("Program ended.")
            break
         
def run():
    if __name__ == "__main__":
        main()
        
run()
 
