from typing import Literal

import allure
from playwright.sync_api import Page, expect
from pytest_assume.plugin import assume
from typing_extensions import Self

from settings import settings
from src.constants.colors import Colors
from src.constants.css_keys_and_values import CssKeysAndValues
from src.constants.ui_text_elements import UITextElements
from src.pages.base_page import BasePage


class ProductVersionInformationPage(BasePage):
    """Описывает страницу информации о версии продукта."""

    # Селекторы и текстовые константы, необходимые для работы класса ProductVersionInformationPage.
    _GREEN_INDICATOR_SECURITY_FUNCTION = ".dropdown__popover [data-status='ok']"
    """Зелёный индикатор функции безопасности или поверхности атаки"""
    _RED_INDICATOR_SECURITY_FUNCTION = ".dropdown__popover [data-status='error']"
    """Красный индикатор функции безопасности или поверхности атаки"""
    _YELLOW_INDICATOR_SECURITY_FUNCTION = ".dropdown__popover [data-status='warning']"
    """Жёлтый индикатор функции безопасности или поверхности атаки"""
    _GREY_INDICATOR_SECURITY_FUNCTION = ".dropdown__popover [data-status='none']"
    """Серый индикатор функции безопасности или поверхности атаки"""
    _RED_BACKLIGHT_FIELD_VERSION = ".popover.fieldError.selectContainer"
    """Красная подсветка поля 'Версия'"""
    _RED_FONT_ERROR = ".fieldErrorText"
    """Красный шрифт текста ошибки"""
    _CHECKBOX_NOT_SPECIFIED = f"div:nth-child(3) .selectContainer__menu div:nth-child(1) {BasePage._PATH}"
    """Checkbox 'Не указана'"""

    def __init__(self, page: Page) -> None:
        """Инициализация объекта страницы.

        :param page: Объект страницы playwright Page.
        """
        super().__init__(page)

    @allure.step("Проверить checkbox 'Не указана'.")
    def check_checkbox_not_specified(self) -> Self:
        """Проверить checkbox 'Не указана'.

        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            expect(
                self.page.locator(self._CHECKBOX_NOT_SPECIFIED),
                UITextElements.CHECKBOX + f"'{UITextElements.NOT_SPECIFIED}'" + UITextElements.NOT_MARKED,
            ).to_have_css(CssKeysAndValues.DISPLAY, CssKeysAndValues.INLINE)
        return self

    @allure.step("Проверить сортировку в паспорте версии продукта, вкладка 'Сборки'.")
    def check_sorting_on_assemblies_tab(self, list_assemblies: list[str]) -> Self:
        """Проверить сортировку в паспорте версии продукта, вкладка 'Сборки'.

        :param list_assemblies: Эталонный список сборок.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            # Переменная i на первой итерации будет равна 9
            for i, assembly in enumerate(list_assemblies, start=9):
                expect(
                    self._locator_link.nth(i), "Неверная сортировка в паспорте версии продукта, вкладка 'Сборки'"
                ).to_have_text(assembly, timeout=settings.DEFAULT_TIMEOUT)
        return self

    @allure.step("Проверить сортировку в паспорте версии продукта, вкладка 'Компонентный состав'.")
    def check_sorting_in_version_passport_component_composition_tab(self, list_components: list[str]) -> Self:
        """Проверить сортировку в паспорте версии продукта, вкладка 'Компонентный состав'.

        :param list_components: Эталонный список компонентов.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            # Перебирает каждый второй элемент списка, начиная с самого первого (с индекса 0)
            for i, product in list(enumerate(list_components))[::2]:
                expect(
                    # Проверяет ссылки на компоненты в таблице 'Компонентный состав'
                    self._locator_link.nth((i * 2) + 9),
                    "Неверная сортировка в паспорте версии продукта, вкладка 'Компонентный состав'",
                ).to_have_text(product, timeout=settings.DEFAULT_TIMEOUT)
        return self

    @allure.step("Проверить видимость красной подсветки поля 'Версия'.")
    def check_visibility_red_backlight_field_version(self) -> Self:
        """Проверить видимость красной подсветки поля 'Версия'.

        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            expect(
                self.page.locator(self._RED_BACKLIGHT_FIELD_VERSION), "Красная подсветка поля 'Версия' не отображается"
            ).to_be_visible()
        return self

    @allure.step("Проверить видимость красного шрифта текста ошибки.")
    def check_visibility_red_font_error(self) -> Self:
        """Проверить видимость красного шрифта текста ошибки.

        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            expect(
                self.page.locator(self._RED_FONT_ERROR), "Красный шрифт текста ошибки не отображается"
            ).to_be_visible()
        return self

    @allure.step("Проверить индикатор в списке функции безопасности или в списке поверхности атаки.")
    def check_indication_in_list_security_function_or_attack_surface(
        self, color: Literal["green", "red", "yellow", "grey"], security_function: bool = True
    ) -> Self:
        """Проверить индикатор в списке функции безопасности или в списке поверхности атаки.

        :param color: Цвет индикатора (возможные значения: green, red, yellow, grey).
        :param security_function: Если 'False', тогда будет проверяться список поверхности атаки.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        colors = {Colors.GREEN, Colors.RED, Colors.YELLOW, Colors.GREY}

        assert color in colors, f"Недопустимое значение ('{color}'). Выберите из: {colors}"

        with assume:
            match color:
                case Colors.GREEN:
                    expect(
                        self.page.locator(self._GREEN_INDICATOR_SECURITY_FUNCTION),
                        f"Зеленый индикатор в списке не отображается или не содержит ожидаемый "
                        f"текст ('{UITextElements.YES if security_function else UITextElements.NOT_INCLUDED}')",
                    ).to_have_text(
                        UITextElements.YES if security_function else UITextElements.NOT_INCLUDED,
                        timeout=settings.DEFAULT_TIMEOUT,
                    )
                case Colors.RED:
                    expect(
                        self.page.locator(self._RED_INDICATOR_SECURITY_FUNCTION),
                        f"Красный индикатор в списке не отображается или не содержит ожидаемый "
                        f"текст ('{UITextElements.NO if security_function else UITextElements.ENTERS}')",
                    ).to_have_text(
                        UITextElements.NO if security_function else UITextElements.ENTERS,
                        timeout=settings.DEFAULT_TIMEOUT,
                    )
                case Colors.YELLOW:
                    expect(
                        self.page.locator(self._YELLOW_INDICATOR_SECURITY_FUNCTION),
                        f"Жёлтый индикатор в списке не отображается или не содержит ожидаемый "
                        f"текст ('{UITextElements.INDIRECTLY}')",
                    ).to_have_text(UITextElements.INDIRECTLY, timeout=settings.DEFAULT_TIMEOUT)
                case Colors.GREY:
                    expect(
                        self.page.locator(self._GREY_INDICATOR_SECURITY_FUNCTION),
                        f"Серый индикатор в списке не отображается или не содержит ожидаемый "
                        f"текст ('{UITextElements.NOT_SPECIFIED}')",
                    ).to_have_text(UITextElements.NOT_SPECIFIED, timeout=settings.DEFAULT_TIMEOUT)
        return self
