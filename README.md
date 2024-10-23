# Проект автоматизации тестирования с использованием Selenium

В этом проекте представлены автоматизированные тесты с использованием Selenium для примера сайта [python.org](https://www.python.org/). Тесты демонстрируют различные возможности, включая логирование, работу с фиктурами и использование тестовых данных.

## Структура проекта

Проект организован в две основные директории:

1. **simple_test**
   - Содержит простой тестовый скрипт, который соответствует базовым требованиям ТЗ.
   - Здесь Sanity-Тест функциональности поиска.

2. **test_pro**
 - Содержит несколько файлов, демонстрирующих продвинутые навыки тестирования:
     - `test.py`: Сложный тест, включающий логирование, фикстуры и тестовые данные.
     - `logger.py`: Модуль для настройки логирования.
     - `test_data.json`: Файл с тестовыми данными для параметризованного тестирования.
     - `requirement.txt`: Файл с зависимостями проекта.
     - `logs/`: Папка для хранения логов.
       - `example_log.log`: Пример файла с логами, содержащий информацию о выполнении тестов.
     - `report.html`: HTML-отчет, созданный по результатам тестирования.
   - Содержит более сложный тестовый скрипт, который демонстрирует продвинутые навыки тестирования.
   - Этот скрипт включает в себя:
     - Возможности логирования для отслеживания выполнения тестов и захвата ошибок.
     - Использование фиктур для настройки и завершения тестовой среды.
     - Интеграцию тестовых данных для параметризованного тестирования.
     - Генерацию HTML-отчетов для лучшей визуализации результатов тестирования.

## Требования
- git
- Python 3.x
- Selenium
- pytest
- pytest-html 
- logging 

## Установка

1. Клонируйте репозиторий на ваш локальный компьютер или скачайте архив и распокуйте его.
   ```bash
git clone https://github.com/makarova1507ana/test_searchInput_python.org.git
```
2. Проверьте, что вы находитесь в папке с проектом.
3. Установите необходимые пакеты с помощью pip:
   ```bash
   pip install -r requirements.txt

## Запуск
Для простого теста
   ```bash
pytest simple_test/test.py 
```
Для продвинутого теста с логированием и отчетами
   ```bash
pytest test_pro/test.py
```
 Для продвинутого теста команда для запустка тестов и генерации HTML-отчет
   ```bash
pytest test_pro/test.py --html=report.html --self-contained-html 
  ```
