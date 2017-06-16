from bs4 import BeautifulSoup
import requests
import pyodbc
import GoalSummary

def getRoster(data, players):
	table = data
	rows = table.findChildren("tr")
	for row in rows[2:4]:
		cells = row.find_all()
		if '<b>' in str(cells[2]):
			cells[2].string = cells[2].b.string
		if len(cells[2].string) < 3:
			continue
		elif bool(cells[2].string):
			players[cells[1].string.strip()] = cells[2].string.strip().split(',')[0].strip() + '.' + cells[2].string.strip().split(',')[1].strip()
		else:
			players[cells[1].string.strip()] = cells[3].string.strip().split(',')[0].strip() + '.' + cells[3].string.strip().split(',')[1].strip()
	for row in rows[4:len(rows)]:
		cells = row.find_all()
		if '<b>' in str(cells[2]):
			cells[2].string = cells[2].b.string
		if len(cells[2].string) < 3:
			continue
		elif bool(cells[2].string):
			players[cells[1].string.strip()] = cells[2].string.strip().split(',')[0].strip() + '.' + cells[2].string.strip().split(',')[1].strip()
		else:
			players[cells[1].string.strip()] = cells[3].string.strip().split(',')[0].strip() + '.' + cells[3].string.strip().split(',')[1].strip()
	players[""] = "None"

def getGoals(away_players, home_players, goals):
	table = all_tables[7]
	rows = table.findChildren("tr")
	for row in rows[2:len(rows)]:
		cells = row.findChildren("td")
		if len(cells[0].string) > 1:
			period = cells[0].string.strip()[0]
			if period in "OT":
				period = 4
			if cells[1].string.strip().split(':')[0] in "":
				clock = 0
			else:
				clock = cells[1].string.strip().split(':')[0]
			time = ((int(period) - 1) * 20) + float(clock) + float(cells[1].string.strip().split(':')[1]) / 60
			minutes = ((int(period) - 1) * 20) + int(clock)
			time_value = str(minutes) + ":" + cells[1].string.strip().split(':')[1]
			#game_situation = cells[2].string.strip()
			if cells[2].string:
				game_situation = cells[2].string.strip()
			else:
				game_situation = "EV"
			# Gets Goal Scorer And Any Assists
			goal_summary = cells[3].string.strip().split('-')
			scorer = away_players[goal_summary[0].strip()]
			if len(goal_summary) > 1:# Assist One
				p_assist = away_players[goal_summary[1].strip()]
			else:
				p_assist = 'None'
			if len(goal_summary) > 2:# Assist Two
				s_assist = away_players[goal_summary[2].strip()]
			else:
				s_assist = 'None'
			# Gets Plus Players
			gf1 = away_players[cells[4].string.strip()]
			gf2 = away_players[cells[5].string.strip()]
			gf3 = away_players[cells[6].string.strip()]
			gf4 = away_players[cells[7].string.strip()]
			gf5 = away_players[cells[8].string.strip()]
			# Gets Minus Players
			ga1 = home_players[cells[10].string.strip()]
			ga2 = home_players[cells[11].string.strip()]
			ga3 = home_players[cells[12].string.strip()]
			ga4 = home_players[cells[13].string.strip()]
			ga5 = home_players[cells[14].string.strip()]
			#print(goal.name + "\t" + p_assist.name + "\t" + s_assist.name)
			goals[time] = GoalSummary.make_goal(period, time_value, "Away", game_situation, scorer, p_assist, s_assist, gf1, gf2, gf3, gf4, gf5, ga1, ga2, ga3, ga4, ga5)

	table = all_tables[8]
	rows = table.findChildren("tr")
	for row in rows[2:len(rows)]:
		cells = row.findChildren("td")
		if len(cells[0].string) > 1:
			period = cells[0].string.strip()[0]
			if period in "OT":
				period = 4
			if cells[1].string.strip().split(':')[0] in "":
				clock = 0
			else:
				clock = cells[1].string.strip().split(':')[0]
			time = ((int(period) - 1) * 20) + float(clock) + float(cells[1].string.strip().split(':')[1]) / 60
			minutes = ((int(period) - 1) * 20) + int(clock)
			time_value = str(minutes) + ":" + cells[1].string.strip().split(':')[1]
			#print(time_value)
			#game_situation = cells[2].string.strip()
			if cells[2].string:
				game_situation = cells[2].string.strip()
			elif cells[4].string.strip() in "":
				game_situation = "PP"
			else:
				game_situation = "EV"
			# Gets Goal Scorer And Any Assists
			goal_summary = cells[3].string.strip().split('-')
			scorer = home_players[goal_summary[0].strip()]
			if len(goal_summary) > 1:# Assist One
				p_assist = home_players[goal_summary[1].strip()]
			else:
				p_assist = 'None'
			if len(goal_summary) > 2:# Assist Two
				s_assist = home_players[goal_summary[2].strip()]
			else:
				s_assist = 'None'
			# Gets Plus Players
			gf1 = home_players[cells[4].string.strip()]
			gf2 = home_players[cells[5].string.strip()]
			gf3 = home_players[cells[6].string.strip()]
			gf4 = home_players[cells[7].string.strip()]
			gf5 = home_players[cells[8].string.strip()]
			# Gets Minus Players
			ga1 = away_players[cells[10].string.strip()]
			ga2 = away_players[cells[11].string.strip()]
			ga3 = away_players[cells[12].string.strip()]
			ga4 = away_players[cells[13].string.strip()]
			ga5 = away_players[cells[14].string.strip()]
			#print(goal.name + "\t" + p_assist.name + "\t" + s_assist.name)
			goals[time] = GoalSummary.make_goal(period, time_value, "Home", game_situation, scorer, p_assist, s_assist, gf1, gf2, gf3, gf4, gf5, ga1, ga2, ga3, ga4, ga5)
