import allure
from selene import browser, by, have


class GithubPage:
    @allure.step('Открыть страницу https://github.com')
    def open_page(self, link):
        browser.open(link)

    @allure.step('Ввести имя репозитория {repo} в поле')
    def search_repository(self, repo):
        browser.element('.header-search-button').click()
        browser.element('#query-builder-test').type(repo).submit()
        browser.element(by.link_text(repo)).click()

    @allure.step('Перейти в найденный репозиторий {repo}')
    def go_to_repository(self, repo):
        browser.element(by.link_text(repo)).click()

    @allure.step('Перейти во вкладку Issues')
    def go_to_issue_tab(self):
        browser.element('#issues-tab').click()

    @allure.step('Проверить название issue {issue_name}')
    def should_have_issue_name(self, name_issue):
        browser.element('[data-testid=issue-pr-title-link]').should(have.exact_text(name_issue))