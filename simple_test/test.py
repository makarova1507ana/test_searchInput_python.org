from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

# URL сайта для тестирования
url = "https://www.python.org"


@pytest.fixture
def driver():

    driver = webdriver.Chrome()
    driver.get(url)

    yield driver
    driver.quit()


# Тест для проверки работы поиска
def test_search(driver):
    # Ожидание загрузки элемента поиска
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )

    # Ввод ключевого слова и отправка запроса
    search_box.send_keys("Python")
    search_box.send_keys(Keys.RETURN)

    # Ожидание загрузки результатов поиска
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#content > div > section > h2"))
    )

    # Проверка, что заголовок страницы поиска содержит "Search Python.org"
    search_page_title = driver.find_element(By.CSS_SELECTOR, "#content > div > section > h2").text
    assert "Search Python.org" in search_page_title, "Search page did not load correctly."

    # Ожидание загрузки результатов поиска
    search_results = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".list-recent-events li"))
    )

    # Проверка, что результаты поиска присутствуют
    assert len(search_results) > 0, "No search results found."

    # Проверка, что хотя бы один результат содержит слово "Python"
    assert any("Python" in result.text for result in search_results), "No search results contain the word 'Python'."
