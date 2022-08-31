import pytest
from selene.support.shared import browser


@pytest.fixture()
def open_and_quit_browser():
    browser.config.window_width = 1265
    browser.config.window_height = 960
    browser.open('https://google.com/ncr')
    yield
    browser.quit()


