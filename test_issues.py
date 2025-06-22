import allure
from allure_commons.types import Severity
from selene import browser, by, have
from models.pages.github_page import GithubPage

def test_issue_with_selene(open_browser):
    browser.element('.header-search-button').click()
    browser.element("#query-builder-test").type("Nirbe3251/qa_guru_hw_10").press_enter()
    browser.element(by.link_text("Nirbe3251/qa_guru_hw_10")).click()
    browser.element('#issues-tab').click()

    browser.element('[data-testid=issue-pr-title-link]').should(have.exact_text("my issue"))

def test_issue_with_allure_steps(open_browser):
    with allure.step("Кликаем на поле поиска"):
        browser.element('.header-search-button').click()

    with allure.step("Вводим текст, нажимаем Enter"):
        browser.element("#query-builder-test").type("Nirbe3251/qa_guru_hw_10").press_enter()

    with allure.step("Ищем элемент по тексту ссылки"):
        browser.element(by.link_text("Nirbe3251/qa_guru_hw_10")).click()

    with allure.step("Переходим в issue"):
        browser.element('#issues-tab').click()

    with allure.step("Ищем текст 'my issue'"):
        browser.element('[data-testid=issue-pr-title-link]').should(have.exact_text("my issue"))

def test_issue_with_decorator():
    github = GithubPage()

    github.open_page('https://github.com')
    github.search_repository('Nirbe3251/qa_guru_hw_10')
    github.go_to_repository('Nirbe3251/qa_guru_hw_10')
    github.go_to_issue_tab()
    github.should_have_issue_name('my issue')

@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'daniil efimow')
@allure.feature('Issues')
@allure.story('Проверка соответствия названия у созданного Issue')
@allure.link('https://github.com', name='My test')
def test_decorator_labels():
    pass

