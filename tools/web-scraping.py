from functions.functions import Functions

cmd = input(
    """
      Hello! This is the Web Scraping Module. Using this, you can fetch HTML content, parse HTML content and more!

      Here are the options to pick from:
        
        - Fetch HTML Content from a webpage (1)
        - Parse HTML Content and retreive certain data from elements/attributes (2)
        - Take Screenshot of any Webpage (3)

        
        -- Suggest More at: https://github.com/RyanBaig/TerminalTools/issues/new?labels=Function%20Request&title=Function%20Request%20For%20Web%20Scraping%20Module
        
        Now, type the number of the command you want to run: """
)

try:
        try:
                cmd = int(cmd)
        except ValueError:
                print("Please input a valid integer!")
        if cmd == 1:
                # Fetch HTML
                url = input("Please provide the website URL: ")
                print(url)
                Functions.WebScraping.fetch_page_content(url)
        if cmd == 2:
                # Parse HTML
                url = input("Please Provide the website URL: ")
                element = input(
                "Please Provide the element you want to search for in the webpage's HTML: "
                )
                attribute = input(
                "(OPTIONAL) Please Provide the Attribute you want to retreieve the results for from the element: "
                )
                Functions.WebScraping.parse_html(url, element, attribute)
        if cmd == 3:
                # Take SS
                url = input("Please Provide the Website URL: ")
                Functions.WebScraping.take_screenshot(url)
except Exception as e:
        print("Error Occured: " + str(e))

