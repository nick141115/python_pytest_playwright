import allure
from playwright.sync_api import Page, expect
from pytest_assume.plugin import assume
from typing_extensions import Self

from settings import settings
from src.constants.ui_text_elements import UITextElements
from src.pages.base_page import BasePage


class ComponentPackageInformationPage(BasePage):
    """Описывает страницу информации о пакете компонента."""

    # Селекторы и текстовые константы, необходимые для работы класса ComponentPackageInformationPage.
    _TEXT_NO_LINK_TO_SOURCE_CODE = "Редактирование списка доступно при наличии ссылки на исходный код"
    _CHIPS_INPUT = ".chipsInput.remoteMultiselect"
    """Элемент, который включает в себя input (для ввода названия ЯП) и блоки с названиями ЯП."""
    _DD_PROGRAMMING_LANGUAGE = f"//dt[text()='{UITextElements.TEXT_PROGRAMMING_LANGUAGE}']/following-sibling::dd[1]"
    """Второй столбец в строке 'Язык программирования'."""
    _CONTAINER_DISABLED = ".selectContainer__controlContainer_disabled"
    """Класс, который делает все элементы внутри себя недоступными."""
    _INPUT_NO_LINK_TO_SOURCE_CODE = f"//div[text()='{_TEXT_NO_LINK_TO_SOURCE_CODE}']/following-sibling::input[1]"
    """Input с placeholder'ом 'Редактирование списка доступно при наличии ссылки на исходный код'."""
    _PROGRAMMING_LANGUAGE_INPUT = ".selectContainer__placeholder"
    """Input 'Язык программирования'."""
    _ICON_PLUS_IN_CIRCLE = ".icon-example-app.icon-app-add.icon-component"
    """Иконка в виде плюса в кружочке."""
    _INPUT_URL = "input[name='url']"
    """Input для ввода url'а на внешний исходный код."""
    _ICON_MENU = ".icon-example-app.icon-app-menu.icon-component"
    """Иконка меню."""

    def __init__(self, page: Page) -> None:
        """Инициализация объекта страницы.

        :param page: Объект страницы playwright Page.
        """
        super().__init__(page)

        # Локаторы, необходимые для работы класса ComponentPackageInformationPage.
        self._locator_input_url = self.page.locator(self._INPUT_URL)
        """Локатор input'а для ввода url'а на внешний исходный код."""

    @allure.step("Проверить Input с placeholder'ом 'Редактирование списка доступно при наличии ссылки на исходный код'")
    def check_input_no_link_to_source_code(self) -> Self:
        """Проверить Input с placeholder'ом 'Редактирование списка доступно при наличии ссылки на исходный код'.

        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        locator_input_no_link_to_source_code = (
            self.page.locator(self._DD_PROGRAMMING_LANGUAGE)
            .locator(self._CONTAINER_DISABLED)
            .locator(self._INPUT_NO_LINK_TO_SOURCE_CODE)
        )

        with assume:
            expect(
                locator_input_no_link_to_source_code,
                f"Input с placeholder'ом '{self._TEXT_NO_LINK_TO_SOURCE_CODE}' не отображается или доступен для "
                f"редактирования",
            ).to_be_visible()
        return self

    @allure.step("Проверить текст в блоке справа от текста 'Язык программирования'.")
    def check_text_in_chips_input(self, text_in_chips_input: str) -> Self:
        """Проверить текст в блоке справа от текста 'Язык программирования'.

        :param text_in_chips_input: Текст в блоке справа от текста 'Язык программирования'.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        chips_locator_input = self.page.locator(self._DD_PROGRAMMING_LANGUAGE).locator(self._CHIPS_INPUT)

        with assume:
            expect(
                chips_locator_input,
                f"Текст '{text_in_chips_input}' в блоке справа от текста 'Язык программирования' не отображается",
            ).to_contain_text(text_in_chips_input, timeout=settings.DEFAULT_TIMEOUT)
        return self

    @allure.step("Проверить количество элементов с определённым текстом в атрибуте title.")
    def check_titles_count(self, title_text: str, count: int) -> Self:
        """Проверить количество элементов с определённым текстом в атрибуте title.

        :param title_text: Текст атрибута title.
        :param count: Ожидаемое количество элементов.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        locator_title = (
            self.page.locator(self._DD_PROGRAMMING_LANGUAGE).locator(self._CHIPS_INPUT).get_by_title(title_text)
        )

        with assume:
            expect(
                locator_title,
                f"Элемент с titl'ом '{title_text}' не отображается на странице или количество таких элементов не "
                f"соответствует ожидаемому (ожидаемое количество: {count})",
            ).to_have_count(count, timeout=settings.DEFAULT_TIMEOUT)
        return self

    @allure.step("Ввести текст в блок справа от текста 'Язык программирования'.")
    def fill_in_chips_input(self, text: str) -> Self:
        """Ввести текст в блок справа от текста 'Язык программирования'.

        :param text: Текст, который будет введён в блок справа от текста 'Язык программирования'.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        locator_input = self.page.locator(self._DD_PROGRAMMING_LANGUAGE).locator(self._CHIPS_INPUT).locator("div").first

        with assume:
            expect(locator_input, "Блок справа от текста 'Язык программирования' не отображается").to_be_visible()
            expect(locator_input, "Блок справа от текста 'Язык программирования' недоступен").to_be_enabled()
            locator_input.click()
            locator_input.type(text)
        return self

    @allure.step("Удалить язык программирования из списка.")
    def delete_programming_language(self, name_programming_language: str) -> Self:
        """Удалить язык программирования из списка.

        :param name_programming_language: Название языка программирования.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        locator_name_programming_language = (
            self.page.locator(self._SPAN)
            .filter(has_text=name_programming_language)
            .locator("xpath=./following-sibling::button[1]")
        )

        with assume:
            expect(
                locator_name_programming_language,
                f"Кнопка удаления языка программирования '{name_programming_language}' не отображается",
            ).to_be_visible(timeout=settings.DEFAULT_TIMEOUT)
            expect(
                locator_name_programming_language,
                f"Кнопка удаления языка программирования '{name_programming_language}' недоступна",
            ).to_be_enabled()
            locator_name_programming_language.click()

            expect(
                locator_name_programming_language,
                f"Кнопка удаления языка программирования '{name_programming_language}' не должна отображаться",
            ).not_to_be_visible(timeout=settings.DEFAULT_TIMEOUT)
        return self

    @allure.step("Кликнуть на иконку в виде плюса в кружочке.")
    def click_on_icon_plus_in_circle(self, nth: int = 0) -> Self:
        """Кликнуть на иконку в виде плюса в кружочке.

        :param nth: Порядковый номер иконки.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        locator_plus_icon_in_circle = self.page.locator(self._ICON_PLUS_IN_CIRCLE).nth(nth)

        with assume:
            expect(
                locator_plus_icon_in_circle,
                f"Иконка в виде плюса в кружочке с порядковым номером '{nth}' не отображается",
            ).to_be_visible(timeout=settings.DEFAULT_TIMEOUT)
            expect(
                locator_plus_icon_in_circle,
                f"Иконка в виде плюса в кружочке с порядковым номером '{nth}' недоступна",
            ).to_be_enabled()
            locator_plus_icon_in_circle.click()
        return self

    @allure.step("Ввести текст в input для ввода url'а на внешний/внутренний исходный код.")
    def fill_in_input_url(self, text: str) -> Self:
        """Ввести текст в input для ввода url'а на внешний/внутренний исходный код.

        :param text: Текст, который будет введён в input для ввода url'а на внешний/внутренний исходный код.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            expect(
                self._locator_input_url, "Input для ввода url'а на внешний/внутренний исходный код не отображается"
            ).to_be_visible(timeout=settings.DEFAULT_TIMEOUT)
            expect(
                self._locator_input_url, "Input для ввода url'а на внешний/внутренний исходный код недоступен"
            ).to_be_enabled()
            self._locator_input_url.fill(text)
        return self

    @allure.step("Кликнуть на иконку меню.")
    def click_on_icon_menu(self, nth: int = 0) -> Self:
        """Кликнуть на иконку меню.

        :param nth: Порядковый номер иконки.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        locator_icon_menu = self.page.locator(self._ICON_MENU).nth(nth)

        with assume:
            expect(
                locator_icon_menu,
                f"Иконка меню с порядковым номером '{nth}' не отображается",
            ).to_be_visible(timeout=settings.DEFAULT_TIMEOUT)
            expect(
                locator_icon_menu,
                f"Иконка меню с порядковым номером '{nth}' недоступна",
            ).to_be_enabled()
            locator_icon_menu.click()
        return self

    @allure.step("Проверить кнопку 'Отмена'.")
    def check_button_cancel(self) -> Self:
        """Проверить кнопку 'Отмена'.

        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            expect(
                self.page.get_by_title(UITextElements.CANCEL),
                "Кнопка 'Отмена' не отображается",
            ).to_be_visible(timeout=settings.DEFAULT_TIMEOUT)
        return self

    @allure.step("Проверить текст в input'е для ввода url'а на внешний/внутренний исходный код.")
    def check_text_in_input_url(self, text: str) -> Self:
        """Проверить текст в input'е для ввода url'а на внешний/внутренний исходный код.

        :param text: Текст, который должен присутствовать в input'е для ввода url'а на внешний/внутренний исходный код.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            expect(
                self._locator_input_url,
                f"Input для ввода url'а на внешний/внутренний исходный код не содержит ожидаемый текст '{text}'",
            ).to_have_value(text)
        return self
