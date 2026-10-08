import allure
import pytest
from playwright.sync_api import Browser

from settings import settings
from src.constants.products import Products
from src.constants.ui_text_elements import UITextElements
from src.constants.usernames import Usernames
from src.constants.versions import Versions
from src.pages.component_page import ComponentPage
from src.pages.component_assembly_by_configuration_page import (
    ComponentAssemblyByConfigurationPage,
)
from src.pages.component_information_page import ComponentInformationPage
from src.pages.component_package_information_page import ComponentPackageInformationPage
from src.pages.component_version_information_page import ComponentVersionInformationPage
from src.pages.impersonation_page import ImpersonationPage
from src.pages.login_page import LoginPage
from src.pages.product_page import ProductPage
from src.pages.product_assembly_information_page import ProductAssemblyInformationPage
from src.pages.product_information_page import ProductInformationPage
from src.pages.product_version_information_page import ProductVersionInformationPage


class BaseTest:
    """Базовый класс для тестов, содержит общую инициализацию страниц."""

    @pytest.fixture(autouse=True)
    def setup_and_teardown(self, browser: Browser) -> None:
        """Автоматически выполняется перед и после каждого теста, создание общих объектов для тестов.

        :param browser: Используемый браузер.
        """
        context = browser.new_context(ignore_https_errors=settings.IGNORE_HTTPS_ERRORS)
        context.tracing.start(screenshots=settings.SCREENSHOTS, snapshots=settings.SNAPSHOTS, sources=settings.SOURCES)
        context.add_init_script(settings.INIT_SCRIPT)

        page = context.new_page()
        page.set_default_timeout(settings.DEFAULT_TIMEOUT)

        self.component_page = ComponentPage(page)
        self.impersonation_page = ImpersonationPage(page)
        self.login_page = LoginPage(page)
        self.component_information_page = ComponentInformationPage(page)
        self.product_information_page = ProductInformationPage(page)
        self.product_page = ProductPage(page)
        self.component_version_information_page = ComponentVersionInformationPage(page)
        self.product_version_information_page = ProductVersionInformationPage(page)
        self.component_package_information_page = ComponentPackageInformationPage(page)
        self.component_assembly_by_configuration_page = ComponentAssemblyByConfigurationPage(page)
        self.product_assembly_information_page = ProductAssemblyInformationPage(page)

        # Логин и имперсонация за пользователя с правами на запись перед каждым тестом
        self.login_page.go_to_login_page().check_username_input().login_as_settings_user()
        self.component_page.check_title().click_on_user_menu_icon().click_on_impersonation_button()
        self.impersonation_page.impersonate_as_another_user(Usernames.USER_WITH_WRITE_PERMISSIONS)

        yield

        # Остановка трейсинга
        context.tracing.stop(path="../../trace/trace.zip")
        context.close()

    def _impersonate_as_user_with_read_or_write_permissions(self, write_permissions: bool) -> None:
        """Имперсонироваться за пользователя с правами на чтение или с правами на запись.

        :param write_permissions: Если 'True', то пользователь должен быть с правами на запись.
        """
        self.component_information_page.fast_logout().refresh_page()
        self.login_page.check_username_input().login_as_settings_user()
        self.component_page.click_on_user_menu_icon().click_on_impersonation_button()
        self.impersonation_page.impersonate_as_another_user(
            Usernames.USER_WITH_WRITE_PERMISSIONS if write_permissions else Usernames.USER_WITH_READ_PERMISSIONS
        )

    def _check_checkboxes_in_table(self) -> None:
        """Проверить галочки у checkbox'ов в таблице."""
        first_checkbox = 1
        last_checkbox = 3

        for i in range(first_checkbox, last_checkbox + 1):
            self.product_version_information_page.check_checkbox_in_table(i)

    def _setup_version_of_product_component_composition(self) -> None:
        """Предусловие: продукт → версия продукта → вкладка 'Компонентный состав'."""
        self.component_page.click_on_link_products()
        self.product_page.click_on_link(UITextElements.ALL_PRODUCTS).click_on_link(Products.COORDINATOR_HW_5)
        self.product_information_page.click_on_link(UITextElements.VERSIONS_TAB).click_on_link(
            Versions.COORDINATOR_HW_5
        )
        self.product_version_information_page.click_on_link(UITextElements.COMPONENT_COMPOSITION)

    @pytest.fixture
    def cleanup_favorites(self) -> None:
        """Фикстура для очистки избранного после автотеста."""
        yield

        with allure.step("Возвращаем стенд к первоначальному состоянию"):
            self._impersonate_as_user_with_read_or_write_permissions(write_permissions=False)
            self.component_page.click_on_link_products()
            (
                self.product_page.click_on_link(UITextElements.FAVORITES)
                .check_active_tab(UITextElements.FAVORITES)
                .click_on_all_favorites_icons_and_all_close_message_icons()
            )
