import allure
import pytest
from allure_commons.types import LinkType

from src.constants.assemblies import Assemblies
from src.constants.products import Products
from src.constants.regular_expressions import RegularExpressions
from src.constants.test_inputs import TestInputs
from src.constants.ui_text_elements import UITextElements
from src.constants.usernames import Usernames
from src.constants.versions import Versions
from tests.base.base_test import BaseTest


@allure.parent_suite("Реестр продуктов.")
@allure.epic("Реестр продуктов.")
@allure.sub_suite("Реестр продуктов.")
class TestProductRegistry(BaseTest):
    """Реестр продуктов."""

    _NINE_ZERO_ONE = "5.1.0.901"
    _PRODUCT_VERSION_BUILD = "Продукт, версия, сборка"
    _NO_ITEMS_TO_SELECT = "Нет элементов для выбора"
    _LOG_ANALYZER = "Log Analyzer"
    _LIST_FIRST_PART = [Products.COORDINATOR_HW_5]
    _LIST_LAST_PART = [Versions.ONE_ONE]
    _LIST_OF_VERSIONS = [
        Versions.FIVE_FIVE_ZERO,
        "5.4.2",
        Versions.FIVE_FOUR_ONE,
        Versions.COORDINATOR_HW_5,
        "5.3.3",
        "5.3.2",
        "5.3.1",
        "5.3.0",
        "5.2.1",
        Versions.FIVE_TWO_ZERO,
        "5.1.2",
        "5.1.1",
        Versions.FIVE_ONE_ZERO,
    ]
    _LIST_OF_ASSEMBLIES = [
        "5.1.0.666",
        "5.1.0.4423",
        "5.1.0.1416",
        "5.1.0.1082",
        _NINE_ZERO_ONE,
        "5.1.0.795",
        "5.1.0.795",
        "5.1.0.780",
    ]

    @allure.suite("Реестр продуктов, переход по ссылкам.")
    @allure.title("Реестр продуктов, переход по ссылкам.")
    @allure.id("1521357")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1557216", LinkType.LINK, "TASK 1557216"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1521357", "TestCase 1521357")
    @allure.severity(allure.severity_level.NORMAL)
    def test_product_registry_clicking_on_links(self) -> None:
        """Реестр продуктов, переход по ссылкам."""
        # Реестр продуктов_переход по ссылкам
        with allure.step(
            "1. Пользователь с правами на чтение и редактирование паспортов продуктов авторизован в сервисе, открыта "
            "страница 'Продукты', вкладка 'Все продукты'."
        ):
            self._setup()

        with allure.step("2. В списке выбрать любой продукт → нажать на название продукта"):
            self.product_page.click_on_link(Products.COORDINATOR_HW_5)
            self.product_information_page.check_page_title(Products.COORDINATOR_HW_5).check_active_tab(
                UITextElements.GENERAL_INFORMATION
            )

        with allure.step("3. Вернуться в реестр продуктов → В списке выбрать любой продукт → нажать на экспандер"):
            self.product_information_page.click_on_link_products()
            (
                self.product_page.click_on_link(UITextElements.ALL_PRODUCTS)
                .fill_in_search_input(Products.COORDINATOR_HW_5)
                .click_on_expander(Products.COORDINATOR_HW_5)
                .check_table_components_or_products(
                    strings=self._LIST_FIRST_PART + self._LIST_OF_VERSIONS + self._LIST_LAST_PART
                )
            )

        with allure.step("4. Нажать на номер версии"):
            self.product_page.click_on_link(Versions.FIVE_ONE_ZERO)
            self.product_version_information_page.check_page_title(f"Версия {Versions.FIVE_ONE_ZERO}").check_active_tab(
                UITextElements.ASSEMBLIES
            )

        with allure.step(
            "5. Вернуться в реестр продуктов → В списке выбрать любой продукт → открыть список версий продукта → в "
            "списке выбрать любую версию → нажать на экспандер"
        ):
            self.product_version_information_page.click_on_link_products()
            (
                self.product_page.click_on_link(UITextElements.ALL_PRODUCTS)
                .fill_in_search_input(Products.COORDINATOR_HW_5)
                .click_on_expander(Products.COORDINATOR_HW_5)
                .click_on_expander(Versions.FIVE_ONE_ZERO)
                .check_table_components_or_products(
                    strings=self._LIST_FIRST_PART
                    + self._LIST_OF_VERSIONS
                    + self._LIST_OF_ASSEMBLIES
                    + self._LIST_LAST_PART
                )
            )

        with allure.step("6. Нажать на номер сборки"):
            self.product_page.click_on_link(self._NINE_ZERO_ONE)
            self.product_version_information_page.check_page_title(f"Сборка {self._NINE_ZERO_ONE}")

    @allure.suite("Реестр продуктов, отображение.")
    @allure.title("Реестр продуктов, отображение.")
    @allure.id("1521356")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1560577", LinkType.LINK, "TASK 1560577"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1521356", "TestCase 1521356")
    @allure.severity(allure.severity_level.NORMAL)
    def test_product_registry_display(self) -> None:
        """Реестр продуктов, отображение."""
        # Реестр продуктов_отображаение
        with allure.step(
            "1. Пользователь с правами на чтение и редактирование паспортов продуктов авторизован в сервисе, открыта "
            "страница 'Продукты', вкладка 'Все продукты'."
        ):
            self._setup()

        with allure.step("2. Проверить отображение страницы"):
            (
                self.product_page.check_reset_filters_button(
                    visible_and_enabled=False
                ).check_text_total_products_with_any_number()
                # Убираем у константы `Products.COORDINATOR_HW_5` последние два символа
                .fill_in_search_input(Products.COORDINATOR_HW_5[:-2])
            )
            count_favorites_indicator = self.product_page.get_count_favorites_indicator()
            self.product_page.check_text_products_found(count_favorites_indicator)

        with allure.step("3. В списке выбрать любой продукт и нажать на экспандер"):
            (
                self.product_page.fill_in_search_input(Products.COORDINATOR_HW_5)
                .click_on_expander(Products.COORDINATOR_HW_5)
                .check_table_components_or_products(
                    strings=self._LIST_FIRST_PART + self._LIST_OF_VERSIONS + self._LIST_LAST_PART
                )
            )

        with allure.step("4. В списке версий продукта выбрать любую версию и нажать на экспандер"):
            (
                self.product_page.click_on_expander(Versions.FIVE_ONE_ZERO)
                .check_invisible_expanders(self._LIST_OF_ASSEMBLIES)
                .check_table_components_or_products(
                    strings=self._LIST_FIRST_PART
                    + self._LIST_OF_VERSIONS
                    + self._LIST_OF_ASSEMBLIES
                    + self._LIST_LAST_PART
                )
            )

    @allure.suite("Реестр продуктов, фильтр 'Верифицированная версия', отображение.")
    @allure.title("Реестр продуктов, фильтр 'Верифицированная версия', отображение.")
    @allure.id("1536311")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1561629", LinkType.LINK, "TASK 1561629"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1536311", "TestCase 1536311")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.multiple_streams
    def test_product_registry_filter_verified_version_display(self) -> None:
        """Реестр продуктов, фильтр 'Верифицированная версия', отображение."""
        # Реестр продуктов_фильтр Верифицированная версия_ отображение
        with allure.step(
            "1. Предусловие: Пользователь с правами на чтение паспортов компонентов и продуктов авторизован в сервисе, "
            "открыт реестр продуктов"
        ):
            self._impersonate_as_user_with_read_or_write_permissions(write_permissions=False)
            self._setup()

        with allure.step("2. Открыть блок фильтров"):
            (
                self.product_page.click_on_funnel_icon()
                .check_reset_filters_button()
                .check_combo_box_in_filter(UITextElements.VERIFIED_VERSION)
            )

        with allure.step("3. Нажать на поле фильтра"):
            (
                self.product_page.click_on_combo_box_in_filter(UITextElements.VERIFIED_VERSION)
                .click_on_element_with_text(UITextElements.YES)
                .click_on_reset_filters_button()
                .click_on_combo_box_in_filter(UITextElements.VERIFIED_VERSION)
                .click_on_element_with_text(UITextElements.NO)
            )

        with allure.step("4. Перейти в паспорт версии продукта, вкладка 'Сборки'"):
            self.product_page.click_on_link(Products.COORDINATOR_HW_5)
            self.product_information_page.click_on_link(UITextElements.VERSIONS_TAB).click_on_link(
                Versions.COORDINATOR_HW_5
            )
            (
                self.product_version_information_page.click_on_funnel_icon()
                .check_reset_filters_button()
                .check_combo_box_in_filter(UITextElements.VERIFIED_VERSION)
                .click_on_combo_box_in_filter(UITextElements.VERIFIED_VERSION)
                .click_on_element_with_text(UITextElements.YES)
                .click_on_reset_filters_button()
                .click_on_combo_box_in_filter(UITextElements.VERIFIED_VERSION)
                .click_on_element_with_text(UITextElements.NO)
            )

        with allure.step("5. Перейти в паспорт версии продукта, вкладка 'Компонентный состав'"):
            (
                self.product_version_information_page.click_on_link(UITextElements.COMPONENT_COMPOSITION)
                .click_on_funnel_icon()
                .check_reset_filters_button()
                .check_combo_box_in_filter(UITextElements.VERIFIED_VERSION)
                .click_on_combo_box_in_filter(UITextElements.VERIFIED_VERSION)
                .click_on_element_with_text(element_text=UITextElements.YES, nth=1)
                .click_on_reset_filters_button()
                .click_on_combo_box_in_filter(UITextElements.VERIFIED_VERSION)
                .click_on_element_with_text(element_text=UITextElements.NO, nth=1)
            )

        with allure.step("6. Перейти в паспорт сборки продукта"):
            self.product_version_information_page.click_on_link(UITextElements.ASSEMBLIES).click_on_link(
                Assemblies.COORDINATOR_HW_5
            )
            (
                self.product_assembly_information_page.click_on_funnel_icon()
                .check_reset_filters_button()
                .check_combo_box_in_filter(UITextElements.VERIFIED_VERSION)
                .click_on_combo_box_in_filter(UITextElements.VERIFIED_VERSION)
                .click_on_element_with_text(element_text=UITextElements.YES, nth=1)
                .click_on_reset_filters_button()
                .click_on_combo_box_in_filter(UITextElements.VERIFIED_VERSION)
                .click_on_element_with_text(element_text=UITextElements.NO, nth=1)
            )

        with allure.step(
            "7. Проверить наличие фильтра в блоке фильтра на страницах: паспорт продукта → вкладка 'Версии', паспорт "
            "продукта → вкладка 'Компонентный состав'"
        ):
            self.product_assembly_information_page.click_on_link(Products.COORDINATOR_HW_5)
            (
                self.product_information_page.click_on_link(UITextElements.VERSIONS_TAB)
                .click_on_funnel_icon()
                .check_reset_filters_button()
                .check_combo_box_in_filter(placeholder=UITextElements.VERIFIED_VERSION, visible=False)
                .click_on_link(UITextElements.COMPONENT_COMPOSITION)
                .click_on_funnel_icon()
                .check_reset_filters_button()
                .check_combo_box_in_filter(placeholder=UITextElements.VERIFIED_VERSION, visible=False)
            )

    @allure.suite("Реестр продуктов, вкладка 'Избранное', нет избранного.")
    @allure.title("Реестр продуктов, вкладка 'Избранное', нет избранного.")
    @allure.id("1559405")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1561589", LinkType.LINK, "TASK 1561589"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1559405", "TestCase 1559405")
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_product_registry_favorites_tab_no_favorites(self) -> None:
        """Реестр продуктов, вкладка 'Избранное', нет избранного."""
        # Реестр продуктов_вкладка Избранное_нет избранного
        with allure.step(
            "1. Пользователь с правами на чтение паспортов продуктов авторизован в сервисе, открыт реестр продуктов"
        ):
            self._impersonate_as_user_with_read_or_write_permissions(write_permissions=False)
            self.component_page.click_on_link_products()

        with allure.step("2. Проверить отображение вкладки 'Избранное'"):
            self.product_page.check_text(UITextElements.FAVORITES_PRODUCTS_ARE_MISSING)

        with allure.step("3. Нажать 'Показать все продукты'"):
            (
                self.product_page.click_on_link(UITextElements.SHOW_ALL_PRODUCTS)
                .check_text_total_products_with_any_number()
                .check_active_tab(UITextElements.ALL_PRODUCTS)
            )

    @allure.suite("Реестр продуктов, фильтр 'Компонентный состав'.")
    @allure.title("Реестр продуктов, фильтр 'Компонентный состав'.")
    @allure.id("1560296")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1562307", LinkType.LINK, "TASK 1562307"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1560296", "TestCase 1560296")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.multiple_streams
    def test_product_registry_filter_component_composition(self) -> None:
        """Реестр продуктов, фильтр 'компонентный состав'."""
        # Фильтр Компонентный состав_ реестр продуктов
        with allure.step("1. Пользователь авторизован в сервисе АР, открыт реестр продуктов, открыт блок фильтра."):
            self.component_page.click_on_link_products()
            self.product_page.click_on_link(
                UITextElements.ALL_PRODUCTS
            ).click_on_funnel_icon().check_reset_filters_button()

        with allure.step("2. Кликнуть по фильтру 'Компонентный состав'"):
            self.product_page.check_combo_box_in_filter(
                UITextElements.COMPONENT_COMPOSITION
            ).click_on_combo_box_in_filter(UITextElements.COMPONENT_COMPOSITION)

        with allure.step("3. Выбрать значение 'Файлы обработаны'"):
            title = [self._PRODUCT_VERSION_BUILD]
            value = [UITextElements.TEXT_COMPONENTS_ENGLISH]
            (
                self.product_page.click_on_element_with_text(UITextElements.FILES_PROCESSED)
                .check_text(
                    page_text=UITextElements.COMPONENT_COMPOSITION
                    + UITextElements.COLON_SPACE
                    + UITextElements.FILES_PROCESSED
                )
                .check_text_products_found_with_any_number()
                .check_table_headings(title)
                .check_table_text_values(value)
            )

        with allure.step("4. Выбрать значение 'Ошибка обработки файлов'"):
            value = [
                Products.COORDINATOR_HW_5,
            ]
            (
                self.product_page.click_on_cross_icon()
                .check_text_total_products_with_any_number()
                .check_combo_box_in_filter(UITextElements.COMPONENT_COMPOSITION)
                .click_on_combo_box_in_filter(UITextElements.COMPONENT_COMPOSITION)
                .click_on_element_with_text(UITextElements.FILE_PROCESSING_ERROR)
                .check_text(
                    page_text=UITextElements.COMPONENT_COMPOSITION
                    + UITextElements.COLON_SPACE
                    + UITextElements.FILE_PROCESSING_ERROR
                )
                .check_text_products_found_with_any_number()
                .check_table_text_values(value)
            )

        with allure.step("5. Нажать Х"):
            (
                self.product_page.click_on_cross_icon()
                .check_combo_box_in_filter(UITextElements.COMPONENT_COMPOSITION)
                .check_text_total_products_with_any_number()
            )

    @allure.suite("Реестр продуктов, добавить продукт/версию/сборку в избранное.")
    @allure.title("Реестр продуктов, добавить продукт/версию/сборку в избранное.")
    @allure.id("1521360")
    @allure.description("Реестр продуктов, добавить продукт/версию/сборку в избранное.")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1563280", LinkType.LINK, "TASK 1563280"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1521360", "TestCase 1521360")
    @allure.severity(allure.severity_level.NORMAL)
    def test_product_registry_add_product_version_build_to_favorites(self, cleanup_favorites: None) -> None:
        """Реестр продуктов, добавить продукт/версию/сборку в избранное.

        :param cleanup_favorites: Фикстура для очистки избранного после автотеста.
        """
        # Реестр продуктов_добавить продукт/версию/сборку в избранное
        with allure.step(
            "1. Пользователь с правами на чтение и редактирование паспортов продуктов авторизован в сервисе, открыта "
            "страница 'Продукты', вкладка 'Все продукты'"
        ):
            self._impersonate_as_user_with_read_or_write_permissions(write_permissions=False)
            self._setup()

        with allure.step(
            "2. В реестре выбрать любой продукт (не добавленный в избранное) → нажать иконку в виде звезды"
        ):
            (
                self.product_page.click_on_favorites_icon_off(Products.COORDINATOR_HW_5)
                .check_text(page_text=Products.COORDINATOR_HW_5 + UITextElements.ADDED_TO_FAVORITES)
                .check_text(RegularExpressions.PATTERN_STRING_TIME)
                .click_on_close_message_icon()
            )

        with allure.step("3. Перейти на вкладку 'Избранное' → проверить отображение выбранного продукта в избранном"):
            self.product_page.click_on_link(UITextElements.FAVORITES).check_active_tab(
                UITextElements.FAVORITES
            ).check_links_count(link_text=Products.COORDINATOR_HW_5, count=1).check_favorites_indicator(count=1)

        with allure.step(
            "4. В реестре выбрать любой продукт → раскрыть экспандер → выбрать любую версию продукта (не добавленную "
            "в избранное) → нажать иконку в виде звезды"
        ):
            (
                self.product_page.click_on_link(UITextElements.ALL_PRODUCTS)
                .click_on_expander(Products.COORDINATOR_HW_5)
                .click_on_favorites_icon_off(Versions.COORDINATOR_HW_5)
                .check_text(page_text=Versions.COORDINATOR_HW_5 + UITextElements.ADDED_TO_FAVORITES)
                .check_text(RegularExpressions.PATTERN_STRING_TIME)
                .click_on_close_message_icon()
            )

            with allure.step("Перейти на вкладку 'Избранное' → проверить отображение выбранной версии в избранном"):
                (
                    self.product_page.click_on_link(UITextElements.FAVORITES)
                    .check_active_tab(UITextElements.FAVORITES)
                    .check_links_count(link_text=Products.COORDINATOR_HW_5, count=1)
                    .check_links_count(link_text=Versions.COORDINATOR_HW_5, count=1)
                    .check_favorites_indicator(count=2)
                )

    @allure.suite("Реестр продуктов, удалить продукт/версию/сборку из избранного.")
    @allure.title("Реестр продуктов, удалить продукт/версию/сборку из избранного.")
    @allure.id("1565394")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1568360", LinkType.LINK, "TASK 1568360"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1565394", "TestCase 1565394")
    @allure.severity(allure.severity_level.NORMAL)
    def test_product_registry_remove_product_version_build_from_favorites(self) -> None:
        """Реестр продуктов, удалить продукт/версию/сборку из избранного."""
        # Реестр продуктов_удалить продукт/версию/сборку из избранного
        with allure.step(
            "1. Пользователь с правами на чтение и редактирование паспортов продуктов авторизован в сервисе, открыт "
            "реестр продуктов"
        ):
            self.component_page.click_on_link_products()
            (
                self.product_page.click_on_link(UITextElements.FAVORITES)
                .click_on_all_favorites_icons_and_all_close_message_icons()
                .click_on_link(UITextElements.ALL_PRODUCTS)
            )

        with allure.step(
            "2. В реестре выбрать любой продукт (добавленный в избранное, версии и сборки не в избранном) → нажать "
            "иконку в виде звезды"
        ):
            (
                self.product_page.click_on_favorites_icon_off(Products.COORDINATOR_HW_5)
                .check_text(page_text=Products.COORDINATOR_HW_5 + UITextElements.ADDED_TO_FAVORITES)
                .check_text(RegularExpressions.PATTERN_STRING_TIME)
                .click_on_close_message_icon()
                .click_on_favorites_icon_on(Products.COORDINATOR_HW_5)
                .check_text(page_text=Products.COORDINATOR_HW_5 + UITextElements.DELETED_FROM_FAVORITES)
                .check_text(RegularExpressions.PATTERN_STRING_TIME)
                .click_on_close_message_icon()
            )

        with allure.step("3. Перейти на вкладку 'Избранное' реестра продуктов"):
            self.product_page.click_on_link_products().check_text(
                UITextElements.FAVORITES_PRODUCTS_ARE_MISSING
            ).check_links_count(link_text=UITextElements.SHOW_ALL_PRODUCTS, count=1)

    @allure.suite("Реестр продуктов, блок фильтра, отображение.")
    @allure.title("Реестр продуктов, блок фильтра, отображение.")
    @allure.id("1565432")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1569418", LinkType.LINK, "TASK 1569418"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1565432", "TestCase 1565432")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.multiple_streams
    def test_product_registry_filter_block_display(self) -> None:
        """Реестр продуктов, блок фильтра, отображение."""
        # Реестр продуктов_блок фильтра_отображение
        with allure.step(
            "1. Предусловие: Пользователь с правами на чтение паспортов продуктов авторизован в сервисе, открыт реестр "
            "продуктов на вкладке 'Все продукты'"
        ):
            self._impersonate_as_user_with_read_or_write_permissions(write_permissions=False)
            self._setup()

        with allure.step("2. Нажать на иконку воронки"):
            (
                self.product_page.click_on_funnel_icon()
                .click_on_close_filter_block_icon()
                .click_on_funnel_icon()
                .check_reset_filters_button()
                .check_combo_box_in_filter(UITextElements.ATTACK_SURFACE)
                .check_combo_box_in_filter(UITextElements.RESPONSIBLE_FOR_IMPLEMENTATION)
                .check_combo_box_in_filter(UITextElements.PACKAGE_MANAGER)
                .check_combo_box_in_filter(UITextElements.VERIFIED_VERSION)
                .check_combo_box_in_filter(UITextElements.COMPONENT_COMPOSITION)
                .check_combo_box_in_filter(UITextElements.TEXT_PROGRAMMING_LANGUAGE)
                .check_combo_box_in_filter(UITextElements.PLATFORM)
                .check_combo_box_in_filter(UITextElements.APPROVAL_STATUS)
                .check_combo_box_in_filter(UITextElements.DEVELOPMENT_STATUS)
                .check_combo_box_in_filter(UITextElements.TECHNICAL_EXPERT)
                .check_combo_box_in_filter(UITextElements.TECHNICAL_RADAR_AREA)
                .check_combo_box_in_filter(UITextElements.OWNER)
                .check_combo_box_in_filter(UITextElements.COMPONENT_TYPE)
            )

        with allure.step("3. Обновить страницу сервиса"):
            self.product_page.refresh_page().check_reset_filters_button(
                visible_and_enabled=False
            ).click_on_funnel_icon()

    @allure.suite("Реестр продуктов, фильтр 'Поверхность атаки'.")
    @allure.title("Реестр продуктов, фильтр 'Поверхность атаки'.")
    @allure.id("1567411")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1569423", LinkType.LINK, "TASK 1569423"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1567411", "TestCase 1567411")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.multiple_streams
    def test_product_registry_filter_attack_surface(self) -> None:
        """Реестр продуктов, фильтр 'Поверхность атаки'."""
        # Реестр продуктов_фильтр Поверхность атаки
        marked_up = "Размечена"
        not_marked_up = "Не размечена"

        with allure.step(
            "1. Предусловие: Пользователь с правами на чтение паспортов продуктов авторизован в сервисе, открыт реестр "
            "продуктов на вкладке 'Все продукты'"
        ):
            self._impersonate_as_user_with_read_or_write_permissions(write_permissions=False)
            self._setup()

        with allure.step("2. Нажать на экспандер в фильтре 'Поверхность атаки'"):
            (
                self.product_page.click_on_funnel_icon()
                .check_reset_filters_button()
                .check_combo_box_in_filter(UITextElements.ATTACK_SURFACE)
                .click_on_combo_box_in_filter(UITextElements.ATTACK_SURFACE)
            )

        with allure.step("3. Выбрать значение 'Размечена'"):
            title = [self._PRODUCT_VERSION_BUILD]
            value = [UITextElements.TEXT_COMPONENTS_ENGLISH]

            (
                self.product_page.click_on_element_with_text(marked_up)
                .check_text(page_text=not_marked_up, visible=False)
                .check_text(page_text=UITextElements.ATTACK_SURFACE + UITextElements.COLON_SPACE + marked_up)
                .check_cross_icon()
                .check_table_headings(title)
                .check_table_text_values(value)
            )

        with allure.step("4. Выбрать значение 'Не размечена'"):
            value = [Products.COORDINATOR_AR_2]

            (
                self.product_page.click_on_reset_filters_button()
                .click_on_combo_box_in_filter(UITextElements.ATTACK_SURFACE)
                .click_on_element_with_text(not_marked_up)
                .check_text(page_text=UITextElements.ATTACK_SURFACE + UITextElements.COLON_SPACE + not_marked_up)
                .check_cross_icon()
                .check_table_headings(title)
                .check_table_text_values(value)
            )

    @allure.suite("Реестр продуктов, фильтр 'Верифицированная версия'.")
    @allure.title("Реестр продуктов, фильтр 'Верифицированная версия'.")
    @allure.id("1565433")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1570267", LinkType.LINK, "TASK 1570267"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1565433", "TestCase 1565433")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.multiple_streams
    def test_product_registry_filter_verified_version(self) -> None:
        """Реестр продуктов, фильтр 'Верифицированная версия'."""
        # Реестр продуктов_фильтр Верифицированная версия
        with allure.step(
            "1. Предусловие: Пользователь с правами на чтение паспортов продуктов авторизован в сервисе, открыт реестр "
            "продуктов на вкладке 'Все продукты'"
        ):
            self._impersonate_as_user_with_read_or_write_permissions(write_permissions=False)
            self._setup()

        with allure.step("2. Нажать на экспандер в фильтре 'Верифицированная версия'"):
            (
                self.product_page.click_on_funnel_icon()
                .check_reset_filters_button()
                .check_combo_box_in_filter(UITextElements.VERIFIED_VERSION)
                .click_on_combo_box_in_filter(UITextElements.VERIFIED_VERSION)
            )

        with allure.step("3. Выбрать значение 'Да'"):
            title = [self._PRODUCT_VERSION_BUILD]

            (
                self.product_page.click_on_element_with_text(UITextElements.YES)
                .check_text(page_text=UITextElements.NO, visible=False)
                .check_text(page_text=UITextElements.VERIFIED_VERSION + UITextElements.COLON_SPACE + UITextElements.YES)
                .check_cross_icon()
                .check_table_headings(title)
                .check_links_count(link_text=Products.COORDINATOR_AR_2, count=0)
            )

        with allure.step("4. Выбрать значение 'Нет'"):
            (
                self.product_page.click_on_reset_filters_button()
                .click_on_combo_box_in_filter(UITextElements.VERIFIED_VERSION)
                .click_on_element_with_text(UITextElements.NO)
                .check_text(page_text=UITextElements.VERIFIED_VERSION + UITextElements.COLON_SPACE + UITextElements.NO)
                .check_cross_icon()
                .check_table_headings(title)
                .check_links_count(link_text=Products.COORDINATOR_IG_4, count=1)
            )

    @allure.suite("Реестр продуктов, фильтр 'Язык программирования'.")
    @allure.title("Реестр продуктов, фильтр 'Язык программирования'.")
    @allure.id("1567414")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1571934", LinkType.LINK, "TASK 1571934"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1567414", "TestCase 1567414")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.multiple_streams
    def test_product_registry_filter_programming_language_text(self) -> None:
        """Реестр продуктов, фильтр 'Язык программирования'."""
        # Реестр продуктов_фильтр Язык программирования
        java = "Java"
        java_script = "JavaScript"

        with allure.step(
            "1. Предусловие: Пользователь с правами на чтение паспортов продуктов авторизован в сервисе, открыт реестр "
            "продуктов на вкладке 'Все продукты'"
        ):
            self._impersonate_as_user_with_read_or_write_permissions(write_permissions=False)
            self._setup()

        with allure.step("2. Нажать на экспандер в фильтре 'Язык программирования'"):
            (
                self.product_page.click_on_funnel_icon()
                .check_reset_filters_button()
                .check_combo_box_in_filter(UITextElements.TEXT_PROGRAMMING_LANGUAGE)
                .click_on_combo_box_in_filter(UITextElements.TEXT_PROGRAMMING_LANGUAGE)
            )

        with allure.step("3. Отметить чек-бокс 'Не указан' галкой"):
            (
                self.product_page.click_on_element_with_text(element_text=UITextElements.ABSENT, nth=1)
                .check_checkbox_not_specified()
                .check_combo_box_in_filter(UITextElements.VERIFIED_VERSION)
                .click_on_combo_box_in_filter(UITextElements.VERIFIED_VERSION)
                .check_text(
                    page_text=UITextElements.TEXT_PROGRAMMING_LANGUAGE
                    + UITextElements.COLON_SPACE
                    + UITextElements.ABSENT
                )
                .check_cross_icon()
            )

        with allure.step("4. Ввести невалидное значение"):
            (
                self.product_page.click_on_reset_filters_button()
                .check_combo_box_in_filter(UITextElements.TEXT_PROGRAMMING_LANGUAGE)
                .click_on_combo_box_in_filter(UITextElements.TEXT_PROGRAMMING_LANGUAGE)
                .fill_in_combo_box_in_filter(
                    placeholder=UITextElements.TEXT_PROGRAMMING_LANGUAGE, text=TestInputs.SPECIAL_CHARACTERS
                )
                .check_text(self._NO_ITEMS_TO_SELECT)
            )

        with allure.step("5. Ввести валидное значение в верхнем/нижнем/смешанном регистре"):
            (
                self.product_page.click_on_reset_filters_button()
                .check_combo_box_in_filter(UITextElements.TEXT_PROGRAMMING_LANGUAGE)
                .click_on_combo_box_in_filter(UITextElements.TEXT_PROGRAMMING_LANGUAGE)
                .fill_in_combo_box_in_filter(
                    placeholder=UITextElements.TEXT_PROGRAMMING_LANGUAGE, text=UITextElements.PYTHON
                )
                .click_on_element_with_text(UITextElements.PYTHON)
                .click_on_reset_filters_button()
                .check_combo_box_in_filter(UITextElements.TEXT_PROGRAMMING_LANGUAGE)
                .click_on_combo_box_in_filter(UITextElements.TEXT_PROGRAMMING_LANGUAGE)
                .fill_in_combo_box_in_filter(
                    placeholder=UITextElements.TEXT_PROGRAMMING_LANGUAGE, text=UITextElements.PYTHON.upper()
                )
                .click_on_element_with_text(UITextElements.PYTHON)
                .click_on_reset_filters_button()
                .check_combo_box_in_filter(UITextElements.TEXT_PROGRAMMING_LANGUAGE)
                .click_on_combo_box_in_filter(UITextElements.TEXT_PROGRAMMING_LANGUAGE)
                .fill_in_combo_box_in_filter(
                    placeholder=UITextElements.TEXT_PROGRAMMING_LANGUAGE, text=UITextElements.PYTHON.lower()
                )
                .click_on_element_with_text(UITextElements.PYTHON)
            )

        with allure.step("6. Ввести валидное значение с пробелами до и после"):
            (
                self.product_page.click_on_reset_filters_button()
                .check_combo_box_in_filter(UITextElements.TEXT_PROGRAMMING_LANGUAGE)
                .click_on_combo_box_in_filter(UITextElements.TEXT_PROGRAMMING_LANGUAGE)
                .fill_in_combo_box_in_filter(
                    placeholder=UITextElements.TEXT_PROGRAMMING_LANGUAGE, text=f" {UITextElements.PYTHON} "
                )
                .click_on_element_with_text(UITextElements.PYTHON)
            )

        with allure.step("7. Выбрать из найденного один ЯП и закрыть выпадающий список"):
            (
                self.product_page.check_combo_box_in_filter(UITextElements.VERIFIED_VERSION)
                .click_on_combo_box_in_filter(UITextElements.VERIFIED_VERSION)
                .check_text(
                    page_text=UITextElements.TEXT_PROGRAMMING_LANGUAGE
                    + UITextElements.COLON_SPACE
                    + UITextElements.PYTHON
                )
                .check_cross_icon()
            )

        with allure.step("8. Выбрать еще один ЯП"):
            (
                self.product_page.click_on_reset_filters_button()
                .check_combo_box_in_filter(UITextElements.TEXT_PROGRAMMING_LANGUAGE)
                .click_on_combo_box_in_filter(UITextElements.TEXT_PROGRAMMING_LANGUAGE)
                .fill_in_combo_box_in_filter(placeholder=UITextElements.TEXT_PROGRAMMING_LANGUAGE, text=java)
                .click_on_element_with_text(java)
                .click_on_element_with_text(java_script)
                .check_combo_box_in_filter(UITextElements.VERIFIED_VERSION)
                .click_on_combo_box_in_filter(UITextElements.VERIFIED_VERSION)
                .check_combo_box_in_filter(UITextElements.TEXT_PROGRAMMING_LANGUAGE)
                .click_on_combo_box_in_filter(UITextElements.TEXT_PROGRAMMING_LANGUAGE)
                .check_text(page_text=UITextElements.TEXT_PROGRAMMING_LANGUAGE + UITextElements.COLON_SPACE_TWO)
                .check_cross_icon()
            )

    @allure.suite("Реестр продуктов, фильтр 'Пакетный менеджер'.")
    @allure.title("Реестр продуктов, фильтр 'Пакетный менеджер'.")
    @allure.id("1567413")
    @allure.description("Баг: Элемент с текстом 'Не указан' не отображается.")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1573561", LinkType.LINK, "TASK 1573561"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1567413", "TestCase 1567413")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.multiple_streams
    def test_product_registry_filter_package_manager(self) -> None:
        """Реестр продуктов, фильтр 'Пакетный менеджер'."""
        # Реестр продуктов_фильтр Пакетный менеджер
        pypi = "Pypi"

        with allure.step(
            "1. Предусловие: Пользователь с правами на чтение паспортов продуктов авторизован в сервисе, открыт реестр "
            "продуктов на вкладке 'Все продукты'"
        ):
            self._impersonate_as_user_with_read_or_write_permissions(write_permissions=False)
            self._setup()

        with allure.step("2. Нажать на экспандер в фильтре 'Пакетный менеджер'"):
            (
                self.product_page.click_on_funnel_icon()
                .check_reset_filters_button()
                .check_combo_box_in_filter(UITextElements.PACKAGE_MANAGER)
                .click_on_combo_box_in_filter(UITextElements.PACKAGE_MANAGER)
            )

        with allure.step("3. Отметить чек-бокс 'Не указан' галкой"):
            list_combo_box_elements = [
                UITextElements.ABSENT,
                UITextElements.ANT_IVY,
                "APT",
                "CONAN",
                "CONAN2",
                "NPM",
                "NUGET",
                pypi.upper(),
            ]
            title = [self._PRODUCT_VERSION_BUILD]
            value = [Products.COORDINATOR_HW_5]

            (
                self.product_page.click_on_element_with_text(element_text=UITextElements.ABSENT, nth=4)
                .check_combo_box_list_and_text_in_filter(
                    UITextElements.PACKAGE_MANAGER + UITextElements.COLON_SPACE + UITextElements.ABSENT,
                    list_combo_box_elements,
                )
                .check_table_headings(title)
                .check_table_text_values(value)
            )

        with allure.step("4. Нажать Х"):
            value = [UITextElements.TEXT_COMPONENTS_ENGLISH]

            (
                self.product_page.click_on_cross_icon()
                .check_combo_box_in_filter(UITextElements.PACKAGE_MANAGER)
                .check_text_total_products_with_any_number()
                .check_table_text_values(value)
            )

        with allure.step("5. Ввести невалидное название пакетного менеджера"):
            (
                self.product_page.fill_in_combo_box_in_filter(
                    UITextElements.PACKAGE_MANAGER, TestInputs.SPECIAL_CHARACTERS
                ).check_text(self._NO_ITEMS_TO_SELECT)
            )

        with allure.step("6. Очистить поле фильтра"):
            (
                self.product_page.click_on_reset_filters_button()
                .check_combo_box_in_filter(UITextElements.PACKAGE_MANAGER)
                .check_text_total_products_with_any_number()
                .check_table_text_values(value)
            )

        with allure.step("7. Ввести часть название пакетного менеджера в верхнем/нижнем/смешанном регистре"):
            (
                self.product_page.check_combo_box_in_filter(UITextElements.PACKAGE_MANAGER)
                .click_on_combo_box_in_filter(UITextElements.PACKAGE_MANAGER)
                # Убираем у переменной `pypi` последний символ
                .fill_in_combo_box_in_filter(placeholder=UITextElements.PACKAGE_MANAGER, text=pypi[:-1])
                .click_on_element_in_combo_box_in_filter(pypi.upper())
                .click_on_reset_filters_button()
                .check_combo_box_in_filter(UITextElements.PACKAGE_MANAGER)
                .click_on_combo_box_in_filter(UITextElements.PACKAGE_MANAGER)
                # Убираем у переменной `pypi` последний символ
                .fill_in_combo_box_in_filter(placeholder=UITextElements.PACKAGE_MANAGER, text=pypi[:-1].lower())
                .click_on_element_in_combo_box_in_filter(pypi.upper())
                .click_on_reset_filters_button()
                .check_combo_box_in_filter(UITextElements.PACKAGE_MANAGER)
                .click_on_combo_box_in_filter(UITextElements.PACKAGE_MANAGER)
                # Убираем у переменной `pypi` последний символ
                .fill_in_combo_box_in_filter(placeholder=UITextElements.PACKAGE_MANAGER, text=pypi[:-1].upper())
                .click_on_element_in_combo_box_in_filter(pypi.upper())
            )

        with allure.step("8. Ввести пробелы до/после названия пакетного менеджера"):
            (
                self.product_page.click_on_reset_filters_button()
                .check_combo_box_in_filter(UITextElements.PACKAGE_MANAGER)
                .click_on_combo_box_in_filter(UITextElements.PACKAGE_MANAGER)
                .fill_in_combo_box_in_filter(placeholder=UITextElements.PACKAGE_MANAGER, text=f" {pypi.upper()} ")
            )

        with allure.step("9. Выбрать пакетный менеджер из списка"):
            value = [self._LOG_ANALYZER]

            (
                self.product_page.click_on_reset_filters_button()
                .check_combo_box_in_filter(UITextElements.PACKAGE_MANAGER)
                .click_on_combo_box_in_filter(UITextElements.PACKAGE_MANAGER)
                .check_checkbox_with_text_in_combo_box_in_filter(text=pypi.upper(), marked=False)
                .click_on_element_in_combo_box_in_filter(pypi.upper())
                .check_checkbox_with_text_in_combo_box_in_filter(pypi.upper())
                .check_combo_box_in_filter(UITextElements.TEXT_PROGRAMMING_LANGUAGE)
                .click_on_combo_box_in_filter(UITextElements.TEXT_PROGRAMMING_LANGUAGE)
                .check_text(page_text=UITextElements.PACKAGE_MANAGER + UITextElements.COLON_SPACE + pypi.upper())
                .check_cross_icon()
                .check_table_text_values(value)
            )

        with allure.step("10. Выбрать еще один пакетный менеджер из списка"):
            value = [UITextElements.CONNECT]

            (
                self.product_page.check_combo_box_in_filter(UITextElements.PACKAGE_MANAGER)
                .click_on_combo_box_in_filter(UITextElements.PACKAGE_MANAGER)
                .check_checkbox_with_text_in_combo_box_in_filter(text=UITextElements.ANT_IVY, marked=False)
                .click_on_element_in_combo_box_in_filter(UITextElements.ANT_IVY)
                .check_checkbox_with_text_in_combo_box_in_filter(UITextElements.ANT_IVY)
                .check_text(page_text=UITextElements.PACKAGE_MANAGER + UITextElements.COLON_SPACE_TWO)
                .check_cross_icon()
                .check_table_text_values(value)
            )

    @allure.suite("Реестр продуктов, фильтр 'Ответственный за реализацию'.")
    @allure.title("Реестр продуктов, фильтр 'Ответственный за реализацию'.")
    @allure.id("1567412")
    @allure.description(
        "Баг или неправильный тест-кейс: иконка в виде крестика не отображается рядом с текстом 'Не указан';\n"
        "Баг: Текст 'Пожалуйста, введите минимум 2 символа' не отображается на странице;"
    )
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1577448", LinkType.LINK, "TASK 1577448"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1567412", "TestCase 1567412")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.multiple_streams
    def test_product_registry_filter_responsible_for_implementation(self) -> None:
        """Реестр продуктов, фильтр 'Ответственный за реализацию'."""
        # Реестр продуктов_фильтр Ответственный за реализацию
        with allure.step(
            "1. Предусловие: Пользователь с правами на чтение паспортов продуктов авторизован в сервисе, открыт реестр "
            "продуктов на вкладке 'Все продукты'"
        ):
            self._impersonate_as_user_with_read_or_write_permissions(write_permissions=False)
            self._setup()

        with allure.step("2. Нажать на экспандер в фильтре 'Ответственный за реализацию'"):
            (
                self.product_page.click_on_funnel_icon()
                .check_reset_filters_button()
                .check_combo_box_in_filter(UITextElements.RESPONSIBLE_FOR_IMPLEMENTATION)
                .click_on_combo_box_in_filter(UITextElements.RESPONSIBLE_FOR_IMPLEMENTATION)
                .check_text("Пожалуйста, введите минимум 2 символа")
            )

        with allure.step("3. Отметить чек-бокс 'Не указан' галкой"):
            (
                self.product_page.click_on_element_with_text(UITextElements.ABSENT)
                .check_text(
                    page_text=UITextElements.RESPONSIBLE_FOR_IMPLEMENTATION
                    + UITextElements.COLON_SPACE
                    + UITextElements.ABSENT
                )
                .check_cross_icon()
                .check_text_products_found_with_any_number()
            )

        with allure.step("4. Нажать 'Сбросить фильтр'"):
            (
                self.product_page.click_on_reset_filters_button()
                .check_combo_box_in_filter(UITextElements.RESPONSIBLE_FOR_IMPLEMENTATION)
                .check_text_total_products_with_any_number()
            )

        with allure.step("5. Установить курсор в поле 'Ответственный за реализацию'"):
            self.product_page.check_combo_box_in_filter(
                UITextElements.RESPONSIBLE_FOR_IMPLEMENTATION
            ).click_on_combo_box_in_filter(UITextElements.RESPONSIBLE_FOR_IMPLEMENTATION)

        with allure.step("6. Ввести невалидное ФИО сотрудника"):
            self.product_page.fill_in_combo_box_in_filter(
                UITextElements.RESPONSIBLE_FOR_IMPLEMENTATION, TestInputs.SPECIAL_CHARACTERS
            ).check_text(self._NO_ITEMS_TO_SELECT)

        with allure.step("7. Очистить поле фильтра"):
            self.product_page.click_on_reset_filters_button().check_combo_box_in_filter(
                UITextElements.RESPONSIBLE_FOR_IMPLEMENTATION
            )

        with allure.step("8. Ввести часть ФИО сотрудника в верхнем/нижнем/смешанном регистре"):
            (
                self.product_page.check_combo_box_in_filter(UITextElements.RESPONSIBLE_FOR_IMPLEMENTATION)
                .click_on_combo_box_in_filter(UITextElements.RESPONSIBLE_FOR_IMPLEMENTATION)
                .fill_in_combo_box_in_filter(
                    placeholder=UITextElements.RESPONSIBLE_FOR_IMPLEMENTATION,
                    # Убираем у константы `Usernames.USER_WITH_READ_PERMISSIONS` последние 5 символов
                    text=Usernames.USER_WITH_READ_PERMISSIONS[:-5].lower(),
                )
                .click_on_element_with_text(element_text=Usernames.USER_WITH_READ_PERMISSIONS, nth=1)
            )

        with allure.step("9. Ввести часть ФИО сотрудника с пробелами до и после ввода"):
            (
                self.product_page.click_on_reset_filters_button()
                .check_combo_box_in_filter(UITextElements.RESPONSIBLE_FOR_IMPLEMENTATION)
                .click_on_combo_box_in_filter(UITextElements.RESPONSIBLE_FOR_IMPLEMENTATION)
                .fill_in_combo_box_in_filter(
                    placeholder=UITextElements.RESPONSIBLE_FOR_IMPLEMENTATION,
                    # Убираем у константы `Usernames.USER_WITH_READ_PERMISSIONS` последние 5 символов
                    text=f" {Usernames.USER_WITH_READ_PERMISSIONS[:-5]} ",
                )
            )

        with allure.step("10. Выбрать сотрудника из списка"):
            title = [self._PRODUCT_VERSION_BUILD]
            value = [self._LOG_ANALYZER]

            (
                self.product_page.click_on_element_with_text(element_text=Usernames.USER_WITH_READ_PERMISSIONS, nth=1)
                .check_checkbox_responsible_for_implementation()
                .check_table_headings(title)
                .check_table_text_values(value)
            )

        with allure.step("11. Нажать за пределами фильтра"):
            (
                self.product_page.check_combo_box_in_filter(UITextElements.TEXT_PROGRAMMING_LANGUAGE)
                .click_on_combo_box_in_filter(UITextElements.TEXT_PROGRAMMING_LANGUAGE)
                .check_cross_icon()
                .check_text_with_ellipses(Usernames.USER_WITH_READ_PERMISSIONS)
            )

        with allure.step("12. Повторить шаги 10 и 11 для выбора еще одного ответственного"):
            value = [UITextElements.TEXT_COMPONENTS_ENGLISH]

            (
                self.product_page.check_combo_box_in_filter(UITextElements.RESPONSIBLE_FOR_IMPLEMENTATION)
                .click_on_combo_box_in_filter(UITextElements.RESPONSIBLE_FOR_IMPLEMENTATION)
                .fill_in_combo_box_in_filter(
                    placeholder=UITextElements.RESPONSIBLE_FOR_IMPLEMENTATION,
                    text=Usernames.USER_WITH_WRITE_PERMISSIONS,
                )
                .click_on_element_with_text(Usernames.USER_WITH_WRITE_PERMISSIONS)
                .check_checkbox_responsible_for_implementation()
                .check_combo_box_in_filter(UITextElements.TEXT_PROGRAMMING_LANGUAGE)
                .click_on_combo_box_in_filter(UITextElements.TEXT_PROGRAMMING_LANGUAGE)
                .check_text(page_text=UITextElements.RESPONSIBLE_FOR_IMPLEMENTATION + UITextElements.COLON_SPACE_TWO)
                .check_cross_icon()
                .check_table_text_values(value)
            )

        with allure.step("13. Нажать Х в фильтре"):
            (
                self.product_page.click_on_cross_icon()
                .check_combo_box_in_filter(UITextElements.RESPONSIBLE_FOR_IMPLEMENTATION)
                .check_text_total_products_with_any_number()
            )

    @allure.suite("Реестр продуктов, поле поиска, невалидные данные")
    @allure.title("Реестр продуктов, поле поиска, невалидные данные")
    @allure.id("1521359")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1557211", LinkType.LINK, "TASK 1557211"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1521359", "TestCase 1521359")
    @allure.severity(allure.severity_level.MINOR)
    def test_product_search_invalid_data(self) -> None:
        """Реестр продуктов, поле поиска, невалидные данные."""
        # Реестр продуктов_поле поиска_НЕ валидные данные
        with allure.step(
            "1. Пользователь с правами на чтение и редактирование паспортов продуктов авторизован в сервисе, открыта "
            "страница 'Продукты', вкладка 'Все продукты'."
        ):
            self._setup()

        with allure.step(
            "2. В поле поиска ввести часть названия несуществующего продукта/номер версии продукта/номер сборки"
        ):
            (
                self.product_page.fill_in_search_input(TestInputs.SPECIAL_CHARACTERS)
                .check_search_input(TestInputs.SPECIAL_CHARACTERS)
                .check_cross_icon()
                .check_text_products_found(count=0)
                .check_text(UITextElements.NOTHING_FOUND)
            )

    @allure.suite("Реестр продуктов, поле поиска, валидные данные")
    @allure.title("Реестр продуктов, поле поиска, валидные данные")
    @allure.id("1521358")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1557213", LinkType.LINK, "TASK 1557213"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1521358", "TestCase 1521358")
    @allure.severity(allure.severity_level.MINOR)
    def test_product_search_valid_data(self) -> None:
        """Реестр продуктов, поле поиска, валидные данные."""
        # Реестр продуктов_поле поиска_валидные данные
        components_found = 1

        with allure.step(
            "1. Пользователь с правами на чтение и редактирование паспортов продуктов авторизован в сервисе, открыта "
            "страница 'Продукты', вкладка 'Все продукты'."
        ):
            self._setup()

        with allure.step("2. В поле поиска ввести часть названия продукта"):
            (
                # Убираем у константы `Products.PRIME` последний символ
                self.product_page.fill_in_search_input(Products.PRIME[:-1])
                .check_search_input(Products.PRIME[:-1])
                .check_cross_icon()
                # Проверяем, что текст 'Prim' выделен жёлтым цветом
                .check_yellow_backlight(Products.PRIME[:-1])
                .check_text_products_found(components_found)
            )

        with allure.step("3. Нажать Х"):
            (
                self.product_page.click_on_cross_icon()
                .check_search_input("")
                .check_cross_icon(visible=False)
                .check_text_total_products_with_any_number()
            )

        with allure.step("4. В поле поиска ввести часть названия продукта в верхнем/нижнем/смешанном регистре"):
            (
                self.product_page.fill_in_search_input(Products.PRIME.upper())
                .check_search_input(Products.PRIME.upper())
                .check_cross_icon()
                .check_yellow_backlight(Products.PRIME)
                .check_text_products_found(components_found)
            )

        with allure.step("5. Нажать Х"):
            (
                self.product_page.click_on_cross_icon()
                .check_search_input("")
                .check_cross_icon(visible=False)
                .check_text_total_products_with_any_number()
            )

        with allure.step(
            "6. В поле поиска ввести часть названия продукта, до/после введенных символов добавить пробелы"
        ):
            (
                self.product_page.fill_in_search_input(f" {Products.PRIME} ")
                .check_search_input(f" {Products.PRIME} ")
                .check_cross_icon()
                .check_yellow_backlight(Products.PRIME)
                .check_text_products_found(components_found)
            )

        with allure.step("7. Нажать Х"):
            (
                self.product_page.click_on_cross_icon()
                .check_search_input("")
                .check_cross_icon(visible=False)
                .check_text_total_products_with_any_number()
            )

    def _setup(self) -> None:
        """Предусловие: реестр продуктов → вкладка 'Все продукты'."""
        self.component_page.click_on_link_products()
        self.product_page.click_on_link(UITextElements.ALL_PRODUCTS)
