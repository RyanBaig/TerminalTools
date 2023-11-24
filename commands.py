import sys

import fire

from old.tools.functions.functions import Functions as funcs

# -------------------- DB Management Module --------------------
def db():
    """Commands related to the Database Management Module

        Available Commands:
        - createdb (Create an SQLite Database)
        - sqlquery (Query an SQLite Database)
        - displaydb (Display an SQLite Database)
        - createtable (Create an SQLite Table in an existing database)
    """

    def createdb(DBPATH, TABLENAME, COLUMNS):
        """
        Create an SQLite Database
        """
        COLUMNS = COLUMNS.split(',')

        
        
        
        funcs.DBManagement.create_database(DBPATH, TABLENAME, COLUMNS)

    def createtable(DBPATH, TABLENAME, COLUMNS):
        """
        Create an SQLite Table in an existing database
        """

        COLUMNS = COLUMNS.split(',')

        funcs.DBManagement.create_table(DBPATH, TABLENAME, COLUMNS)

    def sqlquery(db):
        """
        Query an SQLite Database
        """
        funcs.DBManagement.sql_query(db)

    def displaydb(DBPATH, TABLENAME):
        """
        Display an SQLite Database
        """
        funcs.DBManagement.display_db(DBPATH, TABLENAME)

    return {
        'createdb': createdb,
        'createtable': createtable,
        'sqlquery': sqlquery,
        'displaydb': displaydb,
    }

# -------------------- File Management Module --------------------
def files():
    """Commands related to the File Management Module
    
    Available Commands:
    - list_files_dirs (List Files and Directories in a Directory)
    - create_dir (Create a Directory)
    - delete_files_dirs (Delete a File or Directory)
    - move (Move file or directory)
    - rename (Rename a File or Directory)
    - copy (Copy/Backup Contents of a File or Directory)
    - search (Search Directory/Directories)
    """

    def list_files_dirs(PATH):
        """
        List Files and Directories in a Directory
        """
        funcs.FileManagement.list_files_and_directories(PATH)

    def create_dir(DIRPATH):
        """
        Create a Directory
        """
        funcs.FileManagement.create_directory(DIRPATH)

    def delete_files_dirs(DIRPATH):
        """
        Delete a File or Directory
        """
        funcs.FileManagement.delete_file_or_directory(DIRPATH)

    def move(SOURCE, DEST):
        """
        Move file or directory
        """
        funcs.FileManagement.move(SOURCE, DEST)

    def rename(PATH, NEWNAME):
        """
        Rename a File or Directory
        """
        funcs.FileManagement.rename(PATH, NEWNAME)

    def copy(SOURCE, DEST):
        """
        Copy/Backup Contents of a File or Directory
        """
        funcs.FileManagement.copy(SOURCE, DEST)

    def search(DIR, CRITERIA):
        """
        Search Directory/Directories
        """
        funcs.FileManagement.search(DIR, CRITERIA)

    return {
        'list_files_dirs': list_files_dirs,
        'create_dir': create_dir,
        'delete_files_dirs': delete_files_dirs,
        'move': move,
        'rename': rename,
        'copy': copy,
        'search': search,
    }

# -------------------- Web Scraping Module --------------------
def webscraping():
    """
    Commands related to the Web Scraping Module
    
    Available Commands:
    - fetch_page (Fetch Page Content)
    - parse_html (Parse and Search HTML Content of a Website/Webpage)
    - take_ss (Take Screenshot of a Webpage)
    """

    def fetch_page_content(URL):
        """
        Fetch Content of a secure HTTPS Website/Webpage
        """
        funcs.WebScraping.fetch_page_content(URL)
    
    def parse_html(URL, ELEMENT, ATTRIBUTE=None):
        """
        Parse and Search HTML Content of a Website/Webpage
        """
        funcs.WebScraping.parse_html(URL, ELEMENT, ATTRIBUTE)

    def take_ss(URL):
        """
        Take Screenshot of a Webpage
        """
        funcs.WebScraping.take_screenshot(URL)

    return {
        'fetch_page': fetch_page_content,
        'parse_html': parse_html,
        'take_ss': take_ss
    }

# -------------------- Startup --------------------

if __name__ == '__main__':
    CLI = {
        '--db': db,
        '--files': files,
        '-db': db,
        '-files': files,
        '--webscr': webscraping,
        '-webscr': webscraping
    }

    # -------------------- Welcome MSG --------------------

    if len(sys.argv) == 1:
        url = 'https://terminal-tools-docs.ryanbaig.vercel.app'
        print(f"""
              
 _____                   _             _            _____           _       ______         ______                  
|_   _|                 (_)           | |          |_   _|         | |      | ___ \        | ___ \                 
  | | ___ _ __ _ __ ___  _ _ __   __ _| |  ______    | | ___   ___ | |___   | |_/ /_   _   | |_/ /   _  __ _ _ __  
  | |/ _ \ '__| '_ ` _ \| | '_ \ / _` | | |______|   | |/ _ \ / _ \| / __|  | ___ \ | | |  |    / | | |/ _` | '_ \ 
  | |  __/ |  | | | | | | | | | | (_| | |            | | (_) | (_) | \__ \  | |_/ / |_| |  | |\ \ |_| | (_| | | | |
  \_/\___|_|  |_| |_| |_|_|_| |_|\__,_|_|            \_/\___/ \___/|_|___/  \____/ \__, |  \_| \_\__, |\__,_|_| |_|
                                                                                    __/ |         __/ |            
                                                                                   |___/         |___/             
                                
                                Welcome to Terminal Tools By Ryan!
                        Thank you for using my project! I hope you like it.
                        
I recommend you check out the Documentation ({url}) for each module before using it.

    
        """)
    # -------------------- Start the CLI --------------------
    fire.Fire(CLI, name='tt')
