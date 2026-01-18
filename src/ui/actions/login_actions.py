from ui.pages.login_page import LoginPage


class LoginActions:
    """
    Для работы с логином.
    Содержит последовательность действий над LoginPage.
    """

    def __init__(self, page):
        self.page = page
        self.login_page = LoginPage(page)

    def login_as_user(self, username: str, password: str):
        """
        Выполняет полный вход в систему.
        Можно добавлять любые проверки или дополнительные шаги.
        """
        # 1. Заполняем логин
        self.login_page.enter_login(username)
        # 2. Заполняем пароль
        self.login_page.enter_password(password)
        # 3. Сабмитим форму
        self.login_page.submit()

    def login_with_wrong_password(self, username: str, password: str):
        """
        Специальный сценарий: вход с неверным паролем.
        Можно потом добавить assert на сообщение об ошибке.
        """
        self.login_page.login(username, password)