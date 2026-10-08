import allure
from playwright.sync_api import Page, expect
from pytest_assume.plugin import assume
from typing_extensions import Self

from settings import settings
from src.constants.css_keys_and_values import CssKeysAndValues
from src.pages.base_page import BasePage


class ProductPage(BasePage):
    """Описывает страницу 'Продукты'."""

    # Селекторы и текстовые константы, необходимые для работы класса ProductPage.
    _CHECKBOX_NOT_SPECIFIED = f"div:nth-child(6) .selectContainer__menu__option.includeUnsetOption {BasePage._PATH}"
    """Checkbox 'Не указан'"""
    _CHECKBOX_RESPONSIBLE_FOR_IMPLEMENTATION = f"div:nth-child(5) .selectContainer__menu div {BasePage._PATH}"
    """Checkbox с именем ответственного за реализацию"""
    _TEXT_WITH_ELLIPSES = ".valueContainer__value"
    """Класс, который сокращает текст троеточием"""

    def __init__(self, page: Page) -> None:
        """Инициализация объекта страницы.

        :param page: Объект страницы playwright Page.
        """
        super().__init__(page)

    @allure.step("Проверить текст сокращённый троеточием.")
    def check_text_with_ellipses(self, text: str) -> Self:
        """Проверить текст сокращённый троеточием.

        :param text: Текст, который должен быть сокращён троеточием.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            expect(
                self.page.locator(self._TEXT_WITH_ELLIPSES).get_by_text(text),
                f"Текст ('{text}') не найден или не сокращён троеточием",
            ).to_be_visible()
        return self

    @allure.step("Проверить checkbox с именем ответственного за реализацию.")
    def check_checkbox_responsible_for_implementation(self) -> Self:
        """Проверить checkbox с именем ответственного за реализацию.

        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            expect(
                self.page.locator(self._CHECKBOX_RESPONSIBLE_FOR_IMPLEMENTATION),
                "Checkbox с именем ответственного за реализацию не отмечен",
            ).to_have_css(CssKeysAndValues.DISPLAY, CssKeysAndValues.INLINE)
        return self

    @allure.step("Проверить checkbox 'Не указан'.")
    def check_checkbox_not_specified(self) -> Self:
        """Проверить checkbox 'Не указан'.

        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            expect(self.page.locator(self._CHECKBOX_NOT_SPECIFIED), "Checkbox 'Не указан' не отмечен").to_have_css(
                CssKeysAndValues.DISPLAY, CssKeysAndValues.INLINE
            )
        return self

    @allure.step("Проверить сортировку на вкладке 'Все продукты'.")
    def check_sorting_on_all_products_tab(self, list_products: list[str]) -> Self:
        """Проверить сортировку на вкладке 'Все продукты'.

        :param list_products: Эталонный список продуктов.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            # Переменная i на первой итерации будет равна 6
            for i, product in enumerate(list_products, start=6):
                expect(self._locator_link.nth(i), "Неверная сортировка на вкладке 'Все продукты'").to_have_text(
                    product, timeout=settings.DEFAULT_TIMEOUT
                )
        return self

    @allure.step("Проверить сортировку на вкладке 'Избранное'.")
    def check_sorting_on_favorites_tab(self, list_favorites: list[str]) -> Self:
        """Проверить сортировку на вкладке 'Избранное'.

        :param list_favorites: Эталонный список избранного.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            # Переменная i на первой итерации будет равна 6
            for i, product in enumerate(list_favorites, start=6):
                expect(self._locator_link.nth(i), "Неверная сортировка на вкладке 'Избранное'").to_have_text(
                    product, timeout=settings.DEFAULT_TIMEOUT
                )
        return self
