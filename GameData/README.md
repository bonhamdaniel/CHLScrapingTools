GameScrape.py can be used to scrape game data from specified game scorer sheets and insert that data into a specified database table.

The script requires installing BeautifulSoup, requests and pyodbc, which can be found at the locations specified below:
- https://www.crummy.com/software/BeautifulSoup/
- https://pypi.python.org/pypi/requests
- https://pypi.python.org/pypi/pyodbc

Usage (at command line): python GameScrape.py [league] [starting GameID] [ending GameID]

The data that is accumulated for each game is coded to be written into a new record of a 'Game' table present in a database named after the league specified at the command line, with the following column entries:

GameID, GameDate, Visitor, Home, VisitorGoal, HomeGoals, OT, SO
