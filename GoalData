GoalsScrape.py can be used to scrape goal data from specified game scorer sheets and insert that data into a specified database table.  

The script requires installing BeautifulSoup, requests and pyodbc, which can be found at the locations specified below:
- https://www.crummy.com/software/BeautifulSoup/
- https://pypi.python.org/pypi/requests
- https://pypi.python.org/pypi/pyodbc

The script also requires a python class called GoalSummary, which I have written to simplify accumulating the scraped data for each goal event.  This file is included in the GoalData folder.

The data that is accumulated for each goal is coded to be written into a new record of a 'Goal' table present in a database named 'QMJHL', with the following column entries:
- GameID
- GoalID
- GameTime
- AwayGoals
- HomeGoals
- Team
- GameSituation
- Scorer
- Primary
- Secondary
- GF1
- GF2
- GF3
- GF4
- GF5
- GA1
- GA2
- GA3
- GA4
- GA5
