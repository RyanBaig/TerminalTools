import sys
import os


# Define the hyperlink URL
url = "https://github.com/RyanBaig"

# Define Help MSG
def help():
    print(f"""
          
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
                        
I recommend you check out the Documentation ({url}) for each module before using it.
Here are the commands:

- help
    - Prints this help message

- dbmanagement
    - Opens the Database Management Module

- filemanagement
    - Opens the File Management Module

- webscraping
    - Opens the WebScraping Module

          """)



if len(sys.argv) < 2:
    print("Usage: tt help")
else:
    command = sys.argv[1]

    if command == "help":
        help()
    elif command == "filemanagement":
        os.system("python tools/file-management.py")
    elif command == "dbmanagement":
        os.system("python tools/db-management.py")
    elif command == "webscraping":
        os.system("python tools/web-scraping.py")
    else:
        print("Invalid command. Available commands: help, filemanagement, dbmanagement")
