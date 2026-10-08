import allure
import pytest
from allure_commons.types import LinkType

from src.constants.components import Components
from src.constants.ui_text_elements import UITextElements
from src.constants.usernames import Usernames
from tests.base.base_test import BaseTest


@allure.parent_suite("Тип компонента.")
@allure.epic("Тип компонента.")
@allure.sub_suite("Тип компонента.")
@allure.severity(allure.severity_level.CRITICAL)
class TestComponentType(BaseTest):
    """Тип компонента."""

    @pytest.fixture
    def set_component_type(self, request: pytest.FixtureRequest) -> None:
        """Фикстура возвращения типа компонента к первоначальному после автотеста.

        :param request: Значения передаваемые в фикстуру.
        """
        yield

        component, value = request.param

        with allure.step("Возвращаем стенд к первоначальному состоянию"):
            self._impersonate_as_user_with_read_or_write_permissions(write_permissions=True)
            (
                self.component_page.click_on_title()
                .click_on_link(UITextElements.ALL_COMPONENTS_TAB)
                .click_on_link(component)
            )
            (
                self.component_information_page.click_on_first_combo_box()
                .click_on_element_with_text(value)
                .refresh_page()
                .check_first_combo_box(placeholder=value)
            )

    @allure.suite("Установить тип компонента.")
    @allure.title("Установить тип компонента.")
    @allure.id("1521319")
    @allure.description("Баг: при выборе значения в combobox'е иногда значение не сохраняется.")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1564151", LinkType.LINK, "TASK 1564151"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1521319", "TestCase 1521319")
    @pytest.mark.parametrize("set_component_type", [(Components.ACCORDSDK, UITextElements.ABSENT)], indirect=True)
    def test_set_component_type(self, set_component_type: None) -> None:
        """Установить тип компонента.

        :param set_component_type: Фикстура возвращения типа компонента к первоначальному после автотеста.
        """
        # Установить тип компонента
        with allure.step(
            "1. Предусловие: Пользователь с правами редактирования паспортов компонентов  авторизован в сервисе, "
            "открыта страница 'Компоненты'"
        ):
            self.component_page.click_on_link(UITextElements.ALL_COMPONENTS_TAB)

        with allure.step(
            "2. В списке выбрать компонент, у которого не задан тип → проверить информацию в поле 'Тип компонента'"
        ):
            self.component_page.click_on_link(Components.ACCORDSDK)
            self.component_information_page.check_first_combo_box(UITextElements.ABSENT)

        with allure.step("3. Кликнуть в поле 'Тип'"):
            elements = [
                UITextElements.ABSENT,
                UITextElements.INTERNAL,
                UITextElements.EXTERNAL,
            ]
            self.component_information_page.click_on_first_combo_box()
            self.component_information_page.check_elements_in_combo_box_component_type(elements)

        with allure.step("4. Выбрать один из вариантов, за исключением 'Не указан'"):
            (
                self.component_information_page.click_on_element_with_text(UITextElements.EXTERNAL)
                .refresh_page()
                .check_first_combo_box(placeholder=UITextElements.EXTERNAL)
            )

        with allure.step(
            "5. В списке компонентов выбрать любой другой компонент → далее вернуться к компоненту из ш. 2"
        ):
            self.component_information_page.click_on_title()
            self.component_page.click_on_link(UITextElements.ALL_COMPONENTS_TAB).click_on_link(Components.ACETAO)
            self.component_information_page.click_on_title()
            self.component_page.click_on_link(UITextElements.ALL_COMPONENTS_TAB).click_on_link(Components.ACCORDSDK)
            self.component_information_page.check_first_combo_box(placeholder=UITextElements.EXTERNAL)

        with allure.step(
            "6. Войти в сервис под пользователем с правами на чтение по компоненту из ш. 2 → проверить отображение "
            "типа компонента"
        ):
            self._impersonate_as_user_with_read_or_write_permissions(write_permissions=False)
            (
                self.component_page.click_on_title()
                .click_on_link(UITextElements.ALL_COMPONENTS_TAB)
                .click_on_link(Components.ACCORDSDK)
            )
            self.component_information_page.check_component_type_text(UITextElements.EXTERNAL)

    @allure.suite("Удалить тип компонента.")
    @allure.title("Удалить тип компонента.")
    @allure.id("1521321")
    @allure.description("Баг: при выборе значения в combobox'е иногда значение не сохраняется.")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1564161", LinkType.LINK, "TASK 1564161"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1521321", "TestCase 1521321")
    @pytest.mark.parametrize("set_component_type", [(Components.ADDRESSBOOK, UITextElements.INTERNAL)], indirect=True)
    def test_delete_component_type(self, set_component_type: None) -> None:
        """Удалить тип компонента.

        :param set_component_type: Фикстура возвращения типа компонента к первоначальному после автотеста.
        """
        # Удалить Тип компонента
        with allure.step(
            "1. Предусловие: Пользователь с правами редактирования паспортов компонентов  авторизован в сервисе, "
            "открыта страница 'Компоненты'"
        ):
            self.component_page.click_on_link(UITextElements.ALL_COMPONENTS_TAB)

        with allure.step("2. В списке компонентов выбрать компонент с заданным типом"):
            self.component_page.fill_in_search_input(Components.ADDRESSBOOK).click_on_link(Components.ADDRESSBOOK)
            self.component_information_page.check_first_combo_box(placeholder=UITextElements.INTERNAL)

        with allure.step("3. В поле 'Тип' выбрать значение 'Не указан'"):
            (
                self.component_information_page.click_on_first_combo_box()
                .click_on_element_with_text(UITextElements.ABSENT)
                .refresh_page()
                .check_first_combo_box(UITextElements.ABSENT)
            )

            # Пользователь с правами на чтение
            self._impersonate_as_user_with_read_or_write_permissions(write_permissions=False)
            (
                self.component_page.click_on_title()
                .click_on_link(UITextElements.ALL_COMPONENTS_TAB)
                .fill_in_search_input(Components.ADDRESSBOOK)
                .click_on_link(Components.ADDRESSBOOK)
            )
            self.component_information_page.check_component_type_text(UITextElements.DASH)

    @allure.suite("Изменить тип компонента.")
    @allure.title("Изменить тип компонента.")
    @allure.id("1521320")
    @allure.description("Баг: при выборе значения в combobox'е иногда значение не сохраняется.")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1564958", LinkType.LINK, "TASK 1564958"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1521320", "TestCase 1521320")
    @pytest.mark.parametrize("set_component_type", [(Components.ADDRESSBOOK, UITextElements.INTERNAL)], indirect=True)
    def test_change_component_type(self, set_component_type: None) -> None:
        """Изменить тип компонента.

        :param set_component_type: Фикстура возвращения типа компонента к первоначальному после автотеста.
        """
        # Изменить тип компонента
        with allure.step(
            "1. Предусловие: Пользователь с правами редактирования паспортов компонентов авторизован в сервисе, "
            "открыта страница 'Компоненты'"
        ):
            self.component_page.click_on_link(UITextElements.ALL_COMPONENTS_TAB)

        with allure.step("2. В списке компонентов выбрать компонент с заданным типом"):
            self.component_page.fill_in_search_input(Components.ADDRESSBOOK).click_on_link(Components.ADDRESSBOOK)
            self.component_information_page.check_first_combo_box(placeholder=UITextElements.INTERNAL)

        with allure.step("3. Изменить тип компонента (в выпадающем списке выбрать другое значение)"):
            (
                self.component_information_page.click_on_first_combo_box()
                .click_on_element_with_text(UITextElements.EXTERNAL)
                .refresh_page()
                .check_first_combo_box(placeholder=UITextElements.EXTERNAL)
            )

        with allure.step(
            "4. В списке компонентов выбрать любой другой компонент → далее вернуться к компоненту из ш. 2"
        ):
            self.component_information_page.click_on_title()
            self.component_page.click_on_link(UITextElements.ALL_COMPONENTS_TAB).click_on_link(Components.ACETAO)
            self.component_information_page.click_on_title()
            self.component_page.click_on_link(UITextElements.ALL_COMPONENTS_TAB).click_on_link(Components.ADDRESSBOOK)
            self.component_information_page.check_first_combo_box(placeholder=UITextElements.EXTERNAL)

        with allure.step(
            "5. Войти в сервис под пользователем с правами на чтение по компоненту из ш. 2 → проверить отображение"
            " типа компонента"
        ):
            self._impersonate_as_user_with_read_or_write_permissions(write_permissions=False)
            (
                self.component_page.click_on_title()
                .click_on_link(UITextElements.ALL_COMPONENTS_TAB)
                .click_on_link(Components.ADDRESSBOOK)
            )
            self.component_information_page.check_component_type_text(UITextElements.EXTERNAL)

    @allure.parent_suite("Тип компонента и значение.")
    @allure.suite("Тип компонента, значение по умолчанию.")
    @allure.epic("Тип компонента и значение.")
    @allure.sub_suite("Тип компонента и значение.")
    @allure.title("Тип компонента, значение по умолчанию.")
    @allure.id("1513302")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1533740", LinkType.LINK, "TASK 1533740"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1513302", "TestCase 1513302")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.multiple_streams
    def test_component_type_default_value(self) -> None:
        """Тип компонента, значение по умолчанию."""
        # Тип компонента_значение по умолчанию
        with allure.step("1. Предусловие: Пользователь авторизован в сервисе, открыта страница 'Компоненты'"):
            self.component_page.click_on_link(UITextElements.ALL_COMPONENTS_TAB)

        with allure.step("2. В списке выбрать любой компонент, проверить информацию в поле 'Тип компонента'"):
            self.component_page.click_on_link(Components.ACCORDSDK)
            (
                self.component_information_page.check_first_combo_box(UITextElements.ABSENT)
                .click_on_user_menu_icon()
                .logout()
            )
            self.login_page.check_username_input().login_as_settings_user()
            self.component_page.click_on_user_menu_icon().click_on_impersonation_button()
            self.impersonation_page.impersonate_as_another_user(Usernames.USER_WITH_READ_PERMISSIONS)
            (
                self.component_page.click_on_title()
                .click_on_link(UITextElements.ALL_COMPONENTS_TAB)
                .click_on_link(Components.ACCORDSDK)
            )
            self.component_information_page.check_component_type_text(UITextElements.DASH)
