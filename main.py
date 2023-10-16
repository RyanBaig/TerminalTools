from sys import argv as arg
import os

# Define Help MSG
def help():
    print("""
          
 _____                   _             _            _____           _        _             ______                  
|_   _|                 (_)           | |          |_   _|         | |      | |            | ___ \                 
  | | ___ _ __ _ __ ___  _ _ __   __ _| |  ______    | | ___   ___ | |___   | |__  _   _   | |_/ /   _  __ _ _ __  
  | |/ _ \ '__| '_ ` _ \| | '_ \ / _` | | |______|   | |/ _ \ / _ \| / __|  | '_ \| | | |  |    / | | |/ _` | '_ \ 
  | |  __/ |  | | | | | | | | | | (_| | |            | | (_) | (_) | \__ \  | |_) | |_| |  | |\ \ |_| | (_| | | | |
  \_/\___|_|  |_| |_| |_|_|_| |_|\__,_|_|            \_/\___/ \___/|_|___/  |_.__/ \__, |  \_| \_\__, |\__,_|_| |_|
                                                                                    __/ |         __/ |            
                                                                                   |___/         |___/             
          
                                Welcome to Terminal Tools By Ryan!
                        Thank you for using my project! I hope you like it.
                        
I recommend you check out the documentation for each module before using it.
Here are the commands:

- help
    - Prints this help message

- dbmanagement
    - Opens the Database Management Module

- filemanagement
    - Opens the File Management Module

          """)



help_msgs = ["help", "--help", "-h", "-help", "--h", "h"]
if arg in help_msgs:
    help()
elif arg == "filemanagement":
    os.system("python tools/file-management.py")
elif arg == "dbmanagement":
    os.system("python tools/db-management.py")
else:
    print("Unknown Command!")