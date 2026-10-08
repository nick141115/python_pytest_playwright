import allure
import pytest
from allure_commons.types import LinkType
from playwright.sync_api import Page

from src.constants.components import Components
from src.constants.packages import Packages
from src.constants.radar_area_values import RadarAreaValues
from src.constants.ui_text_elements import UITextElements
from src.constants.versions import Versions
from tests.base.base_test import BaseTest


@allure.parent_suite("Вкладка 'Компоненты-потребители'.")
@allure.epic("Вкладка 'Компоненты-потребители'.")
@allure.sub_suite("Вкладка 'Компоненты-потребители'.")
@allure.severity(allure.severity_level.NORMAL)
class TestConsumerComponentsTab(BaseTest):
    """Вкладка 'Компоненты-потребители'."""

    _TABLE_VALUES = [
        Components.IPS,
        RadarAreaValues.UNKNOWN,
    ]

    @allure.suite(
        "Паспорт компонента, версии компонента, конфигурации компонента, вкладка 'Компоненты-потребители', сброс "
        "значений фильтров, обновление страницы."
    )
    @allure.title(
        "Паспорт компонента, версии компонента, конфигурации компонента, вкладка 'Компоненты-потребители', сброс "
        "значений фильтров, обновление страницы."
    )
    @allure.id("1522372")
    @allure.description("Баг: Текст 'Всего <любое число> компонент(а/ов)' не отображается на странице.")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1553709", LinkType.LINK, "TASK 1553709"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1522372", "TestCase 1522372")
    @pytest.mark.multiple_streams
    def test_consumer_components_tab_resetting_filter_values_refresh_page(self) -> None:
        """Вкладка 'Компоненты-потребители', сброс значений фильтров, обновление страницы."""
        # Паспорт компонента/версии компонента/конфигурации компонента_вкладка Компоненты-потребители_Сброс значений фил
        with allure.step(
            "1. Предусловие: Пользователь с правами редактирования и чтения паспортов продуктов и компонентов "
            "авторизован в сервисе. Открыт реестр компонентов, выбран компонент, открыт паспорт компонента на "
            "вкладке 'Компоненты-потребители', открыт блок фильтра"
        ):
            self.component_page.click_on_link(UITextElements.ALL_COMPONENTS_TAB).click_on_link(Components.ACCORDSDK)
            self.component_information_page.click_on_link(UITextElements.CONSUMER_COMPONENTS_TAB).click_on_funnel_icon()

        with allure.step("2. В фильтре выбрать несколько любых значений"):
            self._apply_radar_filter_and_verify(page=self.component_information_page, table_values=self._TABLE_VALUES)

        with allure.step("3. Нажать кнопку 'Сбросить фильтр'"):
            table_values = [
                Components.CRYPT_PASSWORD_FORGE,
                RadarAreaValues.RECOMMENDED,
            ]

            self._click_reset_filter_button(self.component_information_page, table_values)

        with allure.step("4. Повторить ш.2 и обновить страницу сервиса"):
            self._apply_radar_filter_and_verify(page=self.component_information_page, table_values=self._TABLE_VALUES)
            self._refresh_service_page(page=self.component_information_page)

        with allure.step(
            "5. Повторить шаги тест-кейса для паспорта версии компонента, вкладка 'Компоненты-потребители'"
        ):
            (
                self.component_information_page.click_on_link(UITextElements.VERSIONS_TAB)
                .click_on_link(Versions.ACCORDSDK)
                .click_on_link(UITextElements.CONSUMER_COMPONENTS_TAB)
                .click_on_funnel_icon()
            )

            with allure.step("В фильтре выбрать несколько любых значений"):
                table_values = [
                    Components.IPS,
                    Versions.ACCORDSDK,
                    RadarAreaValues.UNKNOWN,
                ]

                self._apply_radar_filter_and_verify(
                    page=self.component_version_information_page, table_values=table_values
                )

            with allure.step("Нажать кнопку 'Сбросить фильтр'"):
                table_values = [
                    Components.CRYPT_PASSWORD_FORGE,
                    Versions.ONE_ONE,
                    RadarAreaValues.RECOMMENDED,
                ]

                self._click_reset_filter_button(page=self.component_version_information_page, table_values=table_values)

            with allure.step("Повторить ш.2 и обновить страницу сервиса"):
                table_values = [
                    Components.IPS,
                    Versions.ACCORDSDK,
                    RadarAreaValues.UNKNOWN,
                ]

                self._apply_radar_filter_and_verify(
                    page=self.component_version_information_page, table_values=table_values
                )
                self._refresh_service_page(page=self.component_version_information_page)

        with allure.step(
            "6. Повторить шаги тест-кейса для паспорта конфигурации компонента, вкладка 'Компоненты-потребители'"
        ):
            self.component_version_information_page.click_on_link(UITextElements.PACKAGES_TAB).click_on_link(
                Packages.ACCORDSDK
            )
            self.component_package_information_page.click_on_link(
                UITextElements.ASSEMBLIES_BY_CONFIGURATION
            ).click_on_link(UITextElements.DEFAULT_BRAND_TRUNK)
            self.component_assembly_by_configuration_page.click_on_link(
                UITextElements.CONSUMER_COMPONENTS_TAB
            ).click_on_funnel_icon()

            with allure.step("В фильтре выбрать несколько любых значений"):
                table_values = [
                    Components.UPRNG,
                    Versions.ONE_SIX,
                    "1.6.3.1400",
                    UITextElements.LINUX_RELEASE_ONE_SIX_X,
                    RadarAreaValues.UNKNOWN,
                ]

                self._apply_radar_filter_and_verify(
                    page=self.component_assembly_by_configuration_page, table_values=table_values
                )

            with allure.step("Нажать кнопку 'Сбросить фильтр'"):
                self._click_reset_filter_button(
                    page=self.component_assembly_by_configuration_page, table_values=table_values
                )

            with allure.step("Повторить ш.2 и обновить страницу сервиса"):
                self._apply_radar_filter_and_verify(
                    page=self.component_assembly_by_configuration_page, table_values=table_values
                )
                self._refresh_service_page(page=self.component_assembly_by_configuration_page)

    @allure.suite("Паспорт компонента, вкладка 'Компоненты-потребители', фильтр 'Зона техрадара', отображение.")
    @allure.title("Паспорт компонента, вкладка 'Компоненты-потребители', фильтр 'Зона техрадара', отображение.")
    @allure.id("1522370")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1553730", LinkType.LINK, "TASK 1553730"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1522370", "TestCase 1522370")
    @pytest.mark.multiple_streams
    def test_component_passport_consumer_components_tab_technical_radar_zone_filter_display(self) -> None:
        """Паспорт компонента, вкладка 'Компоненты-потребители', фильтр 'Зона техрадара', отображение."""
        # Паспорт компонента_вкладка Компоненты-потребители_фильтр Зона техрадара_отображаение
        with allure.step(
            "1. Предусловие: Пользователь с правами редактирования и чтения паспортов продуктов и компонентов "
            "авторизован в сервисе. Открыт реестр компонентов, выбран компонент и открыт его паспорт на вкладке "
            "'Компоненты-потребители'"
        ):
            self.component_page.click_on_link(UITextElements.ALL_COMPONENTS_TAB).click_on_link(Components.ACCORDSDK)
            self.component_information_page.click_on_link(UITextElements.CONSUMER_COMPONENTS_TAB)

        with allure.step("2. Кликнуть в поле фильтра 'Зона техрадара'"):
            list_combo_box_elements = [
                RadarAreaValues.RECOMMENDED,
                RadarAreaValues.PILOTED_BY,
                RadarAreaValues.INTERESTED_IN,
                RadarAreaValues.AVOID,
                RadarAreaValues.UNKNOWN,
            ]

            self._click_on_tech_radar_zone_filter_field(
                page=self.component_information_page, list_combo_box_elements=list_combo_box_elements
            )

        with allure.step(
            "3. Повторить шаги тест-кейса для паспорта версии компонента, вкладка 'Компоненты-потребители'"
        ):
            (
                self.component_information_page.click_on_link(UITextElements.VERSIONS_TAB)
                .click_on_link(Versions.ACCORDSDK)
                .click_on_link(UITextElements.CONSUMER_COMPONENTS_TAB)
            )

            with allure.step("Кликнуть в поле фильтра 'Зона техрадара'"):
                self._click_on_tech_radar_zone_filter_field(
                    page=self.component_version_information_page, list_combo_box_elements=list_combo_box_elements
                )

        with allure.step(
            "4. Повторить шаги тест-кейса для паспорта конфигурации компонента, вкладка 'Компоненты-потребители'"
        ):
            self.component_version_information_page.click_on_link(UITextElements.PACKAGES_TAB).click_on_link(
                Packages.ACCORDSDK
            )
            self.component_package_information_page.click_on_link(
                UITextElements.ASSEMBLIES_BY_CONFIGURATION
            ).click_on_link(UITextElements.DEFAULT_BRAND_TRUNK)
            self.component_assembly_by_configuration_page.click_on_link(UITextElements.CONSUMER_COMPONENTS_TAB)

            with allure.step("Кликнуть в поле фильтра 'Зона техрадара'"):
                self._click_on_tech_radar_zone_filter_field(
                    page=self.component_assembly_by_configuration_page, list_combo_box_elements=list_combo_box_elements
                )

    def _apply_radar_filter_and_verify(self, page: Page, table_values: list[str]) -> None:
        """Применить фильтр по зоне технического радара и проверить результаты.

        :param page: Объект страницы.
        :param table_values: Список текстовых значений таблицы в первой строке.
        """
        (
            page.check_text_total_components_with_any_number()
            .check_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)
            .click_on_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)
            .click_on_element_in_combo_box_in_filter(RadarAreaValues.PILOTED_BY)
            .click_on_element_in_combo_box_in_filter(RadarAreaValues.UNKNOWN)
            .check_table_text_values(table_values)
            .check_text_components_found_with_any_number()
        )

    def _click_reset_filter_button(self, page: Page, table_values: list[str]) -> None:
        """Нажать кнопку 'Сбросить фильтр'.

        :param page: Объект страницы.
        :param table_values: Список текстовых значений таблицы в первой строке.
        """
        (
            page.click_on_reset_filters_button()
            .check_reset_filters_button()
            .check_table_text_values(table_values)
            .check_text_total_components_with_any_number()
        )

    def _refresh_service_page(self, page: Page) -> None:
        """Обновить страницу сервиса.

        :param page: Объект страницы.
        """
        page.refresh_page().check_text_total_components_with_any_number().check_reset_filters_button(
            visible_and_enabled=False
        )

    def _click_on_tech_radar_zone_filter_field(self, page: Page, list_combo_box_elements: list[str]) -> None:
        """Кликнуть в поле фильтра 'Зона техрадара'.

        :param page: Объект страницы.
        :param list_combo_box_elements: Список элементов combobox'а.
        """
        (
            page.click_on_funnel_icon()
            .check_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)
            .click_on_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)
            .click_on_element_in_combo_box_in_filter(RadarAreaValues.AVOID)
            .click_on_element_in_combo_box_in_filter(RadarAreaValues.UNKNOWN)
            .check_combo_box_list_and_text_in_filter(
                text_in_combo_box=UITextElements.TECHNICAL_RADAR_AREA + UITextElements.COLON_SPACE_TWO,
                list_combo_box_elements=list_combo_box_elements,
            )
        )
