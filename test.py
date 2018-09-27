#!/usr/bin/env python3

import unittests
from unittests import assert_equals, assert_contains, assert_similars
from championship import createChampionship

class SimpleGame:
    def getRoles():
        return [2]

class Tester(unittests.Tester):
    def testNoTeams(self):
        assert_equals([], createChampionship(SimpleGame(), []))

    def testTwoTeams(self):
        assert_contains("blue", createChampionship(SimpleGame(), ["blue", "red"])[0])

    def testThreeTeams(self):
        assert_similars([["a", "b"], ["a", "c"], ["b", "c"]], createChampionship(SimpleGame(), ["a", "b", "c"]))


Tester().runTests()

