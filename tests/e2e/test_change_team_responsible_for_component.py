import allure
import pytest
from allure_commons.types import LinkType

from src.constants.components import Components
from src.constants.test_inputs import TestInputs
from src.constants.ui_text_elements import UITextElements
from src.constants.usernames import Usernames
from tests.base.base_test import BaseTest


@allure.parent_suite("Изменить команду, ответственную за компонент.")
@allure.epic("Изменить команду, ответственную за компонент.")
@allure.sub_suite("Изменить команду, ответственную за компонент.")
@allure.severity(allure.severity_level.CRITICAL)
class TestChangeTeamResponsibleForComponent(BaseTest):
    """Изменить команду, ответственную за компонент."""

    @pytest.fixture
    def remove_implementation_manager(self) -> None:
        """Фикстура удаления ответственного за реализацию (компонент accordsdk)."""
        yield

        with allure.step("Возвращаем стенд к первоначальному состоянию"):
            self._impersonate_as_user_with_read_or_write_permissions(write_permissions=True)
            self._setup()
            self.component_page.click_on_link(Components.ACCORDSDK)
            (
                self.component_information_page.click_on_all_cross_icons()
                .refresh_page()
                .check_responsible_for_implementation_of_component_combo_box(placeholder=UITextElements.ABSENT)
            )

    @pytest.fixture
    def set_team_responsible_for_component(self, request: pytest.FixtureRequest) -> None:
        """Фикстура возвращения команды, ответственной за компонент, к первоначальной после автотеста.

        :param request: Значения передаваемые в фикстуру.
        """
        yield

        component, full_name = request.param

        with allure.step("Возвращаем стенд к первоначальному состоянию"):
            self._impersonate_as_user_with_read_or_write_permissions(write_permissions=True)
            self._setup()
            self.component_page.click_on_link(component)
            (
                self.component_information_page.click_on_responsible_for_implementation_of_component_combo_box()
                .fill_in_responsible_for_implementation_of_component_combo_box(full_name)
                .click_on_component_owner_combo_box()
                .fill_in_component_owner_combo_box(full_name)
                .click_on_technical_expert_combo_box()
                .fill_in_technical_expert_combo_box(full_name)
                .refresh_page()
                .check_responsible_for_implementation_of_component_combo_box(placeholder=full_name)
                .check_component_owner_combo_box(placeholder=full_name)
                .check_technical_expert_combo_box(placeholder=full_name)
            )

    @allure.suite("Удалить ответственного за реализацию.")
    @allure.title("Удалить ответственного за реализацию.")
    @allure.id("1521324")
    @allure.description("Баг: при выборе значения в combobox'е иногда значение не сохраняется.")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1564961", LinkType.LINK, "TASK 1564961"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1521324", "TestCase 1521324")
    @pytest.mark.parametrize(
        "set_team_responsible_for_component", [(Components.ACPI, Usernames.USER_WITH_READ_PERMISSIONS)], indirect=True
    )
    def test_remove_person_responsible_for_implementation(self, set_team_responsible_for_component: None) -> None:
        """Удалить ответственного за реализацию.

        :param set_team_responsible_for_component: Фикстура возвращения ответственной команды к первоначальной.
        """
        # Удалить Ответственного за реализацию
        with allure.step(
            "1. Предусловие: Пользователь с правами редактирования паспортов компонентов авторизован в сервисе, "
            "открыта страница 'Компоненты'. Есть компоненты для которых указаны: 'Ответственный за реализацию', "
            "'Владелец', 'Технический эксперт'"
        ):
            self.component_page.click_on_link(UITextElements.ALL_COMPONENTS_TAB)

        with allure.step(
            "2. В списке выбрать компонент → очистить поля: 'Ответственный за реализацию', 'Владелец', "
            "'Технический эксперт'"
        ):
            self.component_page.fill_in_search_input(Components.ACPI).click_on_link(Components.ACPI)
            self.component_information_page.click_on_all_cross_icons()

        with allure.step("3. Войти в сервис под пользователем с правами на чтение, в списке выбрать компонент из ш. 2"):
            self._impersonate_as_user_with_read_or_write_permissions(write_permissions=False)
            self._setup()
            self.component_page.fill_in_search_input(Components.ACPI).click_on_link(Components.ACPI)
            (
                self.component_information_page.check_responsible_for_implementation_of_component(UITextElements.DASH)
                .check_component_owner(UITextElements.DASH)
                .check_technical_expert_of_component(UITextElements.DASH)
            )

    @allure.suite("Добавить ответственного за реализацию.")
    @allure.title("Добавить ответственного за реализацию.")
    @allure.id("1521322")
    @allure.description("Баг: Текст 'Пожалуйста, введите минимум 3 символа' не отображается на странице.")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1565847", LinkType.LINK, "TASK 1565847"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1521322", "TestCase 1521322")
    def test_add_person_responsible_for_implementation(self, remove_implementation_manager: None) -> None:
        """Добавить ответственного за реализацию.

        :param remove_implementation_manager: Фикстура удаления ответственного за реализацию (компонент accordsdk).
        """
        # Добавить Ответственного за реализацию
        with allure.step(
            "1. Предусловие: Пользователь с правами редактирования паспортов компонентов авторизован в сервисе, "
            "открыта страница 'Компоненты'"
        ):
            self.component_page.click_on_link(UITextElements.ALL_COMPONENTS_TAB)

        with allure.step(
            "2. В списке выбрать компонент, для которого не указаны сотрудники команды, ответственной за компонент"
        ):
            self.component_page.click_on_link(Components.ACCORDSDK)
            (
                self.component_information_page.check_component_owner_combo_box(placeholder=UITextElements.ABSENT)
                .check_responsible_for_implementation_of_component_combo_box(placeholder=UITextElements.ABSENT)
                .check_technical_expert_combo_box(placeholder=UITextElements.ABSENT)
            )

        with allure.step(
            "3. В поле 'Ответственный за реализацию' ввести НЕвалидное значение (ФИО сотрудника не из ЦРПП, цифры, "
            "спец. символы и т.п.)"
        ):
            (
                self.component_information_page.click_on_responsible_for_implementation_of_component_combo_box()
                .fill_in_responsible_for_implementation_of_component_combo_box(
                    full_name=TestInputs.SPECIAL_CHARACTERS, click_on_tooltip=False
                )
                .check_text(UITextElements.NOTHING_FOUND)
                .click_on_responsible_for_implementation_of_component_combo_box()
            )

        with allure.step("4. Очистить поле 'Ответственный за реализацию'"):
            (
                self.component_information_page.refresh_page()
                .check_responsible_for_implementation_of_component_combo_box(placeholder=UITextElements.ABSENT)
                .click_on_responsible_for_implementation_of_component_combo_box()
                .check_text("Пожалуйста, введите минимум 3 символа")
            )

        with allure.step(
            "5. В поле 'Ответственный за реализацию' ввести валидное значение (ФИО любого сотрудника ЦРПП); "
            "6. Выбрать любого сотрудника из списка;"
        ):
            (
                self.component_information_page.fill_in_responsible_for_implementation_of_component_combo_box(
                    Usernames.USER_WITH_READ_PERMISSIONS
                )
                .check_responsible_for_implementation_of_component_combo_box(
                    placeholder=Usernames.USER_WITH_READ_PERMISSIONS
                )
                .check_component_owner_combo_box(placeholder=UITextElements.ABSENT)
                .check_technical_expert_combo_box(placeholder=UITextElements.ABSENT)
            )

        with allure.step("7. В списке выбрать любой другой компонент и вернуться к компоненту из ш. 2"):
            self.component_information_page.click_on_title()
            self.component_page.click_on_link(UITextElements.ALL_COMPONENTS_TAB).click_on_link(Components.ACETAO)
            self.component_information_page.click_on_title()
            self.component_page.click_on_link(UITextElements.ALL_COMPONENTS_TAB).click_on_link(Components.ACCORDSDK)
            (
                self.component_information_page.check_responsible_for_implementation_of_component_combo_box(
                    placeholder=Usernames.USER_WITH_READ_PERMISSIONS
                )
                .check_component_owner_combo_box(placeholder=UITextElements.ABSENT)
                .check_technical_expert_combo_box(placeholder=UITextElements.ABSENT)
            )

        with allure.step(
            "8. Войти в сервис под пользователем, которому доступно только чтение, в списке выбрать компонент из ш. 2"
        ):
            self._impersonate_as_user_with_read_or_write_permissions(write_permissions=False)
            self._setup()
            self.component_page.click_on_link(Components.ACCORDSDK)
            (
                self.component_information_page.check_responsible_for_implementation_of_component(
                    f"{Usernames.USER_WITH_READ_PERMISSIONS} Программист"
                )
                .check_component_owner(UITextElements.DASH)
                .check_technical_expert_of_component(UITextElements.DASH)
            )

    @allure.suite("Изменить команду, ответственную за компонент.")
    @allure.title("Изменить команду, ответственную за компонент.")
    @allure.id("1521323")
    @allure.description("Баг: при выборе значения в combobox'е иногда значение не сохраняется.")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1565853", LinkType.LINK, "TASK 1565853"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1521323", "TestCase 1521323")
    @pytest.mark.parametrize(
        "set_team_responsible_for_component", [(Components.ACPI, Usernames.USER_WITH_READ_PERMISSIONS)], indirect=True
    )
    def test_change_team_responsible_for_component(self, set_team_responsible_for_component: None) -> None:
        """Изменить команду, ответственную за компонент.

        :param set_team_responsible_for_component: Фикстура возвращения ответственной команды к первоначальной.
        """
        # Изменить команду, ответственную за компонент
        senior_test_engineer = "Старший инженер-тестировщик"

        with allure.step(
            "1. Предусловие: Пользователь с правами редактирования паспортов компонентов авторизован в сервисе, "
            "открыта страница 'Компоненты'"
        ):
            self.component_page.click_on_link(UITextElements.ALL_COMPONENTS_TAB)

        with allure.step("2. В списке выбрать компонент для которого указан 'Ответственный за реализацию'"):
            self.component_page.fill_in_search_input(Components.ACPI).click_on_link(Components.ACPI)
            self.component_information_page.check_responsible_for_implementation_of_component_combo_box(
                placeholder=Usernames.USER_WITH_READ_PERMISSIONS
            )

        with allure.step(
            "3. Очистить поле 'Ответственный за реализацию' → ввести ФИО другого сотрудника; "
            "4. Повторить ш. 2 и 3 для изменения 'Владельца' и 'Технического эксперта';"
        ):
            (
                self.component_information_page.click_on_all_cross_icons()
                .click_on_responsible_for_implementation_of_component_combo_box()
                .fill_in_responsible_for_implementation_of_component_combo_box(Usernames.USER_WITH_WRITE_PERMISSIONS)
                .click_on_component_owner_combo_box()
                .fill_in_component_owner_combo_box(Usernames.USER_WITH_WRITE_PERMISSIONS)
                .click_on_technical_expert_combo_box()
                .fill_in_technical_expert_combo_box(Usernames.USER_WITH_WRITE_PERMISSIONS)
                .refresh_page()
                .check_responsible_for_implementation_of_component_combo_box(
                    placeholder=Usernames.USER_WITH_WRITE_PERMISSIONS
                )
                .check_component_owner_combo_box(placeholder=Usernames.USER_WITH_WRITE_PERMISSIONS)
                .check_technical_expert_combo_box(placeholder=Usernames.USER_WITH_WRITE_PERMISSIONS)
            )

        with allure.step("5. В списке выбрать любой другой компонент и вернуться к компоненту из ш. 2"):
            self.component_information_page.click_on_title()
            (self.component_page.click_on_link(UITextElements.ALL_COMPONENTS_TAB).click_on_link(Components.ACETAO))
            self.component_information_page.click_on_title()
            (
                self.component_page.click_on_link(UITextElements.ALL_COMPONENTS_TAB)
                .fill_in_search_input(Components.ACPI)
                .click_on_link(Components.ACPI)
            )
            (
                self.component_information_page.check_responsible_for_implementation_of_component_combo_box(
                    placeholder=Usernames.USER_WITH_WRITE_PERMISSIONS
                )
                .check_component_owner_combo_box(placeholder=Usernames.USER_WITH_WRITE_PERMISSIONS)
                .check_technical_expert_combo_box(placeholder=Usernames.USER_WITH_WRITE_PERMISSIONS)
            )

        with allure.step("6. Войти в сервис под пользователем с правами на чтение, в списке выбрать компонент из ш. 2"):
            self._impersonate_as_user_with_read_or_write_permissions(write_permissions=False)
            self._setup()
            self.component_page.fill_in_search_input(Components.ACPI).click_on_link(Components.ACPI)
            (
                self.component_information_page.check_responsible_for_implementation_of_component(
                    f"{Usernames.USER_WITH_WRITE_PERMISSIONS} {senior_test_engineer}"
                )
                .check_component_owner(f"{Usernames.USER_WITH_WRITE_PERMISSIONS} {senior_test_engineer}")
                .check_technical_expert_of_component(f"{Usernames.USER_WITH_WRITE_PERMISSIONS} {senior_test_engineer}")
            )

    def _setup(self) -> None:
        """Предусловие: открыта вкладка 'Все компоненты'."""
        self.component_page.click_on_title().click_on_link(UITextElements.ALL_COMPONENTS_TAB)
