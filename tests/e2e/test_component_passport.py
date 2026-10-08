import re

import allure
import pytest
from allure_commons.types import LinkType
from playwright.sync_api import Page

from src.constants.components import Components
from src.constants.packages import Packages
from src.constants.products import Products
from src.constants.radar_area_values import RadarAreaValues
from src.constants.regular_expressions import RegularExpressions
from src.constants.ui_text_elements import UITextElements
from src.constants.versions import Versions
from tests.base.base_test import BaseTest


@allure.parent_suite("Паспорт компонента.")
@allure.epic("Паспорт компонента.")
@allure.sub_suite("Паспорт компонента.")
class TestComponentPassport(BaseTest):
    """Паспорт компонента."""

    _COMPONENTS_FOUND = 1
    _TITLES = [
        UITextElements.TEXT_VERSION,
        UITextElements.PACKAGE_MANAGERS,
        UITextElements.DEVELOPMENT_STATUS,
        UITextElements.PLATFORMS,
        UITextElements.LICENSE,
    ]

    @allure.suite("Паспорт компонента уникален.")
    @allure.title("Паспорт компонента уникален.")
    @allure.id("1513301")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1536436", LinkType.LINK, "TASK 1536436"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1513301", "TestCase 1513301")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.multiple_streams
    def test_component_passport_is_unique(self) -> None:
        """Паспорт компонента уникален."""
        # Паспорт компонента уникален
        with allure.step("1. Предусловие: Пользователь авторизован в сервисе, открыта страница 'Компоненты'"):
            self.component_page.click_on_link(UITextElements.ALL_COMPONENTS_TAB)

        with allure.step("2. Проверить список компонентов"):
            list_components = [
                Components.ACCORDSDK,
                Components.ACETAO,
                "accepts",
                Components.ADDUSER,
                Components.ANTCUSTOM,
            ]

            for component in list_components:
                (
                    self.component_page.fill_in_search_input(component)
                    .check_text_components_found(self._COMPONENTS_FOUND)
                    .click_on_cross_icon()
                    .check_search_input("")
                    .check_text_total_components_with_any_number()
                )

    @allure.suite("Паспорт компонента, общая информация.")
    @allure.title("Паспорт компонента, общая информация.")
    @allure.id("1513309")
    @allure.description("Автотест иногда падает из-за тормозов стенда.")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1537054", LinkType.LINK, "TASK 1537054"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1513309", "TestCase 1513309")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_component_passport_general_information(self) -> None:
        """Паспорт компонента, общая информация."""
        # Паспорт компонента_общая информация
        tooltip = "Дата изменения файла в источнике хранения - Artifactory."
        pattern_date = re.compile(r"\d{2}\.\d{2}\.\d{4}\s\d{2}:\d{2}")

        with allure.step(
            "1. Предусловие: Пользователь авторизован в сервисе, открыта страница 'Компоненты' на вкладке 'Все "
            "компоненты'"
        ):
            self._impersonate_as_user_with_read_or_write_permissions(write_permissions=False)
            self.component_page.click_on_title().click_on_link(UITextElements.ALL_COMPONENTS_TAB)

        with allure.step("2. В реестре выбрать любой компонент"):
            self.component_page.click_on_link(Components.ACCORDSDK)

        with allure.step("3. Название компонента"):
            self.component_information_page.check_page_title(Components.ACCORDSDK)

        with allure.step("4. Дата последней синхронизации"):
            self.component_information_page.hover_cursor_over_question_mark().check_text(tooltip)

        with allure.step(
            "5 - 12. Зона радара, Тип, Описание, Пакетные менеджеры, Платформы, Ссылки, Лицензия, 'Ответственный за "
            "реализацию', 'Владелец', 'Технический эксперт'"
        ):
            (
                self.component_information_page.check_title_and_text_in_tab_general_information(
                    title=UITextElements.LAST_SYNC_DATE, text=pattern_date
                )
                .check_title_and_text_in_tab_general_information(title="Зона радара", text=RadarAreaValues.UNKNOWN)
                .check_title_and_text_in_tab_general_information(title=UITextElements.TYPE, text=UITextElements.DASH)
                .check_title_and_text_in_tab_general_information(title="Описание", text=UITextElements.DASH)
                .check_title_and_text_in_tab_general_information(
                    title=UITextElements.PACKAGE_MANAGERS, text=UITextElements.ANT_IVY
                )
                .check_title_and_text_in_tab_general_information(
                    title=UITextElements.PLATFORMS, text=RegularExpressions.PATTERN_WINDOWS
                )
                .check_title_and_text_in_tab_general_information(
                    title=UITextElements.LICENSE, text=UITextElements.LICENSES_LINK
                )
                .check_title_and_text_in_tab_general_information(
                    title=UITextElements.RESPONSIBLE_FOR_IMPLEMENTATION, text=UITextElements.DASH
                )
                .check_title_and_text_in_tab_general_information(title=UITextElements.OWNER, text=UITextElements.DASH)
                .check_title_and_text_in_tab_general_information(
                    title=UITextElements.TECHNICAL_EXPERT, text=UITextElements.DASH
                )
                .check_text(UITextElements.LINKS)
                .check_links_count(link_text=UITextElements.REGULATIONS, count=1)
                .check_links_count(link_text=UITextElements.ARTIFACTORY, count=1)
                .check_grey_indicator_in_table_general_information_component()
            )

    @allure.suite("Паспорт компонента, вкладка 'Продукты-потребители'.")
    @allure.title("Паспорт компонента, вкладка 'Продукты-потребители'.")
    @allure.id("1513323")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1538055", LinkType.LINK, "TASK 1538055"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1513323", "TestCase 1513323")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.multiple_streams
    def test_component_passport_consumer_product_tab(self) -> None:
        """Паспорт компонента, вкладка 'Продукты-потребители'."""
        # Паспорт компонента_вкладка  Продукты-потребители
        with allure.step(
            "1. Предусловие: Пользователь авторизован в сервисе, открыт паспорт компонента на вкладке "
            "'Продукты-потребители'"
        ):
            self.component_page.click_on_link(UITextElements.ALL_COMPONENTS_TAB).click_on_link(Components.ACCORDSDK)
            self.component_information_page.click_on_link(UITextElements.CONSUMER_PRODUCTS_TAB)

        with allure.step("2. Проверить отображение на вкладке 'Продукты-Потребители'"):
            products = [
                UITextElements.CONNECT,
                Products.COORDINATOR_HW_4,
                Products.COORDINATOR_HW_5,
                Products.COORDINATOR_IG_5,
                "CSS Connect 3",
                "Protelion Enterprise Messenger",
                "TDC Archive",
                "TSM-EN",
                "ViPNet Client 5 for Android",
                "Архитектурный Репозиторий",
                "Светофор здоровья проектов",
                "УМЗЧ Апелиотис А110 ФРКЕ.465327.004",
            ]

            self.component_information_page.check_links_in_products_list(products)

        with allure.step("3. Кликнуть по ссылке на продукт"):
            self.component_information_page.click_on_link(UITextElements.CONNECT)
            (
                self.product_information_page.check_item_title_link(UITextElements.PRODUCTS)
                .check_page_title(UITextElements.CONNECT)
                .check_active_tab(UITextElements.GENERAL_INFORMATION)
            )

    @allure.suite("Паспорт компонента, вкладка 'Компоненты-потребители'.")
    @allure.title("Паспорт компонента, вкладка 'Компоненты-потребители'.")
    @allure.id("1513324")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1538658", LinkType.LINK, "TASK 1538658"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1513324", "TestCase 1513324")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.multiple_streams
    def test_component_passport_consumer_component_tab(self) -> None:
        """Паспорт компонента, вкладка 'Компоненты-потребители'."""
        # Паспорт компонента_вкладка Компоненты-потребители
        with allure.step(
            "1. Предусловие: Пользователь авторизован в сервисе, открыт паспорт компонента на вкладке "
            "'Компоненты-потребители'"
        ):
            self.component_page.click_on_link(UITextElements.ALL_COMPONENTS_TAB).click_on_link(Components.ACCORDSDK)
            self.component_information_page.click_on_link(UITextElements.CONSUMER_COMPONENTS_TAB)

        with allure.step("2. Проверить отображение на вкладке 'Компоненты-потребители'"):
            components = [
                Components.CRYPT_PASSWORD_FORGE,
                Components.IPS,
                "itcshub",
                "openssl_engines_gost",
                "ossl_apps",
                "ossl_ex",
                "ossl_itp11util",
                "pkcs11_benchmark",
                "pkcs11_csp4_storage",
                "pkcs11_switch",
                "soft_token",
                "softtoken_ngost_storage",
                Components.UPRNG,
                "vipnet_custom_cms_coder",
                "vipnet_custom_cryptoalg_soft_token",
                "vipnet_custom_key_generation_service",
                "vipnet_custom_key_storage",
                "vipnet_custom_key_system_inproc",
                "vipnet_custom_key_system_utils",
            ]

            self.component_information_page.check_text(
                UITextElements.TECHNICAL_RADAR_AREA
            ).check_links_in_components_list(components)

        with allure.step("3. Кликнуть по ссылке на компонент"):
            (
                self.component_information_page.click_on_link(Components.CRYPT_PASSWORD_FORGE)
                .check_item_title_link(UITextElements.COMPONENTS)
                .check_page_title(Components.CRYPT_PASSWORD_FORGE)
                .check_active_tab(UITextElements.GENERAL_INFORMATION)
            )

    @allure.suite("Уникальная ссылка на паспорт компонента.")
    @allure.title("Уникальная ссылка на паспорт компонента.")
    @allure.id("1513322")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1540966", LinkType.LINK, "TASK 1540966"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1513322", "TestCase 1513322")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.multiple_streams
    def test_unique_link_to_component_passport(self) -> None:
        """Уникальная ссылка на паспорт компонента."""
        # Уникальная ссылка на паспорт компонента
        with allure.step(
            "1. Предусловие: Пользователь авторизован в сервисе, открыта страница 'Компоненты' → вкладка "
            "'Все компоненты'"
        ):
            self.component_page.click_on_link(UITextElements.ALL_COMPONENTS_TAB)

        with allure.step("2. Проверить наличие ссылки"):
            self.component_page.fill_in_search_input(Components.ACCORDSDK).check_text_components_found(
                self._COMPONENTS_FOUND
            )

        with allure.step("3. Перейти по ссылке/открыть в новой вкладке/окне'"):
            self.component_page.click_on_link(Components.ACCORDSDK)
            (
                self.component_information_page.check_item_title_link(UITextElements.COMPONENTS)
                .check_navigation_bar_item_title(Components.ACCORDSDK)
                .check_page_title(Components.ACCORDSDK)
                .check_active_tab(UITextElements.GENERAL_INFORMATION)
            )

    @allure.suite("Паспорт компонента, вкладка 'Компоненты-потребители', отображение фильтра.")
    @allure.title("Паспорт компонента, вкладка 'Компоненты-потребители', отображение фильтра.")
    @allure.id("1522369")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1541923", LinkType.LINK, "TASK 1541923"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1522369", "TestCase 1522369")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.multiple_streams
    def test_consumer_components_tab_filter_display(self) -> None:
        """Паспорт компонента, вкладка 'Компоненты-потребители', отображение фильтра."""
        # Паспорт компонента_вкладка Компоненты-потребители_отображение фильтра
        with allure.step(
            "1. Предусловие: Пользователь с правами редактирования и чтения паспортов продуктов и компонентов "
            "авторизован в сервисе. Открыт реестр компонентов, выбран компонент и открыт его паспорт на вкладке "
            "'Компоненты-потребители'"
        ):
            self.component_page.click_on_link(UITextElements.ALL_COMPONENTS_TAB).click_on_link(Components.ACCORDSDK)
            self.component_information_page.click_on_link(UITextElements.CONSUMER_COMPONENTS_TAB)

        with allure.step("2. Нажать на иконку в виде воронки"):
            (
                self.component_information_page.click_on_funnel_icon()
                .check_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)
                .check_reset_filters_button()
            )

        with allure.step("3. Нажать Х (закрыть)"):
            self.component_information_page.click_on_close_filter_block_icon().check_reset_filters_button(
                visible_and_enabled=False
            )

        with allure.step(
            "4. Повторить шаги тест-кейса для паспорта версии компонента (вкладка 'Компоненты-потребители')"
        ):
            self.component_information_page.click_on_link(UITextElements.VERSIONS_TAB).click_on_link(Versions.ACCORDSDK)
            (
                self.component_version_information_page.click_on_link(UITextElements.CONSUMER_COMPONENTS_TAB)
                .click_on_funnel_icon()
                .check_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)
                .check_reset_filters_button()
                .click_on_close_filter_block_icon()
                .check_reset_filters_button(visible_and_enabled=False)
            )

        with allure.step(
            "5. Повторить шаги тест-кейса для паспорта конфигурации компонента (вкладка 'Компоненты-потребители')"
        ):
            self.component_version_information_page.click_on_link(UITextElements.PACKAGES_TAB).click_on_link(
                Packages.ACCORDSDK
            )
            self.component_package_information_page.click_on_link(
                UITextElements.ASSEMBLIES_BY_CONFIGURATION
            ).click_on_link(UITextElements.DEFAULT_BRAND_TRUNK)
            (
                self.component_assembly_by_configuration_page.click_on_link(UITextElements.CONSUMER_COMPONENTS_TAB)
                .click_on_funnel_icon()
                .check_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)
                .check_reset_filters_button()
                .click_on_close_filter_block_icon()
                .check_reset_filters_button(visible_and_enabled=False)
            )

    @allure.suite("Паспорт компонента, вкладка 'Версии'.")
    @allure.title("Паспорт компонента, вкладка 'Версии'.")
    @allure.id("1513494")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1544913", LinkType.LINK, "TASK 1544913"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1513494", "TestCase 1513494")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.multiple_streams
    def test_component_passport_version_tab(self) -> None:
        """Паспорт компонента, вкладка 'Версии'."""
        # Паспорт компонента_вкладка Версии
        with allure.step(
            "1. Предусловие: Пользователь авторизован в сервисе, открыт паспорт компонента на вкладке 'Версии'"
        ):
            self.component_page.click_on_link(UITextElements.ALL_COMPONENTS_TAB).click_on_link(Components.ACCORDSDK)
            self.component_information_page.click_on_link(UITextElements.VERSIONS_TAB)

        with allure.step("2. Проверить отображение информации на вкладке 'Версии'"):
            values = [
                Versions.ACCORDSDK,
                UITextElements.ANT_IVY,
                UITextElements.ABSENT,
                RegularExpressions.PATTERN_WINDOWS,
                UITextElements.NOT_SPECIFIED,
            ]
            (
                self.component_information_page.check_table_headings(self._TITLES)
                .check_table_text_values(values)
                .check_links_count(link_text=Versions.ACCORDSDK, count=1)
                .check_text("Всего 1 версия")
                .fill_in_search_input(Components.ACCORDSDK)
                .click_on_funnel_icon()
            )

    @allure.suite("Перейти по внешним ссылкам из паспорта компонента.")
    @allure.title("Перейти по внешним ссылкам из паспорта компонента.")
    @allure.id("1513330")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1545454", LinkType.LINK, "TASK 1545454"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1513330", "TestCase 1513330")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.multiple_streams
    def test_follow_external_links_from_component_passport(self) -> None:
        """Перейти по внешним ссылкам из паспорта компонента."""
        # Перейти по внешним ссылкам из паспорта компонента
        with allure.step("1. Предусловие: Пользователь авторизован в сервисе, открыта вкладка 'Компоненты'"):
            self.component_page.click_on_link(UITextElements.ALL_COMPONENTS_TAB)

        with allure.step("2. Выбрать компонент"):
            self.component_page.fill_in_search_input(Components.IGC).click_on_link(Components.IGC)

        with allure.step("3. Перейти по ссылке на документацию"):
            self.component_information_page.check_href(
                link_text=UITextElements.REGULATIONS,
                href="https://wiki.example.int/pages/viewpage.action?pageId=377096397",
                in_table=False,
            ).check_target_blank(UITextElements.REGULATIONS)

        with allure.step("4. Перейти по ссылке на Artifactory"):
            self.component_information_page.check_href(
                link_text=UITextElements.ARTIFACTORY,
                href="https://artifactory.example.ru/ui/repos/tree/General/tdc-local/main/igc",
                in_table=False,
            ).check_target_blank(UITextElements.ARTIFACTORY)

        with allure.step("5. Перейти по ссылке на регламент"):
            self.component_information_page.check_href(
                link_text=UITextElements.REGULATIONS,
                href="https://wiki.example.int/pages/viewpage.action?pageId=377096397",
                in_table=False,
            ).check_target_blank(UITextElements.REGULATIONS)

        with allure.step("6. Перейти по ссылке на лицензию"):
            self.component_information_page.click_on_title()
            (
                self.component_page.click_on_link(UITextElements.ALL_COMPONENTS_TAB)
                .fill_in_search_input(Components.IDENTITY_MODEL)
                .click_on_link(Components.IDENTITY_MODEL)
            )
            self.component_information_page.check_href(
                link_text=UITextElements.APACHE_2_0,
                href=f"https://licenses.nuget.org/{UITextElements.APACHE_2_0}",
                in_table=False,
            ).check_target_blank(UITextElements.APACHE_2_0)

    @allure.suite("Паспорт компонента, вкладка 'Компоненты-потребители', фильтр 'Зона техрадара' (работа).")
    @allure.title("Паспорт компонента, вкладка 'Компоненты-потребители', фильтр 'Зона техрадара' (работа).")
    @allure.id("1565478")
    @allure.description("Баг: Текст 'Всего <любое число> компонент(а/ов)' не отображается на странице.")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1578257", LinkType.LINK, "TASK 1578257"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1565478", "TestCase 1565478")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.multiple_streams
    def test_consumer_components_tab_filter_technical_radar_area(self) -> None:
        """Паспорт компонента, вкладка 'Компоненты-потребители', фильтр 'Зона техрадара' (работа)."""
        # Паспорт компонента_вкладка Компоненты-потребители_фильтр Зона техрадара_работа
        component_count_first_symbol = 7
        component_count_last_symbol = -11

        with allure.step(
            "1. Предусловие: Пользователь с правами редактирования и чтения паспортов продуктов и компонентов "
            "авторизован в сервисе. Открыт реестр компонентов, выбран компонент и открыт его паспорт на вкладке "
            "'Компоненты-потребители'"
        ):
            titles = [
                UITextElements.COMPONENT,
                UITextElements.TECHNICAL_RADAR_AREA,
            ]
            first_values = [
                Components.CRYPT_PASSWORD_FORGE,
                RadarAreaValues.RECOMMENDED,
            ]

            self._check_titles_and_values_in_table(
                first_page=self.component_page,
                second_page=self.component_information_page,
                first_link=UITextElements.ALL_COMPONENTS_TAB,
                second_link=Components.ACCORDSDK,
                titles=titles,
                values=first_values,
            )

        with allure.step("2. В фильтре 'Зона техрадара' выбрать одно любое значение"):
            (
                self.component_information_page.check_text_total_components_with_any_number()
                .click_on_funnel_icon()
                .check_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)
                .click_on_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)
                .click_on_element_in_combo_box_in_filter(RadarAreaValues.RECOMMENDED)
                .check_checkbox_with_text_in_combo_box_in_filter(RadarAreaValues.RECOMMENDED)
                .check_text_components_found_with_any_number()
            )
            temp_text_components_found = self.component_information_page.get_text_components_found_with_any_number()

        with allure.step("3. В фильтре 'Зона техрадара' выбрать еще одно любое значение"):
            (
                self.component_information_page.click_on_element_in_combo_box_in_filter(RadarAreaValues.PILOTED_BY)
                .check_checkbox_with_text_in_combo_box_in_filter(RadarAreaValues.PILOTED_BY)
                .check_text_components_found_with_any_number()
                .check_combo_box_list_and_text_in_filter(
                    text_in_combo_box=UITextElements.TECHNICAL_RADAR_AREA + UITextElements.COLON_SPACE_TWO,
                    list_combo_box_elements=RadarAreaValues,
                )
            )

        with allure.step("4. Закрыть выпадающий список"):
            self.component_information_page.check_combo_box_in_filter(
                placeholder=UITextElements.TECHNICAL_RADAR_AREA + UITextElements.COLON_SPACE_TWO
            ).click_on_combo_box_in_filter(
                placeholder=UITextElements.TECHNICAL_RADAR_AREA + UITextElements.COLON_SPACE_TWO
            )

        with allure.step("5. Открыть выпадающий список, проверить отображение выбранных значений"):
            (
                self.component_information_page.check_combo_box_in_filter(
                    placeholder=UITextElements.TECHNICAL_RADAR_AREA + UITextElements.COLON_SPACE_TWO
                )
                .click_on_combo_box_in_filter(
                    placeholder=UITextElements.TECHNICAL_RADAR_AREA + UITextElements.COLON_SPACE_TWO
                )
                .check_combo_box_list_and_text_in_filter(
                    text_in_combo_box=UITextElements.TECHNICAL_RADAR_AREA + UITextElements.COLON_SPACE_TWO,
                    list_combo_box_elements=RadarAreaValues,
                )
            )

        with allure.step("6. Выбрать все значения в фильтре"):
            (
                self.component_information_page.click_on_element_in_combo_box_in_filter(RadarAreaValues.INTERESTED_IN)
                .click_on_element_in_combo_box_in_filter(RadarAreaValues.AVOID)
                .click_on_element_in_combo_box_in_filter(RadarAreaValues.UNKNOWN)
                .check_text_components_found_with_any_number()
                .check_text(page_text=temp_text_components_found, visible=False)
            )
            temp_text_components_found = self.component_information_page.get_text_components_found_with_any_number()

        with allure.step("7. Нажать 'Сбросить фильтр"):
            (
                self.component_information_page.click_on_reset_filters_button()
                .check_text_total_components_with_any_number()
                .check_text(
                    page_text=temp_text_components_found[component_count_first_symbol:component_count_last_symbol],
                    exact=False,
                )
                .check_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)
                .check_table_text_values(first_values)
            )

        with allure.step(
            "8. Повторить шаги тест-кейса для паспорта версии компонента, вкладка 'Компоненты-потребители'"
        ):
            titles = [
                UITextElements.COMPONENT,
                UITextElements.TEXT_VERSION,
                UITextElements.TECHNICAL_RADAR_AREA,
            ]
            first_values = [
                Components.CRYPT_PASSWORD_FORGE,
                Versions.ONE_ONE,
                RadarAreaValues.RECOMMENDED,
            ]

            self._check_titles_and_values_in_table(
                first_page=self.component_information_page,
                second_page=self.component_version_information_page,
                first_link=UITextElements.VERSIONS_TAB,
                second_link=Versions.ACCORDSDK,
                titles=titles,
                values=first_values,
            )

            with allure.step("В фильтре 'Зона техрадара' выбрать одно любое значение"):
                (
                    self.component_version_information_page.check_text_total_components_with_any_number()
                    .click_on_funnel_icon()
                    .check_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)
                    .click_on_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)
                    .click_on_element_in_combo_box_in_filter(RadarAreaValues.RECOMMENDED)
                    .check_text_components_found_with_any_number()
                )
                temp_text_components_found = (
                    self.component_version_information_page.get_text_components_found_with_any_number()
                )

            with allure.step("В фильтре 'Зона техрадара' выбрать еще одно любое значение"):
                (
                    self.component_version_information_page.click_on_element_in_combo_box_in_filter(
                        RadarAreaValues.PILOTED_BY
                    )
                    .check_text_components_found_with_any_number()
                    .check_combo_box_list_and_text_in_filter(
                        text_in_combo_box=UITextElements.TECHNICAL_RADAR_AREA + UITextElements.COLON_SPACE_TWO,
                        list_combo_box_elements=RadarAreaValues,
                    )
                )

            with allure.step("Закрыть выпадающий список"):
                self.component_version_information_page.check_combo_box_in_filter(
                    placeholder=UITextElements.TECHNICAL_RADAR_AREA + UITextElements.COLON_SPACE_TWO
                ).click_on_combo_box_in_filter(
                    placeholder=UITextElements.TECHNICAL_RADAR_AREA + UITextElements.COLON_SPACE_TWO
                )

            with allure.step("Открыть выпадающий список, проверить отображение выбранных значений"):
                (
                    self.component_version_information_page.check_combo_box_in_filter(
                        placeholder=UITextElements.TECHNICAL_RADAR_AREA + UITextElements.COLON_SPACE_TWO
                    )
                    .click_on_combo_box_in_filter(
                        placeholder=UITextElements.TECHNICAL_RADAR_AREA + UITextElements.COLON_SPACE_TWO
                    )
                    .check_combo_box_list_and_text_in_filter(
                        text_in_combo_box=UITextElements.TECHNICAL_RADAR_AREA + UITextElements.COLON_SPACE_TWO,
                        list_combo_box_elements=RadarAreaValues,
                    )
                )

            with allure.step("Выбрать все значения в фильтре"):
                (
                    self.component_version_information_page.click_on_element_in_combo_box_in_filter(
                        RadarAreaValues.INTERESTED_IN
                    )
                    .click_on_element_in_combo_box_in_filter(RadarAreaValues.AVOID)
                    .click_on_element_in_combo_box_in_filter(RadarAreaValues.UNKNOWN)
                    .check_checkbox_with_text_in_combo_box_in_filter(RadarAreaValues.INTERESTED_IN)
                    .check_checkbox_with_text_in_combo_box_in_filter(RadarAreaValues.AVOID)
                    .check_text_components_found_with_any_number()
                    .check_text(page_text=temp_text_components_found, visible=False)
                )
                temp_text_components_found = (
                    self.component_version_information_page.get_text_components_found_with_any_number()
                )

            with allure.step("Нажать 'Сбросить фильтр"):
                (
                    self.component_version_information_page.click_on_reset_filters_button()
                    .check_text_total_components_with_any_number()
                    .check_text(
                        page_text=temp_text_components_found[component_count_first_symbol:component_count_last_symbol],
                        exact=False,
                    )
                    .check_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)
                    .check_table_text_values(first_values)
                )

        with allure.step(
            "9. Повторить шаги тест-кейса для паспорта конфигурации компонента, вкладка 'Компоненты-потребители'"
        ):
            titles = [
                UITextElements.COMPONENT,
                UITextElements.TEXT_VERSION,
                UITextElements.ASSEMBLY,
                UITextElements.CONFIGURATION,
                UITextElements.TECHNICAL_RADAR_AREA,
            ]
            first_values = [
                Components.UPRNG,
                Versions.ONE_SIX,
                "1.6.3.1400",
                UITextElements.LINUX_RELEASE_ONE_SIX_X,
                RadarAreaValues.UNKNOWN,
            ]

            self.component_version_information_page.click_on_link(UITextElements.PACKAGES_TAB).click_on_link(
                Packages.ACCORDSDK
            )

            self._check_titles_and_values_in_table(
                first_page=self.component_package_information_page,
                second_page=self.component_assembly_by_configuration_page,
                first_link=UITextElements.ASSEMBLIES_BY_CONFIGURATION,
                second_link=UITextElements.DEFAULT_BRAND_TRUNK,
                titles=titles,
                values=first_values,
            )

            with allure.step("В фильтре 'Зона техрадара' выбрать одно любое значение"):
                (
                    self.component_assembly_by_configuration_page.check_text_total_components_with_any_number()
                    .click_on_funnel_icon()
                    .check_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)
                    .click_on_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)
                    .click_on_element_in_combo_box_in_filter(RadarAreaValues.RECOMMENDED)
                    .check_checkbox_with_text_in_combo_box_in_filter(RadarAreaValues.RECOMMENDED)
                    .check_text(UITextElements.NOTHING_FOUND)
                    .check_text_components_found_with_any_number()
                )
                temp_text_components_found = (
                    self.component_assembly_by_configuration_page.get_text_components_found_with_any_number()
                )

            with allure.step("В фильтре 'Зона техрадара' выбрать еще одно любое значение"):
                (
                    self.component_assembly_by_configuration_page.click_on_element_in_combo_box_in_filter(
                        RadarAreaValues.PILOTED_BY
                    )
                    .check_text(UITextElements.NOTHING_FOUND)
                    .check_text_components_found_with_any_number()
                    .check_combo_box_list_and_text_in_filter(
                        text_in_combo_box=UITextElements.TECHNICAL_RADAR_AREA + UITextElements.COLON_SPACE_TWO,
                        list_combo_box_elements=RadarAreaValues,
                    )
                )

            with allure.step("Закрыть выпадающий список"):
                self.component_assembly_by_configuration_page.check_combo_box_in_filter(
                    placeholder=UITextElements.TECHNICAL_RADAR_AREA + UITextElements.COLON_SPACE_TWO
                ).click_on_combo_box_in_filter(
                    placeholder=UITextElements.TECHNICAL_RADAR_AREA + UITextElements.COLON_SPACE_TWO
                )

            with allure.step("Открыть выпадающий список, проверить отображение выбранных значений"):
                (
                    self.component_assembly_by_configuration_page.check_combo_box_in_filter(
                        placeholder=UITextElements.TECHNICAL_RADAR_AREA + UITextElements.COLON_SPACE_TWO
                    )
                    .click_on_combo_box_in_filter(
                        placeholder=UITextElements.TECHNICAL_RADAR_AREA + UITextElements.COLON_SPACE_TWO
                    )
                    .check_combo_box_list_and_text_in_filter(
                        text_in_combo_box=UITextElements.TECHNICAL_RADAR_AREA + UITextElements.COLON_SPACE_TWO,
                        list_combo_box_elements=RadarAreaValues,
                    )
                )

            with allure.step("Выбрать все значения в фильтре"):
                (
                    self.component_assembly_by_configuration_page.click_on_element_in_combo_box_in_filter(
                        RadarAreaValues.INTERESTED_IN
                    )
                    .click_on_element_in_combo_box_in_filter(RadarAreaValues.AVOID)
                    .click_on_element_in_combo_box_in_filter(RadarAreaValues.UNKNOWN)
                    .check_checkbox_with_text_in_combo_box_in_filter(RadarAreaValues.UNKNOWN)
                    .check_text_components_found_with_any_number()
                    .check_text(page_text=temp_text_components_found, visible=False)
                )
                temp_text_components_found = (
                    self.component_assembly_by_configuration_page.get_text_components_found_with_any_number()
                )

            with allure.step("Нажать 'Сбросить фильтр"):
                (
                    self.component_assembly_by_configuration_page.click_on_reset_filters_button()
                    .check_text_total_components_with_any_number()
                    .check_text(
                        temp_text_components_found[component_count_first_symbol:component_count_last_symbol],
                        exact=False,
                    )
                    .check_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)
                    .check_table_text_values(first_values)
                )

    @allure.suite("Перечень версий компонента, отображение неподдерживаемых версий.")
    @allure.title("Перечень версий компонента, отображение неподдерживаемых версий.")
    @allure.id("1513337")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1542742", LinkType.LINK, "TASK 1542742"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1513337", "TestCase 1513337")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.multiple_streams
    def test_list_of_component_versions_display_unsupported_versions(self) -> None:
        """Перечень версий компонента, отображение неподдерживаемых версий."""
        # Перечень версий компонента_отображение неподдерживаемых версий
        with allure.step("1. Пользователь авторизован в сервисе, открыта страница 'Компоненты'"):
            self.component_page.click_on_link(UITextElements.ALL_COMPONENTS_TAB)

        with allure.step(
            "2. В списке выбрать компонент, у которого более двух версий и есть неподдерживаемые версии (например, "
            "'librtpkcs11ecp') → перейти на вкладку 'Версии'"
        ):
            versions = [
                "2014.04",
                "2.13",
                "1.9",
                "1.8",
                Versions.ONE_FOUR,
            ]
            values = [
                "2014.04",
                UITextElements.ANT_IVY,
                UITextElements.ABSENT,
                "Не указаны",
                UITextElements.NOT_SPECIFIED,
            ]

            self.component_page.fill_in_search_input(Components.LIBRTPKCS_11_ECP).click_on_link(
                Components.LIBRTPKCS_11_ECP
            )
            (
                self.component_information_page.click_on_link(UITextElements.VERSIONS_TAB)
                .check_table_versions(versions)
                .check_table_headings(self._TITLES)
                .check_table_text_values(values)
            )

    @allure.suite("Паспорт компонента, дата последнего изменения данных о компоненте.")
    @allure.title("Паспорт компонента, дата последнего изменения данных о компоненте.")
    @allure.id("1565452")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1588835", LinkType.LINK, "TASK 1588835"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1565452", "TestCase 1565452")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_component_passport_date_of_last_change_of_component_data(self) -> None:
        """Паспорт компонента, дата последнего изменения данных о компоненте."""
        # Паспорт компонента_Дата последнего изменения данных о компоненте
        pattern_string = re.compile(r"\b(0[1-9]|[12]\d|3[01])\.(0[1-9]|1[0-2])\.\d{4}\s([01]\d|2[0-3]):[0-5]\d\b")

        with allure.step("1. Предусловие: Пользователь авторизован в сервисе, открыта страница 'Компоненты'"):
            self.component_page.click_on_link(UITextElements.ALL_COMPONENTS_TAB)

        with allure.step("2. В списке выбрать любой компонент"):
            self.component_page.click_on_link(Components.ACCORDSDK)
            last_sync_date = self.component_information_page.get_text_in_tab_general_information(
                title=UITextElements.LAST_SYNC_DATE
            )

        with allure.step(
            "3. В реестре компонентов выбрать любой компонент, перейти в сборку по конфигурации → 'Запустить "
            "сканирование конфигурации'. Вернуться в паспорт компонента, проверить поле 'Дата последней синхронизации'"
        ):
            self.component_information_page.click_on_link(UITextElements.VERSIONS_TAB).click_on_link(Versions.ACCORDSDK)
            self.product_version_information_page.click_on_link(UITextElements.PACKAGES_TAB).click_on_link(
                Packages.ACCORDSDK
            )
            self.component_package_information_page.click_on_link(
                UITextElements.ASSEMBLIES_BY_CONFIGURATION
            ).click_on_link(UITextElements.DEFAULT_BRAND_TRUNK)
            (
                self.component_assembly_by_configuration_page.click_on_element_with_text(
                    "Запустить сканирование конфигурации"
                )
                .wait_for_page_ready()
                .click_on_title()
            )
            self.component_page.click_on_link(UITextElements.ALL_COMPONENTS_TAB).click_on_link(Components.ACCORDSDK)
            (
                self.component_information_page.refresh_page()
                .check_text(pattern_string)
                .check_text(page_text=last_sync_date, visible=False)
            )

    def _check_titles_and_values_in_table(
        self,
        first_page: Page,
        second_page: Page,
        first_link: str,
        second_link: str,
        titles: list[str],
        values: list[str],
    ) -> None:
        """Проверка заголовков и значений в таблице.

        :param first_page: Объект первой страницы.
        :param second_page: Объект второй страницы.
        :param first_link: Первая ссылка по которой необходимо перейти.
        :param second_link: Вторая ссылка по которой необходимо перейти.
        :param titles: Заголовки таблицы.
        :param values: Значения в первой строке таблицы.
        """
        first_page.click_on_link(first_link).click_on_link(second_link)
        (
            second_page.click_on_link(UITextElements.CONSUMER_COMPONENTS_TAB)
            .check_table_headings(titles)
            .check_table_text_values(values)
        )
