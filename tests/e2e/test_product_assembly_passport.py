import allure
import pytest
from allure_commons.types import LinkType

from src.constants.agreement_values import AgreementValues
from src.constants.assemblies import Assemblies
from src.constants.components import Components
from src.constants.packages import Packages
from src.constants.products import Products
from src.constants.radar_area_values import RadarAreaValues
from src.constants.ui_text_elements import UITextElements
from src.constants.versions import Versions
from tests.base.base_test import BaseTest


@allure.parent_suite("Паспорт сборки продукта.")
@allure.epic("Паспорт сборки продукта.")
@allure.sub_suite("Паспорт сборки продукта.")
class TestProductAssemblyPassport(BaseTest):
    """Паспорт сборки продукта."""

    _PACKAGE_LIBC6 = "2.31-13+deb11u8"
    _ACPID_PACKAGE = "1:2.0.32-1"
    _TABLE_TITLES = [
        UITextElements.COMPONENT,
        UITextElements.TEXT_PACKAGE,
        UITextElements.TEXT_PROGRAMMING_LANGUAGE,
        UITextElements.COMPONENT_TYPE,
        UITextElements.AGREEMENT,
        UITextElements.TECHNICAL_RADAR_AREA,
        UITextElements.SECURITY_FUNCTION,
        UITextElements.ATTACK_SURFACE,
    ]
    _TABLE_VALUES_WITHOUT_FILTER = [
        Components.ACPID,
        _ACPID_PACKAGE,
        "",
        UITextElements.ABSENT,
        AgreementValues.CHOICE_IS_NOT_AGREED_UPON,
        RadarAreaValues.UNKNOWN,
        UITextElements.NOT_SPECIFIED,
        UITextElements.NOT_SPECIFIED,
    ]
    _TABLE_VALUES_FIRST = [
        Components.ACPID,
        _ACPID_PACKAGE,
        "Bourne ShellCC++C/C++ HeaderCUDAKotlinLuaPythonSQLSwiftBourne ShellCC++Ещё 7",
        UITextElements.ABSENT,
        AgreementValues.CHOICE_IS_NOT_AGREED_UPON,
        RadarAreaValues.UNKNOWN,
        UITextElements.NOT_SPECIFIED,
        UITextElements.NOT_SPECIFIED,
    ]
    _TABLE_VALUES_SECOND = [
        Components.LIBC6,
        _PACKAGE_LIBC6,
        "AssemblyawkBashBourne ShellCC++C/C++ HeaderKorn Shellm4PerlPHPPythonSQLAssemblyawkBashЕщё 10",
        UITextElements.ABSENT,
        AgreementValues.DEVIATION_IS_AGREED,
        RadarAreaValues.PILOTED_BY,
        UITextElements.NOT_SPECIFIED,
        UITextElements.NOT_SPECIFIED,
    ]

    @allure.suite("Паспорт сборки продукта, блок фильтра, отображение.")
    @allure.title("Паспорт сборки продукта, блок фильтра, отображение.")
    @allure.id("1521382")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1546836", LinkType.LINK, "TASK 1546836"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1521382", "TestCase 1521382")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.multiple_streams
    def test_product_assembly_passport_filter_block_display(self) -> None:
        """Паспорт сборки продукта, блок фильтра, отображение."""
        # Паспорт сборки продукта_ Блок фильтра_отображаение
        with allure.step(
            "1. Предусловие: Пользователь с правами редактирования и чтения паспортов продуктов и компонентов "
            "авторизован в сервисе. Открыт реестр продуктов, выбран продукт, выбрана версия продукта, выбрана сборка "
            "продукта, открыт паспорт сборки продукта"
        ):
            self._setup()

        with allure.step("2. Нажать на иконку в виде воронки"):
            (
                self.product_assembly_information_page.click_on_funnel_icon()
                .check_combo_box_in_filter(UITextElements.COMPONENT_TYPE)
                .check_combo_box_in_filter(UITextElements.APPROVAL_STATUS)
                .check_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)
                .check_combo_box_in_filter(UITextElements.SECURITY_FUNCTION)
                .check_combo_box_in_filter(UITextElements.ATTACK_SURFACE)
                .check_reset_filters_button()
            )

        with allure.step("3. Нажать Х (закрыть)"):
            self.product_assembly_information_page.click_on_close_filter_block_icon().check_reset_filters_button(
                visible_and_enabled=False
            )

    @allure.suite("Паспорт сборки продукта, сброс значений фильтров, обновление страницы.")
    @allure.title("Паспорт сборки продукта, сброс значений фильтров, обновление страницы.")
    @allure.id("1521390")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1547486", LinkType.LINK, "TASK 1547486"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1521390", "TestCase 1521390")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.multiple_streams
    def test_product_assembly_passport_resetting_filter_values_refresh_page(self) -> None:
        """Паспорт сборки продукта, сброс значений фильтров, обновление страницы."""
        # Паспорт сборки продукта_Сброс значений фильтров/обновление страницы
        total_components = 279
        components_found = 0

        with allure.step(
            "1. Предусловие: Пользователь с правами редактирования и чтения паспортов продуктов и компонентов "
            "авторизован в сервисе. Открыт реестр продуктов, выбран продукт, версия продукта, сборка продукта, "
            "открыт паспорт сборки продукта, открыт блок фильтра"
        ):
            self._setup()
            self.product_assembly_information_page.click_on_funnel_icon()

        with allure.step("2. В нескольких фильтрах выбрать любые значения"):
            (
                self.product_assembly_information_page.check_text_total_components(total_components)
                .check_combo_box_in_filter(UITextElements.COMPONENT_TYPE)
                .click_on_combo_box_in_filter(UITextElements.COMPONENT_TYPE)
                .click_on_element_in_combo_box_in_filter(UITextElements.EXTERNAL)
                .check_combo_box_in_filter(UITextElements.APPROVAL_STATUS)
                .click_on_combo_box_in_filter(UITextElements.APPROVAL_STATUS)
                .click_on_element_in_combo_box_in_filter(AgreementValues.CHOICE_IS_NOT_AGREED_UPON)
                .check_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)
                .click_on_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)
                .click_on_element_in_combo_box_in_filter(RadarAreaValues.UNKNOWN)
                .check_combo_box_in_filter(UITextElements.SECURITY_FUNCTION)
                .click_on_combo_box_in_filter(UITextElements.SECURITY_FUNCTION)
                .click_on_element_in_combo_box_in_filter(UITextElements.NO)
                .check_combo_box_in_filter(UITextElements.ATTACK_SURFACE)
                .click_on_combo_box_in_filter(UITextElements.ATTACK_SURFACE)
                .click_on_element_in_combo_box_in_filter(UITextElements.NOT_INCLUDED)
                .check_text_components_found(components_found)
            )

        with allure.step("3. Нажать кнопку 'Сбросить фильтр'"):
            (
                self.product_assembly_information_page.click_on_reset_filters_button()
                .check_reset_filters_button()
                .check_text_total_components(total_components)
            )

        with allure.step("4. Повторить ш.2 и обновить страницу сервиса"):
            (
                self.product_assembly_information_page.check_text_total_components(total_components)
                .check_combo_box_in_filter(UITextElements.COMPONENT_TYPE)
                .click_on_combo_box_in_filter(UITextElements.COMPONENT_TYPE)
                .click_on_element_in_combo_box_in_filter(UITextElements.EXTERNAL)
                .check_combo_box_in_filter(UITextElements.APPROVAL_STATUS)
                .click_on_combo_box_in_filter(UITextElements.APPROVAL_STATUS)
                .click_on_element_in_combo_box_in_filter(AgreementValues.CHOICE_IS_NOT_AGREED_UPON)
                .check_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)
                .click_on_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)
                .click_on_element_in_combo_box_in_filter(RadarAreaValues.UNKNOWN)
                .check_combo_box_in_filter(UITextElements.SECURITY_FUNCTION)
                .click_on_combo_box_in_filter(UITextElements.SECURITY_FUNCTION)
                .click_on_element_in_combo_box_in_filter(UITextElements.NO)
                .check_combo_box_in_filter(UITextElements.ATTACK_SURFACE)
                .click_on_combo_box_in_filter(UITextElements.ATTACK_SURFACE)
                .click_on_element_in_combo_box_in_filter(UITextElements.NOT_INCLUDED)
                .check_text_components_found(components_found)
                .refresh_page()
                .check_text_total_components(total_components)
                .check_reset_filters_button(visible_and_enabled=False)
            )

    @allure.suite("Паспорт сборки продукта, фильтр 'Тип компонента'.")
    @allure.title("Паспорт сборки продукта, фильтр 'Тип компонента'.")
    @allure.id("1521384")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1548598", LinkType.LINK, "TASK 1548598"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1521384", "TestCase 1521384")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.multiple_streams
    def test_product_assembly_passport_filter_component_type(self) -> None:
        """Паспорт сборки продукта, фильтр 'Тип компонента'."""
        # Паспорт сборки продукта_Фильтр Тип компонента
        with allure.step(
            "1. Предусловие: Открыт паспорт сборки продукта, есть используемы компоненты, список используемых "
            "компонентов отображается в виде таблицы. Открыт блок фильтра."
        ):
            self._setup()
            self.product_assembly_information_page.click_on_funnel_icon()

        with allure.step("2. Кликнуть в поле фильтра 'Тип компонента'"):
            list_combo_box_elements = [
                UITextElements.ABSENT,
                UITextElements.INTERNAL,
                UITextElements.EXTERNAL,
            ]

            (
                self.product_assembly_information_page.check_combo_box_in_filter(UITextElements.COMPONENT_TYPE)
                .click_on_combo_box_in_filter(UITextElements.COMPONENT_TYPE)
                .check_combo_box_list_and_text_in_filter(
                    text_in_combo_box=UITextElements.COMPONENT_TYPE, list_combo_box_elements=list_combo_box_elements
                )
            )

        with allure.step("3. Выбрать одно любое значение"):
            (
                self.product_assembly_information_page.check_text_total_components_with_any_number()
                .click_on_element_in_combo_box_in_filter(UITextElements.EXTERNAL)
                .check_combo_box_list_and_text_in_filter(
                    text_in_combo_box=UITextElements.COMPONENT_TYPE
                    + UITextElements.COLON_SPACE
                    + UITextElements.EXTERNAL,
                    list_combo_box_elements=list_combo_box_elements,
                )
                .check_text_components_found_with_any_number()
                .check_cross_icon()
                .check_table_headings(self._TABLE_TITLES)
                .check_table_text_values(self._TABLE_VALUES_FIRST)
            )
            temp_text_components_found = (
                self.product_assembly_information_page.get_text_components_found_with_any_number()
            )

        with allure.step("4. Вернуться в фильтр и выбрать еще одно любое значение"):
            (
                self.product_assembly_information_page.click_on_element_in_combo_box_in_filter(UITextElements.INTERNAL)
                .check_combo_box_list_and_text_in_filter(
                    text_in_combo_box=UITextElements.COMPONENT_TYPE + UITextElements.COLON_SPACE_TWO,
                    list_combo_box_elements=list_combo_box_elements,
                )
                .check_cross_icon()
                .check_table_text_values(self._TABLE_VALUES_FIRST)
                .check_text(page_text=temp_text_components_found, visible=False)
            )

        with allure.step("5. Нажать Х (очистить)"):
            (
                self.product_assembly_information_page.click_on_cross_icon()
                .check_combo_box_in_filter(UITextElements.COMPONENT_TYPE)
                .check_table_text_values(self._TABLE_VALUES_WITHOUT_FILTER)
                .check_text_total_components_with_any_number()
            )

    @allure.suite("Паспорт сборки продукта, фильтр 'Зона техрадара'.")
    @allure.title("Паспорт сборки продукта, фильтр 'Зона техрадара'.")
    @allure.id("1521386")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1548612", LinkType.LINK, "TASK 1548612"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1521386", "TestCase 1521386")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.multiple_streams
    def test_product_assembly_passport_filter_technical_radar_area(self) -> None:
        """Паспорт сборки продукта, фильтр 'Зона техрадара'."""
        # Паспорт сборки продукта_Фильтр Зона техрадара
        with allure.step(
            "1. Предусловие: Открыт паспорт сборки продукта, есть используемые компоненты, список используемых "
            "компонентов отображается в виде таблицы. Открыт блок фильтра."
        ):
            self._setup()
            self.product_assembly_information_page.click_on_funnel_icon()

        with allure.step("2. Кликнуть в поле фильтра 'Зона техрадара'"):
            list_combo_box_elements = [
                RadarAreaValues.RECOMMENDED,
                RadarAreaValues.PILOTED_BY,
                RadarAreaValues.INTERESTED_IN,
                RadarAreaValues.AVOID,
                RadarAreaValues.UNKNOWN,
            ]

            (
                self.product_assembly_information_page.check_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)
                .click_on_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)
                .check_combo_box_list_and_text_in_filter(
                    text_in_combo_box=UITextElements.TECHNICAL_RADAR_AREA,
                    list_combo_box_elements=list_combo_box_elements,
                )
            )

        with allure.step("3. Выбрать одно любое значение"):
            (
                self.product_assembly_information_page.check_text_total_components_with_any_number()
                .click_on_element_in_combo_box_in_filter(RadarAreaValues.PILOTED_BY)
                .check_combo_box_list_and_text_in_filter(
                    text_in_combo_box=UITextElements.TECHNICAL_RADAR_AREA
                    + UITextElements.COLON_SPACE
                    + RadarAreaValues.PILOTED_BY,
                    list_combo_box_elements=list_combo_box_elements,
                )
                .check_text_components_found_with_any_number()
                .check_cross_icon()
                .check_table_headings(self._TABLE_TITLES)
                .check_table_text_values(self._TABLE_VALUES_SECOND)
            )
            temp_text_components_found = (
                self.product_assembly_information_page.get_text_components_found_with_any_number()
            )

        with allure.step("4. Вернуться в фильтр и выбрать еще несколько любых значений"):
            table_values = [
                Components.BASH,
                Packages.BASH,
                "",
                UITextElements.ABSENT,
                AgreementValues.NOT_REQUIRED,
                RadarAreaValues.RECOMMENDED,
                UITextElements.NOT_SPECIFIED,
                UITextElements.NOT_SPECIFIED,
            ]

            (
                self.product_assembly_information_page.click_on_element_in_combo_box_in_filter(
                    RadarAreaValues.RECOMMENDED
                )
                .check_combo_box_list_and_text_in_filter(
                    text_in_combo_box=UITextElements.TECHNICAL_RADAR_AREA + UITextElements.COLON_SPACE_TWO,
                    list_combo_box_elements=list_combo_box_elements,
                )
                .check_cross_icon()
                .check_table_text_values(table_values)
                .check_text(page_text=temp_text_components_found, visible=False)
            )

        with allure.step("5. Нажать Х (очистить)"):
            (
                self.product_assembly_information_page.click_on_cross_icon()
                .check_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)
                .check_table_text_values(self._TABLE_VALUES_WITHOUT_FILTER)
                .check_text_total_components_with_any_number()
            )

    @allure.suite("Паспорт сборки продукта, фильтр 'Функция безопасности'.")
    @allure.title("Паспорт сборки продукта, фильтр 'Функция безопасности'.")
    @allure.id("1521387")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1549556", LinkType.LINK, "TASK 1549556"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1521387", "TestCase 1521387")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.multiple_streams
    def test_product_assembly_passport_filter_security_function(self) -> None:
        """Паспорт сборки продукта, фильтр 'Функция безопасности'."""
        # Паспорт сборки продукта_Фильтр Функция безопасности
        with allure.step(
            "1. Предусловие: Открыт паспорт сборки продукта, есть используемые компоненты, список используемых "
            "компонентов отображается в виде таблицы. Открыт блок фильтра."
        ):
            self._setup()
            self.product_assembly_information_page.click_on_funnel_icon()

        with allure.step("2. Кликнуть в поле фильтра 'Функция безопасности'"):
            list_combo_box_elements = [
                UITextElements.NOT_SPECIFIED,
                UITextElements.YES,
                UITextElements.INDIRECTLY,
                UITextElements.NO,
            ]

            (
                self.product_assembly_information_page.check_combo_box_in_filter(UITextElements.SECURITY_FUNCTION)
                .click_on_combo_box_in_filter(UITextElements.SECURITY_FUNCTION)
                .check_combo_box_list_and_text_in_filter(
                    text_in_combo_box=UITextElements.SECURITY_FUNCTION, list_combo_box_elements=list_combo_box_elements
                )
            )

        with allure.step("3. Выбрать значение 'Не указана'"):
            table_values = [
                Components.ACPID,
                self._ACPID_PACKAGE,
                "Bourne ShellCC++C/C++ HeaderCUDAKotlinLuaPythonSQLSwiftBourne ShellCC++Ещё 7",
                UITextElements.ABSENT,
                AgreementValues.CHOICE_IS_AGREED,
                RadarAreaValues.UNKNOWN,
                UITextElements.NOT_SPECIFIED,
                UITextElements.NOT_SPECIFIED,
            ]

            (
                self.product_assembly_information_page.check_text_total_components_with_any_number()
                .click_on_element_in_combo_box_in_filter(UITextElements.NOT_SPECIFIED)
                .check_combo_box_list_and_text_in_filter(
                    text_in_combo_box=UITextElements.SECURITY_FUNCTION
                    + UITextElements.COLON_SPACE
                    + UITextElements.NOT_SPECIFIED,
                    list_combo_box_elements=list_combo_box_elements,
                )
                .check_text_components_found_with_any_number()
                .check_cross_icon()
                .check_table_headings(self._TABLE_TITLES)
                .check_table_text_values(table_values)
            )
            temp_text_components_found = (
                self.product_assembly_information_page.get_text_components_found_with_any_number()
            )

        with allure.step("4. Вернуться в фильтр и выбрать еще несколько значений"):
            (
                self.product_assembly_information_page.click_on_element_in_combo_box_in_filter(UITextElements.YES)
                .check_combo_box_list_and_text_in_filter(
                    text_in_combo_box=UITextElements.SECURITY_FUNCTION + UITextElements.COLON_SPACE_TWO,
                    list_combo_box_elements=list_combo_box_elements,
                )
                .check_cross_icon()
                .check_table_text_values(table_values)
                .check_text(page_text=temp_text_components_found, visible=False)
            )

        with allure.step("5. Нажать Х (очистить)"):
            (
                self.product_assembly_information_page.click_on_cross_icon()
                .check_combo_box_in_filter(UITextElements.SECURITY_FUNCTION)
                .check_table_text_values(self._TABLE_VALUES_WITHOUT_FILTER)
                .check_text_total_components_with_any_number()
            )

    @allure.suite("Паспорт сборки продукта, фильтр 'Поверхность атаки'.")
    @allure.title("Паспорт сборки продукта, фильтр 'Поверхность атаки'.")
    @allure.id("1521388")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1549562", LinkType.LINK, "TASK 1549562"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1521388", "TestCase 1521388")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.multiple_streams
    def test_product_assembly_passport_filter_attack_surface(self) -> None:
        """Паспорт сборки продукта, фильтр 'Поверхность атаки'."""
        # Паспорт сборки продукта_Фильтр Поверхность атаки
        with allure.step(
            "1. Предусловие: Открыт паспорт сборки продукта, есть используемые компоненты, список используемых "
            "компонентов отображается в виде таблицы. Открыт блок фильтра."
        ):
            self._setup()
            self.product_assembly_information_page.click_on_funnel_icon()

        with allure.step("2. Кликнуть в поле 'Поверхность атаки'"):
            list_combo_box_elements = [
                UITextElements.NOT_SPECIFIED,
                UITextElements.NOT_INCLUDED,
                UITextElements.INDIRECTLY,
                UITextElements.ENTERS,
            ]

            (
                self.product_assembly_information_page.check_combo_box_in_filter(UITextElements.ATTACK_SURFACE)
                .click_on_combo_box_in_filter(UITextElements.ATTACK_SURFACE)
                .check_combo_box_list_and_text_in_filter(
                    text_in_combo_box=UITextElements.ATTACK_SURFACE, list_combo_box_elements=list_combo_box_elements
                )
            )

        with allure.step("3. Выбрать значение 'Не указана'"):
            table_values = [
                Components.ACPID,
                self._ACPID_PACKAGE,
                "Bourne ShellCC++C/C++ HeaderCUDAKotlinLuaPythonSQLSwiftBourne ShellCC++Ещё 7",
                UITextElements.ABSENT,
                AgreementValues.CHOICE_IS_AGREED,
                RadarAreaValues.UNKNOWN,
                UITextElements.NOT_SPECIFIED,
                UITextElements.NOT_SPECIFIED,
            ]

            (
                self.product_assembly_information_page.check_text_total_components_with_any_number()
                .click_on_element_in_combo_box_in_filter(element_name=UITextElements.NOT_SPECIFIED, nth=1)
                .check_combo_box_list_and_text_in_filter(
                    text_in_combo_box=UITextElements.ATTACK_SURFACE
                    + UITextElements.COLON_SPACE
                    + UITextElements.NOT_SPECIFIED,
                    list_combo_box_elements=list_combo_box_elements,
                )
                .check_text_components_found_with_any_number()
                .check_cross_icon()
                .check_table_headings(self._TABLE_TITLES)
                .check_table_text_values(table_values)
            )
            temp_text_components_found = (
                self.product_assembly_information_page.get_text_components_found_with_any_number()
            )

        with allure.step("4. Вернуться в фильтр и выбрать еще несколько значений"):
            (
                self.product_assembly_information_page.click_on_element_in_combo_box_in_filter(UITextElements.ENTERS)
                .click_on_element_in_combo_box_in_filter(UITextElements.NOT_INCLUDED)
                .check_combo_box_list_and_text_in_filter(
                    text_in_combo_box=UITextElements.ATTACK_SURFACE + UITextElements.COLON_SPACE + "3",
                    list_combo_box_elements=list_combo_box_elements,
                )
                .check_cross_icon()
                .check_text(page_text=temp_text_components_found, visible=False)
            )

        with allure.step("5. Нажать Х (очистить)"):
            (
                self.product_assembly_information_page.click_on_cross_icon()
                .check_combo_box_in_filter(UITextElements.ATTACK_SURFACE)
                .check_table_text_values(self._TABLE_VALUES_WITHOUT_FILTER)
                .check_text_total_components_with_any_number()
            )

    @allure.suite("Паспорт сборки продукта, фильтр 'Верифицированная версия'.")
    @allure.title("Паспорт сборки продукта, фильтр 'Верифицированная версия'.")
    @allure.id("1565430")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1570262", LinkType.LINK, "TASK 1570262"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1565430", "TestCase 1565430")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.multiple_streams
    def test_product_assembly_passport_filter_verified_version(self) -> None:
        """Паспорт сборки продукта, фильтр 'Верифицированная версия'."""
        # Паспорт сборки продукта_фильтр Верифицированная версия
        with allure.step(
            "1. Предусловие: Пользователь с правами на чтение паспортов компонентов и продуктов авторизован в сервисе. "
            "Открыт паспорт сборки продукта, открыт блок фильтров"
        ):
            self._impersonate_as_user_with_read_or_write_permissions(write_permissions=False)
            self._setup()
            self.product_assembly_information_page.click_on_funnel_icon()

        with allure.step("2. В фильтре 'Верифицированная версия' нажать на экспандер"):
            (
                self.product_assembly_information_page.check_reset_filters_button()
                .check_combo_box_in_filter(UITextElements.VERIFIED_VERSION)
                .click_on_combo_box_in_filter(UITextElements.VERIFIED_VERSION)
            )

        with allure.step("3. В фильтре 'Верифицированная версия' выбрать значение 'Да'"):
            (
                self.product_assembly_information_page.click_on_element_with_text(
                    element_text=UITextElements.YES, nth=1
                )
                .check_text(page_text=UITextElements.VERIFIED_VERSION + UITextElements.COLON_SPACE + UITextElements.YES)
                .check_cross_icon()
                .hover_cursor_over_check_mark(nth=0)
                .hover_cursor_over_check_mark(nth=1)
            )

        with allure.step("4. В фильтре 'Верифицированная версия' выбрать значение 'Нет'"):
            (
                self.product_assembly_information_page.refresh_page()
                .click_on_funnel_icon()
                .check_combo_box_in_filter(UITextElements.VERIFIED_VERSION)
                .click_on_combo_box_in_filter(UITextElements.VERIFIED_VERSION)
                .click_on_element_with_text(element_text=UITextElements.NO, nth=1)
                .check_text(page_text=UITextElements.VERIFIED_VERSION + UITextElements.COLON_SPACE + UITextElements.NO)
                .check_cross_icon(visible=True)
                .hover_cursor_over_check_mark(visible=False)
            )

        with allure.step("5. Нажать Х (очистить)"):
            (
                self.product_assembly_information_page.click_on_cross_icon()
                .check_combo_box_in_filter(UITextElements.VERIFIED_VERSION)
                .check_text_total_components_with_any_number()
            )

    @allure.suite("Паспорт сборки продукта, фильтр 'Ссылки'.")
    @allure.title("Паспорт сборки продукта, фильтр 'Ссылки'.")
    @allure.id("1565431")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1571124", LinkType.LINK, "TASK 1571124"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1565431", "TestCase 1565431")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.multiple_streams
    def test_product_assembly_passport_filter_links(self) -> None:
        """Паспорт сборки продукта, фильтр 'Ссылки'."""
        # Паспорт сборки продукта_фильтр Сссылки
        there_are_links_to_source_code = "Есть ссылки на исходный код"
        no_links_to_source_code = "Нет ссылок на исходный код"

        with allure.step(
            "1. Предусловие: Пользователь с правами на чтение паспортов компонентов и продуктов авторизован в сервисе. "
            "Открыт паспорт сборки продукта, открыт блок фильтра"
        ):
            self._impersonate_as_user_with_read_or_write_permissions(write_permissions=False)
            self._setup()
            self.product_assembly_information_page.click_on_funnel_icon()

        with allure.step("2. В фильтре 'Ссылки' выбрать значение 'Есть ссылки на исходный код'"):
            (
                self.product_assembly_information_page.check_reset_filters_button()
                .check_combo_box_in_filter(UITextElements.LINKS)
                .click_on_combo_box_in_filter(UITextElements.LINKS)
                .click_on_element_with_text(there_are_links_to_source_code)
                .check_text(
                    page_text=UITextElements.LINKS + UITextElements.COLON_SPACE + there_are_links_to_source_code
                )
                .check_cross_icon()
                .hover_cursor_over_first_link_icon()
                .check_text(UITextElements.ALL_LINKS_HAVE_BEEN_ADDED_TO_PACKAGE)
                .check_links_count(link_text=self._ACPID_PACKAGE, count=1)
                .check_links_count(link_text=Packages.ACPI_SUPPORT_BASE, count=1)
                .check_links_count(link_text="11.1+deb11u9", count=1)
                .check_links_count(link_text="5.1-2+deb11u1", count=1)
            )

        with allure.step("3. В фильтре 'Ссылки' выбрать значение 'Нет ссылок на исходный код'"):
            (
                self.product_assembly_information_page.refresh_page()
                .click_on_funnel_icon()
                .check_combo_box_in_filter(UITextElements.LINKS)
                .click_on_combo_box_in_filter(UITextElements.LINKS)
                .click_on_element_with_text(no_links_to_source_code)
                .check_text(page_text=UITextElements.LINKS + UITextElements.COLON_SPACE + no_links_to_source_code)
                .check_cross_icon()
                .check_visibility_first_link_icon(visible=False)
                .check_links_count(link_text="2.6.0-2", count=1)
                .check_links_count(link_text="1:9.16.50-1~deb11u2", count=6)
            )

    @allure.suite("Паспорт сборки продукта, фильтр 'Статус согласования'.")
    @allure.title("Паспорт сборки продукта, фильтр 'Статус согласования'.")
    @allure.id("1565421")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1575902", LinkType.LINK, "TASK 1575902"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1565421", "TestCase 1565421")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.multiple_streams
    def test_product_assembly_passport_filter_approval_status(self) -> None:
        """Паспорт сборки продукта, фильтр 'Статус согласования'."""
        # Паспорт сборки продукта_Фильтр Статус согласования
        with allure.step(
            "1. Предусловие: Открыт паспорт сборки продукта, есть используемые компоненты, список используемых "
            "компонентов отображается в виде таблицы. Открыт блок фильтра."
        ):
            self._setup()
            self.product_assembly_information_page.click_on_funnel_icon()

        with allure.step("2. Кликнуть в поле фильтра 'Статус согласования'"):
            (
                self.product_assembly_information_page.check_reset_filters_button()
                .check_combo_box_in_filter(UITextElements.APPROVAL_STATUS)
                .click_on_combo_box_in_filter(UITextElements.APPROVAL_STATUS)
            )

        with allure.step("3. Выбрать одно любое значение"):
            (
                self.product_assembly_information_page.check_text_total_components_with_any_number()
                .click_on_element_with_text(AgreementValues.DEVIATION_IS_AGREED)
                .check_checkbox_deviation_is_agreed()
                .check_text_components_found_with_any_number()
                .check_combo_box_list_and_text_in_filter(
                    text_in_combo_box=UITextElements.APPROVAL_STATUS
                    + UITextElements.COLON_SPACE
                    + AgreementValues.DEVIATION_IS_AGREED,
                    list_combo_box_elements=AgreementValues,
                )
                .check_cross_icon()
                .check_table_headings(self._TABLE_TITLES)
                .check_table_text_values(self._TABLE_VALUES_SECOND)
            )

        with allure.step("4. Выбрать в фильтре еще одно любое значение"):
            (
                self.product_assembly_information_page.click_on_element_with_text(
                    AgreementValues.CHOICE_IS_NOT_AGREED_UPON
                )
                .check_combo_box_list_and_text_in_filter(
                    text_in_combo_box=UITextElements.APPROVAL_STATUS + UITextElements.COLON_SPACE_TWO,
                    list_combo_box_elements=AgreementValues,
                )
                .check_cross_icon()
                .check_table_text_values(self._TABLE_VALUES_FIRST)
            )

        with allure.step(
            "5. Выбрать значение отличное от текущих (снять галки со старых значений, установить на новом значении)"
        ):
            table_values = [
                Components.BZIP2,
                "1.0.8-4",
                "Bourne ShellCC/C++ HeaderPerlBourne ShellCC/C++ HeaderЕщё 1",
                UITextElements.ABSENT,
                AgreementValues.DEVIATION_IS_NOT_AGREED_UPON,
                RadarAreaValues.INTERESTED_IN,
                UITextElements.NOT_SPECIFIED,
                UITextElements.NOT_SPECIFIED,
            ]

            (
                self.product_assembly_information_page.click_on_reset_filters_button()
                .check_combo_box_in_filter(UITextElements.APPROVAL_STATUS)
                .click_on_combo_box_in_filter(UITextElements.APPROVAL_STATUS)
                .click_on_element_with_text(AgreementValues.DEVIATION_IS_NOT_AGREED_UPON)
                .check_text(
                    page_text=UITextElements.APPROVAL_STATUS
                    + UITextElements.COLON_SPACE
                    + AgreementValues.DEVIATION_IS_NOT_AGREED_UPON
                )
                .check_cross_icon()
                .check_table_text_values(table_values)
            )

        with allure.step("6. Нажать Х (очистить)"):
            (
                self.product_assembly_information_page.click_on_cross_icon()
                .check_combo_box_in_filter(UITextElements.APPROVAL_STATUS)
                .check_text_total_components_with_any_number()
                .check_table_text_values(self._TABLE_VALUES_WITHOUT_FILTER)
            )

        with allure.step(
            "7. Повторить шаги тест-кейса для фильтрации по каждому статусу согласования и фильтрации по нескольким "
            "статусам одновременно"
        ):
            (
                self.product_assembly_information_page.click_on_element_with_text(
                    AgreementValues.CHOICE_IS_NOT_AGREED_UPON
                )
                .click_on_reset_filters_button()
                .check_combo_box_in_filter(UITextElements.APPROVAL_STATUS)
                .click_on_combo_box_in_filter(UITextElements.APPROVAL_STATUS)
                .click_on_element_with_text(AgreementValues.CHOICE_IS_AGREED)
                .click_on_reset_filters_button()
                .check_combo_box_in_filter(UITextElements.APPROVAL_STATUS)
                .click_on_combo_box_in_filter(UITextElements.APPROVAL_STATUS)
                .click_on_element_with_text(AgreementValues.NOT_REQUIRED)
                .click_on_reset_filters_button()
                .check_combo_box_in_filter(UITextElements.APPROVAL_STATUS)
                .click_on_combo_box_in_filter(UITextElements.APPROVAL_STATUS)
                .click_on_element_with_text(AgreementValues.CHOICE_IS_AGREED)
                .click_on_element_with_text(AgreementValues.NOT_REQUIRED)
            )

    def _setup(self) -> None:
        """Предусловие: открыть паспорт сборки продукта."""
        self.component_page.click_on_link_products()
        self.product_page.click_on_link(UITextElements.ALL_PRODUCTS).click_on_link(Products.COORDINATOR_HW_5)
        self.product_information_page.click_on_link(UITextElements.VERSIONS_TAB).click_on_link(
            Versions.COORDINATOR_HW_5
        )
        self.product_version_information_page.click_on_link(Assemblies.COORDINATOR_HW_5)
