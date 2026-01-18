from ui.pages.base_page import BasePage


class LoginPage(BasePage):
    # блок логина
    @property
    def login_button(self): return self.page.get_by_role("button", name="Войти")

    @property
    def login_input(self): return self.page.get_by_role("textbox", name="Логин")

    @property
    def password_input(self): return self.page.get_by_role("textbox", name="Пароль")


    def open_login_page(self, base_url:str):
        self.go_to(base_url +"/login")

    # атомарные методы
    def enter_login(self, login: str):
        """Заполняет поле логина"""
        self.login_input.fill(login)

    def enter_password(self, password: str):
        """Заполняет поле пароля"""
        self.password_input.fill(password)

    def submit(self):
        """Нажимает кнопку входа"""
        self.login_button.click()

    def login(self, login:str, password:str):
        """Выполняет вход с заданными логином и паролем"""
        self.enter_login(login)
        self.enter_password(password)
        self.submit()