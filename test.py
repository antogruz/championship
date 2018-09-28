#!/usr/bin/env python3

import unittests
from unittests import assert_equals, assert_contains, assert_similars
from championship import createChampionship

def main():
    #Tester().runTests()

    team_names = ["Jaune", "Blanc", "Bleu", "Vert", "Noir", "Orange", "Rouge"]
    print("Real")
    championship = createChampionship(FranckGame(), team_names)

    for name in team_names:
        print(name, count_roles(FranckGame(), championship, name), count_different_opponents(championship, name))

    print_championship(championship)


def print_championship(c):
    print(c)

class SimpleGame:
    def get_roles(self):
        return [2]

    def get_games(self):
        return 1

class RefGame:
    def get_roles(self):
        return [2, 1]

    def get_games(self):
        return 1

class FranckGame:
    def get_roles(self):
        return [2, 2, 1, 2]

    def get_games(self):
        return 2

class Tester(unittests.Tester):
    def testNoTeams(self):
        assert_equals([], createChampionship(SimpleGame(), []))

    def testTwoTeams(self):
        assert_contains("blue", createChampionship(SimpleGame(), ["blue", "red"])[0])

    def testThreeTeams(self):
        assert_similars([["a", "b"], ["c", "a"], ["b", "c"]], createChampionship(SimpleGame(), ["a", "b", "c"]))

    def testEightTeams(self):
        assert_equals(28, len(createChampionship(SimpleGame(), ["a"] * 8)))

    def testReferees(self):
        assert_similars([["a", "b", "c"], ["c", "a", "b"], ["b", "c", "a"]], createChampionship(RefGame(), ["a", "b", "c"]))

    def testThatAllGamesDone(self):
        championship = createChampionship(FranckGame(), ["a", "b", "c", "d", "e", "f", "g", "h"])
        assert_equals(7, count_different_opponents(championship, "a"))


def count_roles(game_format, championship, team_name):
    sizes = game_format.get_roles()
    counts = []
    index = 0
    for role in range(len(sizes)):
        count = 0
        for i in range(sizes[role]):
            for game in championship:
                if team_name == game[index]:
                    count += 1
            index += 1
        counts.append(count)

    return counts

def count_different_opponents(championship, team_name):
    opponents = []
    for game in championship:
        for i in [0, 1, 2, 3]:
            if game[i] == team_name:
                if i <= 1:
                    opp = game[1 - i]
                if i == 2:
                    opp = game[3]
                if i == 3:
                    opp = game[2]
                if not opp in opponents:
                    opponents.append(opp)

    return len(opponents)


main()
