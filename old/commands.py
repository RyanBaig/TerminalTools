import os
import sys

# Define the hyperlink URL
url = "https://terminaltools-docs.ryanbaig.vercel.app"

# Define Help MSG
def help():
    print(f"""
          
 _____                   _             _            _____           _        _             ______                  
|_   _|                 (_)           | |          |_   _|         | |      | |            | ___ \\               
  | | ___ _ __ _ __ ___  _ _ __   __ _| |  ______    | | ___   ___ | |___   | |__  _   _   | |_/ /   _  __ _ _ __  
  | |/ _ \\ '__| '_ ` _ \\| | '_ \\ / _` | | |______|   | |/ _ \\ / _ \\| / __|  | '_ \\| | | |  |    / | | |/ _` | '_ \\ 
  | |  __/ |  | | | | | | | | | | (_| | |            | | (_) | (_) | \\__ \\  | |_) | |_| |  | |\\ \\ |_| | (_| | | | |
  \\_/\\___|_|  |_| |_| |_|_|_| |_|\\__,_|_|            \\_/\\___/ \\___/|_|___/  |_.__/ \\__, |  \\_| \\_\\__, |\\__,_|_| |_|
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

- misc
    - Opens the Miscellaneous Module

          """)



if len(sys.argv) < 2:
    print("Usage: tt help")
else:
    command: str = sys.argv[1]

    if command == "help":
        help()

    elif command == "filemanagement":
        path = os.path.abspath(os.path.join(os.path.dirname(__file__))) + "\\tools\\file-management.py"
        os.system(f"python {path}")

    elif command == "dbmanagement":
        path = os.path.abspath(os.path.join(os.path.dirname(__file__))) + "\\tools\\db-management.py"
        os.system(f"python {path}")

    elif command == "webscraping":
        path = os.path.abspath(os.path.join(os.path.dirname(__file__))) + "\\tools\\web-scraping.py"
        os.system(f"python {path}")

    elif "misc" in command:
        path = os.path.abspath(os.path.join(os.path.dirname(__file__))) + "\\tools\\misc.py"
        args = " ".join(sys.argv[2:])
        os.system(f"python {path} {args}")

    elif command == "misc":
        path = os.path.abspath(os.path.join(os.path.dirname(__file__))) + "\\tools\\misc.py"
        os.system(f"python {path}")

    else:
        print("Invalid command. Available commands: help, filemanagement, dbmanagement, misc")