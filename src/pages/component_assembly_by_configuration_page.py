import allure
from playwright.sync_api import Page, expect
from pytest_assume.plugin import assume
from typing_extensions import Self

from src.pages.base_page import BasePage


class ComponentAssemblyByConfigurationPage(BasePage):
    """Описывает страницу о сборке по конфигурации (компонент)."""

    def __init__(self, page: Page) -> None:
        """Инициализация объекта страницы.

        :param page: Объект страницы playwright Page.
        """
        super().__init__(page)

    @allure.step("Проверить серый индикатор в первой строке в таблице на вкладке 'Компоненты-потребители'.")
    def check_grey_indicator_in_table_consumer_components_assembly_page(self) -> Self:
        """Проверить серый индикатор в первой строке в таблице на вкладке 'Компоненты-потребители'.

        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        # Пятый столбец, в котором находится серый индикатор
        fifth_column = 4

        with assume:
            expect(
                self._locator_table_first_row_and_column.nth(fifth_column).locator(self._GREY_INDICATOR),
                "Серый индикатор в столбце номер 5 не отображается",
            ).to_be_visible()
        return self
