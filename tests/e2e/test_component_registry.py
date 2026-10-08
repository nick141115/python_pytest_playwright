import allure
import pytest
from allure_commons.types import LinkType

from src.constants.components import Components
from src.constants.radar_area_values import RadarAreaValues
from src.constants.test_inputs import TestInputs
from src.constants.ui_text_elements import UITextElements
from src.constants.versions import Versions
from tests.base.base_test import BaseTest


@allure.parent_suite("Реестр компонентов.")
@allure.epic("Реестр компонентов.")
@allure.sub_suite("Реестр компонентов.")
@allure.severity(allure.severity_level.CRITICAL)
class TestComponentRegistry(BaseTest):
    """Реестр компонентов."""

    _SHOW_ALL_COMPONENTS = "Показать все компоненты"

    @allure.suite("Реестр компонентов, отображение.")
    @allure.title("Реестр компонентов, отображение.")
    @allure.id("1513491")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1543718", LinkType.LINK, "TASK 1543718"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1513491", "TestCase 1513491")
    @pytest.mark.multiple_streams
    def test_component_registry_display(self) -> None:
        """Реестр компонентов, отображение."""
        # Реестр компонентов_отображаение
        version_4_5_0 = "4.5.0"
        system_io_pipelines = "System.IO.Pipelines"
        version_4_5 = "4.5"
        version_4_5_2 = "4.5.2"
        default = "default"

        with allure.step(
            "1. Пользователь авторизован в сервисе, открыт реестр компонентов, отсутствуют избранные компоненты; "
            "2. Проверить отображение страницы по умолчанию;"
        ):
            self._impersonate_as_user_with_read_or_write_permissions(write_permissions=False)
            self.component_page.check_text("Отсутствуют избранные компоненты").check_links_count(
                link_text=self._SHOW_ALL_COMPONENTS, count=1
            )

        with allure.step("3. Нажать 'Показать все компоненты'"):
            list_first_part = [
                "minipass-pipeline",
                Components.PIP,
                "Pipelines.Sockets.Unofficial",
                "python-pip-whl",
                "python3-pip",
                system_io_pipelines,
            ]
            list_second_part = [
                "System.IO.Pipes",
                "System.IO.Pipes.AccessControl",
                "unpipe",
                "WireMock.Net.OpenApiParser",
            ]
            (
                self.component_page.click_on_link(self._SHOW_ALL_COMPONENTS)
                .check_text_total_components_with_any_number()
                .fill_in_search_input(Components.PIP)
                .check_favorites_indicator(count=10)
                .check_table_components_or_products(strings=list_first_part + list_second_part)
            )

        with allure.step("4. В списке выбрать любой компонент и раскрыть экспандер"):
            list_of_versions = [
                "8.0",
                "7.0",
                "6.0",
                "5.0",
                version_4_5,
            ]
            (
                self.component_page.click_on_expander(text_with_expander=system_io_pipelines)
                .check_favorites_indicator(count=15)
                .check_table_components_or_products(strings=list_first_part + list_of_versions + list_second_part)
            )

        with allure.step("5. В списке выбрать любую версию компонента и раскрыть экспандер"):
            list_of_packages = [
                "4.5.3",
                version_4_5_2,
                version_4_5_0,
            ]
            (
                self.component_page.click_on_expander(text_with_expander=version_4_5)
                .check_favorites_indicator(count=18)
                .check_table_components_or_products(
                    strings=list_first_part + list_of_versions + list_of_packages + list_second_part
                )
            )

        with allure.step("6. В списке выбрать любой пакет компонента и раскрыть экспандер"):
            list_of_assemblies = [default]
            (
                self.component_page.click_on_expander(version_4_5_0)
                .check_favorites_indicator(count=19)
                .check_table_components_or_products(
                    strings=list_first_part
                    + list_of_versions
                    + list_of_packages
                    + list_of_assemblies
                    + list_second_part
                )
            )

        with allure.step("7. Нажать на название любого компонента"):
            self.component_page.check_href(
                link_text=system_io_pipelines, href="/components/component/system_io_pipelines"
            )

        with allure.step("8. Нажать на номер любой версии компонента"):
            self.component_page.check_href(
                link_text=version_4_5, href="/components/componentVersion/system_io_pipelines__4_5", exact=True
            )

        with allure.step("9. Нажать на любой пакет компонента"):
            self.component_page.check_href(
                link_text=version_4_5_2,
                href="/components/componentPackage/nuget__System_IO_Pipelines__4_5_2",
            )

        with allure.step("10. Нажать на любую сборку по конфигурации"):
            (
                self.component_page.check_href(
                    link_text=default,
                    href="/components/componentConfiguration/"
                    "5bed7a4cc08a75806ae243d4635f41c0c4415fbc74a8acb255d454aaedf9f2d6",
                ).click_on_funnel_icon()
            )

    @allure.suite("Реестр компонентов, фильтр 'Верифицированная версия', отображение.")
    @allure.title("Реестр компонентов, фильтр 'Верифицированная версия', отображение.")
    @allure.id("1536276")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1561612", LinkType.LINK, "TASK 1561612"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1536276", "TestCase 1536276")
    @pytest.mark.multiple_streams
    def test_component_registry_filter_verified_version_display(self) -> None:
        """Реестр компонентов, фильтр 'Верифицированная версия', отображение."""
        # Реестр компонентов_фильтр Верифицированная версия_ отображение
        with allure.step(
            "1. Предусловие: Пользователь с правами на чтение паспортов компонентов авторизован в сервисе. Открыт "
            "реестр компонентов"
        ):
            self._impersonate_as_user_with_read_or_write_permissions(write_permissions=False)
            self.component_page.click_on_title().click_on_link(UITextElements.ALL_COMPONENTS_TAB)

        with allure.step("2. Открыть блок фильтров"):
            (
                self.component_page.click_on_funnel_icon()
                .check_reset_filters_button()
                .check_combo_box_in_filter(UITextElements.VERIFIED_VERSION)
            )

        with allure.step("3. Нажать на поле фильтра"):
            (
                self.component_page.click_on_combo_box_in_filter(UITextElements.VERIFIED_VERSION)
                .click_on_element_with_text(UITextElements.YES)
                .click_on_reset_filters_button()
                .click_on_combo_box_in_filter(UITextElements.VERIFIED_VERSION)
                .click_on_element_with_text(UITextElements.NO)
            )

        with allure.step("4. Перейти в паспорт версии компонента, вкладка 'Пакеты' → Открыть блок фильтров "):
            self.component_page.click_on_link(Components.ACCORDSDK)
            self.component_information_page.click_on_link(UITextElements.VERSIONS_TAB).click_on_link(Versions.ACCORDSDK)
            (
                self.component_version_information_page.click_on_link(UITextElements.PACKAGES_TAB)
                .click_on_funnel_icon()
                .check_reset_filters_button()
                .check_combo_box_in_filter(UITextElements.VERIFIED_VERSION)
            )

        with allure.step("5. Нажать на поле фильтра"):
            (
                self.component_version_information_page.click_on_combo_box_in_filter(UITextElements.VERIFIED_VERSION)
                .click_on_element_with_text(UITextElements.YES)
                .click_on_reset_filters_button()
                .click_on_combo_box_in_filter(UITextElements.VERIFIED_VERSION)
                .click_on_element_with_text(UITextElements.NO)
            )

        with allure.step(
            "6. Проверить наличие фильтра в блоке фильтра на страницах: паспорт компонента → вкладка 'Версии', "
            "паспорт компонента → вкладка 'Компоненты-потребители', паспорт версии компонента → вкладка "
            "'Компоненты-потребители'"
        ):
            self.component_version_information_page.click_on_link(Components.ACCORDSDK)
            (
                self.component_information_page.click_on_link(UITextElements.VERSIONS_TAB)
                .click_on_funnel_icon()
                .check_reset_filters_button()
                .check_combo_box_in_filter(placeholder=UITextElements.VERIFIED_VERSION, visible=False)
                .click_on_link(UITextElements.CONSUMER_COMPONENTS_TAB)
                .click_on_funnel_icon()
                .check_reset_filters_button()
                .check_combo_box_in_filter(placeholder=UITextElements.VERIFIED_VERSION, visible=False)
                .click_on_link(UITextElements.VERSIONS_TAB)
                .click_on_link(Versions.ACCORDSDK)
            )
            (
                self.component_version_information_page.click_on_link(UITextElements.CONSUMER_COMPONENTS_TAB)
                .click_on_funnel_icon()
                .check_reset_filters_button()
                .check_combo_box_in_filter(placeholder=UITextElements.VERIFIED_VERSION, visible=False)
            )

    @allure.suite("Реестр компонентов, блок фильтра, отображение.")
    @allure.title("Реестр компонентов, блок фильтра, отображение.")
    @allure.id("1565480")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1579173", LinkType.LINK, "TASK 1579173"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1565480", "TestCase 1565480")
    @pytest.mark.multiple_streams
    def test_component_registry_filter_block_display(self) -> None:
        """Реестр компонентов, блок фильтра, отображение."""
        # Реестр компонентов_блок фильтра_отображаение
        with allure.step(
            "1. Предусловие: Пользователь с правами на чтение паспортов компонентов авторизован в сервисе, открыт "
            "реестр компонентов на вкладке 'Все компоненты'"
        ):
            self._impersonate_as_user_with_read_or_write_permissions(write_permissions=False)
            self.component_page.click_on_title().click_on_link(UITextElements.ALL_COMPONENTS_TAB)

        with allure.step("2. Нажать на иконку воронки"):
            (
                self.component_page.click_on_funnel_icon()
                .click_on_close_filter_block_icon()
                .click_on_funnel_icon()
                .check_reset_filters_button()
                .check_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)
                .check_combo_box_in_filter(UITextElements.TEXT_PROGRAMMING_LANGUAGE)
                .check_combo_box_in_filter(UITextElements.LICENSE)
                .check_combo_box_in_filter(UITextElements.TECHNICAL_EXPERT)
                .check_combo_box_in_filter(UITextElements.COMPONENT_TYPE)
                .check_combo_box_in_filter(UITextElements.DEVELOPMENT_STATUS)
                .check_combo_box_in_filter("Документация")
                .check_combo_box_in_filter(UITextElements.VERIFIED_VERSION)
                .check_combo_box_in_filter(UITextElements.PACKAGE_MANAGER)
                .check_combo_box_in_filter("Продукт-потребитель")
                .check_combo_box_in_filter(UITextElements.RESPONSIBLE_FOR_IMPLEMENTATION)
                .check_combo_box_in_filter(UITextElements.LINKS)
                .check_combo_box_in_filter(UITextElements.PLATFORM)
                .check_combo_box_in_filter("Компонент-потребитель")
                .check_combo_box_in_filter(UITextElements.OWNER)
            )

        with allure.step("3. Обновить страницу сервиса"):
            self.component_page.refresh_page().check_reset_filters_button(
                visible_and_enabled=False
            ).click_on_funnel_icon()

    @allure.suite("Реестр компонентов, фильтр 'Зона техрадара'.")
    @allure.title("Реестр компонентов, фильтр 'Зона техрадара'.")
    @allure.id("1565481")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1579183", LinkType.LINK, "TASK 1579183"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1565481", "TestCase 1565481")
    @pytest.mark.multiple_streams
    def test_component_registry_filter_technical_radar_area(self) -> None:
        """Реестр компонентов, фильтр 'Зона техрадара'."""
        # Реестр компонентов_фильтр Зона техрадара
        with allure.step(
            "1. Предусловие: Пользователь с правами на чтение паспортов компонентов авторизован в сервисе, открыт "
            "реестр компонентов на вкладке 'Все компоненты', открыт блок фильтров"
        ):
            title = ["Компонент, версия, пакет, конфигурация"]
            first_value = ["@aashutoshrathi/word-wrap"]

            self._impersonate_as_user_with_read_or_write_permissions(write_permissions=False)
            (
                self.component_page.click_on_title()
                .click_on_link(UITextElements.ALL_COMPONENTS_TAB)
                .click_on_funnel_icon()
                .check_reset_filters_button()
                .check_table_headings(title)
                .check_table_text_values(first_value)
            )

        with allure.step("2. В фильтре 'Зона техрадара' нажать на экспандер"):
            self.component_page.check_combo_box_in_filter(
                placeholder=UITextElements.TECHNICAL_RADAR_AREA
            ).click_on_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)

        with allure.step("3. В фильтре 'Зона техрадара' выбрать одно любое значение"):
            value = [Components.BASH]

            (
                self.component_page.check_text_total_components_with_any_number()
                .click_on_element_in_combo_box_in_filter(RadarAreaValues.RECOMMENDED)
                .check_checkbox_with_text_in_combo_box_in_filter(RadarAreaValues.RECOMMENDED)
                .check_text_components_found_with_any_number()
                .check_table_text_values(value)
            )
            temp_text_components_found = self.component_page.get_text_components_found_with_any_number()

        with allure.step("4. В фильтре 'Зона техрадара' выбрать еще одно любое значение"):
            (
                self.component_page.click_on_element_in_combo_box_in_filter(RadarAreaValues.PILOTED_BY)
                .check_combo_box_list_and_text_in_filter(
                    text_in_combo_box=UITextElements.TECHNICAL_RADAR_AREA + UITextElements.COLON_SPACE_TWO,
                    list_combo_box_elements=RadarAreaValues,
                )
                .check_checkbox_with_text_in_combo_box_in_filter(RadarAreaValues.PILOTED_BY)
                .check_text(temp_text_components_found, False)
            )

        with allure.step("5. Закрыть выпадающий список"):
            self.component_page.check_combo_box_in_filter(
                placeholder=UITextElements.TECHNICAL_RADAR_AREA + UITextElements.COLON_SPACE_TWO
            ).click_on_combo_box_in_filter(
                placeholder=UITextElements.TECHNICAL_RADAR_AREA + UITextElements.COLON_SPACE_TWO
            )

        with allure.step("6. Открыть выпадающий список, проверить отображение выбранных значений"):
            (
                self.component_page.check_combo_box_in_filter(
                    placeholder=UITextElements.TECHNICAL_RADAR_AREA + UITextElements.COLON_SPACE_TWO
                )
                .click_on_combo_box_in_filter(
                    placeholder=UITextElements.TECHNICAL_RADAR_AREA + UITextElements.COLON_SPACE_TWO
                )
                .check_combo_box_list_and_text_in_filter(
                    text_in_combo_box=UITextElements.TECHNICAL_RADAR_AREA + UITextElements.COLON_SPACE_TWO,
                    list_combo_box_elements=RadarAreaValues,
                )
                .check_checkbox_with_text_in_combo_box_in_filter(RadarAreaValues.RECOMMENDED)
                .check_checkbox_with_text_in_combo_box_in_filter(RadarAreaValues.PILOTED_BY)
            )

        with allure.step("7. Выбрать все значения в фильтре"):
            (
                self.component_page.click_on_element_in_combo_box_in_filter(RadarAreaValues.INTERESTED_IN)
                .click_on_element_in_combo_box_in_filter(RadarAreaValues.AVOID)
                .click_on_element_in_combo_box_in_filter(RadarAreaValues.UNKNOWN)
                .check_checkbox_with_text_in_combo_box_in_filter(RadarAreaValues.INTERESTED_IN)
                .check_checkbox_with_text_in_combo_box_in_filter(RadarAreaValues.AVOID)
                .check_checkbox_with_text_in_combo_box_in_filter(RadarAreaValues.UNKNOWN)
            )
            temp_text_components_found = self.component_page.get_text_components_found_with_any_number()

        with allure.step("8. Нажать 'Сбросить фильтр"):
            component_count_first_symbol = 7
            component_count_last_symbol = -11

            (
                self.component_page.click_on_reset_filters_button()
                .check_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)
                .check_table_text_values(first_value)
                .check_text(
                    page_text=temp_text_components_found[component_count_first_symbol:component_count_last_symbol],
                    exact=False,
                )
            )

    @allure.suite("Реестр компонентов, вкладка 'Избранное', нет избранного.")
    @allure.title("Реестр компонентов, вкладка 'Избранное', нет избранного.")
    @allure.id("1567145")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1580041", LinkType.LINK, "TASK 1580041"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1567145", "TestCase 1567145")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.multiple_streams
    def test_component_registry_favorites_tab_no_favorites(self) -> None:
        """Реестр компонентов, вкладка 'Избранное', нет избранного."""
        # Реестр компонентов_вкладка Избранное_нет избранного
        with allure.step(
            "1. Предусловие: Пользователь с правами на чтение паспортов компонентов авторизован в сервисе, открыт "
            "реестр компонентов на вкладке 'Все компоненты', отсутствуют избранные субъекты компонента"
        ):
            self._impersonate_as_user_with_read_or_write_permissions(write_permissions=False)
            self.component_page.click_on_title().click_on_link(UITextElements.ALL_COMPONENTS_TAB)

        with allure.step("2. Перейти на вкладку 'Избранное'"):
            self.component_page.click_on_link(UITextElements.FAVORITES).check_text("Отсутствуют избранные компоненты")

        with allure.step("3. Нажать 'Показать все компоненты'"):
            (
                self.component_page.click_on_link(self._SHOW_ALL_COMPONENTS)
                .check_text_total_components_with_any_number()
                .check_active_tab(UITextElements.ALL_COMPONENTS_TAB)
            )

    @allure.suite("Поиск компонента, невалидные данные")
    @allure.title("Поиск компонента, невалидные данные")
    @allure.id("1513326")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1534643", LinkType.LINK, "TASK 1534643"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1513326", "TestCase 1513326")
    @pytest.mark.multiple_streams
    def test_component_search_invalid_data(self) -> None:
        """Поиск компонента, невалидные данные."""
        # Поиск_невалидные данные
        with allure.step("1. Предусловие: Пользователь авторизован в сервисе, открыта страница 'Компоненты'"):
            self.component_page.click_on_link(UITextElements.ALL_COMPONENTS_TAB)

        with allure.step("2. В поле поиска ввести: наименование несуществующего компонента/цифры/спец символы"):
            (
                self.component_page.fill_in_search_input(TestInputs.SPECIAL_CHARACTERS)
                .check_text_components_found(count=0)
                .check_text(UITextElements.NOTHING_FOUND)
            )

    @allure.suite("Поиск компонента, валидные данные")
    @allure.title("Поиск компонента, валидные данные")
    @allure.id("1513325")
    @allure.description("Автотест иногда падает из-за тормозов стенда.")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1535707", LinkType.LINK, "TASK 1535707"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1513325", "TestCase 1513325")
    @pytest.mark.multiple_streams
    def test_component_search_valid_data(self) -> None:
        """Поиск компонента, валидные данные."""
        # Поиск_валидные данные
        components_found = 1

        with allure.step(
            "1. Предусловие: Пользователь авторизован в сервисе, открыта страница 'Компоненты' → Вкладка 'Все "
            "компоненты'"
        ):
            self.component_page.click_on_link(
                UITextElements.ALL_COMPONENTS_TAB
            ).check_text_total_components_with_any_number()

        with allure.step("2. В поле поиска ввести часть наименования компонента"):
            (
                # Убираем у константы `Components.ACCORDSDK` последний символ
                self.component_page.fill_in_search_input(Components.ACCORDSDK[:-1])
                .check_cross_icon()
                # Проверяем, что текст 'accordsd' выделен жёлтым цветом
                .check_yellow_backlight(Components.ACCORDSDK[:-1])
                .check_text_components_found(components_found)
            )

        with allure.step("3. Изменить поисковый запрос, ввести пробелы перед и после наименования компонента"):
            (
                self.component_page.fill_in_search_input(f" {Components.ACCORDSDK} ")
                .check_yellow_backlight(Components.ACCORDSDK)
                .check_text_components_found(components_found)
            )

        with allure.step("4. Очистить поле поиска, нажав крестик"):
            (
                self.component_page.click_on_cross_icon()
                .check_search_input("")
                .check_text_total_components_with_any_number()
            )

        with allure.step(
            "5. В поле поиска ввести наименование компонента в верхнем регистре/смешанном регистре/нижнем регистре"
        ):
            (
                self.component_page.fill_in_search_input(Components.ACCORDSDK.upper())
                .check_yellow_backlight(Components.ACCORDSDK)
                .check_text_components_found(components_found)
            )

        with allure.step("6. Перейти к интересующему результату поиска"):
            self.component_page.click_on_link(Components.ACCORDSDK)
            self.component_information_page.check_first_combo_box(UITextElements.ABSENT)

        with allure.step("7. Вернуться в реестр компонентов"):
            self.component_information_page.click_on_title()
            (
                self.component_page.click_on_link(UITextElements.ALL_COMPONENTS_TAB)
                .check_text_total_components_with_any_number()
                .check_search_input("")
            )

    @allure.suite("Реестр компонентов, переход по ссылкам.")
    @allure.title("Реестр компонентов, переход по ссылкам.")
    @allure.id("1567144")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1587940", LinkType.LINK, "TASK 1587940"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1567144", "TestCase 1567144")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.multiple_streams
    def test_component_registry_clicking_on_links(self) -> None:
        """Реестр компонентов, переход по ссылкам."""
        # Реестр компонентов_переход по ссылкам
        documentation_version_10_2 = "Документация (по версии 10.2)"
        component_fmt = "fmt"
        license_mit = "MIT"

        with allure.step(
            "1. Предусловие: Пользователь с правами на чтение паспортов компонентов авторизован в сервисе, открыт "
            "паспорт компонента на вкладке 'Общая информация'"
        ):
            (
                self.component_page.click_on_link(UITextElements.ALL_COMPONENTS_TAB)
                .fill_in_search_input(component_fmt)
                .click_on_link(component_fmt)
            )

        with allure.step("2. Перейти по ссылке на документацию последней версии"):
            self.component_information_page.check_target_blank(documentation_version_10_2).check_href(
                link_text=documentation_version_10_2,
                href="https://tfs.example.ru/tfs/exampletc1/DEP_Components/_git/contrib_fmt?"
                "path=%2FREADME.md&version=GBdevelop",
                in_table=False,
            )

        with allure.step("3. Перейти по ссылке на Artifactory"):
            self.component_information_page.check_target_blank(UITextElements.ARTIFACTORY).check_href(
                link_text=UITextElements.ARTIFACTORY,
                href="https://10.0.23.87/ui/repos/tree/General/components-conan/platform-1.6/fmt",
                in_table=False,
            )

        with allure.step("4. Перейти по ссылке на лицензию"):
            self.component_information_page.check_target_blank(license_mit).check_href(
                link_text=license_mit,
                href="https://tfs.example.ru/tfs/exampletc1/DEP_Components/_git/contrib_fmt?"
                "path=%2FLICENSE&version=GBdevelop",
                in_table=False,
            )
