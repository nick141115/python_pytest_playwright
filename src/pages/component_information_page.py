import allure
from playwright.sync_api import Page, expect
from pytest_assume.plugin import assume
from typing_extensions import Self

from settings import settings
from src.constants.ui_text_elements import UITextElements
from src.pages.base_page import BasePage


class ComponentInformationPage(BasePage):
    """Описывает страницу информации о компоненте."""

    # Селекторы и текстовые константы, необходимые для работы класса ComponentInformationPage.
    _QUESTION_MARK = ".icon-app-help"
    """Знак вопроса."""
    _LIST_LINKS_IN_PRODUCTS_AND_COMPONENTS = f"tbody > {BasePage._TR} a"
    """Ссылки в списке продуктов и в списке компонентов."""
    _LINKS = ".componentCommonInfo__terminList > dd"
    """CSS-селектор для ссылок на документацию и artifactory."""
    _TEXT_COMPONENT_TYPE = f"//dt[text()='{UITextElements.TYPE}']/following-sibling::dd[1]"
    """Текст типа компонента."""
    _RESPONSIBLE_FOR_IMPLEMENTATION_OF_COMPONENT = (
        f"//dt[text()='{UITextElements.RESPONSIBLE_FOR_IMPLEMENTATION}']/following-sibling::dd[1]"
    )
    """Ответственный за реализацию компонента."""
    _COMPONENT_OWNER = f"//dt[text()='{UITextElements.OWNER}']/following-sibling::dd[1]"
    """Владелец компонента."""
    _TECHNICAL_EXPERT_OF_COMPONENT = f"//dt[text()='{UITextElements.TECHNICAL_EXPERT}']/following-sibling::dd[1]"
    """Технический эксперт компонента."""
    _ELEMENT_IN_COMBO_BOX_COMPONENT_TYPE = ".option"
    """Элемент в выпадающем списке типа компонента."""

    def __init__(self, page: Page) -> None:
        """Инициализация объекта страницы.

        :param page: Объект страницы playwright Page.
        """
        super().__init__(page)

    @allure.step("Навести курсор на знак вопроса.")
    def hover_cursor_over_question_mark(self) -> Self:
        """Навести курсор на знак вопроса.

        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        locator_question_mark = self.page.locator(self._QUESTION_MARK)

        with assume:
            expect(locator_question_mark, "Знак вопроса не отображается").to_be_visible()
            locator_question_mark.hover()
        return self

    @allure.step("Проверить сортировку ссылок в алфавитном порядке в списке продуктов.")
    def check_links_in_products_list(self, list_products: list[str]) -> Self:
        """Проверить сортировку ссылок в алфавитном порядке в списке продуктов.

        :param list_products: Список продуктов.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        locator_links_in_product_list = self.page.locator(self._LIST_LINKS_IN_PRODUCTS_AND_COMPONENTS)

        with assume:
            for i, product in enumerate(list_products):
                expect(
                    locator_links_in_product_list.nth(i),
                    f"Ссылка номер {i + 1} не содержит ожидаемый текст '{product}'",
                ).to_have_text(product, timeout=settings.DEFAULT_TIMEOUT)
        return self

    @allure.step("Проверить сортировку ссылок в алфавитном порядке в списке компонентов.")
    def check_links_in_components_list(self, list_components: list[str]) -> Self:
        """Проверить сортировку ссылок в алфавитном порядке в списке компонентов.

        :param list_components: Список компонентов.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        locator_links_in_components_list = self.page.locator(self._LIST_LINKS_IN_PRODUCTS_AND_COMPONENTS)

        with assume:
            for i, component in enumerate(list_components):
                expect(
                    locator_links_in_components_list.nth(i),
                    f"Ссылка номер {i + 1} не содержит ожидаемый текст '{component}'",
                ).to_have_text(component)
        return self

    @allure.step("Проверить серый индикатор в таблице на вкладке 'Общая информация' (Компонент).")
    def check_grey_indicator_in_table_general_information_component(self) -> Self:
        """Проверить серый индикатор в таблице на вкладке 'Общая информация' (Компонент).

        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            expect(
                self.page.locator(self.SECOND_COLUMN_OF_TABLE).nth(1).locator(self._GREY_INDICATOR),
                "Серый индикатор не отображается",
            ).to_be_visible()
        return self

    @allure.step("Проверить таблицу на вкладке 'Версии'.")
    def check_table_versions(self, list_versions: list[str]) -> Self:
        """Проверить таблицу на вкладке 'Версии'.

        :param list_versions: Список версий.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        not_supported = "Не поддерживается"

        # Проверка первого столбца с версиями
        with assume:
            for i, version in enumerate(list_versions):
                expect(
                    self._locator_table_row.nth(i).locator(self.TABLE_COLUMN).first,
                    f"Версия в строке номер {i + 1} не отображается или значение не соответствует ожидаемому "
                    f"'{version}'",
                ).to_have_text(version)

            third_column = 2
            fifth_line = 4
            # Проверка столбца со статусом разработки (проверка в цикле первых четырёх строк)
            for i in range(4):
                expect(
                    self._locator_table_row.nth(i).locator(self.TABLE_COLUMN).nth(third_column),
                    f"Статус разработки в строке номер {i + 1} не отображается или значение не соответствует "
                    f"ожидаемому '{UITextElements.ABSENT}'",
                ).to_have_text(UITextElements.ABSENT)

            expect(
                self._locator_table_row.nth(fifth_line).locator(self.TABLE_COLUMN).nth(third_column),
                "Статус разработки в строке номер 5 не отображается или значение не соответствует ожидаемому "
                f"'{not_supported}'",
            ).to_have_text(not_supported)
        return self

    @allure.step("Проверить текст типа компонента.")
    def check_component_type_text(self, type_text: str) -> Self:
        """Проверить текст типа компонента.

        :param type_text: Ожидаемый текст типа компонента.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        locator_component_type_text = self.page.locator(self._TEXT_COMPONENT_TYPE)

        with assume:
            expect(
                locator_component_type_text, "Элемент с текстом типа компонента не отображается на странице."
            ).to_be_visible()
            expect(
                locator_component_type_text,
                f"Элемент с текстом типа компонента не содержит ожидаемый текст '{type_text}'.",
            ).to_contain_text(type_text, timeout=settings.DEFAULT_TIMEOUT)
        return self

    @allure.step("Проверить ответственного за реализацию компонента.")
    def check_responsible_for_implementation_of_component(self, full_name: str) -> Self:
        """Проверить ответственного за реализацию компонента.

        :param full_name: ФИО ответственного за реализацию компонента.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        locator_responsible_for_implementation_of_component = self.page.locator(
            self._RESPONSIBLE_FOR_IMPLEMENTATION_OF_COMPONENT
        )

        with assume:
            expect(
                locator_responsible_for_implementation_of_component,
                "Элемент с ФИО ответственного за реализацию компонента не отображается на странице.",
            ).to_be_visible()
            expect(
                locator_responsible_for_implementation_of_component,
                f"Элемент с ФИО ответственного за реализацию компонента не содержит ожидаемый текст '{full_name}'.",
            ).to_contain_text(full_name, timeout=settings.DEFAULT_TIMEOUT)
        return self

    @allure.step("Проверить владельца компонента.")
    def check_component_owner(self, full_name: str) -> Self:
        """Проверить владельца компонента.

        :param full_name: ФИО владельца компонента.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        locator_component_owner = self.page.locator(self._COMPONENT_OWNER)

        with assume:
            expect(
                locator_component_owner,
                "Элемент с ФИО владельца компонента не отображается на странице.",
            ).to_be_visible()
            expect(
                locator_component_owner,
                f"Элемент с ФИО владельца компонента не содержит ожидаемый текст '{full_name}'.",
            ).to_contain_text(full_name, timeout=settings.DEFAULT_TIMEOUT)
        return self

    @allure.step("Проверить технического эксперта компонента.")
    def check_technical_expert_of_component(self, full_name: str) -> Self:
        """Проверить технического эксперта компонента.

        :param full_name: ФИО технического эксперта компонента.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        locator_technical_expert_of_component = self.page.locator(self._TECHNICAL_EXPERT_OF_COMPONENT)

        with assume:
            expect(
                locator_technical_expert_of_component,
                "Элемент с ФИО технического эксперта компонента не отображается на странице.",
            ).to_be_visible()
            expect(
                locator_technical_expert_of_component,
                f"Элемент с ФИО технического эксперта компонента не содержит ожидаемый текст '{full_name}'.",
            ).to_contain_text(full_name, timeout=settings.DEFAULT_TIMEOUT)
        return self

    @allure.step("Проверить элементы в выпадающем списке типа компонента.")
    def check_elements_in_combo_box_component_type(self, elements: list[str]) -> Self:
        """Проверить элементы в выпадающем списке типа компонента.

        :param elements: Список элементов.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        locator_element_in_combo_box = self.page.locator(self._ELEMENT_IN_COMBO_BOX_COMPONENT_TYPE)

        with assume:
            for i, element in enumerate(elements):
                expect(
                    locator_element_in_combo_box.nth(i), f"Элемент с текстом '{element}' не содержится в combobox'е."
                ).to_contain_text(element)
        return self
