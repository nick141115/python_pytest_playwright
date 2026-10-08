import allure
import pytest
from allure_commons.types import LinkType

from src.constants.assemblies import Assemblies
from src.constants.components import Components
from src.constants.lists import Lists
from src.constants.products import Products
from src.constants.radar_area_values import RadarAreaValues
from src.constants.regular_expressions import RegularExpressions
from src.constants.test_inputs import TestInputs
from src.constants.ui_text_elements import UITextElements
from src.constants.versions import Versions
from tests.base.base_test import BaseTest


@allure.sub_suite("Конфигурация компонента.")
@allure.epic("Конфигурация компонента.")
@allure.parent_suite("Конфигурация компонента.")
@allure.severity(allure.severity_level.CRITICAL)
class TestComponentConfiguration(BaseTest):
    """Конфигурация компонента."""

    _PACKAGE = "6.4.6.67"
    _ASSEMBLY_BY_CONFIGURATION_DEFAULT_BRAND_TRUNK = "Сборка по конфигурации DEFAULT_BRAND_trunk"
    _TEXT_VERSION_ACETAO = "Версия 6.4"
    _TITLES_CONSUMER_COMPONENTS = [
        UITextElements.COMPONENT,
        UITextElements.TEXT_VERSION,
        UITextElements.ASSEMBLY,
        UITextElements.CONFIGURATION,
        UITextElements.TECHNICAL_RADAR_AREA,
    ]
    _VALUES_VPN_INTERFACES = [
        Components.VPN_INTERFACES,
        Versions.TWO_NINE,
        Assemblies.VPN_INTERFACES,
        UITextElements.DEFAULT_BRAND_TRUNK,
        RadarAreaValues.UNKNOWN,
    ]

    @allure.suite("Конфигурация компонента.")
    @allure.title("Конфигурация компонента.")
    @allure.id("1513332")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1542753", LinkType.LINK, "TASK 1542753"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1513332", "TestCase 1513332")
    @pytest.mark.multiple_streams
    def test_component_configuration(self) -> None:
        """Конфигурация компонента."""
        # Конфигурация компонента
        with allure.step(
            "1. Предусловие: Пользователь авторизован в сервисе, открыта страница 'Компоненты', выбран один из "
            "компонентов списка, выбрана версия компонента, выбран пакет, выбрана сборка пакета"
        ):
            self._setup()

        with allure.step("2. Проверить отображение информации по выбранной сборке пакета компонента"):
            titles = [
                UITextElements.PRODUCT,
                UITextElements.TEXT_VERSION,
            ]
            values = [
                Products.VIPNET_CLIENT_4_X_FOR_WINDOWS,
                Versions.VIPNET_CLIENT_4_X_FOR_WINDOWS,
            ]

            (
                self.component_assembly_by_configuration_page.check_page_title(
                    self._ASSEMBLY_BY_CONFIGURATION_DEFAULT_BRAND_TRUNK
                )
                .check_favorites_indicator()
                .check_item_title_link(title=UITextElements.COMPONENTS)
                .check_item_title_link(title=Components.ACETAO, nth=1)
                .check_item_title_link(title=self._TEXT_VERSION_ACETAO, nth=2)
                .check_item_title_link(title=f"{UITextElements.TEXT_PACKAGE} {self._PACKAGE}", nth=3)
                .check_navigation_bar_item_title(self._ASSEMBLY_BY_CONFIGURATION_DEFAULT_BRAND_TRUNK)
                .check_active_tab(UITextElements.GENERAL_INFORMATION)
                .check_title_and_text_in_tab_general_information(
                    title=UITextElements.TEXT_VERSION, text=Versions.ACETAO
                )
                .check_title_and_text_in_tab_general_information(
                    title=UITextElements.PACKAGE_MANAGER, text=UITextElements.ANT_IVY
                )
                .check_title_and_text_in_tab_general_information(
                    title=UITextElements.PLATFORM, text=RegularExpressions.PATTERN_WINDOWS
                )
                .click_on_link(UITextElements.CONSUMER_PRODUCTS_TAB)
                .check_active_tab(UITextElements.CONSUMER_PRODUCTS_TAB)
                .check_table_headings(titles)
                .check_table_text_values(values)
                .click_on_link(UITextElements.CONSUMER_COMPONENTS_TAB)
                .check_active_tab(UITextElements.CONSUMER_COMPONENTS_TAB)
            )
            (
                self.component_assembly_by_configuration_page.check_table_headings(self._TITLES_CONSUMER_COMPONENTS)
                .check_table_text_values(self._VALUES_VPN_INTERFACES)
                .check_grey_indicator_in_table_consumer_components_assembly_page()
            )

    @allure.suite("Конфигурация компонента, посмотреть сведения (все вкладки).")
    @allure.title("Конфигурация компонента, посмотреть сведения (все вкладки).")
    @allure.id("1565464")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1584265", LinkType.LINK, "TASK 1584265"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1565464", "TestCase 1565464")
    @pytest.mark.multiple_streams
    def test_component_configuration_view_details_all_tabs(self) -> None:
        """Конфигурация компонента, посмотреть сведения (все вкладки)."""
        # Конфигурация компонента_посмотреть сведения (все вкладки)
        with allure.step(
            "1. Предусловие: Пользователь авторизован в сервисе, открыта страница 'Компоненты', выбран один из "
            "компонентов списка, выбрана версия компонента, выбран пакет, выбрана сборка пакета"
        ):
            self._impersonate_as_user_with_read_or_write_permissions(write_permissions=False)
            self._setup()

        with allure.step("2. Проверить отображение информации по выбранному пакету компонента"):
            with allure.step("Вкладка 'Общая информация'"):
                (
                    self.component_assembly_by_configuration_page.check_active_tab(UITextElements.GENERAL_INFORMATION)
                    .check_text_in_navigation_bar(
                        UITextElements.COMPONENTS
                        + Components.ACETAO
                        + self._TEXT_VERSION_ACETAO
                        + UITextElements.TEXT_PACKAGE
                        + " "
                        + self._PACKAGE
                        + self._ASSEMBLY_BY_CONFIGURATION_DEFAULT_BRAND_TRUNK
                    )
                    .check_links_count(link_text=UITextElements.COMPONENTS, count=3)
                    .check_links_count(link_text=Components.ACETAO, count=1)
                    .check_links_count(link_text=self._TEXT_VERSION_ACETAO, count=1)
                    .check_favorites_indicator()
                    .check_text(self._ASSEMBLY_BY_CONFIGURATION_DEFAULT_BRAND_TRUNK, nth=1)
                    .check_title_and_text_in_tab_general_information(
                        title=UITextElements.TEXT_VERSION, text=Versions.ACETAO
                    )
                    .check_title_and_text_in_tab_general_information(
                        title=UITextElements.PACKAGE_MANAGER, text=UITextElements.ANT_IVY
                    )
                    .check_title_and_text_in_tab_general_information(
                        title=UITextElements.PLATFORM, text=RegularExpressions.PATTERN_WINDOWS
                    )
                )

            with allure.step("Вкладка 'Продукты-потребители'"):
                values = [
                    Products.VIPNET_CLIENT_4_X_FOR_WINDOWS,
                    Versions.VIPNET_CLIENT_4_X_FOR_WINDOWS,
                ]

                (
                    self.component_assembly_by_configuration_page.click_on_link(UITextElements.CONSUMER_PRODUCTS_TAB)
                    .check_active_tab(UITextElements.CONSUMER_PRODUCTS_TAB)
                    .check_text_total_products_with_any_number()
                    .check_table_headings(Lists.TITLES_TABLE_CONSUMER_PRODUCTS)
                    .check_table_text_values(values)
                    .check_links_count(link_text=Products.VIPNET_CLIENT_4_X_FOR_WINDOWS, count=3)
                    .check_links_count(link_text=Versions.VIPNET_CLIENT_4_X_FOR_WINDOWS, count=1)
                    .fill_in_search_input(TestInputs.SPECIAL_CHARACTERS)
                )

            with allure.step("Вкладка 'Компоненты-потребители'"):
                (
                    self.component_assembly_by_configuration_page.click_on_link(UITextElements.CONSUMER_COMPONENTS_TAB)
                    .check_active_tab(UITextElements.CONSUMER_COMPONENTS_TAB)
                    .check_text_total_components_with_any_number()
                    .check_table_headings(self._TITLES_CONSUMER_COMPONENTS)
                    .check_table_text_values(self._VALUES_VPN_INTERFACES)
                    .check_links_count(link_text=Components.VPN_INTERFACES, count=5)
                    .check_links_count(link_text=Versions.TWO_NINE, count=1, exact=True)
                    .check_links_count(link_text=Assemblies.VPN_INTERFACES, count=1)
                    .check_links_count(link_text=UITextElements.DEFAULT_BRAND_TRUNK, count=15)
                    .fill_in_search_input(TestInputs.SPECIAL_CHARACTERS)
                    .click_on_funnel_icon()
                )

    def _setup(self) -> None:
        """Предусловие: открыта сборка пакета компонента."""
        (
            self.component_page.click_on_title()
            .click_on_link(UITextElements.ALL_COMPONENTS_TAB)
            .click_on_link(Components.ACETAO)
        )
        self.component_information_page.click_on_link(UITextElements.VERSIONS_TAB).click_on_link(Versions.ACETAO)
        self.component_version_information_page.click_on_link(UITextElements.PACKAGES_TAB).click_on_link(self._PACKAGE)
        self.component_package_information_page.click_on_link(UITextElements.ASSEMBLIES_BY_CONFIGURATION).click_on_link(
            UITextElements.DEFAULT_BRAND_TRUNK
        )
