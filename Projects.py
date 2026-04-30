#Calculator
def calc(num1, num2, op):
    if op == 1:
        return num1 + num2
    elif op == 2:
        return num1 - num2
    elif op == 3:
        return num1 * num2
    elif op == 4:
        return num1 / num2
    else:
        return "Invalid operation"

# File Mnanagement
import os
def create_file(filename):
    try:
        with open(filename , "x") as f:
            print(f"{filename} created succesfully")
    except FileExistsError:
        print("File already exists")
    except Exception as e:
        print("An error occurred")

def view_all_files():
    try:
        files = os.listdir()
        if not files:
            print("file not found!")
        else:
            print("file found succesfully")
            for file in files:
                print(file)
    except FileNotFoundError:
        print("File already exists")
    except Exception as e:
        print("An error occurred")

def read_file(filename):
    try:
        with open(filename , "r") as f:
            content = f.read()
            print(f"Content of{filename}: /n{content}")
    except FileExistsError:
        print("File already exists")
    except Exception as e:
        print("An error occurred")

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"'{filename}':deleted succesfully")
    except FileExistsError:
        print("File already exists")
    except Exception as e:
        print("An error occurred")

def edit_file(filename):
    try:
        with open(filename , "a") as f:
            content = input()
            f.write(content + "/n")
            print("Content added to {filename succesfully}")
    except FileExistsError:
        print("File already exists")
    except Exception as e:
        print("An error occurred")

def main():
    while True:
        print("File Mnanagement")
        print("1:Create File")
        print("2:Read File")
        print("3:Edit File")
        print("4:Delete File")
        print("5:View All File")
        print("6:Exit")

        choose = input("Enter a number: ")
        if choose == '1':
            filename = input("Enter the file name:")
            create_file(filename)
        elif choose == "2":
            filename = input("Enter the file name:")
            read_file(filename)
        elif choose == "3":
            filename = input("Enter the file name:")
            edit_file(filename)
        elif choose == "4":
            filename = input("Enter the file name:")
            delete_file(filename)
        elif choose == "5":
            view_all_files()
        elif choose == "6":
            print("Exit Succesfully")
            break
        else:
            print("Invalid Input")
        
if __name__ == "__main__":
    main()
        


