from datetime import datetime
import pytest
import logging
import os

# Фикстура для настройки логирования (один раз на сессию)
@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    # Создаем папку для логов, если она не существует
    logs_directory = "logs"
    if not os.path.exists(logs_directory):
        os.makedirs(logs_directory)
        print(f"Создана директория для логов: {logs_directory}")
    else:
        print(f"Директория для логов уже существует: {logs_directory}")

    # Название лог-файла с текущей датой и временем
    log_filename = f"{logs_directory}/test_log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

    # Настройка логирования
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Создание обработчика для записи в файл
    file_handler = logging.FileHandler(log_filename)
    file_handler.setLevel(logging.INFO)

    # Формат логов
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    file_handler.setFormatter(formatter)

    # Добавляем обработчик к логгеру
    logger.addHandler(file_handler)

    logging.info("Тестирование начато")
    yield
    logging.info("Тестирование завершено")


# Декоратор для логирования тестов
def log_test_step(func):
    def wrapper(driver, test_data, *args, **kwargs):
        test_name = test_data.get("name", "unknown test")
        logging.info(f"Start test: {test_name}")
        try:
            result = func(driver, test_data, *args, **kwargs)
            logging.info(f"Test {test_name} if finished successfully")
            return result
        except Exception as e:
            logging.error(f"Error in the test {test_name}: {str(e)}", exc_info=True)
            raise e

    return wrapper