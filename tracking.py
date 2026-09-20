from datetime import datetime
import os
from openpyxl import Workbook, load_workbook

# Excel file name
file_name = "daily_tracking.xlsx"

# values we are tracking
tracking_list = [
    "push_ups", "pull_ups", "curls", "curls_weight", 
    "hammer_curls", "hammer_curls_weight", "body_weight", 
    "calories", "drinks", "reading", 
    "creatine", "supplements" ,"mood"
    ]

#input prompts -- one for each value we want to track, feel free to modify both lists
tracking_questions = [
    "Push ups completed: ", 
    "Pull ups completed: ",
    "Bicep curls completed: ",
    "Dumbell weight for bicep curls: ",
    "Hammer curls completed: ",
    "Dumbell weight for hammer curls ",
    "Empty stomach & empty bladder weight: ",
    "~Calories consumed: ",
    "Drinks consumed: ",
    "Reading (0 - no, 1 - yes): ",
    "Creatine taken (0 - no, 1 - yes): ",
    "Supplements taken (0 - no, 1 - yes): ",
    "How we feelin', chief? 1 (shit) - 10 (God): ",
]

# creates a dict. {variable_name : variable_question}
tracking_dict = {}
for key, value in zip(tracking_list, tracking_questions):
    tracking_dict[key] = value


# get valid numerical inputs from user 
def get_valid_number(number):
    while True:
        user_input = input(number).strip()

        # Ease of use, pressing enter rather than entering a number - " skipping " - is equal to zero
        if user_input == "":
            return 0
        try:
            return float(user_input)

        except ValueError:
            print("^ ain't a number, my man!")


# determine whether user wants to edit or append
def get_choice():
    while True:
        choice = input(
            "Choose to add or append:\n"
            "1 = Add new entry\n"
            "2 = Alter previous entry\n"
        ).strip()

        if choice in ["1", "2"]:
            return choice

        print("Invalid input, please enter 1 or 2!")


# excel setup
def initialize_workbook():
    #create
    if not os.path.exists(file_name):
        workbook = Workbook()
        sheet = workbook.active

        headers = ["Date"] + tracking_list
        sheet.append(headers)

        workbook.save(file_name)

    return load_workbook(file_name)


# add new entry
def create_new_entry():
    #  creates a dict. {variable_name - variable_value}
    values_dict = {}

    # mapping
    for key, value in tracking_dict.items():
        values_dict[key] = get_valid_number(f"{value}: ")

    return values_dict


# append excel file
def append_entry(sheet, entry):
    # get date
    current_date = datetime.now().strftime("%Y-%m-%d")

    row = [current_date]

    # append all values to the row and the row to the sheet
    for field in tracking_list:
        row.append(entry[field])
    sheet.append(row)


# alter last row in excel file
def alter_previous_entry(sheet):
    # header row plus at least one data row required for editing to make sense
    if sheet.max_row < 2:
        print("There's no previous entry to alter, chief : | ")
        return

    # find last row 
    last_row = sheet.max_row

    # Loop through each field besides the date
    for index, field in enumerate(tracking_list, start=2):

        current_value = sheet.cell(row=last_row, column=index).value
        # ask the user to enter a new value for each field (enter to skip)
        prompt = tracking_dict[str(field)]
        amount_to_add = get_valid_number(f"{prompt}")

        # and append that value to the preexisting one 
        new_value = current_value + amount_to_add
        sheet.cell(row=last_row, column=index).value = new_value
        if new_value != 0:
            print(f"Updated value: {new_value}")

def main():

    workbook = initialize_workbook()
    sheet = workbook.active
    # append or modify
    choice = get_choice()

    # add new entry
    if choice == "1":
        # make and append a list of values
        entry = create_new_entry()
        append_entry(sheet, entry)

    # alter
    elif choice == "2":
        alter_previous_entry(sheet)

    workbook.save(file_name)

# run the program
if __name__ == "__main__":
    main()