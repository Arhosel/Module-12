import unittest

import Tournament

from runner_and_tournament import Runner

# class Runner:
#     def __init__(self, name, speed):
#         self.name = name
#         self.speed = speed
#
# class Tournament:
#     def __init__(self, distance, *runners):
#         self.distance = distance
#         self.runners = runners
#
#     def start(self):
#         results = {}
#         for runner in self.runners:
#             time = self.distance / runner.speed
#             results[time] = runner.name
#         return dict(sorted(results.items()))

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nick = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for time, name in cls.all_results.items():
            print(f"{time}: {name}")

    def test_usain_and_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        results = tournament.start()
        TournamentTest.all_results.update(results)
        self.assertTrue(list(results.values())[-1] == "Ник")

    def test_andrey_and_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        results = tournament.start()
        TournamentTest.all_results.update(results)
        self.assertTrue(list(results.values())[-1] == "Ник")

    def test_usain_andrey_and_nick(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        results = tournament.start()
        TournamentTest.all_results.update(results)
        self.assertTrue(list(results.values())[-1] == "Ник")

if __name__ == '__main__':
    unittest.main()