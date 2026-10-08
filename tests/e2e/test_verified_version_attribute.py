import allure
from allure_commons.types import LinkType

from src.constants.ui_text_elements import UITextElements
from tests.base.base_test import BaseTest


@allure.parent_suite("Атрибут 'Верифицированная версия'.")
@allure.epic("Атрибут 'Верифицированная версия'.")
@allure.sub_suite("Атрибут 'Верифицированная версия'.")
@allure.severity(allure.severity_level.CRITICAL)
class TestVerifiedVersionAttribute(BaseTest):
    """Атрибут 'Верифицированная версия'."""

    @allure.suite(
        "Атрибут 'Верифицированная версия', отображение в паспорте компонента/версии компонента/пакете компонента"
    )
    @allure.title(
        "Атрибут 'Верифицированная версия', отображение в паспорте компонента/версии компонента/пакете компонента"
    )
    @allure.id("1567178")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1568356", LinkType.LINK, "TASK 1568356"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1567178", "TestCase 1567178")
    def test_verified_version_attribute_display(self) -> None:
        """Атрибут 'Верифицированная версия', отображение в паспорте компонента/версии компонента/пакете компонента."""
        # Атрибут "Верифицированная версия"_отображение в паспорте компонента /версии компонента/пакета компонента
        component_abab = "abab"
        abab_version = "2.0"
        abab_package = "2.0.6"

        with allure.step(
            "1. Предусловие: Пользователь с правами на чтение паспортов компонентов авторизован в сервисе. "
            "В определенном пакете установлен атрибут 'Верифицированная версия'. Открыт паспорт пакета компонента"
        ):
            self._impersonate_as_user_with_read_or_write_permissions(write_permissions=False)
            (
                self.component_page.click_on_title()
                .click_on_link(UITextElements.ALL_COMPONENTS_TAB)
                .fill_in_search_input(component_abab)
                .click_on_link(component_abab)
            )
            self.component_information_page.click_on_link(UITextElements.VERSIONS_TAB).click_on_link(abab_version)
            self.product_version_information_page.click_on_link(UITextElements.PACKAGES_TAB).click_on_link(abab_package)

        with allure.step("2. Проверить отображение атрибута 'Верифицированная версия'"):
            self.component_package_information_page.check_text(UITextElements.VERIFIED_VERSION)

        with allure.step(
            "3. Подняться на уровень выше (открыть паспорт версии компонента) → Проверить отображение атрибута "
            "'Верифицированная версия'"
        ):
            self.component_package_information_page.go_to_previous_or_next_page(previous=True)
            self.product_version_information_page.go_to_previous_or_next_page(previous=True).check_text(
                page_text=UITextElements.VERIFIED_VERSION, visible=False
            )

        with allure.step(
            "4. Перейти на вкладку 'Пакеты' паспорта версии компонента → Проверить отображение атрибута "
            "'Верифицированная версия'"
        ):
            table_headings = [
                UITextElements.TEXT_PACKAGE,
                UITextElements.VERIFIED_VERSION,
                UITextElements.PACKAGE_MANAGER,
            ]
            self.product_version_information_page.go_to_previous_or_next_page(previous=False).check_table_headings(
                table_headings
            )

        with allure.step(
            "5. Подняться на уровень паспорта компонента → Проверить отображение атрибута 'Верифицированная версия'"
        ):
            self.product_version_information_page.go_to_previous_or_next_page(count=2, previous=True)
            self.component_information_page.go_to_previous_or_next_page(previous=True).check_text(
                "Содержит верифицированную версию"
            )
