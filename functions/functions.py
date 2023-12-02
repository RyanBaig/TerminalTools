"""
Functions for TerminalTools.
"""
import datetime

# File management imports
import os
import platform
import shutil
import sqlite3
import fnmatch
import glob
from concurrent.futures import ThreadPoolExecutor
# DB management imports
import subprocess
import webbrowser
# Misc imports
from urllib.parse import quote
import requests
# WebScraping imports
from bs4 import BeautifulSoup
from envhub import get_var
from prettytable import PrettyTable


class Functions:
    """
    TerminalTools Functions.
    """
    # Function to list files and directories in the current directory
    class FileManagement:
        @staticmethod
        def list_files_and_directories(dir):
            if dir is None:
                print("Args: --PATH <path to dir>")
            else:
                contents = os.listdir(dir)
                for item in contents:
                    print(item)

        # Function to create a new directory
        @staticmethod
        def create_directory(directory_name):
            try:
                if directory_name is None:
                    print("Args: --DIRPATH <path to dir>")
                else:
                    os.mkdir(directory_name)
                    print(f"Directory '{directory_name}' created.")
            except FileExistsError:
                print(f"Directory '{directory_name}' already exists.")
            except Exception as e:
                print(f"An error occurred: {str(e)}")

        # Function to delete a file or directory
        @staticmethod
        def delete_file_or_directory(path):
            try:
                if path is None:
                    print("Args: --DIRPATH <path to dir>")
                else:
                    if os.path.isfile(path):
                        os.remove(path)
                        print(f"File '{path}' deleted.")
                    elif os.path.isdir(path):
                        os.rmdir(path)
                        print(f"Directory '{path}' deleted.")
                    else:
                        print(f"'{path}' is not a valid file or directory.")
            except Exception as e:
                print(f"An error occurred: {str(e)}")

        # Function to rename a file or directory
        @staticmethod
        def move(source, destination):
            try:
                if source is None or destination is None:
                    print("Args: --SOURCE <path to source> --DEST <path to destination>")
                else:
                    shutil.move(source, destination)
                    print(f"'{source}' has been moved or renamed to '{destination}'.")
            except Exception as e:
                print(f"An error occurred: {str(e)}")

        # Function to Move a file or directory
        @staticmethod
        def rename(path: str, new_name: str):
            try:
                if path is None or new_name is None:
                    print("Args: --PATH <path to file/dir> --NEWNAME <new name of file/dir>")
                else: 
                    if os.path.isdir(path):
                        # Rename a directory by changing its name
                        os.rename(path, new_name)
                        print(f"Renamed directory to '{path}'")
                    elif os.path.isfile(path):
                        # Rename a file by changing its name

                        new_path = os.path.join(os.path.dirname(path), new_name)
                        os.rename(path, new_path)
                        print(f"Renamed file to '{new_path}'")
                    else:
                        print(f"'{path}' is not a valid file or directory.")
            except Exception as e:
                print(f"An error occurred: {str(e)}")

        @staticmethod
        # Function to copy a file or folder to the destination
        def copy(source, destination):
            try:
                if source is None or destination is None:
                    print("Args: --SOURCE <path to source> --DEST <path to destination>")
                else:
                    if os.path.exists(source):
                        if os.path.isfile(source):
                            shutil.copy2(source, destination)
                            print(f"File '{source}' copied to '{destination}'")
                        elif os.path.isdir(source):
                            shutil.copytree(source, destination)
                            print(f"Directory '{source}' copied to '{destination}'")
                        else:
                            print(f"'{source}' is not a valid file or directory.")
                    else:
                        print(f"'{source}' does not exist.")
            except Exception as e:
                print(f"An error occurred: {str(e)}")
        
        # Function to search for files
        @staticmethod
        def search(directory, criteria):
            if directory is None or criteria is None:
                print("Args: --DB ")
            else:
                input('Please make sure the criteria you provided is following the correct types: file name, extension, or content')
                if input:
                    try:
                        found_files = []
                        # If search pattern is a file name
                        if os.path.exists(os.path.join(directory, criteria)):
                            found_files.append(os.path.join(directory, criteria))
                        # If search pattern is an extension
                        elif criteria.startswith('*'):
                            pattern = '*' + criteria
                            found_files.extend(glob.glob(os.path.join(directory, pattern)))

                        # If search pattern is content within files
                        else:
                            for root, dirnames, filenames in os.walk(directory):
                                for filename in fnmatch.filter(filenames, '*'):  
                                    file_path = os.path.join(root, filename)
                                    with open(file_path, 'r', encoding="utf-8", errors='ignore') as file:     
                                        if criteria in file.read():
                                            found_files.append(file_path)

                            if len(found_files) == 0:
                                print("No files found matching the search pattern.")
                            else:
                                print("Found files:")
                                path = os.path.join(os.getcwd(), "found_files.txt")
                                for file_path in found_files:
                                    print(file_path)
                                    
                                    with open(path, 'a') as f:
                                        f.write(file_path + '\n')
                                print(f"Found {len(found_files)} files matching the search pattern and saved to {path}.")

                    except Exception as e:
                        print('An Error Occured: ' + str(e))

    class DBManagement:
        @staticmethod
        # Function to send queries to a database
        def sql_query(db):
            if db is None:
                print("Args: --DB <path to db>")
            else:
            
                query_file = os.path.abspath("old/tools/functions/query.sql")
                
                if os.path.exists(db):
                    try:
                        # open the file
                        if platform.system() == 'Windows':
                            subprocess.Popen(['start', query_file], shell=True)
                        elif platform.system() == 'Darwin':  # macOS
                            subprocess.Popen(['open', query_file])
                        else:  # Linux
                            subprocess.Popen(['xdg-open', query_file])

                        # Wait for user to press Enter before proceeding
                        input("Press Enter when you have finished editing the query...")


                        # Read the contents
                        with open(query_file, "r") as file:
                            sql_commands = file.read().splitlines()
                            
                        # Establish a connection to your SQLite database
                        conn = sqlite3.connect(db)
                        cursor = conn.cursor()

                        for cmd in sql_commands:
                            # Execute the query
                            cursor.execute(cmd)

                        # Commit the changes if necessary
                        conn.commit()

                        # Close the connection
                        conn.close()

                        print("Query executed successfully.")

                    except FileNotFoundError:
                        print("Query file not found.")
                    except sqlite3.Error as e:
                        print(f"SQLite error: {e}")
                    except Exception as e:
                        print(f"An error occurred: {e}")
                else:
                    print(
                        f"Error: The database file '{db}' doesn't exist or the file path is incorrect."
                    )

        @staticmethod
        def create_database(db_path, table_name, columns):
            if db_path is None or table_name is None or columns is None:

                print("Args: --DBPATH <Database Path Here> --TABLENAME <TableName Here> --COLUMNS <Columns Here>")
            else:

                print("""Disclaimer: The format of the columns with data types should match the format EXACTLY, otherwise it will result in an error.
                COLUMN FORMAT: 
                id(INTEGER), name(TEXT), age(INTEGER)""")

                input("Are you sure you have provided the columns with the correct format as shown above? Press Enter to continue...")

                db_folder, db_file = os.path.split(db_path)
                
                if not os.path.exists(db_folder):
                    os.makedirs(db_folder)

                try:
                    # Establish a connection to the database or create a new one if it doesn't exist
                    conn = sqlite3.connect(db_path)
                    cursor = conn.cursor()

                    # Create the table with specified columns
                    column_defs = []

                    for column in columns:
                        column_parts = column.split('(')
                        if len(column_parts) < 2:
                            raise ValueError(f"Invalid column format: {column}. Expected format: column_name(data_type)")
                        
                        column_name = column_parts[0].strip()
                        data_type = column_parts[1].split(')')[0].strip()
                        
                        column_def = f"{column_name} {data_type}"
                        column_defs.append(column_def)

                    query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(column_defs)})"
                    cursor.execute(query)

                    # Commit the changes
                    conn.commit()

                    # Close the connection
                    conn.close()

                    print(f"Database '{db_path}' and table '{table_name}' created successfully with columns: {', '.join(column_defs)}")
                except sqlite3.Error as e:
                    print(f"SQLite error: {e}")
                except Exception as e:
                    print(f"An error occurred: {e}")

        @staticmethod
        # function to display the contents/data of a database using PrettyTables' tables
        def display_db(db, table):
            if db is None or table is None:
                print("Args: --DBPATH <Database Path Here> --TABLENAME <TableName Here>")
            else:
                if os.path.exists(db):
                    # Connect to DB
                    conn = sqlite3.connect(db)
                    cursor = conn.cursor()
                    # Retreive the data
                    cursor.execute(f"SELECT * FROM {table}")  # Get table name
                    data = cursor.fetchall()
                    
                    # Display it
                    table = PrettyTable()
                    table.field_names = [
                        i[0] for i in cursor.description
                    ]  # Get column names

                    for row in data:
                        
                        table.add_row(row)

                    print(table)
                    # Close the Connection
                    conn.close()
                else:
                    print(
                        f"Error: The database file '{db}' doesn't exist or the file path is incorrect."
                    )

        @staticmethod
        # function to create a table in pre-existing database
        def create_table(db_path, table_name, columns):
            
            if db_path is None or table_name is None or columns is None:
                print("Args: --DBPATH <Database Path Here> --TABLENAME <TableName Here> --COLUMNS <Columns Here>")
            else:
                if os.path.exists(db_path):
                    print("""Disclaimer: The format of the columns with data types should match the format EXACTLY, otherwise it will result in an error.
                    COLUMN FORMAT: 
                    id(INTEGER), name(TEXT), age(INTEGER) """)
                    input("Are you sure you have provided the columns with the correct format as shown above? Press Enter to continue...")
                    try:
                        # Establish a connection to the database or create a new one if it doesn't exist
                        conn = sqlite3.connect(db_path)
                        cursor = conn.cursor()
                        
                        # Create the table with specified columns
                        column_defs = []

                        for column in columns:
                            column_parts = column.split('(')
                            if len(column_parts) < 2:
                                raise ValueError(f"Invalid column format: {column}. Expected format: column_name(data_type)")
                            
                            column_name = column_parts[0].strip()
                            data_type = column_parts[1].split(')')[0].strip()
                            
                            column_def = f"{column_name} {data_type}"
                            column_defs.append(column_def)

                        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(column_defs)})"
                        cursor.execute(query)

                        # Commit the changes
                        conn.commit()

                        # Close the connection
                        conn.close()

                        print(f"Database '{db_path}' and table '{table_name}' created successfully with columns: {', '.join(column_defs)}")
                    except sqlite3.Error as e:
                        print(f"SQLite error: {e}")
                    except Exception as e:
                        print(f"An error occurred: {e}")
                else:
                    print(f"Error: The database file '{db_path}' doesn't exist or the file path is incorrect.")

    class WebScraping:
        @staticmethod
        # self-explanatory
        def fetch_page_content(url: str):
            try:
                if not url.startswith("https://"):
                    better_url = "https://" + url
                    
                else:
                    better_url = url
                username = os.path.expanduser("~")
                enddir = os.path.join(username, "Desktop", "WebsiteContent")
                if not os.path.exists(enddir):
                    os.makedirs(enddir)
                response = requests.get(better_url)
                if response.status_code == 200:
                    html = response.text
                    with open(f"{enddir}/Page_Content_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S') }.html", "w") as file:
                        file.write(html)
                    print(
                        f"""
                          Web Scraper Results
                          
                          Status Code: {response.status_code}
                          
                          
                          PAGE CONTENT:
                          {html}
                          
                          
                          The Content Has Also Been Saved to {enddir}/Page_Content_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S') }.html.html
                          """
                    )

                else:
                    print(
                        f"Failed to retrieve page. Status code: {response.status_code}"
                    )
            except requests.exceptions.RequestException as e:
                print("Request Error: " + str(e))
            return None

        @staticmethod
        # self-explanatory
        def return_page_content(url):
            try:
                if not url.startswith("https://"):
                    better_url = "https://" + url
                else:
                    better_url = url
                response = requests.get(better_url)
                if response.status_code == 200:
                    return response.text
                else:
                    print(
                        f"Failed to retrieve page. Status code: {response.status_code}"
                    )
            except requests.exceptions.RequestException as e:
                print("Request Error: " + str(e))
            return None

        @staticmethod
        # function to parse html and return the values of elements and attributes, if provided.
        def parse_html(url: str, element: str, attr=None):
            if not url.startswith("https://"):
                url = "https://" + url

            html = Functions.WebScraping.return_page_content(url)
            soup = BeautifulSoup(html, "html.parser")

            if attr:
                elements = soup.find_all(element, class_=attr)
            else:
                elements = soup.find_all(element)

            if elements:
                for el in elements:
                    print(el.text if el.text else "No text found")
            else:
                print("No elements found.")

            return None

        @staticmethod
        # function to take screenshot of any website
        def take_screenshot(url: str):
            try:
                if not url.startswith("https://"):
                    better_url = "https://" + url
                else:
                    better_url = url

                token = get_var("SHOT_API_TOKEN")
                
                apiUrl = f"https://api.screenshotone.com/animate?url={better_url}&scenario=scroll&access_key={token}"
                r = requests.get(apiUrl)

                if r.status_code == 200:
                    current_directory = os.getcwd()
                    image_path = os.path.join(
                        current_directory, f"{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}_website_screenshot.mp4"
                    )

                    with open(image_path, "wb") as image_file:
                        image_file.write(r.content)

                    print(f"Screenshot saved at path: {image_path}")
                else:
                    print(
                        f"Failed to capture a screenshot. Status code: {r.status_code} and Message:\n {r.json()}\n and URL: {apiUrl}"
                    )

            except Exception as e:
                print(f"Error: {str(e)}")
    class Miscellaneous:
        @staticmethod
        def coder_search(args):
            # Get the user's query from the command line.
            try:
                if args:
                    query = " ".join(args)  # Concatenate the words in the tuple
                    
                    query = query + " site:stackoverflow.com OR site:github.com"
                    query = query.replace("'", '"')

                    # Encode the query for safe transmission over the network.
                    query = quote(query)

                    # Open the Google search results page for the encoded query in a web browser.
                    webbrowser.open(f"https://www.google.com/search?q={query}")
                else:
                    print("ERROR! Please Make Sure Your Query is Present.")
            except IndexError:
                print("Indexing Error! Please Make Sure Your Query is Present.")
                exit()
        
        @staticmethod
        def devserver(cmd):
            # function to open/close a local development server
            if cmd:
                if cmd == "start":
                    current_directory = os.getcwd()
                    subprocess.Popen(["python", "-m", "http.server", "8080"], cwd=current_directory)
                    print(f"Server started at http://localhost:8080. Serving from {current_directory}")
                    webbrowser.open("http://localhost:8080")
                elif cmd == "stop":
                    if platform.system() == "Windows":
                        subprocess.Popen(["taskkill", "/f", "/im", "python.exe"])
                        print("Server stopped")
                    else:
                        subprocess.Popen(["pkill", "-f", "python -m http.server"])
                        print("Server stopped")
                else:
                    print("Invalid command!")
            else:
                print("Please provide a command!")
        @staticmethod
        # self-explanatory
        def exe():
            os.system("./auto-py-to-exe.exe")
            print("Auto-PY-To-EXE dialog box closed and process finished.")
