import unittest
from runner import Runner
from runner_and_tournament import Runner, Tournament
import runner_and_tournament as rt

class RunnerTest(unittest.TestCase):
    is_frozen = False

# Класс RunnerTest — содержит три теста:
    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        runner = Runner("Walker")  # test_walk проверяет, что 10 шагов увеличивают дистанцию до 50
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_run(self):
        runner = Runner("Runner")  # test_run проверяет, что 10 забегов увеличивают дистанцию до 100.
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        runner1 = Runner("Runner1")  # test_challenge проверяет, что дистанции двух бегунов с разными действиями не равны
        runner2 = Runner("Runner2")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runer_1 = rt.Runner('Усейн', 10)
        self.runer_2 = rt.Runner('Андрей', 9)
        self.runer_3 = rt.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for test_key, test_value in cls.all_results.items():
            print(f'Тест: {test_key}')
            for key, value in test_value.items():
                print(f'\t{key}: {value.name}')

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_turn1(self):

        # list_test = [[self.runer_1, self.runer_3], [self.runer_2, self.runer_3],
        #              [self.runer_1, self.runer_2, self.runer_3]]
        turn_1 = rt.Tournament(90, self.runer_1, self.runer_3)
        result = turn_1.start()
        # print(result[list(result.keys())[-1]] == 'Ник')
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Последним должен быть Ник')
        self.all_results['test_turn1'] = result     # test_turn

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_turn2(self):
        turn_2 = rt.Tournament(90, self.runer_2, self.runer_3)
        result = turn_2.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Последним должен быть Ник')
        self.all_results['test_turn2'] = result

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_turn3(self):
        turn_3 = rt.Tournament(90, self.runer_1, self.runer_2, self.runer_3)
        result = turn_3.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Последним должен быть Ник')
        self.all_results['test_turn3'] = result

    if __name__ == '__main__':
        unittest.main()
    # Запускает все тесты
