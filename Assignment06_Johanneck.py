# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Jason Johanneck, 5/23/2022, Modified code to complete assignment 06
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
strFileName = "ToDoList.txt"  # The name of the data file
file_obj = None  # An object that represents a file
row_dic = {}  # A row of data separated into elements of a dictionary {Task,Rank}
lstTable = []  # A list that acts as a 'table' of rows
choice_str = ""  # Captures the user option selection


# Processing  --------------------------------------------------------------- #
class Processor:
    """ Processes the data in a list of dictionaries to and from a text file """

    @staticmethod
    def read_file_to_list_of_dictionaries(file_name, list_of_dictionary_rows):
        list_of_dictionary_rows.clear()  # clear any old data before loading
        file = open(file_name, "r")  # Causes ERROR if file does not exist!
        for line in file:
            item, value = line.split(",")
            row = {"Task": item.strip(), "Rank": value.strip()}
            list_of_dictionary_rows.append(row)
        file.close()
        return list_of_dictionary_rows, 'success'

    @staticmethod
    def remove_data_from_list_of_dictionaries(list_of_dictionary_rows, task_to_remove):
        for row in list_of_dictionary_rows:
            if row["Task"].lower() == task_to_remove.lower():
                lstTable.remove(row)
                # print("row removed")
        return list_of_dictionary_rows, 'success'

    @staticmethod
    def add_data_to_list_of_dictionaries(list_of_dictionary_rows, item, value):
        row = {"Task": str(item).strip(), "Rank": str(value).strip()}
        list_of_dictionary_rows.append(row)
        return list_of_dictionary_rows, 'success'

    @staticmethod
    def write_file_from_list_of_dictionaries(file_name, list_of_dictionary_rows):
        file = open(file_name, "w")
        for row in list_of_dictionary_rows:
            file.write(row["Task"] + "," + row["Rank"] + "\n")
        file.close()
        return list_of_dictionary_rows, 'success'

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    @staticmethod
    def print_menu():
        print('''
        Menu of Options
        1) Load Data from File
        2) Add a new Task
        3) Remove an existing Task
        4) Save Data to File
        5) Exit Program
        ''')

    @staticmethod
    def input_menu_choice():
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_list_items(list_of_rows):
        print("******* The Current Items Are: *******")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Rank"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_task_and_rank():
        task = str(input("What is the Task? - ")).strip()
        rank = str(input("What is the Rank? - ")).strip()
        print()  # Add an extra line for looks
        return task, rank

    @staticmethod
    def input_task_to_remove():
        task = str(input("Remove which item? - ")).strip()
        print()  # Add an extra line for looks
        return task


# Main Body of the Script  -------------------------------------------------- #
while(True):
    IO.print_current_list_items(lstTable)
    IO.print_menu()   # Test menu
    strChoice = IO.input_menu_choice()    # Test user choice

    if (strChoice == "1"):  # 1) Load Data from File
        lstTable, status = Processor.read_file_to_list_of_dictionaries(strFileName, lstTable)
        if status == 'success':
            print('Done!')
    elif (strChoice == "2"):  # 2) Add a new item
        strTask, strRank = IO.input_task_and_rank()
        lstTable, status = Processor.add_data_to_list_of_dictionaries(lstTable, strTask,strRank)
        if status == 'success':
            print('Done!')
    elif (strChoice == "3"):  # 3) Remove an existing item
        strTask = IO.input_task_to_remove()
        lstTable, status = Processor.remove_data_from_list_of_dictionaries(lstTable, strTask)
        if status == 'success':
            print('Done!')
    elif (strChoice == "4"):  # 4) Save Data to File And Exit Program
        lstTable, status = Processor.write_file_from_list_of_dictionaries(strFileName, lstTable)
        if status == 'success':
            print('Done!')
    elif (strChoice == "5"):
        print("Goodbye!")
        break
