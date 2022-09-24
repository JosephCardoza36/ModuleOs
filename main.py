import os, sys
from colorama import init
from termcolor import colored  #adds color to command line
import platform

init()  #initalize colorama


class MyOps:
    def __init__(self):
        self.cwd = os.getcwd()
        self.name = platform.uname()
        self.system = sys.version

    def get_cwd(self):
        return f"\nCurrent working directory: " + colored(f"{self.cwd}", 'yellow', 'on_blue')

    def list_files(self):
        path = input("\nEnter '/' for root DIR or Enter the path to your folder: ")
        try: 
            dir_list = os.listdir(path)
        except:
            return colored("Path not found.", 'green', 'on_red')
        return f"\nFiles and directories in {path}: " + colored(f"{dir_list}", 'yellow', 'on_blue')

    def file_size(self):
        filename = "main.py"
        size = os.path.getsize(filename)
        return f"\nSize of the main.py is {size} bytes"

    def change_path(self):
        new_path = input("Enter your new path you want to work with: ")
        os.chdir(new_path)
        print(f"We are now in the following path: {os.getcwd()}")


my_comp = MyOps()
#checks for all methods in class that don't start with "__" the underscore are the built in methods
method_list = [method for method in dir(my_comp) if method.startswith('__') is False]

foo = True
while foo:
    user_choice = input(f"\n\nEnter 'exit' to close out of app. Choose from the following OS options: {method_list}\nEnter here: ").lower()

    if user_choice not in method_list and user_choice != "exit":
        print(colored("Invalid entry, try again", 'green', 'on_red'))

    elif user_choice == "exit":
        foo = False

    elif user_choice == "get_cwd":
        print(my_comp.get_cwd())

    elif user_choice == "list_files":
        print(my_comp.list_files())

    elif user_choice == "file_size":
        print(my_comp.file_size())

    elif user_choice == "name":
        print(f"The name of your computer is " + colored(f"{my_comp.name}", 'blue', 'on_yellow'))

    elif user_choice == "system":
        print(f"The name of your system is " + colored(f"{my_comp.system}", 'blue', 'on_yellow'))

    elif user_choice == "change_path":
        my_comp.change_path()

