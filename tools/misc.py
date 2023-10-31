from sys import argv
from functions.functions import Functions
import os

def startup():
    print("""
        Hello! This is the Miscellaneous Module. It contains some functions that do not belong in any other module.

        Here are the options to pick from:
            
            - Coder-Search (Searches your query and only gets results from GitHub or StackOverflow) 
                - For Example: `tt misc coder-search what are LLMS?` 

            - Local Development Server (Opens a local devlopment server at localhost:8080 with files from the current directory. use `dev start` and `dev stop`) 
                - For Example: `tt misc dev start` OR `tt misc dev stop`

            - EXE (I use it to automatically open the auto-py-to-exe dialog to package my projects.) 
                - For Example: `tt misc exe`
            
            -- Suggest More at: https://github.com/RyanBaig/TerminalTools/issues/new?labels=Function%20Request&title=Function%20Request%20For%20Miscellaneous%20Module
            
            ALIASES:

                - Coder-Search: `tt misc coder-search` OR `tt misc cs`

                - Local Development Server: `tt misc dev` OR `tt misc devserver`

                - EXE: `tt misc exe`

            Tip: To activate these, type `tt misc {FUNCTION_NAME}`
            
        """)

# Call the startup function
startup()
try:
        cmd = argv[1]   
        if cmd == "coder-search" or cmd == "cs":
                # Coder-Search
                Functions.Miscellaneous.coder_search(argv[2:])
        if cmd == "dev" or cmd == "devserver":
                # DevServer
                Functions.Miscellaneous.devserver(argv[2])
        if cmd == "exe":
                Functions.Miscellaneous.exe()
        elif cmd not in ["coder-search", "cs", "dev", "devserver", "exe"]:
            print("Invalid Function! Available Functions: coder-search/cs, dev/devserver, exe")
except Exception as e:
        print("Error Occured: " + str(e))

