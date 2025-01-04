import unittest
import logging

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,  # Уровень логирования - INFO
    filename='runner_tests.log',  # Имя файла для логов
    filemode='w',  # Перезапись файла при каждом запуске
    encoding='utf-8',  # Кодировка файла
    format='%(asctime)s - %(levelname)s - %(message)s'  # Формат записи логов
)

# Заглушка для класса Runner
class Runner:
    # Инициализация объекта Runner с именем и скоростью
    def __init__(self, name, speed=5):
        # Проверка типа имени
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        # Проверка, что скорость неотрицательная
        if speed < 0:
            raise ValueError("Speed must be non-negative")
        self.name = name
        self.speed = speed
        self.distance = 0  # Начальная дистанция

    # Метод для передвижения шагом
    def walk(self):
        self.distance += 5

    # Метод для передвижения бегом
    def run(self):
        self.distance += 10

# Тесты для класса Runner
class RunnerTest(unittest.TestCase):

    # Тест метода walk
    def test_walk(self):
        try:
            logging.info('Запуск теста "test_walk"')  # Лог начала теста
            # Создание объекта Runner с некорректной скоростью
            runner = Runner("Walker", -1)  # Передаём отрицательное значение скорости
            # Пробежка в цикле
            for _ in range(10):
                runner.walk()
            # Проверка, что пройденное расстояние верное
            self.assertEqual(runner.distance, 50)
            logging.info('"test_walk" выполнен успешно')  # Лог успешного выполнения
        except ValueError as e:
            # Лог ошибки в случае некорректного значения скорости
            logging.warning(f"Неверная скорость для Runner: {e}")

    # Тест метода run
    def test_run(self):
        try:
            logging.info('Запуск теста "test_run"')  # Лог начала теста
            # Создание объекта Runner с некорректным именем
            runner = Runner(123)  # Передаём не строку в качестве имени
            # Пробежка в цикле
            for _ in range(10):
                runner.run()
            # Проверка, что пройденное расстояние верное
            self.assertEqual(runner.distance, 100)
            logging.info('"test_run" выполнен успешно')  # Лог успешного выполнения
        except TypeError as e:
            # Лог ошибки в случае некорректного типа имени
            logging.warning(f"Неверный тип данных для объекта Runner: {e}")

    # Тест на сравнение результатов двух бегунов
    def test_challenge(self):
        logging.info('Запуск теста "test_challenge"')  # Лог начала теста
        # Создание двух объектов Runner
        runner1 = Runner("Runner1")
        runner2 = Runner("Runner2")
        # Один бежит, другой идет в цикле
        for _ in range(10):
            runner1.run()
            runner2.walk()
        # Проверка, что результаты не равны
        self.assertNotEqual(runner1.distance, runner2.distance)
        logging.info('"test_challenge" выполнен успешно')  # Лог успешного выполнения
