import allure
from playwright.sync_api import Page, expect
from pytest_assume.plugin import assume
from typing_extensions import Self

from settings import settings
from src.constants.roles import Roles
from src.pages.base_page import BasePage


class ImpersonationPage(BasePage):
    """Описывает страницу имперсонации."""

    # Селекторы и текстовые константы, необходимые для работы класса ImpersonationPage.
    _ACCOUNT_FOR_IMPERSONATION_INPUT = ".form-control.ui-autocomplete-input"
    """Input 'Учетная запись для имперсонализации'."""
    _OK_BUTTON = "ОК"
    """Кнопка 'ОК'."""
    _SEARCH_RESULTS = ".ui-menu-item-wrapper"
    """Выпадающая строка с нужным сотрудником под имперсонацию."""

    def __init__(self, page: Page) -> None:
        """Инициализация объекта страницы.

        :param page: Объект страницы playwright Page.
        """
        super().__init__(page)

    @allure.step("Имперсонироваться за другого пользователя.")
    def impersonate_as_another_user(self, full_name: str) -> Self:
        """Имперсонироваться за другого пользователя.

        :param full_name: Полные ФИО сотрудника.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        locator_account_for_impersonation_input = self.page.locator(self._ACCOUNT_FOR_IMPERSONATION_INPUT)
        locator_search_results = self.page.locator(self._SEARCH_RESULTS)
        locator_ok_button = self.page.get_by_role(Roles.BUTTON, name=self._OK_BUTTON)

        with assume:
            expect(
                locator_account_for_impersonation_input, "Input 'Учетная запись для имперсонализации' не отображается"
            ).to_be_visible()
            expect(
                locator_account_for_impersonation_input, "Input 'Учетная запись для имперсонализации' недоступен"
            ).to_be_enabled()
            locator_account_for_impersonation_input.fill(full_name)

            expect(locator_search_results, "Выпадающий блок с ФИО не отображается").to_be_visible(
                timeout=settings.DEFAULT_TIMEOUT
            )
            expect(locator_search_results, "Выпадающий блок с ФИО недоступен").to_be_enabled()
            locator_search_results.click()

            expect(locator_ok_button, "Кнопка 'ОК' не отображается").to_be_visible()
            expect(
                locator_ok_button,
                "Кнопка 'ОК' недоступна",
            ).to_be_enabled()
            locator_ok_button.click()
        return self
