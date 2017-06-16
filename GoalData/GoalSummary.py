class Goal(object):
	period = ""
	time_value =""
	team = ""
	game_situation = ""
	scorer = ""
	p_assist = ""
	s_assist = ""
	gf1 = ""
	gf2 = ""
	gf3 = ""
	gf4 = ""
	gf5 = ""
	ga1 = ""
	ga2 = ""
	ga3 = ""
	ga4 = ""
	ga5 = ""

def make_goal(period, time_value, team, game_situation, scorer, p_assist, s_assist, gf1, gf2, gf3, gf4, gf5, ga1, ga2, ga3, ga4, ga5):
	goal = Goal()
	goal.period = period
	goal.time_value = time_value
	goal.team = team
	goal.game_situation = game_situation
	goal.scorer = scorer
	goal.p_assist = p_assist
	goal.s_assist = s_assist
	goal.gf1 = gf1
	goal.gf2 = gf2
	goal.gf3 = gf3
	goal.gf4 = gf4
	goal.gf5 = gf5
	goal.ga1 = ga1
	goal.ga2 = ga2
	goal.ga3 = ga3
	goal.ga4 = ga4
	goal.ga5 = ga5
	return goal