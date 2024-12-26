import unittest
from runner import Runner

# class Runner:
#     def __init__(self, name):                                            #Класс Runner — представляет участника с именем и дистанцией
#         self.name = name
#         self.distance = 0
#
#     def walk(self):
#         self.distance += 5
#                                                                          #Методы walk и run — увеличивают дистанцию на 5 и 10 соответственно.
#     def run(self):
#         self.distance += 10

class RunnerTest(unittest.TestCase):
                                                                           #Класс RunnerTest — содержит три теста:
    def test_walk(self):
        runner = Runner("Walker")                                          #test_walk проверяет, что 10 шагов увеличивают дистанцию до 50
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = Runner("Runner")                                          #test_run проверяет, что 10 забегов увеличивают дистанцию до 100.
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner1 = Runner("Runner1")                                        #test_challenge проверяет, что дистанции двух бегунов с разными действиями не равны
        runner2 = Runner("Runner2")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)

if __name__ == '__main__':
    unittest.main()