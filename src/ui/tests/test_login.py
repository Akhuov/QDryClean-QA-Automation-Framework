from playwright.sync_api import expect, Page
from ui.actions.login_actions import LoginActions
from ui.pages.login_page import LoginPage


def test_success_login(page:Page, settings):

    login_page = LoginPage(page)
    login_page.go_to(settings.front_end_url)
    actions = LoginActions(page)
    actions.login_as_user(settings.test_login, settings.test_password)

    expect(login_page.page).to_have_url(settings.front_end_url+"/users")
    expect(login_page.page.get_by_role('heading', name='Users')).to_be_visible()

def test_login_with_wrong_password(page:Page, settings):

    login_page = LoginPage(page)
    login_page.go_to(settings.front_end_url)
    actions = LoginActions(page)
    actions.login_with_wrong_password(settings.test_login, "wrong_password")

    error_alert = page.get_by_text(text="Неверный логин или пароль")
    error_alert.wait_for()
    expect(error_alert).to_be_visible()