from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
from logger import *
# URL сайта для тестирования
url = "https://www.python.org"


# Загрузка тестовых данных из JSON-файла
def load_test_data():
    with open('test_data.json', 'r') as file:
        return json.load(file)["tests"]


# Фикстура для настройки драйвера Selenium
@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")  # Включаем headless режим
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Инициализация драйвера
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    yield driver
    driver.quit()


# Тест для проверки поиска
@pytest.mark.parametrize("test_data", load_test_data(), ids=lambda test_data: test_data["name"])
@log_test_step  # Применяем декоратор для логирования
def test_search(driver, test_data):
    # Ожидание поля ввода для поиска
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )

    # Выполнение поиска
    search_box.send_keys(test_data["input"])
    search_box.send_keys(Keys.RETURN)

    # Проверяем, что произошел переход на страницу поиска
    search_page_title = driver.find_element(By.CSS_SELECTOR, "#content > div > section > h2").text
    assert "Search Python.org" in search_page_title, "Переход на страницу поиска не произошел"

    # Проверяем, содержит ли результат искомое значение
    results = driver.find_elements(By.CSS_SELECTOR, ".list-recent-events")

    if test_data["contains"]:
        assert any(test_data["expected"] in result.text for result in results), \
            f"Результаты не содержат ключевое слово '{test_data['expected']}'"
    else:
        # Проверяем, что отображается сообщение "No results found."
        no_results_message = driver.find_elements(By.XPATH, "//*[contains(text(), 'No results found')]")
        assert len(no_results_message) >= 0, "Сообщение 'No results found' не отображается"