def scrape(game_num):
	#print(soup)
	# Dictionaries To Players For Each Team
	away_players = {}
	home_players = {}
	goals = {}

	# Get All Roster Information For Both Teams
	getRoster(all_tables[2], away_players)
	getRoster(all_tables[4], home_players)

	# Get All Penalty Information For Both Teams
	getGoals(away_players, home_players, goals)

	keys = sorted(goals.keys())

	home = 0
	away = 0
	for i in range(0, len(goals)):
		value = goals[keys[i]]
		if value.team in "Away":
			away += 1
		else:
			home += 1
		#print(game_num, i+1, value.time_value.split(":")[0] + "." + value.time_value.split(":")[1], away, home, value.team, value.game_situation, str(value.scorer), str(value.p_assist), str(value.s_assist), value.gf1, value.gf2, value.gf3, value.gf4, value.gf5, value.ga1, value.ga2, value.ga3, value.ga4, value.ga5)
		sql = """INSERT INTO Goal (GameID, GoalID, GameTime, AwayGoals, HomeGoals, Team, GameSituation, Scorer, Primary, Secondary, GF1, GF2, GF3, GF4, GF5, GA1, GA2, GA3, GA4, GA5) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
		params = (str(game_num), str(i+1), value.time_value.split(":")[0] + "." + value.time_value.split(":")[1], str(away), str(home), value.team, value.game_situation, str(value.scorer), str(value.p_assist), str(value.s_assist), value.gf1, value.gf2, value.gf3, value.gf4, value.gf5, value.ga1, value.ga2, value.ga3, value.ga4, value.ga5)
		cursor.execute(sql, params)
		connection.commit()

db_file = 'QMJHL.accdb'
conn_str = ("DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:/PythonPrograms/QMJHL/" + db_file + ";")
connection = pyodbc.connect(conn_str)
cursor = connection.cursor()

# QMJHL Games Include: 49 - 26383
# Done: 49-3705
# Errors on official scorers sheet:
#	2156/2157 - references Ottawa player #5, who doesn't exist, as on-ice for several goals
#	3706 - references Cape Breton player #25, who doesn't exist, as on-ice for several goals
for game_num in range(3707, 26383):
	gamesheet = 'http://cluster.leaguestat.com/game_reports/official-game-report.php?client_code=lhjmq&game_id=' + str(game_num) + '&lang=en'
	page = requests.get(gamesheet)
	soup = BeautifulSoup(page.text, 'html.parser')

	all_tables = soup.find_all("table")
	if len(all_tables) > 1:
		print(game_num)
		scrape(game_num)

connection.close()