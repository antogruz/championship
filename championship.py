#!/usr/bin/env python3

class Team():
    def __init__(self, name, games, categories):
        self.name = name
        self.games = games
        self.done = [0] * categories


def team_score(team):
    count = 0
    for i in range(team.games):
        count += team.done[i]
    return count

def createChampionship(game_format, team_names):
    steps = []
    games = []
    roles = game_format.get_roles()
    teams = [Team(name, game_format.get_games(), len(roles)) for name in team_names]

    while not all_teams_done(teams, game_format):
        step = pick_step(games, game_format, sorted(teams, key = team_score))
        print_teams(step)
        print("roles orange", teams[5].done)
        steps.append(step)
        for i in range(game_format.get_games()):
            games.append([step[2*i], step[2*i + 1]])

    championship = [ [ team.name for team in step ] for step in steps]
    return championship

def pick_step(games, game_format, teams):
    roles = game_format.get_roles()
    game = []
    for r in range(len(roles)):
        for i in range(roles[r]):
            forbidden = []
            if r < game_format.get_games() and i == 1:
                forbidden = opponents(game[2 * r], games)
            team = pick_team(teams, r, forbidden)
            team.done[r] += 1
            print(team.name)
            game.append(team)
            teams.remove(team)

    return game

def print_teams(teams):
    print([team.name for team in teams])

def opponents(team, games):
    opps = []
    for game in games:
        for i in [0, 1]:
            if game[i] == team:
                opps.append(game[1 - i])
    return opps


def pick_team(teams, role, forbidden):
    less_played = 9999999
    team = None
    print("role", role)

    for t in teams:
        if not t in forbidden and t.done[role] < less_played:
            print(t.name, t.done[role])
            team = t
            less_played = t.done[role]

    return team

def all_teams_done(teams, game_format):
    for t in teams:
        games_done = 0
        for i in range(game_format.get_games()):
            games_done += t.done[i]

        if games_done < len(teams) - 1:
            return False

    return True
