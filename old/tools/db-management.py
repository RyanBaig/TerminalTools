from functions.functions import Functions

cmd = input(
    """
      Hello! This is the Database Management Module. Using this, you can edit database tables, columns, data and more using SQLite!

      Here are the options to pick from:
        
        - Create Database (1)
        - Create Table in Existing Database (2)
        - Insert Query to Database (3)
        - Display Contents of a Database (4)
        
        
        -- Suggest More at: https://github.com/RyanBaig/TerminalTools/issues/new?labels=Function%20Request&title=Function%20Request%20For%20DB%20Management%20Module
        
        Now, type the number of the command you want to run: 
      """
)

try:
    try:
        cmd = int(cmd)
    except ValueError:
        print("Please input a valid integer!")
    if cmd == 1:
        # Create Database
        dbname = input(
            "Enter the name of the database with path (e.g, C:\\Users\\Hp\\Documents\\sqlite.db): "
        )
        print(
            """
              Disclaimer: The format of the columns with data types should match the format EXACTLY, otherwise it will result in an error.
              COLUMN FORMAT: 
              id INTEGER, name TEXT, age INTEGER 
              """
        )
        columns_input = input(
            "Enter a list of columns with data types (e.g., 'id INTEGER, name TEXT, age INTEGER'): "
        )

        tablename = input("Enter the name of the table in the database: ")
        columns = [col.strip() for col in columns_input.split(",")]
        Functions.DBManagement.create_database(dbname, tablename, columns)
    if cmd == 2:
        # Create Table
        dbname = input(
            "Enter the name of the path of the database (e.g, C:\\Users\\Hp\\Documents\\sqlite.db): "
        )
        print(
            """
              Disclaimer: The format of the columns with data types should match the format EXACTLY, otherwise it will result in an error.
              COLUMN FORMAT: 
              id INTEGER, name TEXT, age INTEGER 
              """
        )
        columns_input = input(
            "Enter a list of columns with data types (e.g., 'id INTEGER, name TEXT, age INTEGER'): "
        )
        tablename = input("Enter the name of the table in the database: ")
        columns = [col.strip() for col in columns_input.split(",")]
        Functions.DBManagement.create_table(dbname, tablename, columns)

    if cmd == 3:
        # Query a DB
        dbpath = input("Please Enter the path of the Database: ")
        Functions.DBManagement.sql_query(dbpath)
    if cmd == 4:
        # Display Contents
        db_name = input("Please enter the path to the database: ")
        table_name = input(
            "Please enter the name of the table you want to display information from: "
        )
        Functions.DBManagement.display_db(db_name, table_name)

except Exception as e:
    print("Error Occured: " + str(e))
