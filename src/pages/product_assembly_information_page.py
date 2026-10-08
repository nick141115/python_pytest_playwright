import allure
from playwright.sync_api import Page, expect
from pytest_assume.plugin import assume
from typing_extensions import Self

from settings import settings
from src.constants.css_keys_and_values import CssKeysAndValues
from src.constants.ui_text_elements import UITextElements
from src.pages.base_page import BasePage


class ProductAssemblyInformationPage(BasePage):
    """Описывает страницу информации о сборке продукта."""

    # Селекторы и текстовые константы, необходимые для работы класса ProductAssemblyInformationPage.
    _VERIFIED_ICON = ".verifiedIcon"
    """Иконка в виде галочки."""
    _VERIFIED_VERSION = f"//span[text()='{UITextElements.VERIFIED_VERSION}']"
    """Подсказка 'Верифицированная версия', отображающаяся при наведении курсора."""
    _LINK_ICON = "[aria-label='В пакет добавлены все ссылки']"
    """Иконка ссылок."""
    _CHECKBOX_DEVIATION_IS_AGREED = f"div:nth-child(2) > .selectContainer__menu div:nth-child(1) {BasePage._PATH}"
    """Checkbox 'Отклонение согласовано'."""

    def __init__(self, page: Page) -> None:
        """Инициализация объекта страницы.

        :param page: Объект страницы playwright Page.
        """
        super().__init__(page)

        # Локаторы, необходимые для работы класса ProductAssemblyInformationPage.
        self._locator_link_icon = self.page.locator(self._LINK_ICON).first
        """Локатор иконки ссылок."""

    @allure.step("Навести курсор на галочку.")
    def hover_cursor_over_check_mark(self, nth: int = 0, visible: bool = True) -> Self:
        """Навести курсор на галочку.

        :param nth: Порядковый номер элемента.
        :param visible: Элемент должен быть видимым или нет (если 'False', то элемент должен отсутствовать на странице).
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        self.page.wait_for_timeout(5_000)

        locator_verified_icon = self.page.locator(self._VERIFIED_ICON).nth(nth)

        with assume:
            if visible:
                expect(locator_verified_icon, "Иконка в виде галочки не отображается").to_be_visible()
                locator_verified_icon.hover()
                expect(
                    locator_verified_icon.locator(self._VERIFIED_VERSION),
                    "Подсказка 'Верифицированная версия', отображающаяся при наведении курсора, не отображается",
                ).to_be_visible()
            else:
                expect(locator_verified_icon, "Иконка в виде галочки не должна отображаться").not_to_be_visible(
                    timeout=settings.DEFAULT_TIMEOUT
                )
        return self

    @allure.step("Проверить видимость первой иконки ссылок.")
    def check_visibility_first_link_icon(self, visible: bool = True) -> Self:
        """Проверить видимость первой иконки ссылок.

        :param visible: Элемент должен быть видимым или нет (если 'False', то элемент должен отсутствовать на странице).
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        self.page.wait_for_timeout(1_500)

        with assume:
            if visible:
                expect(self._locator_link_icon, "Иконка ссылок не отображается").to_be_visible()
            else:
                expect(self._locator_link_icon, "Иконка ссылок не должна отображаться").not_to_be_visible()
        return self

    @allure.step("Навести курсор на первую иконку ссылок.")
    def hover_cursor_over_first_link_icon(self) -> Self:
        """Навести курсор на первую иконку ссылок.

        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            self.check_visibility_first_link_icon()
            self._locator_link_icon.hover()
        return self

    @allure.step("Проверить checkbox 'Отклонение согласовано'.")
    def check_checkbox_deviation_is_agreed(self) -> Self:
        """Проверить checkbox 'Отклонение согласовано'.

        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            expect(
                self.page.locator(self._CHECKBOX_DEVIATION_IS_AGREED), "Checkbox 'Отклонение согласовано' не отмечен"
            ).to_have_css(CssKeysAndValues.DISPLAY, CssKeysAndValues.INLINE)
        return self

    @allure.step("Проверить сортировку в паспорте сборки продукта.")
    def check_sorting_in_assembly_passport(self, list_components: list[str]) -> Self:
        """Проверить сортировку в паспорте сборки продукта.

        :param list_components: Эталонный список компонентов.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            # Перебирает каждый второй элемент списка, начиная с самого первого (с индекса 0)
            for i, product in list(enumerate(list_components))[::2]:
                expect(
                    # Проверяет ссылки на компоненты в таблице в паспорте сборки продукта
                    self._locator_link.nth((i * 2) + 9),
                    "Неверная сортировка в паспорте сборки продукта",
                ).to_have_text(product, timeout=settings.DEFAULT_TIMEOUT)
        return self
