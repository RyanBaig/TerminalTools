# File management imports
import os
import shutil
import fnmatch

# DB management imports
import subprocess
import sqlite3
from prettytable import PrettyTable

# WebScraping imports
from bs4 import BeautifulSoup
import requests
import datetime
from datetime import date


class Functions:
    # Function to list files and directories in the current directory
    class FileManagement:
        @staticmethod
        def list_files_and_directories(dir):
            contents = os.listdir(dir)
            for item in contents:
                print(item)

        # Function to create a new directory
        @staticmethod
        def create_directory(directory_name):
            try:
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
                shutil.move(source, destination)
                print(f"'{source}' has been moved or renamed to '{destination}'.")
            except Exception as e:
                print(f"An error occurred: {str(e)}")

        # Function to Move a file or directory
        @staticmethod
        def rename(path: str, new_name: str):
            try:
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
        def copy(source, destination):
            try:
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

        @staticmethod
        def search(directory, criteria):
            results = []
            try:
                for root, _, files in os.walk(directory):
                    for file in files:
                        if fnmatch.fnmatch(file, criteria):
                            results.append(os.path.join(root, file))
                if results:
                    print("Search Results:")
                    for result in results:
                        print(result)
                else:
                    print("No matching files or directories found.")
            except Exception as e:
                print(f"An error occurred: {str(e)}")

    class DBManagement:
        @staticmethod
        def sql_query(db):
            query_file = os.path.abspath("tools/functions/query.sql")
            print("Query File Path: " + query_file)
            if os.path.exists(db):
                try:
                    # Open the notepad
                    subprocess.run(["notepad.exe", query_file])

                    # Read the contents
                    with open(query_file, "r") as file:
                        query = file.read()

                    # Establish a connection to your SQLite database
                    conn = sqlite3.connect(db)
                    cursor = conn.cursor()

                    # Execute the query
                    cursor.execute(query)

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
        def create_database(db_name, table_name, columns):
            db_folder, db_file = os.path.split(db_name)
            
            if not os.path.exists(db_folder):
                os.makedirs(db_folder)
            
            try:
                # Establish a connection to the database or create a new one if it doesn't exist
                conn = sqlite3.connect(db_name)
                cursor = conn.cursor()

                # Create the table with specified columns
                query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(columns)})"
                cursor.execute(query)

                # Commit the changes
                conn.commit()

                # Close the connection
                conn.close()

                print(
                    f"Database '{db_name}' and table '{table_name}' created successfully with columns: {', '.join(columns)}"
                )

            except sqlite3.Error as e:
                print(f"SQLite error: {e}")
            except Exception as e:
                print(f"An error occurred: {e}")

        @staticmethod
        def display_db(db, table):
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
        def create_table(db_name, table_name, columns):
            if os.path.exists(db_name):
                try:
                    # Establish a connection to the database or create a new one if it doesn't exist
                    conn = sqlite3.connect(db_name)
                    cursor = conn.cursor()

                    # Create the table with specified columns
                    query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(columns)})"
                    cursor.execute(query)

                    # Commit the changes
                    conn.commit()

                    # Close the connection
                    conn.close()

                    print(
                        f"Database '{db_name}' and table '{table_name}' created successfully with columns: {', '.join(columns)}"
                    )
                except sqlite3.Error as e:
                    print(f"SQLite error: {e}")
                except Exception as e:
                    print(f"An error occurred: {e}")
            else:
                print(
                    f"Error: The database file '{db_name}' doesn't exist or the file path is incorrect."
                )

    class WebScraping:
        @staticmethod
        def fetch_page_content(url: str):
            try:
                if not url.startswith("https://"):
                    better_url = "https://" + url
                    print(f"Fetching URL: {better_url}")
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
        def parse_html(url: str, element: str, attr=None):

            if not url.startswith("https://"):
                better_url = "https://" + url
            else:
                better_url = url
            html = Functions.WebScraping.return_page_content(better_url)
            soup = BeautifulSoup(html, "html.parser")
            if attr and element:
                found_html = [elements.get(attr) for elements in soup.find_all(element)]
                print("Results with attributes:")
                for __ in found_html:
                    print(__)
            elif not attr and element:
                found_html = [elements.text for elements in soup.find_all(element)]
                print("Results without attributes:")
                for _ in found_html:
                    print(_)

            return None

        @staticmethod
        def take_screenshot(url: str):
            try:
                if not url.startswith("https://"):
                    better_url = "https://" + url
                else:
                    better_url = url

                token = os.environ.get("SHOT_API_TOKEN")
                if not token:
                    token = "P1Y95B2-XKWM858-H3MFG80-J0AQS4F"
                apiUrl = f"https://shot.screenshotapi.net/screenshot?token={token}&url={better_url}&output=image&file_type=png&wait_for_event=load"
                r = requests.get(apiUrl)

                if r.status_code == 200:
                    current_directory = os.getcwd()
                    image_path = os.path.join(
                        current_directory, f"{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}_website_screenshot.png"
                    )

                    with open(image_path, "wb") as image_file:
                        image_file.write(r.content)

                    print(f"Screenshot saved at path: {image_path}")
                else:
                    print(
                        f"Failed to capture a screenshot. Status code: {r.status_code}"
                    )

            except Exception as e:
                print(f"Error: {str(e)}")
