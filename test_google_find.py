from selene.support.shared import browser
from selene import have


def test_google_should_find_selene(open_and_quit_browser):
    browser.element('[name="q"]').type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_google_should_not_find_selene(open_and_quit_browser):
    browser.element('[name="q"]').type('selene').press_enter()
    browser.element('[id="search"]').should(have.no.text('Selene - it is easy!'))

