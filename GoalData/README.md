GoalScrape.py can be used to scrape goal data from specified game scorer sheets and insert that data into a specified database table.  

The script requires installing BeautifulSoup, requests and pyodbc, which can be found at the locations specified below:
- https://www.crummy.com/software/BeautifulSoup/
- https://pypi.python.org/pypi/requests
- https://pypi.python.org/pypi/pyodbc

The script also requires a python class called GoalSummary, which I have written to simplify accumulating the scraped data for each goal event.  This file is included in the GoalData folder.

Usage (at command line): python GoalScrape.py [league] [starting GameID] [ending GameID] 

The data that is accumulated for each goal is coded to be written into a new record of a 'Goal' table present in a database named after the league specified at the command line, with the following column entries:
- GameID, GoalID, GameTime, AwayGoals, HomeGoals, Team, GameSituation, Scorer, Primary, Secondary, GF1, GF2, GF3, GF4, GF5, GA1, GA2, GA3, GA4, GA5

*Issues with league supplied scorer sheets for GameID's:
- WHL: 1009871, 1010377, 1010576, 1010833, 1010851 (non-existant player marked as on-ice for goal event)
- OHL: 5286, 5288, 10631 (All-Star games with incomplete scorer sheets)

GoalScrapeKeyError.py can be used to handle games with the non-existent player error.  It has built in error handling to account for the KeyErrors that are encountered with these erroneous scorer sheets.  Its usage is: python GoalScrapeKeyError.py [league] [GameID].
