from playwright.sync_api import Page

class BasePage:
    """
    Базовый класс для всех страниц.
    Содержит общие действия, которые могут понадобиться на любой странице.
    """

    def __init__(self, page: Page):
        self.page = page

    # Навигация по URL
    def go_to(self, url: str):
        """Переход на указанный URL"""
        self.page.goto(url, wait_until='networkidle')

    # Пример получения заголовка страницы
    def get_title(self) -> str:
        """Возвращает заголовок текущей страницы"""
        return self.page.title()

    # # Пример метода ожидания элемента
    # def wait_for_element(self, locator: Locator, timeout: int = 5000):
    #     """Ожидает появления элемента на странице"""
    #     locator.wait_for(timeout=timeout)