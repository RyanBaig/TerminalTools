from functions.functions import Functions

cmd = input("""
      Hello! This is the File Management Module. Using this, you can edit files, directories, and more!

      Here are the options to pick from:
        
        - List Items/Directories in a Directory (1)
        - Create a Directory (2)
        - Delete a File or Directory (3)
        - Move file or directory (4)
        - Rename a File or Directory (5)
        - Copy Contents of a File or Directory (6)
        - Search Directory/Directories (VERY POWERFUL!) (7)
        
        -- Suggest More at: https://github.com/RyanBaig/TerminalTools/issues/new?labels=Function%20Request&title=Function%20Request%20For%20File%20Management%20Module
        
        Now, type the number of the command you want to run: 
      """)

try:
        try:
                cmd = int(cmd)
        except ValueError:
                print("Please input a valid integer!")
        if cmd == 1:
                # List files and directories
                dir = input("Enter the directory path: ")
                Functions.FileManagement.list_files_and_directories(dir)
        if cmd == 2:
                # Create a new directory
                dir = input("Enter the directory path: ")
                Functions.FileManagement.create_directory(dir)
        if cmd == 3:
                # Delete a file
                file_or_dir = input("Enter the file or directory path: ")
                Functions.FileManagement.delete_file_or_directory(file_or_dir)
        if cmd == 4:
                # Move a file
                file_or_dir = input("Enter the file or directory path: ")
                destination = input("Input the destination path: ")
                Functions.FileManagement.move(source=file_or_dir, destination=destination)
        if cmd == 5:
                # rename a file
                file = input("Enter the file or directory path: ")
                name = input("Provide the new name for the file: ")
                Functions.FileManagement.rename(path=file, new_name=name)
        if cmd == 6:
                # copy a file or dir
                s = input("Input the Path or Directory that you want to Copy: ")
                dest = input("Provide the destination of the copied file/folder: ")
                Functions.FileManagement.copy(source=s, destination=dest)
        if cmd == 7:
                # Search for files or directories
                directory = input("Enter the directory to search in: ")
                criteria = input("Enter search criteria (e.g., file name, extension, content): ")
                Functions.FileManagement.search(directory, criteria)
except Exception as e:
        print("An error occurred:", str(e))