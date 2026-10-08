import allure
from allure_commons.types import LinkType

from src.constants.assemblies import Assemblies
from src.constants.components import Components
from src.constants.products import Products
from src.constants.ui_text_elements import UITextElements
from src.constants.versions import Versions
from tests.base.base_test import BaseTest


@allure.parent_suite("Объекты продукта.")
@allure.epic("Объекты продукта.")
@allure.sub_suite("Объекты продукта.")
class TestProductObjects(BaseTest):
    """Объекты продукта."""

    @allure.suite("Объекты продукта, сортировка.")
    @allure.title("Объекты продукта, сортировка.")
    @allure.id("1565398")
    @allure.description("Объекты продукта, сортировка.")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1590620", LinkType.LINK, "TASK 1590620"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1565398", "TestCase 1565398")
    @allure.severity(allure.severity_level.NORMAL)
    def test_product_objects_sorting(self, cleanup_favorites: None) -> None:
        """Объекты продукта, сортировка.

        :param cleanup_favorites: Фикстура для очистки избранного после автотеста.
        """
        # Объекты продукта_сортировка
        bind9_dnsutils = "bind9-dnsutils"
        base_files = "base-files"
        coordinator_hw_5_assembly = "5.4.0.5177"

        with allure.step("1. Пользователь авторизован в сервисе, открыта страница 'Продукты'."):
            self._impersonate_as_user_with_read_or_write_permissions(write_permissions=False)
            self.component_page.click_on_link_products()

        with allure.step("2. Проверить сортировку на вкладке 'Избранное'"):
            list_favorites = [
                Products.COORDINATOR_HW_5,
                Versions.FIVE_FOUR_ONE,
                Versions.COORDINATOR_HW_5,
                Assemblies.COORDINATOR_HW_5,
                coordinator_hw_5_assembly,
                Products.COORDINATOR_IG_4,
            ]

            self.product_page.click_on_link(UITextElements.ALL_PRODUCTS)

            self._add_to_favorites_and_verify(Products.COORDINATOR_HW_5)
            self._add_to_favorites_and_verify(Products.COORDINATOR_IG_4)

            self.product_page.click_on_expander(Products.COORDINATOR_HW_5)

            self._add_to_favorites_and_verify(Versions.FIVE_FOUR_ONE)
            self._add_to_favorites_and_verify(Versions.COORDINATOR_HW_5)

            self.product_page.click_on_expander(Versions.COORDINATOR_HW_5)

            self._add_to_favorites_and_verify(Assemblies.COORDINATOR_HW_5)
            self._add_to_favorites_and_verify(coordinator_hw_5_assembly)

            self.product_page.click_on_link(UITextElements.FAVORITES).check_sorting_on_favorites_tab(list_favorites)

        with allure.step("3. Проверить сортировку на вкладке 'Все продукты'"):
            list_products = [
                UITextElements.TEXT_COMPONENTS_ENGLISH,
                UITextElements.CONNECT,
                Products.COORDINATOR_AR_2,
                Products.COORDINATOR_HW_4,
                Products.COORDINATOR_HW_5,
                Products.COORDINATOR_IG_4,
                Products.COORDINATOR_IG_5,
                "CryptoUnderground",
                Products.CSP_WINDOWS_4,
                "CSP Windows 5",
            ]

            self.product_page.click_on_link(UITextElements.ALL_PRODUCTS).check_sorting_on_all_products_tab(
                list_products
            )

        with allure.step("4. Проверить сортировку в паспорте продукта, вкладка 'Версии'"):
            self.product_page.click_on_link(Products.COORDINATOR_HW_5)
            self.product_information_page.click_on_link(UITextElements.VERSIONS_TAB).check_links_sorting(
                number_of_first_element=9, reverse=True
            )

        with allure.step("5. Проверить сортировку в паспорте продукта, вкладка 'Компонентный состав'"):
            list_components = [
                Components.BONNIE_PLUS_PLUS,
                Components.BZIP2,
                Components.CRYPTO_UNDERGROUND_V2,
                Components.UTIL_LINUX,
                Components.ZLIB1G,
                Components.ACCORDSDK,
                Components.ACETAO,
                Components.ACPI_SUPPORT_BASE,
                Components.ADDRESSBOOK,
                Components.ADDUSER,
            ]

            self.product_information_page.click_on_link(
                UITextElements.COMPONENT_COMPOSITION
            ).check_sorting_in_product_passport_component_composition_tab(list_components)

        with allure.step("6. Проверить сортировку в паспорте версии продукта, вкладка 'Сборки'"):
            list_assemblies = [
                "5.4.0.7008",
                Assemblies.COORDINATOR_HW_5,
                "5.4.0.5539",
                "5.4.0.5418",
                "5.4.0.5415",
                "5.4.0.5367",
                "5.4.0.5329",
                "5.4.0.5288",
                "5.4.0.5278",
                "5.4.0.5213",
            ]

            self.product_information_page.click_on_link(UITextElements.VERSIONS_TAB).click_on_link(
                Versions.COORDINATOR_HW_5
            )
            self.product_version_information_page.check_sorting_on_assemblies_tab(list_assemblies)

        with allure.step("7. Проверить сортировку в паспорте версии продукта, вкладка 'Компонентный состав'"):
            list_components = [
                Components.ACPI_SUPPORT_BASE,
                Components.ACPID,
                Components.ATOP,
                base_files,
                Components.BASH,
                Components.BIND9,
                bind9_dnsutils,
            ]

            self.product_version_information_page.click_on_link(
                UITextElements.COMPONENT_COMPOSITION
            ).check_sorting_in_version_passport_component_composition_tab(list_components)

        with allure.step("8. Проверить сортировку в паспорте сборки продукта"):
            list_components = [
                Components.ACPID,
                Components.ACPI_SUPPORT_BASE,
                Components.ATOP,
                base_files,
                Components.BASH,
                Components.BIND9,
                Components.BIND9_DEV,
                bind9_dnsutils,
            ]

            self.product_version_information_page.click_on_link(UITextElements.ASSEMBLIES).click_on_link(
                Assemblies.COORDINATOR_HW_5
            )
            self.product_assembly_information_page.check_sorting_in_assembly_passport(
                list_components
            ).click_on_link_products()

    def _add_to_favorites_and_verify(self, item_name: str) -> None:
        """Добавить в избранное и проверить.

        :param item_name: Название элемента.
        """
        (
            self.product_page.click_on_favorites_icon_off(item_name)
            .check_text(item_name + UITextElements.ADDED_TO_FAVORITES)
            .click_on_close_message_icon()
        )
