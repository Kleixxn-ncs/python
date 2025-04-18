import os

# 1. Function to clear the screen
def cls():
    os.system("cls" if os.name == "nt" else "clear")

# 2. Function to create an empty file
def create_file(file_name):
    try:
        with open(file_name, 'x') as file:
            print(f"File '{file_name}' has been created.")
    except FileExistsError:
        print(f"Error: The file '{file_name}' already exists.")

# 3. Function to write content to an existing file
def write_to_file(file_name, content):
    if os.path.isfile(file_name):  # Check if file exists
        with open(file_name, 'w') as file:
            file.write(content)
        print(f"Content successfully written to '{file_name}'.")
    else:
        print(f"Error: The file does not exist. Writing aborted.")

# 4. Function to read the content of a file
def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return f"Error: The file '{file_name}' does not exist."

# 5. Function to delete a file
def delete_file(file_name):
    try:
        os.remove(file_name)
        print(f"File '{file_name}' has been deleted.")
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")

def employee_Data():
    fname = input("Enter First Name: ")
    lname = input("Enter Last Name: ")
    age = input("Age: ")
    gender = input("Gender: ")
    return {"First Name": fname, "Last Name": lname, "Age": age, "Gender": gender}

def deduction_List():
    # Deduction details
    sss = input("Enter SSS Contribution: ")
    pagIbig = input("Enter Pag-IBIG Contribution: ")
    philHealth = input("Enter PhilHealth Contribution: ")
    bir_tax = input("Enter BIR Tax: ")

    # Returning the deductions as a dictionary
    return {
        "SSS": sss,
        "Pag-IBIG": pagIbig,
        "PhilHealth": philHealth,
        "BIR Tax": bir_tax
    }
def confirmDelete():
    comms = input("Enter Command: ").lower()
    if comms == "e":
        file_name_del = 'employee.txt'
    elif comms == "d":
        file_name_del = 'deductions.txt'
    else:
        print("Invalid Command: ")
    return file_name_del