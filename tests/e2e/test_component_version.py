import allure
import pytest
from allure_commons.types import LinkType

from src.constants.components import Components
from src.constants.lists import Lists
from src.constants.packages import Packages
from src.constants.radar_area_values import RadarAreaValues
from src.constants.regular_expressions import RegularExpressions
from src.constants.test_inputs import TestInputs
from src.constants.ui_text_elements import UITextElements
from src.constants.versions import Versions
from tests.base.base_test import BaseTest


@allure.parent_suite("Версия компонента.")
@allure.epic("Версия компонента.")
@allure.sub_suite("Версия компонента.")
@allure.severity(allure.severity_level.CRITICAL)
class TestComponentVersion(BaseTest):
    """Версия компонента."""

    @pytest.fixture
    def set_development_status(self, request: pytest.FixtureRequest) -> None:
        """Фикстура возвращения статуса разработки к первоначальному после автотеста.

        :param request: Значение статуса разработки передаваемое в фикстуру.
        """
        yield

        value = request.param

        with allure.step("Возвращаем стенд к первоначальному состоянию"):
            self._impersonate_as_user_with_read_or_write_permissions(write_permissions=True)
            self._setup()
            (
                self.component_version_information_page.click_on_first_combo_box()
                .click_on_element_with_text(value)
                .refresh_page()
                .check_first_combo_box(value)
            )

    @allure.suite("Версия компонента, посмотреть сведения.")
    @allure.title("Версия компонента, посмотреть сведения.")
    @allure.id("1513327")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1539687", LinkType.LINK, "TASK 1539687"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1513327", "TestCase 1513327")
    @pytest.mark.multiple_streams
    def test_component_version_view_information(self) -> None:
        """Версия компонента, посмотреть сведения."""
        # Версия компонента_ посмотреть сведения
        with allure.step(
            "1. Предусловие: Пользователь авторизован в сервисе, открыта страница 'Компоненты', выбран один из "
            "компонентов списка, выбрана версия компонента."
        ):
            self._impersonate_as_user_with_read_or_write_permissions(write_permissions=False)
            self._setup()

        with allure.step("2. Проверить отображение информации по выбранной версии компонента"):
            (
                self.component_version_information_page.check_page_title(UITextElements.VERSION_ONE)
                .check_favorites_indicator()
                .check_active_tab(UITextElements.GENERAL_INFORMATION)
                .check_title_and_text_in_tab_general_information(
                    title=UITextElements.DEVELOPMENT_STATUS, text=UITextElements.DASH
                )
                .check_title_and_text_in_tab_general_information(
                    title=UITextElements.PACKAGE_MANAGERS, text=UITextElements.ANT_IVY
                )
                .check_title_and_text_in_tab_general_information(
                    title=UITextElements.PLATFORMS, text=RegularExpressions.PATTERN_WINDOWS
                )
                .check_title_and_text_in_tab_general_information(
                    title=UITextElements.LICENSE, text=UITextElements.LICENSES_LINK
                )
                .check_links_count(link_text=UITextElements.REGULATIONS, count=1)
                .check_links_count(link_text=UITextElements.PACKAGES_TAB, count=1)
                .check_links_count(link_text=UITextElements.CONSUMER_PRODUCTS_TAB, count=1)
                .check_links_count(link_text=UITextElements.CONSUMER_COMPONENTS_TAB, count=1)
            )

    @allure.suite("Версия компонента, редактирование статуса.")
    @allure.title("Версия компонента, редактирование статуса.")
    @allure.id("1521334")
    @allure.description("Баг: при выборе значения в combobox'е иногда значение не сохраняется.")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1566860", LinkType.LINK, "TASK 1566860"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1521334", "TestCase 1521334")
    @pytest.mark.parametrize("set_development_status", [UITextElements.ABSENT], indirect=True)
    def test_component_version_editing_status(self, set_development_status: None) -> None:
        """Версия компонента, редактирование статуса.

        :param set_development_status: Фикстура возвращения статуса разработки к первоначальному после автотеста.
        """
        # Версия компонента_редактирование статуса
        with allure.step(
            "1. Предусловие: Пользователь с правами редактирования паспортов компонентов авторизован в сервисе, "
            "открыта страница 'Компоненты', выбран один из компонентов списка, выбрана версия компонента, статус "
            "разработки 'Не указан'."
        ):
            self._setup()

        with allure.step("2. Проверить отображение информации в поле 'Статус разработки'"):
            self.component_version_information_page.check_first_combo_box(UITextElements.ABSENT)

        with allure.step("3. Установить курсор в поле 'Статус разработки'"):
            self.component_version_information_page.click_on_first_combo_box()

        with allure.step("4. Выбрать любой статус кроме 'Не указан' и 'Не поддерживается'"):
            (
                self.component_version_information_page.click_on_element_with_text(UITextElements.DEVELOPING)
                .refresh_page()
                .check_first_combo_box(UITextElements.DEVELOPING)
            )

        with allure.step("5. Выбрать любую другую версию компонента и вернуться обратно в первоначальную версию"):
            (
                self.component_page.click_on_title()
                .click_on_link(UITextElements.ALL_COMPONENTS_TAB)
                .click_on_link(Components.ACETAO)
            )
            self.component_information_page.click_on_link(UITextElements.VERSIONS_TAB).click_on_link(Versions.ACETAO)
            self.component_version_information_page.click_on_title()
            self.component_page.click_on_link(UITextElements.ALL_COMPONENTS_TAB).click_on_link(Components.ACCORDSDK)
            (
                self.component_information_page.click_on_link(UITextElements.VERSIONS_TAB).click_on_link(
                    Versions.ACCORDSDK
                )
            )
            self.component_version_information_page.check_first_combo_box(UITextElements.DEVELOPING)

    @allure.suite("Паспорт версии компонента, посмотреть сведения.")
    @allure.title("Паспорт версии компонента, посмотреть сведения.")
    @allure.id("1565459")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1585936", LinkType.LINK, "TASK 1585936"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1565459", "TestCase 1565459")
    @pytest.mark.multiple_streams
    def test_component_version_view_details(self) -> None:
        """Паспорт версии компонента, посмотреть сведения."""
        # Паспорт версии компонента_ посмотреть сведения
        with allure.step(
            "1. Предусловие: Пользователь авторизован в сервисе, открыта страница 'Компоненты', выбран один из "
            "компонентов списка, выбрана версия компонента"
        ):
            self._impersonate_as_user_with_read_or_write_permissions(write_permissions=False)
            self._setup()

        with allure.step("2. Проверить отображение информации по выбранной версии компонента"):
            with allure.step("Вкладка 'Общая информация'"):
                (
                    self.component_version_information_page.check_active_tab(UITextElements.GENERAL_INFORMATION)
                    .check_text_in_navigation_bar(
                        UITextElements.COMPONENTS + Components.ACCORDSDK + UITextElements.VERSION_ONE
                    )
                    .check_links_count(link_text=UITextElements.COMPONENTS, count=3)
                    .check_links_count(link_text=Components.ACCORDSDK, count=1)
                    .check_favorites_indicator()
                    .check_text(UITextElements.VERSION_ONE, nth=1)
                    .check_title_and_text_in_tab_general_information(
                        title=UITextElements.DEVELOPMENT_STATUS, text=UITextElements.DASH
                    )
                    .check_title_and_text_in_tab_general_information(
                        title=UITextElements.PACKAGE_MANAGERS, text=UITextElements.ANT_IVY
                    )
                    .check_title_and_text_in_tab_general_information(
                        title=UITextElements.PLATFORMS, text=RegularExpressions.PATTERN_WINDOWS
                    )
                    .check_title_and_text_in_tab_general_information(
                        title=UITextElements.LICENSE, text=UITextElements.LICENSES_LINK
                    )
                    .check_links_count(link_text=UITextElements.REGULATIONS, count=1)
                )

            with allure.step("Вкладка 'Пакеты'"):
                titles = [
                    UITextElements.TEXT_PACKAGE,
                    UITextElements.VERIFIED_VERSION,
                    UITextElements.PACKAGE_MANAGER,
                ]
                values = [Packages.ACCORDSDK, "", UITextElements.ANT_IVY]

                (
                    self.component_version_information_page.click_on_link(UITextElements.PACKAGES_TAB)
                    .check_active_tab(UITextElements.PACKAGES_TAB)
                    .check_text_total_packages_with_any_number()
                    .check_table_headings(titles)
                    .check_table_text_values(values)
                    .check_links_count(link_text=Packages.ACCORDSDK, count=1)
                    .fill_in_search_input(TestInputs.SPECIAL_CHARACTERS)
                    .click_on_funnel_icon()
                )

            with allure.step("Вкладка 'Продукты-потребители'"):
                values = [UITextElements.CONNECT, Versions.FIVE_TWO_ZERO]

                (
                    self.component_version_information_page.click_on_link(UITextElements.CONSUMER_PRODUCTS_TAB)
                    .check_active_tab(UITextElements.CONSUMER_PRODUCTS_TAB)
                    .check_text_total_products_with_any_number()
                    .check_table_headings(Lists.TITLES_TABLE_CONSUMER_PRODUCTS)
                    .check_table_text_values(values)
                    .check_links_count(link_text=UITextElements.CONNECT, count=3)
                    .check_links_count(link_text=Versions.FIVE_TWO_ZERO, count=5)
                    .fill_in_search_input(TestInputs.SPECIAL_CHARACTERS)
                )

            with allure.step("Вкладка 'Компоненты-потребители'"):
                titles = [
                    UITextElements.COMPONENT,
                    UITextElements.TEXT_VERSION,
                    UITextElements.TECHNICAL_RADAR_AREA,
                ]
                values = [
                    Components.CRYPT_PASSWORD_FORGE,
                    Versions.ONE_ONE,
                    RadarAreaValues.RECOMMENDED,
                ]

                (
                    self.component_version_information_page.click_on_link(UITextElements.CONSUMER_COMPONENTS_TAB)
                    .check_active_tab(UITextElements.CONSUMER_COMPONENTS_TAB)
                    .check_text_total_components_with_any_number()
                    .check_table_headings(titles)
                    .check_table_text_values(values)
                    .check_links_count(link_text=Components.CRYPT_PASSWORD_FORGE, count=3)
                    .check_links_count(link_text=Versions.ONE_ONE, count=1)
                    .fill_in_search_input(TestInputs.SPECIAL_CHARACTERS)
                    .click_on_funnel_icon()
                )

    def _setup(self) -> None:
        """Предусловие: открыта версия компонента."""
        (
            self.component_page.click_on_title()
            .click_on_link(UITextElements.ALL_COMPONENTS_TAB)
            .click_on_link(Components.ACCORDSDK)
        )
        self.component_information_page.click_on_link(UITextElements.VERSIONS_TAB).click_on_link(Versions.ACCORDSDK)
