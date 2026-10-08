from contextlib import nullcontext

import allure
from playwright.sync_api import Page, expect
from typing_extensions import Self

from settings import settings
from src.constants.regular_expressions import RegularExpressions
from src.pages.base_page import BasePage


class ProductInformationPage(BasePage):
    """Описывает страницу информации о продукте."""

    # Селекторы и текстовые константы, необходимые для работы класса ProductInformationPage.
    _TEXTAREA_JUSTIFICATION_COMMENT = "textarea"
    """Textarea 'Обоснование/Комментарий'."""
    _RED_BACKLIGHT_FOR_TEXTAREA = "div[data-status='error']"
    """Красная подсветка для textarea 'Обоснование/Комментарий'."""
    _CANCEL_EDITING_BUTTON = ".icon-example-app.icon-app-cancel.icon-component"
    """Кнопка отмены редактирования."""
    _CHECKBOX_AGREEMENT = ".checkboxMark"
    """Checkbox 'Согласование'."""

    def __init__(self, page: Page) -> None:
        """Инициализация объекта страницы.

        :param page: Объект страницы playwright Page.
        """
        super().__init__(page)

        # Локаторы, необходимые для работы класса ProductInformationPage.
        self._locator_first_textarea = self.page.locator(self._TEXTAREA_JUSTIFICATION_COMMENT).first
        """Локатор первой textarea 'Обоснование/Комментарий'."""

    @allure.step("Проверить видимость первой textarea 'Обоснование/Комментарий'.")
    def check_visibility_textarea_justification_comment(self) -> Self:
        """Проверить видимость первой textarea 'Обоснование/Комментарий'.

        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with nullcontext():
            expect(self._locator_first_textarea, "Textarea 'Обоснование/Комментарий' не отображается").to_be_visible()
        return self

    @allure.step("Ввести текст в первую textarea 'Обоснование/Комментарий'.")
    def fill_in_textarea_justification_comment(self, text: str) -> Self:
        """Ввести текст в первую textarea 'Обоснование/Комментарий'.

        :param text: Текст вводимый в textarea.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with nullcontext():
            self.check_visibility_textarea_justification_comment()
            expect(self._locator_first_textarea, "Textarea 'Обоснование/Комментарий' недоступна").to_be_enabled()
            self._locator_first_textarea.fill(text)
        return self

    @allure.step("Проверить текст в первой textarea 'Обоснование/Комментарий'.")
    def check_text_in_textarea_justification_comment(self, text: str) -> Self:
        """Проверить текст в первой textarea 'Обоснование/Комментарий'.

        :param text: Текст, который должен присутствовать в textarea.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with nullcontext():
            expect(
                self._locator_first_textarea, f"Textarea 'Обоснование/Комментарий' не содержит ожидаемый текст '{text}'"
            ).to_have_text(text)
        return self

    @allure.step("Проверить красную подсветку для первой textarea 'Обоснование/Комментарий'.")
    def check_red_backlight_for_textarea(self) -> Self:
        """Проверить красную подсветку для первой textarea 'Обоснование/Комментарий'.

        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with nullcontext():
            expect(
                self.page.locator(self._RED_BACKLIGHT_FOR_TEXTAREA),
                "Красная подсветка для textarea 'Обоснование/Комментарий' не отображается",
            ).to_be_visible()
        return self

    @allure.step("Проверить вертикальный скролл и отображение первых 3 строк в первой textarea.")
    def check_attributes_in_textarea_justification_comment(self) -> Self:
        """Проверить вертикальный скролл и отображение первых 3 строк в первой textarea.

        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with nullcontext():
            expect(
                self._locator_first_textarea,
                "Textarea 'Обоснование/Комментарий' не отображает ожидаемое количество строк (три строки)",
            ).to_have_attribute("rows", "3")
            expect(
                self._locator_first_textarea.locator(".."),
                "Textarea 'Обоснование/Комментарий' не отображает ожидаемый вертикальный скролл (с классом "
                "'scrollThin')",
            ).to_have_class(RegularExpressions.PATTERN_CLASS_SCROLL_THIN)
        return self

    @allure.step("Проверить видимость кнопки отмены редактирования.")
    def check_visibility_cancel_editing_button(self) -> Self:
        """Проверить видимость кнопки отмены редактирования.

        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with nullcontext():
            expect(
                self.page.locator(self._CANCEL_EDITING_BUTTON), "Кнопка отмены редактирования не отображается"
            ).to_be_visible()
        return self

    @allure.step("Проверить сортировку в паспорте продукта, вкладка 'Компонентный состав'.")
    def check_sorting_in_product_passport_component_composition_tab(self, list_components: list[str]) -> Self:
        """Проверить сортировку в паспорте продукта, вкладка 'Компонентный состав'.

        :param list_components: Эталонный список компонентов.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with nullcontext():
            # Переменная i на первой итерации будет равна 10
            for i, product in enumerate(list_components, start=10):
                expect(
                    self._locator_link.nth(i), "Неверная сортировка в паспорте продукта, вкладка 'Компонентный состав'"
                ).to_have_text(product, timeout=settings.DEFAULT_TIMEOUT)
        return self

    @allure.step("Проверить checkbox 'Согласование' и кликнуть на него, если он не отмечен.")
    def check_checkbox_agreement_and_click(self, marked: bool = True) -> Self:
        """Проверить checkbox 'Согласование' и кликнуть на него, если он не отмечен.

        :param marked: Checkbox должен быть отмечен или нет (если 'False', то checkbox должен быть не отмечен).
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        # Ожидание в одну секунду
        self.page.wait_for_timeout(1_000)

        locator_checkbox_agreement = self.page.locator(self._CHECKBOX_AGREEMENT)
        locator_checkbox_mark_checked = self.page.locator(self._CHECKBOX)

        with nullcontext():
            expect(locator_checkbox_agreement, "Checkbox 'Согласование' не отображается").to_be_visible(
                timeout=settings.DEFAULT_TIMEOUT
            )
            expect(locator_checkbox_agreement, "Checkbox 'Согласование' недоступен").to_be_enabled()

            if marked:
                if not locator_checkbox_mark_checked.is_visible():
                    locator_checkbox_agreement.click()
            else:
                if locator_checkbox_mark_checked.is_visible():
                    locator_checkbox_agreement.click()
        return self
