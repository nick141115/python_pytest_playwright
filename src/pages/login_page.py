import allure
from playwright.sync_api import Page, expect
from pytest_assume.plugin import assume
from typing_extensions import Self

from settings import settings
from src.pages.base_page import BasePage


class LoginPage(BasePage):
    """Описывает страницу входа в систему."""

    # Селекторы и текстовые константы, необходимые для работы класса LoginPage.
    _USERNAME_INPUT = "input[name='Username']"
    """Поле ввода логина пользователя."""
    _PASSWORD_INPUT = "input[name='Password']"
    """Поле ввода пароля пользователя."""
    _SIGN_IN_BUTTON = "button[value='login']"
    """Кнопка 'Ок'."""

    def __init__(self, page: Page) -> None:
        """Инициализация объекта страницы.

        :param page: Объект страницы playwright Page.
        """
        super().__init__(page)

        # Локаторы, необходимые для работы класса LoginPage.
        self._locator_username_input = self.page.locator(self._USERNAME_INPUT)
        """Локатор поля ввода логина пользователя."""

    @allure.step("Перейти на страницу авторизации.")
    def go_to_login_page(self) -> Self:
        """Перейти на страницу авторизации.

        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        self.page.goto(settings.URL)
        return self

    @allure.step("Залогиниться под пользователем, который прописан в файле 'settings.py'.")
    def login_as_settings_user(self) -> Self:
        """Залогиниться под пользователем, который прописан в settings.py.

        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        locator_password_input = self.page.locator(self._PASSWORD_INPUT)
        locator_sign_in_button = self.page.locator(self._SIGN_IN_BUTTON)

        with assume:
            expect(self._locator_username_input, "Поле ввода логина пользователя недоступно").to_be_enabled()
            self._locator_username_input.fill(settings.LOGIN)

            expect(locator_password_input, "Поле ввода пароля пользователя не отображается").to_be_visible()
            expect(locator_password_input, "Поле ввода пароля пользователя недоступно").to_be_enabled()
            locator_password_input.fill(settings.PASSWORD)

            expect(locator_sign_in_button, "Кнопка 'Ок' не отображается").to_be_visible()
            expect(locator_sign_in_button, "Кнопка 'Ок' недоступна").to_be_enabled()
            locator_sign_in_button.click()
        return self

    @allure.step("Проверить видимость поля ввода логина пользователя.")
    def check_username_input(self) -> Self:
        """Проверить видимость поля ввода логина пользователя.

        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            expect(self._locator_username_input, "Поле ввода логина пользователя не отображается").to_be_visible(
                timeout=settings.DEFAULT_TIMEOUT
            )
        return self
