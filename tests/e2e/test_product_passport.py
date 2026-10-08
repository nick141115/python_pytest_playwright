import allure
import pytest
from allure_commons.types import LinkType

from src.constants.agreement_values import AgreementValues
from src.constants.assemblies import Assemblies
from src.constants.components import Components
from src.constants.lists import Lists
from src.constants.products import Products
from src.constants.radar_area_values import RadarAreaValues
from src.constants.regular_expressions import RegularExpressions
from src.constants.ui_text_elements import UITextElements
from src.constants.versions import Versions
from tests.base.base_test import BaseTest


@allure.parent_suite("Паспорт продукта.")
@allure.epic("Паспорт продукта.")
@allure.sub_suite("Паспорт продукта.")
@allure.severity(allure.severity_level.NORMAL)
class TestProductPassport(BaseTest):
    """Паспорт продукта."""

    _APPROVAL_CHANGED_SUCCESSFULLY = "Согласование успешно изменено"

    _TITLES = [
        " ",
        UITextElements.COMPONENT,
        UITextElements.TECHNICAL_RADAR_AREA,
        UITextElements.AGREEMENT,
        "Обоснование/Комментарий",
    ]

    @pytest.fixture
    def clear_comment_and_checkbox(self) -> None:
        """Фикстура для очистки комментария и checkbox'а."""
        yield

        with allure.step("Возвращаем стенд к первоначальному состоянию"):
            with allure.step(
                "Пользователь с правами на чтение и редактирование паспортов продуктов авторизован в сервисе, "
                "открыт паспорт продукта на вкладке 'Компонентный состав'"
            ):
                self._impersonate_as_user_with_read_or_write_permissions(write_permissions=True)
                self.component_page.click_on_link_products()
                self.product_page.click_on_link(UITextElements.ALL_PRODUCTS).click_on_link(Products.COORDINATOR_HW_5)
                self.product_information_page.click_on_link(UITextElements.COMPONENT_COMPOSITION)

            with allure.step("Нажать 'Редактировать'"):
                self.product_information_page.click_on_element_with_text(UITextElements.EDIT)

            with allure.step("Убрать галку в чек-боксе 'Согласование'"):
                (
                    self.product_information_page.click_on_funnel_icon()
                    .click_on_combo_box_in_filter(UITextElements.APPROVAL_STATUS)
                    .click_on_element_with_text(AgreementValues.CHOICE_IS_AGREED)
                    .click_on_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)
                    .click_on_element_with_text(RadarAreaValues.UNKNOWN)
                    .click_on_element_with_text(element_text=UITextElements.AGREEMENT, nth=1)
                )

            with allure.step("В поле 'Обоснование/Комментарий' очистить комментарий"):
                self.product_information_page.fill_in_textarea_justification_comment("")

            with allure.step("Нажать 'Сохранить'"):
                self.product_information_page.click_on_icon_floppy_disk()

            with allure.step("Нажать 'Да'"):
                (
                    self.product_information_page.click_on_element_with_text(UITextElements.YES)
                    .check_text(self._APPROVAL_CHANGED_SUCCESSFULLY)
                    .check_text(RegularExpressions.PATTERN_STRING_TIME)
                    .check_visibility_close_message_icon()
                )

    @allure.suite("Паспорт продукта, вкладка 'Компонентный состав', отображение фильтра.")
    @allure.title("Паспорт продукта, вкладка 'Компонентный состав', отображение фильтра.")
    @allure.id("1521367")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1546051", LinkType.LINK, "TASK 1546051"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1521367", "TestCase 1521367")
    @pytest.mark.multiple_streams
    def test_product_passport_component_composition_tab_display_filter(self) -> None:
        """Паспорт продукта, вкладка 'Компонентный состав', отображение фильтра."""
        # Паспорт продукта_вкладка Компонентный состав_отображаение фильтра
        with allure.step(
            "1. Предусловие: Пользователь с правами редактирования и чтения паспортов продуктов и компонентов "
            "авторизован в сервисе. Открыт реестр продуктов, выбран продукт и открыт его паспорт на вкладке "
            "'Компонентный состав'"
        ):
            self._setup()

        with allure.step("2. Нажать на иконку в виде воронки"):
            (
                self.product_information_page.click_on_funnel_icon()
                .check_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)
                .check_combo_box_in_filter(UITextElements.APPROVAL_STATUS)
                .check_reset_filters_button()
            )

        with allure.step("3. Нажать Х (закрыть)"):
            self.product_information_page.click_on_close_filter_block_icon().check_reset_filters_button(
                visible_and_enabled=False
            )

    @allure.suite("Паспорт продукта, вкладка 'Компонентный состав', сброс значений фильтров, обновление страницы.")
    @allure.title("Паспорт продукта, вкладка 'Компонентный состав', сброс значений фильтров, обновление страницы.")
    @allure.id("1521373")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1546060", LinkType.LINK, "TASK 1546060"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1521373", "TestCase 1521373")
    @pytest.mark.multiple_streams
    def test_product_passport_component_composition_tab_resetting_filter_values_refresh_page(self) -> None:
        """Паспорт продукта, вкладка 'Компонентный состав', сброс значений фильтров, обновление страницы."""
        # Паспорт продукта_вкладка Компонентный состав_Сброс значений фильтров_ обновление страницы
        with allure.step(
            "1. Предусловие: Пользователь с правами редактирования и чтения паспортов продуктов и компонентов "
            "авторизован в сервисе. Открыт реестр продуктов, выбран продукт и открыт его паспорт на вкладке "
            "'Компонентный состав', открыт блок фильтра"
        ):
            self._setup()
            self.product_information_page.click_on_funnel_icon()

        with allure.step("2. В фильтрах 'Зона техрадара' и 'Статус согласования' выбрать любые значения"):
            (
                self.product_information_page.check_text_total_components_with_any_number()
                .check_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)
                .click_on_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)
                .click_on_element_in_combo_box_in_filter(RadarAreaValues.AVOID)
                .check_combo_box_in_filter(UITextElements.APPROVAL_STATUS)
                .click_on_combo_box_in_filter(UITextElements.APPROVAL_STATUS)
                .click_on_element_in_combo_box_in_filter(AgreementValues.DEVIATION_IS_NOT_AGREED_UPON)
                .check_text_components_found_with_any_number()
            )

        with allure.step("3. Нажать 'Сбросить фильтр'"):
            (
                self.product_information_page.click_on_reset_filters_button()
                .check_reset_filters_button()
                .check_text_total_components_with_any_number()
            )

        with allure.step("4. Повторить шаг 2 текущего тест-кейса"):
            (
                self.product_information_page.check_text_total_components_with_any_number()
                .check_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)
                .click_on_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)
                .click_on_element_in_combo_box_in_filter(RadarAreaValues.AVOID)
                .check_combo_box_in_filter(UITextElements.APPROVAL_STATUS)
                .click_on_combo_box_in_filter(UITextElements.APPROVAL_STATUS)
                .click_on_element_in_combo_box_in_filter(AgreementValues.DEVIATION_IS_NOT_AGREED_UPON)
                .check_text_components_found_with_any_number()
            )

        with allure.step("5. Обновить страницу сервиса"):
            (
                self.product_information_page.refresh_page()
                .check_text_total_components_with_any_number()
                .check_reset_filters_button(visible_and_enabled=False)
            )

    @allure.suite("Паспорт продукта, вкладка 'Компонентный состав', фильтр 'Статус согласования', отображение.")
    @allure.title("Паспорт продукта, вкладка 'Компонентный состав', фильтр 'Статус согласования', отображение.")
    @allure.id("1521369")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1547495", LinkType.LINK, "TASK 1547495"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1521369", "TestCase 1521369")
    @pytest.mark.multiple_streams
    def test_product_passport_component_composition_tab_filter_approval_status_display(self) -> None:
        """Паспорт продукта, вкладка 'Компонентный состав', фильтр 'Статус согласования', отображение."""
        # Паспорт продукта_вкладка Компонентный состав_фильтр Статус согласования_ отображение
        with allure.step(
            "1. Предусловие: Пользователь с правами редактирования и чтения паспортов продуктов и компонентов "
            "авторизован в сервисе. Открыт реестр продуктов, выбран продукт и открыт его паспорт на вкладке "
            "'Компонентный состав', открыт блок фильтра"
        ):
            self._setup()
            self.product_information_page.click_on_funnel_icon()

        with allure.step("2. Кликнуть в поле фильтра 'Статус согласования'"):
            (
                self.product_information_page.check_combo_box_in_filter(UITextElements.APPROVAL_STATUS)
                .click_on_combo_box_in_filter(UITextElements.APPROVAL_STATUS)
                .click_on_element_in_combo_box_in_filter(AgreementValues.DEVIATION_IS_NOT_AGREED_UPON)
                .click_on_element_in_combo_box_in_filter(AgreementValues.CHOICE_IS_NOT_AGREED_UPON)
                .check_combo_box_list_and_text_in_filter(
                    text_in_combo_box=UITextElements.APPROVAL_STATUS + UITextElements.COLON_SPACE_TWO,
                    list_combo_box_elements=AgreementValues,
                )
            )

    @allure.suite("Паспорт продукта, вкладка 'Компонентный состав', фильтр 'Зона техрадара', отображение.")
    @allure.title("Паспорт продукта, вкладка 'Компонентный состав', фильтр 'Зона техрадара', отображение.")
    @allure.id("1521368")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1548076", LinkType.LINK, "TASK 1548076"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1521368", "TestCase 1521368")
    @pytest.mark.multiple_streams
    def test_product_passport_component_composition_tab_filter_technical_radar_area_display(self) -> None:
        """Паспорт продукта, вкладка 'Компонентный состав', фильтр 'Зона техрадара', отображение."""
        # Паспорт продукта_вкладка Компонентный состав_фильтр Зона техрадара_отображаение
        with allure.step(
            "1. Предусловие: Пользователь с правами редактирования и чтения паспортов продуктов и компонентов "
            "авторизован в сервисе. Открыт реестр продуктов, выбран продукт и открыт его паспорт на вкладке "
            "'Компонентный состав', открыт блок фильтра"
        ):
            self._setup()
            self.product_information_page.click_on_funnel_icon()

        with allure.step("2. Кликнуть в поле фильтра 'Зона техрадара'"):
            (
                self.product_information_page.check_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)
                .click_on_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)
                .click_on_element_in_combo_box_in_filter(RadarAreaValues.AVOID)
                .click_on_element_in_combo_box_in_filter(RadarAreaValues.UNKNOWN)
                .check_combo_box_list_and_text_in_filter(
                    text_in_combo_box=UITextElements.TECHNICAL_RADAR_AREA + UITextElements.COLON_SPACE_TWO,
                    list_combo_box_elements=RadarAreaValues,
                )
            )

    @allure.suite("Фильтр 'Компонентный состав', паспорт продукта, вкладка 'Версии'.")
    @allure.title("Фильтр 'Компонентный состав', паспорт продукта, вкладка 'Версии'.")
    @allure.id("1560297")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1562330", LinkType.LINK, "TASK 1562330"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1560297", "TestCase 1560297")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.multiple_streams
    def test_product_passport_filter_component_composition_versions_tab(self) -> None:
        """Фильтр 'Компонентный состав', паспорт продукта, вкладка 'Версии'."""
        # Фильтр Компонентный состав_ паспорт продукта, вкладка Версии
        with allure.step(
            "1. Пользователь авторизован в сервисе АР, открыт паспорт продукта → вкладка 'Версии', открыт блок фильтра"
        ):
            self.component_page.click_on_link_products()
            self.product_page.click_on_link(UITextElements.ALL_PRODUCTS).click_on_link(Products.COORDINATOR_HW_5)
            (
                self.product_information_page.click_on_link(UITextElements.VERSIONS_TAB)
                .click_on_funnel_icon()
                .check_reset_filters_button()
            )

        with allure.step("2. Кликнуть по фильтру 'Компонентный состав'"):
            self.product_information_page.check_combo_box_in_filter(
                UITextElements.COMPONENT_COMPOSITION
            ).click_on_combo_box_in_filter(UITextElements.COMPONENT_COMPOSITION)

        with allure.step("3. Выбрать значение 'Файлы обработаны'"):
            title = [UITextElements.TEXT_VERSION]
            value = [Versions.FIVE_FIVE_ZERO]

            (
                self.product_information_page.click_on_element_with_text(UITextElements.FILES_PROCESSED)
                .check_text(
                    page_text=UITextElements.COMPONENT_COMPOSITION
                    + UITextElements.COLON_SPACE
                    + UITextElements.FILES_PROCESSED
                )
                .check_text_versions_found_with_any_number()
                .check_table_headings(title)
                .check_table_text_values(value)
            )

        with allure.step("4. Выбрать значение 'Ошибка обработки файлов'"):
            value = [
                Versions.FIVE_ONE_ZERO,
            ]
            (
                self.product_information_page.click_on_cross_icon()
                .check_text_total_versions_with_any_number()
                .check_combo_box_in_filter(UITextElements.COMPONENT_COMPOSITION)
                .click_on_combo_box_in_filter(UITextElements.COMPONENT_COMPOSITION)
                .click_on_element_with_text(UITextElements.FILE_PROCESSING_ERROR)
                .check_text(
                    page_text=UITextElements.COMPONENT_COMPOSITION
                    + UITextElements.COLON_SPACE
                    + UITextElements.FILE_PROCESSING_ERROR
                )
                .check_text_versions_found_with_any_number()
                .check_table_text_values(value)
            )

        with allure.step("5. Нажать Х"):
            (
                self.product_information_page.click_on_cross_icon()
                .check_combo_box_in_filter(UITextElements.COMPONENT_COMPOSITION)
                .check_text_total_versions_with_any_number()
            )

    @allure.suite("Паспорт продукта, вкладка 'Компонентный состав', фильтр 'Статус согласования'.")
    @allure.title("Паспорт продукта, вкладка 'Компонентный состав', фильтр 'Статус согласования'.")
    @allure.id("1565412")
    @allure.description("Баг: Текст 'Всего <любое число> компонент(а/ов)' не отображается на странице.")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1571131", LinkType.LINK, "TASK 1571131"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1565412", "TestCase 1565412")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.multiple_streams
    def test_product_passport_component_composition_tab_filter_approval_status(self) -> None:
        """Паспорт продукта, вкладка 'Компонентный состав', фильтр 'Статус согласования'."""
        # Паспорт продукта_вкладка Компоненты_фильтр Статус согласования
        with allure.step(
            "1. Предусловие: Пользователь с правами редактирования и чтения паспортов продуктов и компонентов "
            "авторизован в сервисе. Открыт реестр продуктов, выбран продукт и открыт его паспорт на вкладке "
            "'Компонентный состав', открыт блок фильтра"
        ):
            self._setup()
            self.product_information_page.click_on_funnel_icon()

        with allure.step("2. В фильтре 'Статус согласования' нажать на экспандер"):
            (
                self.product_information_page.check_combo_box_in_filter(UITextElements.APPROVAL_STATUS)
                .click_on_combo_box_in_filter(UITextElements.APPROVAL_STATUS)
                .click_on_element_in_combo_box_in_filter(AgreementValues.DEVIATION_IS_NOT_AGREED_UPON)
                .click_on_element_in_combo_box_in_filter(AgreementValues.CHOICE_IS_NOT_AGREED_UPON)
                .check_combo_box_list_and_text_in_filter(
                    text_in_combo_box=UITextElements.APPROVAL_STATUS + UITextElements.COLON_SPACE_TWO,
                    list_combo_box_elements=AgreementValues,
                )
            )

        with allure.step("3. В фильтре 'Статус согласования' выбрать одно любое значение"):
            (
                self.product_information_page.click_on_reset_filters_button()
                .check_text_total_components_with_any_number()
                .check_combo_box_in_filter(UITextElements.APPROVAL_STATUS)
                .click_on_combo_box_in_filter(UITextElements.APPROVAL_STATUS)
                .click_on_element_in_combo_box_in_filter(AgreementValues.DEVIATION_IS_NOT_AGREED_UPON)
                .check_checkbox_with_text_in_combo_box_in_filter(AgreementValues.DEVIATION_IS_NOT_AGREED_UPON)
                .check_text_components_found_with_any_number()
            )
            temp_text_components_found = self.product_information_page.get_text_components_found_with_any_number()

        with allure.step("4. В фильтре 'Статус согласования' выбрать еще одно любое значение"):
            (
                self.product_information_page.click_on_element_in_combo_box_in_filter(
                    AgreementValues.CHOICE_IS_NOT_AGREED_UPON
                )
                .check_checkbox_with_text_in_combo_box_in_filter(AgreementValues.CHOICE_IS_NOT_AGREED_UPON)
                .check_text(page_text=temp_text_components_found, visible=False)
            )

        with allure.step("5. Выбрать все значения в фильтре"):
            (
                self.product_information_page.click_on_element_in_combo_box_in_filter(
                    AgreementValues.DEVIATION_IS_AGREED
                )
                .click_on_element_in_combo_box_in_filter(AgreementValues.CHOICE_IS_AGREED)
                .click_on_element_in_combo_box_in_filter(AgreementValues.NOT_REQUIRED)
                .check_text_components_found_with_any_number()
            )
            temp_text_components_found = self.product_information_page.get_text_components_found_with_any_number()

        with allure.step("6. Нажать 'Сбросить фильтр'"):
            component_count_first_symbol = 7
            component_count_last_symbol = -11

            (
                self.product_information_page.click_on_reset_filters_button()
                .check_combo_box_in_filter(UITextElements.APPROVAL_STATUS)
                .check_text_total_components_with_any_number()
                .check_text(
                    page_text=temp_text_components_found[component_count_first_symbol:component_count_last_symbol],
                    exact=False,
                )
            )

    @allure.suite("Паспорт продукта, вкладка 'Компонентный состав', фильтр 'Зона техрадара'.")
    @allure.title("Паспорт продукта, вкладка 'Компонентный состав', фильтр 'Зона техрадара'.")
    @allure.id("1565411")
    @allure.description("Баг: Текст 'Всего <любое число> компонент(а/ов)' не отображается на странице.")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1572639", LinkType.LINK, "TASK 1572639"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1565411", "TestCase 1565411")
    @pytest.mark.multiple_streams
    def test_product_passport_component_composition_tab_filter_technical_radar_area(self) -> None:
        """Паспорт продукта, вкладка 'Компонентный состав', фильтр 'Зона техрадара'."""
        # Паспорт продукта_вкладка Компонентный состав_фильтр Зона техрадар
        with allure.step(
            "1. Предусловие: Пользователь с правами редактирования и чтения паспортов продуктов и компонентов "
            "авторизован в сервисе. Открыт реестр продуктов, выбран продукт и открыт его паспорт на вкладке "
            "'Компонентный состав', открыт блок фильтра"
        ):
            first_values = [
                " ",
                Components.BONNIE_PLUS_PLUS,
                RadarAreaValues.INTERESTED_IN,
                AgreementValues.DEVIATION_IS_NOT_AGREED_UPON,
                "",
            ]

            self._setup()
            (
                self.product_information_page.click_on_funnel_icon()
                .check_table_headings(self._TITLES)
                .check_table_text_values(first_values)
            )

        with allure.step("2. В фильтре 'Зона техрадара' нажать на экспандер"):
            self.product_information_page.check_combo_box_in_filter(
                UITextElements.TECHNICAL_RADAR_AREA
            ).click_on_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)

        with allure.step("3. В фильтре 'Зона техрадара' выбрать одно любое значение"):
            (
                self.product_information_page.check_text_total_components_with_any_number()
                .click_on_element_in_combo_box_in_filter(RadarAreaValues.RECOMMENDED)
                .check_checkbox_with_text_in_combo_box_in_filter(RadarAreaValues.RECOMMENDED)
                .check_text_components_found_with_any_number()
                .check_table_text_values(Lists.VALUES_BASH)
            )
            temp_text_components_found = self.product_information_page.get_text_components_found_with_any_number()

        with allure.step("4. В фильтре 'Зона техрадара' выбрать еще одно любое значение"):
            values = [
                " ",
                Components.UTIL_LINUX,
                RadarAreaValues.PILOTED_BY,
                AgreementValues.DEVIATION_IS_NOT_AGREED_UPON,
                "",
            ]

            (
                self.product_information_page.click_on_element_in_combo_box_in_filter(RadarAreaValues.PILOTED_BY)
                .check_checkbox_with_text_in_combo_box_in_filter(RadarAreaValues.PILOTED_BY)
                .check_text(page_text=temp_text_components_found, visible=False)
                .check_table_text_values(values)
            )

        with allure.step("5. Закрыть выпадающий список"):
            (
                self.product_information_page.check_combo_box_list_and_text_in_filter(
                    text_in_combo_box=UITextElements.TECHNICAL_RADAR_AREA + UITextElements.COLON_SPACE_TWO,
                    list_combo_box_elements=RadarAreaValues,
                )
                .check_combo_box_in_filter(UITextElements.APPROVAL_STATUS)
                .click_on_combo_box_in_filter(UITextElements.APPROVAL_STATUS)
            )

        with allure.step("6. Открыть выпадающий список, проверить отображение выбранных значений"):
            (
                self.product_information_page.check_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)
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
                self.product_information_page.click_on_element_in_combo_box_in_filter(RadarAreaValues.INTERESTED_IN)
                .click_on_element_in_combo_box_in_filter(RadarAreaValues.AVOID)
                .click_on_element_in_combo_box_in_filter(RadarAreaValues.UNKNOWN)
                .check_table_text_values(first_values)
            )
            temp_text_components_found = self.product_information_page.get_text_components_found_with_any_number()

        with allure.step("8. Нажать 'Сбросить фильтр'"):
            component_count_first_symbol = 7
            component_count_last_symbol = -11

            (
                self.product_information_page.click_on_reset_filters_button()
                .check_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)
                .check_table_text_values(first_values)
                .check_text_total_components_with_any_number()
                .check_text(
                    page_text=temp_text_components_found[component_count_first_symbol:component_count_last_symbol],
                    exact=False,
                )
            )

    @allure.suite("Паспорт продукта, вкладка 'Компонентный состав', комбинация фильтров.")
    @allure.title("Паспорт продукта, вкладка 'Компонентный состав', комбинация фильтров.")
    @allure.id("1565410")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1577457", LinkType.LINK, "TASK 1577457"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1565410", "TestCase 1565410")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.multiple_streams
    def test_product_passport_component_composition_tab_filter_combination(self) -> None:
        """Паспорт продукта, вкладка 'Компонентный состав', комбинация фильтров."""
        # Паспорт продукта_вкладка Компонентный состав_комбинация фильтров
        with allure.step(
            "1. Предусловие: Пользователь с правами редактирования и чтения паспортов продуктов и компонентов "
            "авторизован в сервисе. Открыт реестр продуктов, выбран продукт и открыт его паспорт на вкладке "
            "'Компонентный состав', открыт блок фильтра"
        ):
            self._setup()
            self.product_information_page.click_on_funnel_icon()

        with allure.step("2. В фильтре 'Статус согласования' выбрать значение 'Не требуется'"):
            (
                self.product_information_page.check_text_total_components_with_any_number()
                .check_combo_box_in_filter(UITextElements.APPROVAL_STATUS)
                .click_on_combo_box_in_filter(UITextElements.APPROVAL_STATUS)
                .click_on_element_in_combo_box_in_filter(AgreementValues.NOT_REQUIRED)
                .check_text(
                    page_text=UITextElements.APPROVAL_STATUS + UITextElements.COLON_SPACE + AgreementValues.NOT_REQUIRED
                )
                .check_table_headings(self._TITLES)
                .check_table_text_values(Lists.VALUES_BASH)
                .check_text_components_found_with_any_number()
            )

        with allure.step("3. Очистить значение фильтра 'Статус согласования'"):
            (
                self.product_information_page.click_on_reset_filters_button()
                .check_combo_box_in_filter(UITextElements.APPROVAL_STATUS)
                .check_text_total_components_with_any_number()
            )

        with allure.step("4. В фильтре 'Зона техрадара' выбрать значение 'Рекомендуется'"):
            (
                self.product_information_page.check_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)
                .click_on_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)
                .click_on_element_in_combo_box_in_filter(RadarAreaValues.RECOMMENDED)
                .check_combo_box_list_and_text_in_filter(
                    text_in_combo_box=UITextElements.TECHNICAL_RADAR_AREA
                    + UITextElements.COLON_SPACE
                    + RadarAreaValues.RECOMMENDED,
                    list_combo_box_elements=RadarAreaValues,
                )
                .check_text_components_found_with_any_number()
            )

        with allure.step("5. Комбинации фильтров:"):
            with allure.step("6. 'Рекомендуется' + 'Выбор не согласован'/'Отклонение не согласовано'"):
                (
                    self.product_information_page.click_on_reset_filters_button()
                    .check_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)
                    .click_on_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)
                    .click_on_element_in_combo_box_in_filter(RadarAreaValues.RECOMMENDED)
                    .check_combo_box_in_filter(UITextElements.APPROVAL_STATUS)
                    .click_on_combo_box_in_filter(UITextElements.APPROVAL_STATUS)
                    .click_on_element_in_combo_box_in_filter(AgreementValues.DEVIATION_IS_NOT_AGREED_UPON)
                    .check_text(UITextElements.NOTHING_FOUND)
                )

            with allure.step("7. 'Неизвестна' + 'Выбор согласован'"):
                (
                    self.product_information_page.click_on_reset_filters_button()
                    .check_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)
                    .click_on_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)
                    .click_on_element_in_combo_box_in_filter(RadarAreaValues.UNKNOWN)
                    .check_combo_box_in_filter(UITextElements.APPROVAL_STATUS)
                    .click_on_combo_box_in_filter(UITextElements.APPROVAL_STATUS)
                    .click_on_element_in_combo_box_in_filter(AgreementValues.CHOICE_IS_AGREED)
                    .check_table_text_values(Lists.VALUES_ACPID)
                )

            with allure.step("8. 'Неизвестна' + 'Выбор не согласован'"):
                (
                    self.product_information_page.click_on_reset_filters_button()
                    .check_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)
                    .click_on_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)
                    .click_on_element_in_combo_box_in_filter(RadarAreaValues.UNKNOWN)
                    .check_combo_box_in_filter(UITextElements.APPROVAL_STATUS)
                    .click_on_combo_box_in_filter(UITextElements.APPROVAL_STATUS)
                    .click_on_element_in_combo_box_in_filter(AgreementValues.CHOICE_IS_NOT_AGREED_UPON)
                    .check_table_text_values(Lists.VALUES_ACCORDSDK)
                )

            with allure.step("9. 'Избегать'/'Пилотируется'/'Интересует' (один из статусов) + 'Отклонение согласовано'"):
                (
                    self.product_information_page.click_on_reset_filters_button()
                    .check_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)
                    .click_on_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)
                    .click_on_element_in_combo_box_in_filter(RadarAreaValues.AVOID)
                    .check_combo_box_in_filter(UITextElements.APPROVAL_STATUS)
                    .click_on_combo_box_in_filter(UITextElements.APPROVAL_STATUS)
                    .click_on_element_in_combo_box_in_filter(AgreementValues.DEVIATION_IS_AGREED)
                    .check_table_text_values(Lists.VALUES_CRYPT_CPU_FEATURES)
                )

            with allure.step("10. ('Избегать' + 'Пилотируется') + 'Отклонение согласовано'"):
                (
                    self.product_information_page.click_on_reset_filters_button()
                    .check_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)
                    .click_on_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)
                    .click_on_element_in_combo_box_in_filter(RadarAreaValues.AVOID)
                    .click_on_element_in_combo_box_in_filter(RadarAreaValues.PILOTED_BY)
                    .check_combo_box_in_filter(UITextElements.APPROVAL_STATUS)
                    .click_on_combo_box_in_filter(UITextElements.APPROVAL_STATUS)
                    .click_on_element_in_combo_box_in_filter(AgreementValues.DEVIATION_IS_AGREED)
                )

            with allure.step(
                "11. 'Избегать'/'Пилотируется'/'Интересует' (один из статусов) + 'Отклонение не согласовано'"
            ):
                (
                    self.product_information_page.click_on_reset_filters_button()
                    .check_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)
                    .click_on_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)
                    .click_on_element_in_combo_box_in_filter(RadarAreaValues.AVOID)
                    .check_combo_box_in_filter(UITextElements.APPROVAL_STATUS)
                    .click_on_combo_box_in_filter(UITextElements.APPROVAL_STATUS)
                    .click_on_element_in_combo_box_in_filter(AgreementValues.DEVIATION_IS_NOT_AGREED_UPON)
                    .check_table_text_values(Lists.VALUES_CRYPTO_UNDERGROUND_V2)
                )

            with allure.step("12. ('Избегать' + 'Пилотируется' + 'Интересует') + 'Отклонение не согласовано'"):
                (
                    self.product_information_page.click_on_reset_filters_button()
                    .check_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)
                    .click_on_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)
                    .click_on_element_in_combo_box_in_filter(RadarAreaValues.AVOID)
                    .click_on_element_in_combo_box_in_filter(RadarAreaValues.PILOTED_BY)
                    .click_on_element_in_combo_box_in_filter(RadarAreaValues.INTERESTED_IN)
                    .check_combo_box_in_filter(UITextElements.APPROVAL_STATUS)
                    .click_on_combo_box_in_filter(UITextElements.APPROVAL_STATUS)
                    .click_on_element_in_combo_box_in_filter(AgreementValues.DEVIATION_IS_NOT_AGREED_UPON)
                )

                temp_text_components_found = self.product_information_page.get_text_components_found_with_any_number()

            with allure.step("13. Очистить фильтр 'Зона радара', проверить значения в таблице"):
                values = [
                    " ",
                    Components.BONNIE_PLUS_PLUS,
                    RadarAreaValues.INTERESTED_IN,
                    AgreementValues.DEVIATION_IS_NOT_AGREED_UPON,
                    "",
                ]

                (
                    self.product_information_page.refresh_page()
                    .click_on_funnel_icon()
                    .check_combo_box_in_filter(UITextElements.APPROVAL_STATUS)
                    .click_on_combo_box_in_filter(UITextElements.APPROVAL_STATUS)
                    .click_on_element_in_combo_box_in_filter(AgreementValues.DEVIATION_IS_NOT_AGREED_UPON)
                    .check_table_text_values(values)
                    .check_text(temp_text_components_found)
                )

    @allure.suite("Паспорт объекта продукта, удалить из избранного.")
    @allure.title("Паспорт объекта продукта, удалить из избранного.")
    @allure.id("1565393")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1582302", LinkType.LINK, "TASK 1582302"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1565393", "TestCase 1565393")
    @allure.severity(allure.severity_level.NORMAL)
    def test_product_passport_delete_from_favorites(self) -> None:
        """Паспорт объекта продукта, удалить из избранного."""
        # Пасторт объекта продукта_ удалить из Избранного
        with allure.step(
            "1. Пользователь с правами на чтение и редактирование паспортов продуктов авторизован в сервисе, открыта "
            "страница 'Продукты'"
        ):
            self._impersonate_as_user_with_read_or_write_permissions(write_permissions=False)
            self.component_page.click_on_link_products()
            (
                self.product_page.click_on_link(UITextElements.ALL_PRODUCTS)
                .click_on_favorites_icon_off(Products.COORDINATOR_HW_5)
                .check_text(page_text=Products.COORDINATOR_HW_5 + UITextElements.ADDED_TO_FAVORITES)
                .check_text(RegularExpressions.PATTERN_STRING_TIME)
                .click_on_close_message_icon()
                .click_on_expander(Products.COORDINATOR_HW_5)
                .click_on_favorites_icon_off(Versions.COORDINATOR_HW_5)
                .check_text(page_text=Versions.COORDINATOR_HW_5 + UITextElements.ADDED_TO_FAVORITES)
                .check_text(RegularExpressions.PATTERN_STRING_TIME)
                .click_on_close_message_icon()
                .click_on_expander(Versions.COORDINATOR_HW_5)
                .click_on_favorites_icon_off(Assemblies.COORDINATOR_HW_5)
                .check_text(page_text=Assemblies.COORDINATOR_HW_5 + UITextElements.ADDED_TO_FAVORITES)
                .check_text(RegularExpressions.PATTERN_STRING_TIME)
                .click_on_close_message_icon()
                .click_on_link(UITextElements.FAVORITES)
            )

        with allure.step(
            "2. В реестре продуктов выбрать любой продукт с индикатором избранного → перейти в паспорт продукта"
        ):
            self.product_page.click_on_link(UITextElements.ALL_PRODUCTS).click_on_link(Products.COORDINATOR_HW_5)

        with allure.step("3. Нажать на индикатор избранного"):
            (
                self.product_information_page.click_on_favorites_icon()
                .check_text(UITextElements.FAVORITES)
                .check_text(page_text=Products.COORDINATOR_HW_5 + UITextElements.DELETED_FROM_FAVORITES)
                .check_text(RegularExpressions.PATTERN_STRING_TIME)
                .click_on_close_message_icon()
                .check_favorites_icon_off()
            )

        with allure.step(
            "4. Вернуться в реестр продуктов, выбрать любой продукт → раскрыть экспандер → выбрать любую версию "
            "продукта, добавленную в избранное → открыть паспорт версии продукта → Нажать на индикатор избранного"
        ):
            self.product_information_page.click_on_link_products()
            (
                self.product_page.click_on_link(UITextElements.ALL_PRODUCTS)
                .click_on_expander(Products.COORDINATOR_HW_5)
                .click_on_link(Versions.COORDINATOR_HW_5)
            )
            (
                self.product_version_information_page.click_on_favorites_icon()
                .check_text(UITextElements.FAVORITES)
                .check_text(page_text=Versions.COORDINATOR_HW_5 + UITextElements.DELETED_FROM_FAVORITES)
                .check_text(RegularExpressions.PATTERN_STRING_TIME)
                .click_on_close_message_icon()
                .check_favorites_icon_off()
            )

        with allure.step(
            "5. Вернуться в реестр продуктов, выбрать любой продукт → раскрыть экспандер → выбрать любую версию "
            "продукта → раскрыть экспандер → выбрать любую сборку продукта, добавленную в избранное → открыть "
            "паспорт сборки продукта → Нажать на индикатор избранного"
        ):
            self.product_version_information_page.click_on_link_products()
            (
                self.product_page.click_on_link(UITextElements.ALL_PRODUCTS)
                .click_on_expander(Products.COORDINATOR_HW_5)
                .click_on_expander(Versions.COORDINATOR_HW_5)
                .click_on_link(Assemblies.COORDINATOR_HW_5)
            )
            (
                self.product_assembly_information_page.click_on_favorites_icon()
                .check_text(UITextElements.FAVORITES)
                .check_text(page_text=Assemblies.COORDINATOR_HW_5 + UITextElements.DELETED_FROM_FAVORITES)
                .check_text(RegularExpressions.PATTERN_STRING_TIME)
                .click_on_close_message_icon()
                .check_favorites_icon_off()
            )

        with allure.step(
            "6. Вернуться в реестр продуктов → для продукта из ш2, версии продукта из ш4, сборки продукта из ш5 "
            "проверить отображение индикатора избранного"
        ):
            self.product_assembly_information_page.click_on_link_products()
            (
                self.product_page.click_on_link(UITextElements.ALL_PRODUCTS)
                .click_on_expander(text_with_expander=Products.COORDINATOR_HW_5)
                .click_on_expander(text_with_expander=Versions.COORDINATOR_HW_5)
                .check_count_favorites_indicator_on(count=0)
            )

        with allure.step("7. Перейти на вкладку 'Избранное'"):
            (
                self.product_page.go_to_previous_or_next_page()
                .click_on_link(UITextElements.FAVORITES)
                .check_text(UITextElements.FAVORITES_PRODUCTS_ARE_MISSING)
                .check_links_count(link_text=UITextElements.SHOW_ALL_PRODUCTS, count=1)
            )

    @allure.suite("Паспорт объекта продукта, добавить в Избранное.")
    @allure.title("Паспорт объекта продукта, добавить в Избранное.")
    @allure.id("1565392")
    @allure.description("Паспорт объекта продукта, добавить в Избранное.")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1586824", LinkType.LINK, "TASK 1586824"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1565392", "TestCase 1565392")
    @allure.severity(allure.severity_level.NORMAL)
    def test_product_passport_add_to_favorites(self, cleanup_favorites: None) -> None:
        """Паспорт объекта продукта, добавить в Избранное.

        :param cleanup_favorites: Фикстура для очистки избранного после автотеста.
        """
        # Паспорт объекта продукта_ добавить в Избранное
        with allure.step(
            "1. Пользователь с правами на чтение и редактирование паспортов продуктов авторизован в сервисе, открыта "
            "страница 'Продукты'"
        ):
            self._impersonate_as_user_with_read_or_write_permissions(write_permissions=False)
            self.component_page.click_on_link_products()

        with allure.step(
            "2. В списке выбрать любой продукт не добавленный в избранное → открыть паспорт продукта → Нажать на "
            "индикатор избранного"
        ):
            (
                self.product_page.click_on_link(UITextElements.ALL_PRODUCTS)
                .click_on_link(Products.COORDINATOR_HW_5)
                .click_on_favorites_icon()
                .check_text(UITextElements.FAVORITES)
                .check_text(page_text=Products.COORDINATOR_HW_5 + UITextElements.ADDED_TO_FAVORITES)
                .check_text(RegularExpressions.PATTERN_STRING_TIME)
                .click_on_close_message_icon()
                .check_favorites_icon_on()
            )

        with allure.step(
            "3. Вернуться в реестр продуктов, выбрать любой продукт → раскрыть экспандер → выбрать любую версию "
            "продукта не добавленную в избранное → открыть паспорт версии продукта → Нажать на индикатор избранного"
        ):
            self.product_information_page.click_on_link_products()
            (
                self.product_page.click_on_link(UITextElements.ALL_PRODUCTS)
                .click_on_expander(Products.COORDINATOR_HW_5)
                .click_on_link(Versions.COORDINATOR_HW_5)
            )
            (
                self.product_version_information_page.click_on_favorites_icon()
                .check_text(UITextElements.FAVORITES)
                .check_text(page_text=Versions.COORDINATOR_HW_5 + UITextElements.ADDED_TO_FAVORITES)
                .check_text(RegularExpressions.PATTERN_STRING_TIME)
                .click_on_close_message_icon()
                .check_favorites_icon_on()
            )

        with allure.step(
            "4. Вернуться в реестр продуктов, выбрать любой продукт → раскрыть экспандер → выбрать любую версию "
            "продукта → раскрыть экспандер → выбрать любую сборку продукта не добавленную в избранное → открыть "
            "паспорт сборки продукта → Нажать на индикатор избранного"
        ):
            self.product_version_information_page.click_on_link_products()
            (
                self.product_page.click_on_link(UITextElements.ALL_PRODUCTS)
                .click_on_expander(Products.COORDINATOR_HW_5)
                .click_on_expander(Versions.COORDINATOR_HW_5)
                .click_on_link(Assemblies.COORDINATOR_HW_5)
            )
            (
                self.product_assembly_information_page.click_on_favorites_icon()
                .check_text(UITextElements.FAVORITES)
                .check_text(page_text=Assemblies.COORDINATOR_HW_5 + UITextElements.ADDED_TO_FAVORITES)
                .check_text(RegularExpressions.PATTERN_STRING_TIME)
                .click_on_close_message_icon()
                .check_favorites_icon_on()
            )

        with allure.step(
            "5. Вернуться в реестр продуктов → для продукта из ш2, версии продукта из ш3, сборки продукта из ш4 "
            "проверить отображение индикатора избранного"
        ):
            self.product_assembly_information_page.click_on_link_products()
            (
                self.product_page.click_on_link(UITextElements.ALL_PRODUCTS)
                .click_on_expander(Products.COORDINATOR_HW_5)
                .click_on_expander(Versions.COORDINATOR_HW_5)
                .check_count_favorites_indicator_on(count=3)
            )

        with allure.step("6. Перейти на вкладку 'Избранное'"):
            (
                self.product_page.click_on_link_products()
                .click_on_favorites_icon_on(Assemblies.COORDINATOR_HW_5)
                .check_text(page_text=Assemblies.COORDINATOR_HW_5 + UITextElements.DELETED_FROM_FAVORITES)
                .check_text(RegularExpressions.PATTERN_STRING_TIME)
                .click_on_close_message_icon()
                .click_on_favorites_icon_on(Products.COORDINATOR_HW_5)
                .check_text(page_text=Products.COORDINATOR_HW_5 + UITextElements.DELETED_FROM_FAVORITES)
                .check_text(RegularExpressions.PATTERN_STRING_TIME)
                .click_on_close_message_icon()
                .click_on_favorites_icon_on(Versions.COORDINATOR_HW_5)
                .check_text(page_text=Versions.COORDINATOR_HW_5 + UITextElements.DELETED_FROM_FAVORITES)
                .check_text(RegularExpressions.PATTERN_STRING_TIME)
                .click_on_close_message_icon()
            )

    @allure.suite("Паспорт продукта, согласование отклонения от техрадара.")
    @allure.title("Паспорт продукта, согласование отклонения от техрадара.")
    @allure.id("1565399")
    @allure.description("Паспорт продукта, согласование отклонения от техрадара.")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1589790", LinkType.LINK, "TASK 1589790"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1565399", "TestCase 1565399")
    @allure.severity(allure.severity_level.NORMAL)
    def test_product_passport_approval_of_deviations_from_technical_radar(
        self, clear_comment_and_checkbox: None
    ) -> None:
        """Паспорт продукта, согласование отклонения от техрадара.

        :param clear_comment_and_checkbox: Фикстура для очистки комментария и checkbox'а.
        """
        # Паспорт продукта_ согласование отклонения от техрадара
        # TODO проверить тест-кейс (его должны актуализировать), возможно нужно будет изменить автотест после этого
        comment = "a" * 1000

        with allure.step(
            "Пользователь с правами на чтение и редактирование паспортов продуктов авторизован в сервисе, открыт "
            "паспорт продукта на вкладке 'Компонентный состав'"
        ):
            self._setup()

        with allure.step("Нажать 'Редактировать'"):
            (
                self.product_information_page.click_on_element_with_text(UITextElements.EDIT)
                .check_text(page_text=UITextElements.EDIT, visible=False)
                .check_visibility_cancel_editing_button()
            )

        with allure.step(
            "В списке выбрать любой несогласованный компонент с зоной техрадара 'Неизвестна' → отметить чек-бокс "
            "'Согласование' галкой"
        ):
            (
                self.product_information_page.click_on_funnel_icon()
                .click_on_combo_box_in_filter(UITextElements.APPROVAL_STATUS)
                .click_on_element_with_text(AgreementValues.CHOICE_IS_NOT_AGREED_UPON)
                .click_on_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)
                .click_on_element_with_text(RadarAreaValues.UNKNOWN)
                .click_on_element_with_text(element_text=UITextElements.AGREEMENT, nth=1)
                .fill_in_textarea_justification_comment("")
                .check_text("Поле с обоснованием не заполнено")
                .check_checkbox_with_text_in_combo_box_in_filter(UITextElements.AGREEMENT)
                .check_visibility_textarea_justification_comment()
                .check_red_backlight_for_textarea()
                .check_text_in_textarea_justification_comment("")
            )

        with allure.step("Нажать 'Сохранить'"):
            self.product_information_page.click_on_icon_floppy_disk().check_text(
                page_text=UITextElements.QUESTION, visible=False
            )

        with allure.step(
            "В поле 'Обоснование/Комментарий' добавить валидный комментарий до 1000 символов (включительно)"
        ):
            (
                self.product_information_page.fill_in_textarea_justification_comment(comment)
                .check_text_in_textarea_justification_comment(comment)
                .check_attributes_in_textarea_justification_comment()
            )

        with allure.step("Нажать 'Сохранить'"):
            (
                self.product_information_page.click_on_icon_floppy_disk()
                .check_text(UITextElements.QUESTION)
                .check_text(UITextElements.NO)
                .check_title_modal()
            )

        with allure.step("Нажать 'Да'"):
            (
                self.product_information_page.click_on_element_with_text(UITextElements.YES)
                .check_text(self._APPROVAL_CHANGED_SUCCESSFULLY)
                .check_text(RegularExpressions.PATTERN_STRING_TIME)
                .check_visibility_close_message_icon()
                .check_text(page_text=self._APPROVAL_CHANGED_SUCCESSFULLY, visible=False, timeout=6_000)
            )

    def _setup(self) -> None:
        """Предусловие: паспорт продукта → вкладка 'Компонентный состав'."""
        self.component_page.click_on_link_products()
        self.product_page.click_on_link(UITextElements.ALL_PRODUCTS).click_on_link(Products.COORDINATOR_HW_5)
        self.product_information_page.click_on_link(UITextElements.COMPONENT_COMPOSITION)
