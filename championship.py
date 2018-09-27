#!/usr/bin/env python3

def createChampionship(game_format, teams):
    games = []
    for i in range(len(teams)):
        for j in range(i + 1, len(teams)):
            games.append([teams[i], teams[j]])
    return games
