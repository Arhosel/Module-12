import runner_and_tournament as rt
import unittest


class TournamentTest(unittest.TestCase):

#тестовый класс "TournamentTest`, который наследуется от "unittest".TestCase`. Этот класс содержит модульные тесты для моделирования турнира
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
#Это метод класса, который запускается один раз перед выполнением всех тестов.
#Он инициализирует переменную класса `all_results` как пустой словарь для хранения результатов всех тестов
    def setUp(self):
        self.runer_1 = rt.Runner('Усейн', 10)
        self.runer_2 = rt.Runner('Андрей', 9)
        self.runer_3 = rt.Runner('Ник', 3)
#Этот метод запускается перед каждым тестом.
#Он создает три объекта "Runner" с разными именами и скоростями
    @classmethod
    def tearDownClass(cls):
        for test_key, test_value in cls.all_results.items():
            print(f'Тест: {test_key}')
            for key, value in test_value.items():
                print(f'\t{key}: {value.name}')
#Этот метод класса запускается один раз после завершения всех тестов.
#Он выводит результаты, сохраненные в "all_results", с указанием имени каждого участника и его позиции для каждого теста.
    def test_turn1(self):

        # list_test = [[self.runer_1, self.runer_3], [self.runer_2, self.runer_3],
        #              [self.runer_1, self.runer_2, self.runer_3]]
        turn_1 = rt.Tournament(90, self.runer_1, self.runer_3)
        result = turn_1.start()
        # print(result[list(result.keys())[-1]] == 'Ник')
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Последним должен быть Ник')
        self.all_results['test_turn1'] = result     # test_turn

    def test_turn2(self):
        turn_2 = rt.Tournament(90, self.runer_2, self.runer_3)
        result = turn_2.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Последним должен быть Ник')
        self.all_results['test_turn2'] = result

    def test_turn3(self):
        turn_3 = rt.Tournament(90, self.runer_1, self.runer_2, self.runer_3)
        result = turn_3.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Последним должен быть Ник')
        self.all_results['test_turn3'] = result
#Каждый метод создает объект `Турнир` с дистанцией в 90 единиц и различными комбинациями участников.
#Вызывается метод `start()` турнира, и результат сохраняется.
#Утверждение проверяет, является ли 'Nik' (ник) последним участником в каждом турнире.
#Результаты сохраняются в словаре `all_results`.

    # def test_turn4(self):
    #     #тестирует более короткую гонку (6 этапов) со всеми тремя бегунами
    #     turn_4 = rt.Tournament(6, self.runer_1, self.runer_2, self.runer_3)
    #     result = turn_4.start()
    #     self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Последним должен быть Ник')
    #     self.all_results['test_turn4'] = result

    if __name__ == '__main__':
        unittest.main()
    # Запускает все тесты
