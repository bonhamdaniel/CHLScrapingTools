from bs4 import BeautifulSoup
import sys
import requests
import pyodbc

league = sys.argv[1]
db_file = league + '.accdb'
conn_str = ("DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:/PythonPrograms/" + league + "/" + db_file + ";")
connection = pyodbc.connect(conn_str)
cursor = connection.cursor()

if league in 'OHL' or league in 'WHL':
	league = league.lower()
elif league in 'QMJHL':
	league = 'lhjmq'

print(league)

# WHL Games Include:  20013- 27661,  1000000 - 1014620
# completed: 49 - 
for game_id in range(int(sys.argv[2]), int(sys.argv[3])+1):
	gamesheet = 'http://cluster.leaguestat.com/game_reports/official-game-report.php?client_code=' + league + '&game_id=' + str(game_id) + '&lang=en'
	page = requests.get(gamesheet)
	soup = BeautifulSoup(page.text, 'html.parser')

	all_tables = soup.find_all("table")

	if len(all_tables) < 2:
		continue

	print(game_id)
	date_row = all_tables[1].findChildren("tr")[0]
	date_cell = date_row.findChildren("td")[0].findChildren("br")[0]
	date = str(date_cell)
	#date = date[date.index("</b>")+4:date.index("<br>\n</br>")].strip()
	date = date[date.index("</b>")+4:].strip()
	date = date[:date.index("<")].strip()
	#print(date)

	rows = all_tables[2].findChildren("tr")
	team_cell = rows[0].findChildren("td")[0].string
	visiting_team = team_cell[:-7]
	#print(visiting_team)

	rows = all_tables[4].findChildren("tr")
	team_cell = rows[0].findChildren("td")[0].string
	home_team = team_cell[:-7]
	#print(home_team)

	rows = all_tables[13].findChildren("tr")
	visiting_cells = rows[2].findChildren("tr")[0].findChildren("td")
	cell_num = len(visiting_cells) - 1
	visiting_goals = visiting_cells[cell_num].string
	#print(visiting_goals)

	rows = all_tables[13].findChildren("tr")
	home_cells = rows[2].findChildren("tr")[1].findChildren("td")
	cell_num = len(home_cells) - 1
	home_goals = home_cells[cell_num].string
	#print(home_goals)

	if (cell_num) == 5:
		OT = 'Yes'
	else:
		OT = 'No'
	#print(OT)

	if (cell_num) == 6:
		SO = 'Yes'
	else:
		SO = 'No'
	#print(SO)

	sql = """INSERT INTO GAME (GameID, GameDate, Visitor, Home, VisitorGoals, HomeGoals, OT, SO) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
	params = (str(game_id), date, visiting_team, home_team, visiting_goals, home_goals, OT, SO)
	cursor.execute(sql, params)
	connection.commit()

connection.close