from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class BasicInstallTest(unittest.TestCase):
    # Пользователь интересуется как делать когортный анализ.
    # Пользователь зашел в Google, ввел запрос "Когортный анализ" и кликнул по одной из ссылок в выдаче.

    # при каждом запуске теста создается новый веб драйвер
    def setUp(self):
        self.browser = webdriver.Chrome()

    # закрывается сессия в тестовом браузере
    def tearDown(self):
        self.browser.quit()

    # запуск тестового браузера по локальному адресу
    def test_home_page_title(self):
        # В браузере пользователя открылся сайт (по адресу 'http://127.0.0.1:8000')
        # В заголовке сайта пользователь прочитал "Блог Вероники Рыжковой"
        self.browser.get('http://127.0.0.1:8000')
        self.assertIn('Блог Вероники Рыжковой', self.browser.title)

    def test_home_page_header(self):
        # В шапке сайта написано "Вероника Рыжкова"
        self.browser.get('http://127.0.0.1:8000')
        header = self.browser.find_elements(By.TAG_NAME, "h1")[0]
        self.assertIn('Вероника Рыжкова', header.text)

    def test_home_page_blog(self):
        # Под шапкой сайта расположен блок со статьями
        self.browser.get('http://127.0.0.1:8000')
        article_list = self.browser.find_element(By.CLASS_NAME, 'article-list')
        self.assertTrue(article_list)

    def test_home_page_articles_look_correct(self):
        # У каждой статьи есть заголовок и абзац с текстом
        self.browser.get('http://127.0.0.1:8000')
        article_title = self.browser.find_element(
            By.CLASS_NAME, 'article-title')
        article_summary = self.browser.find_element(
            By.CLASS_NAME, 'article-summary')
        self.assertTrue(article_title)
        self.assertTrue(article_summary)


if __name__ == '__main__':
    unittest.main()

# Описываем user story как будет тестироваться функционал

# Пользователь кликнул по заголовку и у него открылась страница с полным текстом статьи
# Прочитал статью пользователь кликнул по тексту "Вероника Рыжкова" в шапке сайта и попал обратно на главную страницу
