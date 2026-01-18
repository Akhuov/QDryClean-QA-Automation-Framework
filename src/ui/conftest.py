import os
import pytest
from playwright.sync_api import Browser
from ui.actions.login_actions import LoginActions


@pytest.fixture
def logged_page(browser: Browser, settings):
    base_url = settings.front_end_url
    storage_path = settings.storage_state_path

    # создаём storage файл, если не существует
    if not os.path.exists(storage_path):
        os.makedirs(os.path.dirname(storage_path), exist_ok=True)
        with open(storage_path, "w") as f:
            f.write("{}")

    context = browser.new_context(storage_state=storage_path)
    page = context.new_page()

    page.goto(base_url, timeout=60_000)

    # если уже залогинены
    if page.url.endswith("/users"):
        return page

    # page.set_viewport_size({"width": 1920, "height": 1080})
    # page.set_default_timeout(60_000)
    # page.set_default_navigation_timeout(60_000)

    # иначе логиним через Action
    login_actions = LoginActions(page)
    login_actions.login_as_user(settings.test_login, settings.test_password)

    # сохраняем storage state
    context.storage_state(path=storage_path)

    return page