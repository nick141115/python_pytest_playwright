import allure
from allure_commons.types import LinkType

from src.constants.components import Components
from src.constants.lists import Lists
from src.constants.packages import Packages
from src.constants.products import Products
from src.constants.radar_area_values import RadarAreaValues
from src.constants.ui_text_elements import UITextElements
from src.constants.versions import Versions
from tests.base.base_test import BaseTest


@allure.parent_suite("Паспорт версии продукта.")
@allure.epic("Паспорт версии продукта.")
@allure.sub_suite("Паспорт версии продукта.")
@allure.severity(allure.severity_level.NORMAL)
class TestProductVersionPassport(BaseTest):
    """Паспорт версии продукта."""

    _COMPONENT_COUNT_FIRST_SYMBOL = 7
    _COMPONENT_COUNT_LAST_SYMBOL = -11
    _FIRST_STRING_VALUES_WITHOUT_FILTERS = [
        " ",
        Components.ACPI_SUPPORT_BASE,
        RadarAreaValues.UNKNOWN,
        Packages.ACPI_SUPPORT_BASE,
        UITextElements.NOT_SPECIFIED,
        "",
        UITextElements.NOT_SPECIFIED,
        "",
    ]
    _FIRST_STRING_VALUES = [
        " ",
        Components.BIND9_DEV,
        RadarAreaValues.UNKNOWN,
        "1:9.16.50-1~deb11u2",
        UITextElements.NO,
        "",
        UITextElements.NOT_INCLUDED,
        "",
    ]

    @allure.suite("Паспорт версии продукта, вкладка 'Компонентный состав', отображение фильтра.")
    @allure.title("Паспорт версии продукта, вкладка 'Компонентный состав', отображение фильтра.")
    @allure.id("1521374")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1546832", LinkType.LINK, "TASK 1546832"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1521374", "TestCase 1521374")
    def test_product_version_passport_component_composition_tab_display_filter(self) -> None:
        """Паспорт версии продукта, вкладка 'Компонентный состав', отображение фильтра."""
        # Паспорт версии продукта_вкладка Компонентный состав_отображаение фильтра
        with allure.step(
            "1. Предусловие: Пользователь с правами редактирования и чтения паспортов продуктов и компонентов "
            "авторизован в сервисе. Открыт реестр продуктов, выбран продукт, выбрана версия продукта, открыт паспорт "
            "версии продукта на вкладке 'Компонентный состав'"
        ):
            self._setup_version_of_product_component_composition()

        with allure.step("2. Нажать на иконку в виде воронки"):
            (
                self.product_version_information_page.click_on_funnel_icon()
                .check_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)
                .check_combo_box_in_filter(UITextElements.SECURITY_FUNCTION)
                .check_combo_box_in_filter(UITextElements.ATTACK_SURFACE)
                .check_reset_filters_button()
            )

        with allure.step("3. Нажать Х (закрыть)"):
            self.product_information_page.click_on_close_filter_block_icon().check_reset_filters_button(
                visible_and_enabled=False
            )

    @allure.suite(
        "Паспорт версии продукта, вкладка 'Компонентный состав', сброс значений фильтров, обновление страницы."
    )
    @allure.title(
        "Паспорт версии продукта, вкладка 'Компонентный состав', сброс значений фильтров, обновление страницы."
    )
    @allure.id("1521389")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1546826", LinkType.LINK, "TASK 1546826"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1521389", "TestCase 1521389")
    def test_product_version_passport_component_composition_tab_resetting_filter_values_refresh_page(self) -> None:
        """Паспорт версии продукта, вкладка 'Компонентный состав', сброс значений фильтров, обновление страницы."""
        # Паспорт версии продукта_вкладка Компонентный состав_Сброс значений фильтров/обновление страницы
        with allure.step(
            "1. Предусловие: Пользователь с правами редактирования и чтения паспортов продуктов и компонентов "
            "авторизован в сервисе. Открыт реестр продуктов, выбран продукт, версия продукта, открыт паспорт версии "
            "продукта на вкладке 'Компонентный состав', открыт блок фильтра"
        ):
            self._setup_version_of_product_component_composition()
            self.product_version_information_page.click_on_funnel_icon()

        with allure.step("2. В нескольких фильтрах выбрать любые значения"):
            (
                self.product_version_information_page.check_text_total_components_with_any_number()
                .check_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)
                .click_on_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)
                .click_on_element_in_combo_box_in_filter(RadarAreaValues.UNKNOWN)
                .check_combo_box_in_filter(UITextElements.SECURITY_FUNCTION)
                .click_on_combo_box_in_filter(UITextElements.SECURITY_FUNCTION)
                .click_on_element_in_combo_box_in_filter(UITextElements.YES)
                .check_combo_box_in_filter(UITextElements.ATTACK_SURFACE)
                .click_on_combo_box_in_filter(UITextElements.ATTACK_SURFACE)
                .click_on_element_in_combo_box_in_filter(UITextElements.NOT_INCLUDED)
                .check_text_components_found_with_any_number()
            )

        with allure.step("3. Нажать кнопку 'Сбросить фильтр'"):
            (
                self.product_version_information_page.click_on_reset_filters_button()
                .check_reset_filters_button()
                .check_text_total_components_with_any_number()
            )

        with allure.step("4. Повторить ш.2 и обновить страницу сервиса"):
            (
                self.product_version_information_page.check_text_total_components_with_any_number()
                .check_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)
                .click_on_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)
                .click_on_element_in_combo_box_in_filter(RadarAreaValues.UNKNOWN)
                .check_combo_box_in_filter(UITextElements.SECURITY_FUNCTION)
                .click_on_combo_box_in_filter(UITextElements.SECURITY_FUNCTION)
                .click_on_element_in_combo_box_in_filter(UITextElements.YES)
                .check_combo_box_in_filter(UITextElements.ATTACK_SURFACE)
                .click_on_combo_box_in_filter(UITextElements.ATTACK_SURFACE)
                .click_on_element_in_combo_box_in_filter(UITextElements.NOT_INCLUDED)
                .check_text_components_found_with_any_number()
                .refresh_page()
                .check_text_total_components_with_any_number()
                .check_reset_filters_button(visible_and_enabled=False)
            )

    @allure.suite("Паспорт версии продукта, вкладка 'Компонентный состав', фильтр 'Зона техрадара', отображение.")
    @allure.title("Паспорт версии продукта, вкладка 'Компонентный состав', фильтр 'Зона техрадара', отображение.")
    @allure.id("1521375")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1548077", LinkType.LINK, "TASK 1548077"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1521375", "TestCase 1521375")
    def test_product_version_passport_component_composition_tab_filter_technical_radar_area_display(self) -> None:
        """Паспорт версии продукта, вкладка 'Компонентный состав', фильтр 'Зона техрадара', отображение."""
        # Паспорт версии продукта_вкладка Компонентный состав_фильтр Зона техрадара_отображаение
        with allure.step(
            "1. Предусловие: Пользователь с правами редактирования и чтения паспортов продуктов и компонентов "
            "авторизован в сервисе. Открыт реестр продуктов, выбран продукт, выбрана версия продукта, открыт "
            "паспорт версии продукта на вкладке 'Компонентный состав'"
        ):
            self._setup_version_of_product_component_composition()

        with allure.step("2. Кликнуть в поле фильтра 'Зона техрадара'"):
            self._select_filter_value(
                placeholder=UITextElements.TECHNICAL_RADAR_AREA,
                first_element=RadarAreaValues.AVOID,
                second_element=RadarAreaValues.UNKNOWN,
                list_combo_box_elements=list(RadarAreaValues),
            )

    @allure.suite("Паспорт версии продукта, вкладка 'Компонентный состав', фильтр 'Функция безопасности', отображение.")
    @allure.title("Паспорт версии продукта, вкладка 'Компонентный состав', фильтр 'Функция безопасности', отображение.")
    @allure.id("1521377")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1548080", LinkType.LINK, "TASK 1548080"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1521377", "TestCase 1521377")
    def test_product_version_passport_component_composition_tab_filter_security_function_display(self) -> None:
        """Паспорт версии продукта, вкладка 'Компонентный состав', фильтр 'Функция безопасности', отображение."""
        # Паспорт версии продукта_вкладка Компонентный состав_фильтр Функция безопасности_отображение
        with allure.step(
            "1. Предусловие: Пользователь с правами редактирования и чтения паспортов продуктов и компонентов "
            "авторизован в сервисе. Открыт реестр продуктов, выбран продукт, выбрана версия продукта, открыт "
            "паспорт версии продукта на вкладке 'Компонентный состав'"
        ):
            self._setup_version_of_product_component_composition()

        with allure.step("2. Кликнуть в поле фильтра 'Функция безопасности'"):
            list_combo_box_elements = [
                UITextElements.NOT_SPECIFIED,
                UITextElements.YES,
                UITextElements.INDIRECTLY,
                UITextElements.NO,
            ]

            self._select_filter_value(
                placeholder=UITextElements.SECURITY_FUNCTION,
                first_element=UITextElements.YES,
                second_element=UITextElements.NO,
                list_combo_box_elements=list_combo_box_elements,
            )

    @allure.suite("Паспорт версии продукта, вкладка 'Компонентный состав', фильтр 'Поверхность атаки', отображение.")
    @allure.title("Паспорт версии продукта, вкладка 'Компонентный состав', фильтр 'Поверхность атаки', отображение.")
    @allure.id("1521380")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1548081", LinkType.LINK, "TASK 1548081"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1521380", "TestCase 1521380")
    def test_product_version_passport_component_composition_tab_filter_attack_surface_display(self) -> None:
        """Паспорт версии продукта, вкладка 'Компонентный состав', фильтр 'Поверхность атаки', отображение."""
        # Паспорт версии продукта_вкладка Компонентный состав _фильтр Поверхность атаки_отображение
        with allure.step(
            "1. Предусловие: Пользователь с правами редактирования и чтения паспортов продуктов и компонентов "
            "авторизован в сервисе. Открыт реестр продуктов, выбран продукт, выбрана версия продукта, открыт "
            "паспорт версии продукта на вкладке 'Компонентный состав'"
        ):
            self._setup_version_of_product_component_composition()

        with allure.step("2. Кликнуть в поле фильтра 'Поверхность атаки'"):
            list_combo_box_elements = [
                UITextElements.NOT_SPECIFIED,
                UITextElements.NOT_INCLUDED,
                UITextElements.INDIRECTLY,
                UITextElements.ENTERS,
            ]

            self._select_filter_value(
                placeholder=UITextElements.ATTACK_SURFACE,
                first_element=UITextElements.NOT_INCLUDED,
                second_element=UITextElements.ENTERS,
                list_combo_box_elements=list_combo_box_elements,
            )

    @allure.suite("Фильтр 'Компонентный состав', паспорт версии продукта, вкладка 'Сборки'.")
    @allure.title("Фильтр 'Компонентный состав', паспорт версии продукта, вкладка 'Сборки'.")
    @allure.id("1560298")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1562343", LinkType.LINK, "TASK 1562343"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1560298", "TestCase 1560298")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_product_version_passport_filter_component_composition_assemblies_tab(self) -> None:
        """Фильтр 'Компонентный состав', паспорт версии продукта, вкладка 'Сборки'."""
        # Фильтр Компонентный состав_ паспорт версии продукта, вкладка Сборки
        with allure.step(
            "1. Пользователь авторизован в сервисе АР, открыт паспорт версии продукта → вкладка 'Сборки', открыт блок "
            "фильтра"
        ):
            self.component_page.click_on_link_products()
            self.product_page.click_on_link(UITextElements.ALL_PRODUCTS).click_on_link(Products.COORDINATOR_HW_5)
            self.product_information_page.click_on_link(UITextElements.VERSIONS_TAB).click_on_link(
                Versions.COORDINATOR_HW_5
            )
            self.product_version_information_page.click_on_funnel_icon().check_reset_filters_button()

        with allure.step("2. Кликнуть по фильтру 'Компонентный состав'"):
            self.product_version_information_page.check_combo_box_in_filter(
                UITextElements.COMPONENT_COMPOSITION
            ).click_on_combo_box_in_filter(UITextElements.COMPONENT_COMPOSITION)

        with allure.step("3. Выбрать значение 'Файлы обработаны'"):
            titles = [
                UITextElements.ASSEMBLY,
                "Дистрибутив",
                "Хранилище сборок",
            ]
            value = [
                "5.4.0.2299",
                "Coordinator HWVA",
                "PDC",
            ]
            (
                self.product_version_information_page.click_on_element_with_text(UITextElements.FILES_PROCESSED)
                .check_text(
                    page_text=UITextElements.COMPONENT_COMPOSITION
                    + UITextElements.COLON_SPACE
                    + UITextElements.FILES_PROCESSED
                )
                .check_text_assemblies_found_with_any_number()
                .check_table_headings(titles)
                .check_table_text_values(value)
            )

        with allure.step("4. Выбрать значение 'Ошибка обработки файлов'"):
            (
                self.product_version_information_page.click_on_cross_icon()
                .check_text_total_assemblies_with_any_number()
                .check_combo_box_in_filter(UITextElements.COMPONENT_COMPOSITION)
                .click_on_combo_box_in_filter(UITextElements.COMPONENT_COMPOSITION)
                .click_on_element_with_text(UITextElements.FILE_PROCESSING_ERROR)
                .check_text(
                    page_text=UITextElements.COMPONENT_COMPOSITION
                    + UITextElements.COLON_SPACE
                    + UITextElements.FILE_PROCESSING_ERROR
                )
                .check_text_assemblies_found_with_any_number()
                .check_text(UITextElements.NOTHING_FOUND)
            )

        with allure.step("5. Нажать Х"):
            value = [
                "5.4.0.7008",
                "",
                "",
            ]
            (
                self.product_version_information_page.click_on_cross_icon()
                .check_combo_box_in_filter(UITextElements.COMPONENT_COMPOSITION)
                .check_text_total_assemblies_with_any_number()
                .check_table_text_values(value)
            )

    @allure.suite("Паспорт версии продукта, вкладка 'Компонентный состав', фильтр 'Зона техрадара'.")
    @allure.title("Паспорт версии продукта, вкладка 'Компонентный состав', фильтр 'Зона техрадара'.")
    @allure.id("1565414")
    @allure.description("Баг: Текст 'Всего <любое число> компонент(а/ов)' не отображается на странице.")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1572645", LinkType.LINK, "TASK 1572645"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1565414", "TestCase 1565414")
    def test_product_version_passport_component_composition_tab_filter_technical_radar_area(self) -> None:
        """Паспорт версии продукта, вкладка 'Компонентный состав', фильтр 'Зона техрадара'."""
        # Паспорт версии продукта_вкладка Компонентный состав_фильтр Зона техрадара
        with allure.step(
            "1. Предусловие: Пользователь с правами редактирования и чтения паспортов продуктов и компонентов "
            "авторизован в сервисе. Открыт реестр продуктов, выбран продукт, выбрана версия продукта, открыт паспорт "
            "версии продукта на вкладке 'Компонентный состав'"
        ):
            self._setup_version_of_product_component_composition()
            (
                self.product_version_information_page.click_on_funnel_icon()
                .check_table_headings(Lists.TITLES_TABLE_COMPONENT_COMPOSITION)
                .check_table_text_values(self._FIRST_STRING_VALUES_WITHOUT_FILTERS)
            )

        with allure.step("2. Кликнуть в поле фильтра 'Зона техрадара'"):
            self.product_version_information_page.check_combo_box_in_filter(
                UITextElements.TECHNICAL_RADAR_AREA
            ).click_on_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)

        with allure.step("3. В фильтре 'Зона техрадара' выбрать одно любое значение"):
            values = [
                " ",
                Components.BASH,
                RadarAreaValues.RECOMMENDED,
                Packages.BASH,
                UITextElements.NOT_SPECIFIED,
                "",
                UITextElements.NOT_SPECIFIED,
                "",
            ]

            (
                self.product_version_information_page.check_text_total_components_with_any_number()
                .click_on_element_in_combo_box_in_filter(RadarAreaValues.RECOMMENDED)
                .check_checkbox_with_text_in_combo_box_in_filter(RadarAreaValues.RECOMMENDED)
                .check_text_components_found_with_any_number()
                .check_table_text_values(values)
            )
            temp_text_components_found = self.product_information_page.get_text_components_found_with_any_number()

        with allure.step("4. В фильтре 'Зона техрадара' выбрать еще одно любое значение"):
            (
                self.product_version_information_page.click_on_element_in_combo_box_in_filter(
                    RadarAreaValues.PILOTED_BY
                )
                .check_checkbox_with_text_in_combo_box_in_filter(RadarAreaValues.PILOTED_BY)
                .check_text(page_text=temp_text_components_found, visible=False)
            )

        with allure.step("5. Закрыть выпадающий список"):
            (
                self.product_version_information_page.check_combo_box_list_and_text_in_filter(
                    text_in_combo_box=UITextElements.TECHNICAL_RADAR_AREA + UITextElements.COLON_SPACE_TWO,
                    list_combo_box_elements=RadarAreaValues,
                )
                .check_combo_box_in_filter(UITextElements.SECURITY_FUNCTION)
                .click_on_combo_box_in_filter(UITextElements.SECURITY_FUNCTION)
            )

        with allure.step("6. Открыть выпадающий список, проверить отображение выбранных значений"):
            (
                self.product_version_information_page.check_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)
                .click_on_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)
                .check_checkbox_with_text_in_combo_box_in_filter(RadarAreaValues.RECOMMENDED)
                .check_checkbox_with_text_in_combo_box_in_filter(RadarAreaValues.PILOTED_BY)
                .check_combo_box_list_and_text_in_filter(
                    text_in_combo_box=UITextElements.TECHNICAL_RADAR_AREA + UITextElements.COLON_SPACE_TWO,
                    list_combo_box_elements=RadarAreaValues,
                )
            )

        with allure.step("7. Выбрать все значения в фильтре"):
            (
                self.product_version_information_page.click_on_element_in_combo_box_in_filter(
                    RadarAreaValues.INTERESTED_IN
                )
                .click_on_element_in_combo_box_in_filter(RadarAreaValues.AVOID)
                .click_on_element_in_combo_box_in_filter(RadarAreaValues.UNKNOWN)
                .check_table_text_values(self._FIRST_STRING_VALUES_WITHOUT_FILTERS)
            )
            temp_text_components_found = self.product_information_page.get_text_components_found_with_any_number()

        with allure.step("8. Нажать 'Сбросить фильтр'"):
            (
                self.product_version_information_page.click_on_reset_filters_button()
                .check_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)
                .check_table_text_values(self._FIRST_STRING_VALUES_WITHOUT_FILTERS)
                .check_text_total_components_with_any_number()
                .check_text(
                    page_text=temp_text_components_found[
                        self._COMPONENT_COUNT_FIRST_SYMBOL : self._COMPONENT_COUNT_LAST_SYMBOL
                    ],
                    exact=False,
                )
            )

    @allure.suite("Паспорт версии продукта, вкладка 'Компонентный состав', фильтр 'Поверхность атаки'.")
    @allure.title("Паспорт версии продукта, вкладка 'Компонентный состав', фильтр 'Поверхность атаки'.")
    @allure.id("1565416")
    @allure.description("Баг: Текст 'Всего <любое число> компонент(а/ов)' не отображается на странице.")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1576542", LinkType.LINK, "TASK 1576542"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1565416", "TestCase 1565416")
    def test_product_version_passport_component_composition_tab_filter_attack_surface(self) -> None:
        """Паспорт версии продукта, вкладка 'Компонентный состав', фильтр 'Поверхность атаки'."""
        # Паспорт версии продукта_вкладка Компонентный состав_фильтр Поверхность атаки
        with allure.step(
            "1. Предусловие: Пользователь с правами редактирования и чтения паспортов продуктов и компонентов "
            "авторизован в сервисе. Открыт реестр продуктов, выбран продукт, выбрана версия продукта, открыт паспорт "
            "версии продукта на вкладке 'Компонентный состав'"
        ):
            self._setup_version_of_product_component_composition()

        with allure.step("2. Кликнуть в поле фильтра 'Поверхность атаки'"):
            (
                self.product_version_information_page.click_on_funnel_icon()
                .check_combo_box_in_filter(UITextElements.ATTACK_SURFACE)
                .click_on_combo_box_in_filter(UITextElements.ATTACK_SURFACE)
            )

        with allure.step("3. В фильтре 'Поверхность атаки' выбрать значение 'Не указана'"):
            (
                self.product_version_information_page.check_text_total_components_with_any_number()
                .click_on_element_with_text(element_text=UITextElements.NOT_SPECIFIED, nth=1)
                .check_checkbox_not_specified()
                .check_text_components_found_with_any_number()
            )

        with allure.step("4. Нажать 'Сбросить фильтр'"):
            (
                self.product_version_information_page.click_on_reset_filters_button()
                .check_combo_box_in_filter(UITextElements.ATTACK_SURFACE)
                .check_text_total_components_with_any_number()
            )

        with allure.step("5. Повторить шаги тест кейса для выбора следующих значений в фильтре 'Поверхность атаки':"):
            with allure.step("6. Не указана + одно из значений: Входит/Косвенно/Не входит"):
                list_combo_box_elements = [
                    UITextElements.NOT_SPECIFIED,
                    UITextElements.NOT_INCLUDED,
                    UITextElements.INDIRECTLY,
                    UITextElements.ENTERS,
                ]

                (
                    self.product_version_information_page.check_combo_box_in_filter(UITextElements.ATTACK_SURFACE)
                    .click_on_combo_box_in_filter(UITextElements.ATTACK_SURFACE)
                    .click_on_element_with_text(element_text=UITextElements.NOT_SPECIFIED, nth=1)
                    .check_checkbox_not_specified()
                    .click_on_element_with_text(UITextElements.NOT_INCLUDED)
                    .check_checkbox_with_text_in_combo_box_in_filter(UITextElements.NOT_INCLUDED)
                    .check_combo_box_list_and_text_in_filter(
                        text_in_combo_box=UITextElements.ATTACK_SURFACE + UITextElements.COLON_SPACE_TWO,
                        list_combo_box_elements=list_combo_box_elements,
                    )
                    .check_text_components_found_with_any_number()
                )

            with allure.step("7. Значение 'Входит'"):
                first_string_values = [
                    " ",
                    "libcrypt1",
                    RadarAreaValues.UNKNOWN,
                    "1:4.4.18-4",
                    UITextElements.NO,
                    "",
                    UITextElements.ENTERS,
                    "",
                ]

                (
                    self.product_version_information_page.click_on_reset_filters_button()
                    .check_text_total_components_with_any_number()
                    .check_combo_box_in_filter(UITextElements.ATTACK_SURFACE)
                    .click_on_combo_box_in_filter(UITextElements.ATTACK_SURFACE)
                    .click_on_element_with_text(UITextElements.ENTERS)
                    .check_text_components_found_with_any_number()
                    .check_table_headings(Lists.TITLES_TABLE_COMPONENT_COMPOSITION)
                    .check_table_text_values(first_string_values)
                )

            with allure.step("8. Значение 'Не входит'"):
                (
                    self.product_version_information_page.click_on_reset_filters_button()
                    .check_text_total_components_with_any_number()
                    .check_combo_box_in_filter(UITextElements.ATTACK_SURFACE)
                    .click_on_combo_box_in_filter(UITextElements.ATTACK_SURFACE)
                    .click_on_element_with_text(UITextElements.NOT_INCLUDED)
                    .check_text_components_found_with_any_number()
                    .check_table_text_values(self._FIRST_STRING_VALUES)
                )

            with allure.step("9. Значение 'Косвенно'"):
                first_string_values = [
                    " ",
                    "libgcc-s1",
                    RadarAreaValues.UNKNOWN,
                    "10.2.1-6",
                    UITextElements.NOT_SPECIFIED,
                    "",
                    UITextElements.INDIRECTLY,
                    "",
                ]

                (
                    self.product_version_information_page.click_on_reset_filters_button()
                    .check_text_total_components_with_any_number()
                    .check_combo_box_in_filter(UITextElements.ATTACK_SURFACE)
                    .click_on_combo_box_in_filter(UITextElements.ATTACK_SURFACE)
                    .click_on_element_with_text(element_text=UITextElements.INDIRECTLY, nth=1)
                    .check_text_components_found_with_any_number()
                    .check_table_text_values(first_string_values)
                )

            with allure.step("10. 'Не указана' + 'Не входит' + 'Косвенно' + 'Входит'"):
                (
                    self.product_version_information_page.click_on_reset_filters_button()
                    .check_text_total_components_with_any_number()
                    .check_combo_box_in_filter(UITextElements.ATTACK_SURFACE)
                    .click_on_combo_box_in_filter(UITextElements.ATTACK_SURFACE)
                    .click_on_element_with_text(element_text=UITextElements.INDIRECTLY, nth=1)
                    .click_on_element_with_text(element_text=UITextElements.NOT_SPECIFIED, nth=1)
                    .click_on_element_with_text(UITextElements.NOT_INCLUDED)
                    .click_on_element_with_text(UITextElements.ENTERS)
                    .check_text_components_found_with_any_number()
                    .check_table_text_values(self._FIRST_STRING_VALUES_WITHOUT_FILTERS)
                )

                temp_text_components_found = (
                    self.product_version_information_page.get_text_components_found_with_any_number()
                )

                (
                    self.product_version_information_page.click_on_reset_filters_button()
                    .check_text_total_components_with_any_number()
                    .check_text(
                        page_text=temp_text_components_found[
                            self._COMPONENT_COUNT_FIRST_SYMBOL : self._COMPONENT_COUNT_LAST_SYMBOL
                        ],
                        exact=False,
                    )
                )

    @allure.suite("Паспорт версии продукта, вкладка 'Компонентный состав', фильтр 'Функция безопасности'.")
    @allure.title("Паспорт версии продукта, вкладка 'Компонентный состав', фильтр 'Функция безопасности'.")
    @allure.id("1565415")
    @allure.description("Баг: Текст 'Всего <любое число> компонент(а/ов)' не отображается на странице.")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1576539", LinkType.LINK, "TASK 1576539"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1565415", "TestCase 1565415")
    def test_product_version_passport_component_composition_tab_filter_security_function(self) -> None:
        """Паспорт версии продукта, вкладка 'Компонентный состав', фильтр 'Функция безопасности'."""
        # Паспорт версии продукта_вкладка Компонентный состав_фильтр Функция безопасности
        with allure.step(
            "1. Предусловие: Пользователь с правами редактирования и чтения паспортов продуктов и компонентов "
            "авторизован в сервисе. Открыт реестр продуктов, выбран продукт, выбрана версия продукта, открыт "
            "паспорт версии продукта на вкладке 'Компонентный состав'"
        ):
            self._setup_version_of_product_component_composition()

        with allure.step("2. Кликнуть в поле фильтра 'Функция безопасности'"):
            (
                self.product_version_information_page.click_on_funnel_icon()
                .check_combo_box_in_filter(UITextElements.SECURITY_FUNCTION)
                .click_on_combo_box_in_filter(UITextElements.SECURITY_FUNCTION)
            )

        with allure.step("3. В фильтре 'Функция безопасности' выбрать значение 'Не указана'"):
            (
                self.product_version_information_page.check_text_total_components_with_any_number()
                .click_on_element_with_text(UITextElements.NOT_SPECIFIED)
                .check_text_components_found_with_any_number()
            )

        with allure.step("4. Нажать 'Сбросить фильтр'"):
            (
                self.product_version_information_page.click_on_reset_filters_button()
                .check_combo_box_in_filter(UITextElements.SECURITY_FUNCTION)
                .check_text_total_components_with_any_number()
            )

        with allure.step(
            "5. Повторить шаги тест кейса для выбора следующих значений в фильтре 'Функция безопасности':"
        ):
            with allure.step("6. Не указана + одно из значений: Да/Косвенно/Нет"):
                list_combo_box_elements = [
                    UITextElements.NOT_SPECIFIED,
                    UITextElements.YES,
                    UITextElements.INDIRECTLY,
                    UITextElements.NO,
                ]

                (
                    self.product_version_information_page.check_combo_box_in_filter(UITextElements.SECURITY_FUNCTION)
                    .click_on_combo_box_in_filter(UITextElements.SECURITY_FUNCTION)
                    .click_on_element_with_text(UITextElements.NOT_SPECIFIED)
                    .click_on_element_with_text(UITextElements.YES)
                    .check_combo_box_list_and_text_in_filter(
                        text_in_combo_box=UITextElements.SECURITY_FUNCTION + UITextElements.COLON_SPACE_TWO,
                        list_combo_box_elements=list_combo_box_elements,
                    )
                    .check_text_components_found_with_any_number()
                )

            with allure.step("7. Значение 'Да'"):
                first_string_values = [
                    " ",
                    "libxtables12",
                    RadarAreaValues.UNKNOWN,
                    "1.8.7-1",
                    UITextElements.YES,
                    "",
                    UITextElements.NOT_SPECIFIED,
                    "",
                ]

                (
                    self.product_version_information_page.click_on_reset_filters_button()
                    .check_text_total_components_with_any_number()
                    .check_combo_box_in_filter(UITextElements.SECURITY_FUNCTION)
                    .click_on_combo_box_in_filter(UITextElements.SECURITY_FUNCTION)
                    .click_on_element_with_text(UITextElements.YES)
                    .check_checkbox_with_text_in_combo_box_in_filter(UITextElements.YES)
                    .check_text_components_found_with_any_number()
                    .check_table_headings(Lists.TITLES_TABLE_COMPONENT_COMPOSITION)
                    .check_table_text_values(first_string_values)
                )

            with allure.step("8. Значение 'Нет'"):
                (
                    self.product_version_information_page.click_on_reset_filters_button()
                    .check_text_total_components_with_any_number()
                    .check_combo_box_in_filter(UITextElements.SECURITY_FUNCTION)
                    .click_on_combo_box_in_filter(UITextElements.SECURITY_FUNCTION)
                    .click_on_element_with_text(UITextElements.NO)
                    .check_checkbox_with_text_in_combo_box_in_filter(UITextElements.NO)
                    .check_text_components_found_with_any_number()
                    .check_table_text_values(self._FIRST_STRING_VALUES)
                    .click_on_reset_filters_button()
                    .check_combo_box_in_filter(UITextElements.SECURITY_FUNCTION)
                    .click_on_combo_box_in_filter(UITextElements.SECURITY_FUNCTION)
                    .click_on_element_with_text(UITextElements.NO)
                    .check_checkbox_with_text_in_combo_box_in_filter(UITextElements.NO)
                    .click_on_element_with_text(UITextElements.YES)
                    .check_checkbox_with_text_in_combo_box_in_filter(UITextElements.YES)
                )

            with allure.step("9. Значение 'Косвенно'"):
                first_string_values = [
                    " ",
                    "libtinfo6",
                    RadarAreaValues.UNKNOWN,
                    "6.2+20201114-2+deb11u1",
                    UITextElements.INDIRECTLY,
                    "",
                    UITextElements.NOT_SPECIFIED,
                    "",
                ]

                (
                    self.product_version_information_page.click_on_reset_filters_button()
                    .check_text_total_components_with_any_number()
                    .check_combo_box_in_filter(UITextElements.SECURITY_FUNCTION)
                    .click_on_combo_box_in_filter(UITextElements.SECURITY_FUNCTION)
                    .click_on_element_with_text(UITextElements.INDIRECTLY)
                    .check_text_components_found_with_any_number()
                    .check_table_text_values(first_string_values)
                )

            with allure.step("10. 'Не указана' + 'Да' + 'Косвенно' + 'Нет'"):
                (
                    self.product_version_information_page.click_on_reset_filters_button()
                    .check_text_total_components_with_any_number()
                    .check_combo_box_in_filter(UITextElements.SECURITY_FUNCTION)
                    .click_on_combo_box_in_filter(UITextElements.SECURITY_FUNCTION)
                    .click_on_element_with_text(UITextElements.INDIRECTLY)
                    .click_on_element_with_text(UITextElements.NOT_SPECIFIED)
                    .click_on_element_with_text(UITextElements.NO)
                    .click_on_element_with_text(UITextElements.YES)
                    .check_text_components_found_with_any_number()
                    .check_table_text_values(self._FIRST_STRING_VALUES_WITHOUT_FILTERS)
                )

                temp_text_components_found = (
                    self.product_version_information_page.get_text_components_found_with_any_number()
                )

                (
                    self.product_version_information_page.click_on_reset_filters_button()
                    .check_text_total_components_with_any_number()
                    .check_text(
                        page_text=temp_text_components_found[
                            self._COMPONENT_COUNT_FIRST_SYMBOL : self._COMPONENT_COUNT_LAST_SYMBOL
                        ],
                        exact=False,
                    )
                )

    def _select_filter_value(
        self, placeholder: str, first_element: str, second_element: str, list_combo_box_elements: list[str]
    ) -> None:
        """Открыть выпадающий список и выбрать в нём элемент.

        :param placeholder: Placeholder выпадающего списка.
        :param first_element: Первый элемент в выпадающем списке.
        :param second_element: Второй элемент в выпадающем списке.
        :param list_combo_box_elements: Список элементов combobox'а.
        """
        (
            self.product_version_information_page.click_on_funnel_icon()
            .check_combo_box_in_filter(placeholder)
            .click_on_combo_box_in_filter(placeholder)
            .click_on_element_in_combo_box_in_filter(first_element)
            .click_on_element_in_combo_box_in_filter(second_element)
            .check_combo_box_list_and_text_in_filter(
                text_in_combo_box=placeholder + UITextElements.COLON_SPACE_TWO,
                list_combo_box_elements=list_combo_box_elements,
            )
        )
