import allure
import pytest
from allure_commons.types import LinkType

from src.constants.colors import Colors
from src.constants.components import Components
from src.constants.lists import Lists
from src.constants.packages import Packages
from src.constants.products import Products
from src.constants.radar_area_values import RadarAreaValues
from src.constants.regular_expressions import RegularExpressions
from src.constants.ui_text_elements import UITextElements
from src.constants.versions import Versions
from tests.base.base_test import BaseTest


@allure.parent_suite("Групповая разметка.")
@allure.epic("Групповая разметка.")
@allure.sub_suite("Групповая разметка.")
class TestGroupMarkup(BaseTest):
    """Групповая разметка."""

    _CHECKBOX_ALL = 0
    _FIRST_CHECKBOX = 14
    _LAST_CHECKBOX = 16
    _COMPONENTS_INFORMATION_UPDATED_SUCCESSFULLY = "Информация о компонентах успешно обновлена"
    _GROUP_MARKUP = "Групповая разметка"
    _ERROR_MESSAGE = "Во время обновления информации о компонентах произошла ошибка"
    _INFORMATION_MESSAGE_SECURITY_FUNCTION = (
        'Для выбранных компонентов в параметре "Функция безопасности" будет установлено значение "Косвенно".Продолжить?'
    )
    _INFORMATION_MESSAGE_ATTACK_SURFACE = (
        'Для выбранных компонентов в параметре "Поверхность атаки" будет установлено значение "Косвенно".Продолжить?'
    )
    _VALUES = [
        " ",
        Components.ACPI_SUPPORT_BASE,
        RadarAreaValues.UNKNOWN,
        Packages.ACPI_SUPPORT_BASE,
        UITextElements.NOT_SPECIFIED,
        "",
        UITextElements.NOT_SPECIFIED,
        "",
    ]

    @pytest.fixture
    def return_security_function_or_attack_surface_to_all_components(self, request: pytest.FixtureRequest) -> None:
        """Фикстура для возвращения функции безопасности или поверхности атаки всем компонентам.

        :param request: Значения передаваемые в фикстуру.
        """
        yield

        # Если `security_function == False`, тогда возвращаем 'Поверхность атаки' всем компонентам
        security_function = request.param

        with allure.step("Возвращаем стенд к первоначальному состоянию"):
            self._impersonate_as_user_with_read_or_write_permissions(write_permissions=True)
            self.component_page.click_on_link_products()
            self.product_page.click_on_link(UITextElements.ALL_PRODUCTS).click_on_link(
                Products.VIPNET_CLIENT_4_X_FOR_WINDOWS
            )
            (
                self.product_version_information_page.click_on_link(UITextElements.VERSIONS_TAB)
                .click_on_link(Versions.VIPNET_CLIENT_4_X_FOR_WINDOWS)
                .click_on_link(UITextElements.COMPONENT_COMPOSITION)
                .click_on_checkbox_in_table(self._CHECKBOX_ALL)
                .click_on_element_with_text(
                    UITextElements.SECURITY_FUNCTION if security_function else UITextElements.ATTACK_SURFACE
                )
                .click_on_element_with_text(UITextElements.NOT_SPECIFIED)
                .click_on_button_with_text(UITextElements.YES)
            )

            if security_function:
                self.product_version_information_page.click_on_checkbox_in_table(self._CHECKBOX_ALL)
            else:
                values = [
                    " ",
                    Components.ACETAO,
                    RadarAreaValues.UNKNOWN,
                    "6.4.6.67",
                    UITextElements.NOT_SPECIFIED,
                    "",
                    UITextElements.NOT_SPECIFIED,
                    "",
                ]

                self.product_version_information_page.check_table_text_values(values)

    @allure.suite("Групповая разметка, функция безопасности, отказ.")
    @allure.title("Групповая разметка, функция безопасности, отказ.")
    @allure.id("1571944")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1606175", LinkType.LINK, "TASK 1606175"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1571944", "TestCase 1571944")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.multiple_streams
    def test_group_markup_security_function_rejection(self) -> None:
        """Групповая разметка, функция безопасности, отказ."""
        # Групповая разметка - Функция безопасности - отказ
        with allure.step(
            "1. Предусловие: Пользователь с правами редактирования паспортов продуктов авторизован в сервисе, открыт "
            "паспорт версии продукта на вкладке 'Компонентный состав', 'Функция безопасности' и 'Поверхность атаки' не "
            "размечены"
        ):
            self._setup()

        with allure.step("2. Выбрать 2-3 компонента с помощью чекбоксов"):
            self._select_checkboxes_and_checks()

        with allure.step("3. В списке выбрать произвольное значение функции безопасности"):
            self._select_arbitrary_value_for_security_function_or_attack_surface(UITextElements.SECURITY_FUNCTION)

        with allure.step("4. Нажать кнопку 'Нет'"):
            self._click_no_button(UITextElements.SECURITY_FUNCTION)
            self._check_checkboxes_in_table()

    @allure.suite("Групповая разметка, поверхность атаки, отказ.")
    @allure.title("Групповая разметка, поверхность атаки, отказ.")
    @allure.id("1571961")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1606181", LinkType.LINK, "TASK 1606181"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1571961", "TestCase 1571961")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.multiple_streams
    def test_group_markup_attack_surface_rejection(self) -> None:
        """Групповая разметка, поверхность атаки, отказ."""
        # Групповая разметка - Поверхность атаки - отказ
        with allure.step(
            "1. Предусловие: Пользователь с правами редактирования паспортов продуктов авторизован в сервисе, открыт "
            "паспорт версии продукта на вкладке 'Компонентный состав', 'Функция безопасности' и 'Поверхность атаки' не "
            "размечены"
        ):
            self._setup()

        with allure.step("2. Выбрать 2-3 компонента с помощью чекбоксов"):
            self._select_checkboxes_and_checks()

        with allure.step("3. В списке выбрать произвольное значение поверхности атаки"):
            self._select_arbitrary_value_for_security_function_or_attack_surface(UITextElements.ATTACK_SURFACE)

        with allure.step("4. Нажать кнопку 'Нет'"):
            self._click_no_button(UITextElements.ATTACK_SURFACE)
            self._check_checkboxes_in_table()

    @allure.suite("Групповая разметка, поверхность атаки, неудачно.")
    @allure.title("Групповая разметка, поверхность атаки, неудачно.")
    @allure.id("1571962")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1608534", LinkType.LINK, "TASK 1608534"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1571962", "TestCase 1571962")
    @allure.severity(allure.severity_level.NORMAL)
    def test_group_markup_attack_surface_unsuccessful(self) -> None:
        """Групповая разметка, поверхность атаки, неудачно."""
        # Групповая разметка - Поверхность атаки - неудачно
        with allure.step(
            "1. Предусловие: Пользователь с правами редактирования паспортов продуктов авторизован в сервисе, открыт "
            "паспорт версии продукта на вкладке 'Компонентный состав', 'Функция безопасности' и 'Поверхность атаки' не "
            "размечены"
        ):
            self._setup()

        with allure.step("2. Выбрать 2-3 компонента с помощью чекбоксов"):
            self._select_checkboxes_and_checks()

        with allure.step("3. В списке выбрать произвольное значение поверхности атаки"):
            self._select_arbitrary_value_for_security_function_or_attack_surface(UITextElements.ATTACK_SURFACE)

        with allure.step("4. Отключить сеть → Нажать кнопку 'Да'"):
            self._disconnect_network_and_click_yes_button()
            self._click_on_close_message_icon_and_check_table_headings()
            self.product_version_information_page.check_table_text_values(self._VALUES)
            self._check_checkboxes_in_table()

    @allure.suite("Групповая разметка, функция безопасности, неудачно.")
    @allure.title("Групповая разметка, функция безопасности, неудачно.")
    @allure.id("1571948")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1608549", LinkType.LINK, "TASK 1608549"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1571948", "TestCase 1571948")
    @allure.severity(allure.severity_level.MINOR)
    def test_group_markup_security_function_unsuccessful(self) -> None:
        """Групповая разметка, функция безопасности, неудачно."""
        # Групповая разметка Функция безопасности - неудачно
        with allure.step(
            "1. Предусловие: Пользователь с правами редактирования паспортов продуктов авторизован в сервисе, открыт "
            "паспорт версии продукта на вкладке 'Компонентный состав', 'Функция безопасности' и 'Поверхность атаки' не "
            "размечены"
        ):
            self._setup()

        with allure.step("2. Выбрать 2-3 компонента с помощью чекбоксов"):
            self._select_checkboxes_and_checks()

        with allure.step("3. В списке выбрать произвольное значение функции безопасности"):
            self._select_arbitrary_value_for_security_function_or_attack_surface(UITextElements.SECURITY_FUNCTION)

        with allure.step("4. Отключить сеть → Нажать кнопку 'Да'"):
            self._disconnect_network_and_click_yes_button()
            self._click_on_close_message_icon_and_check_table_headings()
            self.product_version_information_page.check_table_text_values(self._VALUES)
            self._check_checkboxes_in_table()

    @allure.suite("Групповая разметка, функция безопасности.")
    @allure.title("Групповая разметка, функция безопасности.")
    @allure.id("1571937")
    @allure.description("Групповая разметка, функция безопасности.")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1622496", LinkType.LINK, "TASK 1622496"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1571937", "TestCase 1571937")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("return_security_function_or_attack_surface_to_all_components", [True], indirect=True)
    def test_group_markup_security_function(
        self, return_security_function_or_attack_surface_to_all_components: None
    ) -> None:
        """Групповая разметка, функция безопасности.

        :param return_security_function_or_attack_surface_to_all_components: Фикстура для возвращения ФБ или ПА.
        """
        # Групповая разметка - Функция безопасности
        first_checkbox = 1
        last_checkbox = 3

        with allure.step(
            "1. Предусловие: Пользователь с правами редактирования паспортов продуктов авторизован в сервисе, открыт "
            "паспорт версии продукта на вкладке 'Компонентный состав', ФБ и ПА не размечены."
        ):
            self.component_page.click_on_link_products()
            self.product_page.click_on_link(UITextElements.ALL_PRODUCTS).click_on_link(
                Products.VIPNET_CLIENT_4_X_FOR_WINDOWS
            )
            self.product_information_page.click_on_link(UITextElements.VERSIONS_TAB).click_on_link(
                Versions.VIPNET_CLIENT_4_X_FOR_WINDOWS
            )
            self.product_version_information_page.click_on_link(UITextElements.COMPONENT_COMPOSITION)

        with allure.step("2. Выбрать 2-3 компонента с помощью чекбоксов"):
            for i in range(first_checkbox, last_checkbox + 1):
                self.product_version_information_page.click_on_checkbox_in_table(i)

            (
                self.product_version_information_page.check_text(UITextElements.THREE_CHOSEN)
                .check_text(UITextElements.SECURITY_FUNCTION)
                .check_text(UITextElements.ATTACK_SURFACE)
                .check_text(UITextElements.TRANSFER_MARKUP)
                .check_checkbox_component_in_table()
            )
            self._check_checkboxes_in_table()

        with allure.step("3. Открыть выпадающий список 'Функция безопасности'"):
            (
                self.product_version_information_page.click_on_element_with_text(UITextElements.SECURITY_FUNCTION)
                .check_indication_in_list_security_function_or_attack_surface(Colors.GREEN)
                .check_indication_in_list_security_function_or_attack_surface(Colors.YELLOW)
                .check_indication_in_list_security_function_or_attack_surface(Colors.RED)
                .check_indication_in_list_security_function_or_attack_surface(Colors.GREY)
            )

        with allure.step("4. В списке выбрать произвольное значение функции безопасности"):
            self.product_version_information_page.click_on_element_with_text(UITextElements.YES).check_button_with_text(
                UITextElements.NO
            )

        with allure.step("5. Нажать кнопку 'Да'"):
            values = [
                " ",
                Components.ACETAO,
                RadarAreaValues.UNKNOWN,
                "6.4.6.67",
                UITextElements.YES,
                "",
                UITextElements.NOT_SPECIFIED,
                "",
            ]

            (
                self.product_version_information_page.click_on_button_with_text(UITextElements.YES)
                .check_visibility_indication(Colors.GREEN)
                .check_text(self._GROUP_MARKUP)
                .check_text(self._COMPONENTS_INFORMATION_UPDATED_SUCCESSFULLY)
                .check_text(RegularExpressions.PATTERN_STRING_TIME)
            )
            self._click_on_close_message_icon_and_check_table_headings()
            self.product_version_information_page.check_table_text_values(values)

            for i in range(first_checkbox - 1, last_checkbox):
                self.product_version_information_page.check_text(UITextElements.YES, nth=i)

        with allure.step("6. Повторить шаги кейса выставив одному компоненту функцию безопасности, используя чекбоксы"):
            (
                self.product_version_information_page.click_on_checkbox_in_table(first_checkbox)
                .click_on_element_with_text(UITextElements.SECURITY_FUNCTION)
                .click_on_element_with_text(UITextElements.INDIRECTLY)
                .check_text(self._INFORMATION_MESSAGE_SECURITY_FUNCTION)
                .click_on_button_with_text(UITextElements.YES)
            )

        with allure.step("7. Повторить шаги кейса выставив всем компонентам функцию безопасности"):
            (
                self.product_version_information_page.click_on_checkbox_in_table(self._CHECKBOX_ALL)
                .click_on_element_with_text(UITextElements.SECURITY_FUNCTION)
                .click_on_element_with_text(UITextElements.NO)
                .click_on_button_with_text(UITextElements.YES)
                .click_on_checkbox_in_table(self._CHECKBOX_ALL)
            )

    @allure.suite("Групповая разметка, поверхность атаки.")
    @allure.title("Групповая разметка, поверхность атаки.")
    @allure.id("1571957")
    @allure.description("Групповая разметка, поверхность атаки.")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1623066", LinkType.LINK, "TASK 1623066"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1571957", "TestCase 1571957")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("return_security_function_or_attack_surface_to_all_components", [False], indirect=True)
    def test_group_markup_attack_surface(
        self, return_security_function_or_attack_surface_to_all_components: None
    ) -> None:
        """Групповая разметка, поверхность атаки.

        :param return_security_function_or_attack_surface_to_all_components: Фикстура для возвращения ФБ или ПА.
        """
        # Групповая разметка - Поверхность атаки
        first_checkbox = 1
        last_checkbox = 3

        with allure.step(
            "1. Предусловие: Пользователь с правами редактирования паспортов продуктов авторизован в сервисе, открыт "
            "паспорт версии продукта на вкладке  'Компонентный состав', ФБ и ПА не размечены."
        ):
            self.component_page.click_on_link_products()
            self.product_page.click_on_link(UITextElements.ALL_PRODUCTS).click_on_link(
                Products.VIPNET_CLIENT_4_X_FOR_WINDOWS
            )
            self.product_information_page.click_on_link(UITextElements.VERSIONS_TAB).click_on_link(
                Versions.VIPNET_CLIENT_4_X_FOR_WINDOWS
            )
            self.product_version_information_page.click_on_link(UITextElements.COMPONENT_COMPOSITION)

        with allure.step("2. Выбрать 2-3 компонента с помощью чекбоксов"):
            for i in range(first_checkbox, last_checkbox + 1):
                self.product_version_information_page.click_on_checkbox_in_table(i)

            (
                self.product_version_information_page.check_text(UITextElements.THREE_CHOSEN)
                .check_text(UITextElements.SECURITY_FUNCTION)
                .check_text(UITextElements.ATTACK_SURFACE)
                .check_text(UITextElements.TRANSFER_MARKUP)
                .check_checkbox_component_in_table()
            )
            self._check_checkboxes_in_table()

        with allure.step("3. Открыть выпадающий список 'Поверхность атаки'"):
            (
                self.product_version_information_page.click_on_element_with_text(UITextElements.ATTACK_SURFACE)
                .check_indication_in_list_security_function_or_attack_surface(Colors.GREEN, security_function=False)
                .check_indication_in_list_security_function_or_attack_surface(Colors.YELLOW, security_function=False)
                .check_indication_in_list_security_function_or_attack_surface(Colors.RED, security_function=False)
                .check_indication_in_list_security_function_or_attack_surface(Colors.GREY, security_function=False)
            )

        with allure.step("4. В списке выбрать произвольное значение поверхности атаки"):
            self.product_version_information_page.click_on_element_with_text(
                UITextElements.NOT_INCLUDED
            ).check_button_with_text(UITextElements.NO)

        with allure.step("5. Нажать кнопку 'Да'"):
            (
                self.product_version_information_page.click_on_button_with_text(UITextElements.YES)
                .check_visibility_indication(Colors.GREEN)
                .check_text(self._GROUP_MARKUP)
                .check_text(self._COMPONENTS_INFORMATION_UPDATED_SUCCESSFULLY)
                .check_text(RegularExpressions.PATTERN_STRING_TIME)
            )
            self._click_on_close_message_icon_and_check_table_headings()

        with allure.step("6. Повторить шаги кейса выставив одному компоненту поверхность атаки, используя чекбоксы"):
            (
                self.product_version_information_page.click_on_checkbox_in_table(first_checkbox)
                .click_on_element_with_text(UITextElements.ATTACK_SURFACE)
                .click_on_element_with_text(UITextElements.INDIRECTLY)
                .check_text(self._INFORMATION_MESSAGE_ATTACK_SURFACE)
                .click_on_button_with_text(UITextElements.YES)
            )

        with allure.step("7. Повторить шаги кейса выставив всем компонентам поверхность атаки"):
            (
                self.product_version_information_page.click_on_checkbox_in_table(self._CHECKBOX_ALL)
                .click_on_element_with_text(UITextElements.ATTACK_SURFACE)
                .click_on_element_with_text(UITextElements.ENTERS)
                .click_on_button_with_text(UITextElements.YES)
            )

            for i in range(first_checkbox - 1, last_checkbox):
                self.product_version_information_page.check_text(UITextElements.ENTERS, nth=i)

    def _setup(self) -> None:
        """Предусловие: версия продукта → вкладка 'Компонентный состав', ФБ и ПА не размечены."""
        self.component_page.click_on_link_products()
        self.product_page.click_on_link(UITextElements.ALL_PRODUCTS).click_on_link(Products.COORDINATOR_HW_5)
        self.product_information_page.click_on_link(UITextElements.VERSIONS_TAB).click_on_link(
            Versions.COORDINATOR_HW_5
        )
        (
            self.product_version_information_page.click_on_link(UITextElements.COMPONENT_COMPOSITION)
            .click_on_funnel_icon()
            .check_reset_filters_button()
            .check_combo_box_in_filter(UITextElements.SECURITY_FUNCTION)
            .click_on_combo_box_in_filter(UITextElements.SECURITY_FUNCTION)
            .click_on_element_in_combo_box_in_filter(UITextElements.NOT_SPECIFIED)
            .check_combo_box_in_filter(UITextElements.ATTACK_SURFACE)
            .click_on_combo_box_in_filter(UITextElements.ATTACK_SURFACE)
            .click_on_element_with_text(element_text=UITextElements.NOT_SPECIFIED, nth=2)
            .click_on_element_with_text(element_text=UITextElements.NOT_SPECIFIED, nth=4)
        )

    def _select_checkboxes_and_checks(self) -> None:
        """Выбрать чекбоксы и произвести проверки."""
        for i in range(self._FIRST_CHECKBOX, self._LAST_CHECKBOX + 1):
            self.product_version_information_page.click_on_checkbox_in_table(i)

        (
            self.product_version_information_page.check_text(UITextElements.THREE_CHOSEN)
            .check_text(UITextElements.SECURITY_FUNCTION)
            .check_text(UITextElements.ATTACK_SURFACE)
            .check_text(UITextElements.TRANSFER_MARKUP)
            .check_checkbox_component_in_table()
        )
        self._check_checkboxes_in_table()

    def _select_arbitrary_value_for_security_function_or_attack_surface(self, element_text: str) -> None:
        """Выбрать произвольное значение функции безопасности или поверхности атаки.

        :param element_text: Текст элемента.
        """
        (
            self.product_version_information_page.click_on_element_with_text(element_text)
            .click_on_element_with_text(UITextElements.INDIRECTLY)
            .check_text(
                self._INFORMATION_MESSAGE_SECURITY_FUNCTION
                if element_text == UITextElements.SECURITY_FUNCTION
                else self._INFORMATION_MESSAGE_ATTACK_SURFACE
            )
            .check_text(page_text=UITextElements.YES, nth=1)
        )

    def _click_on_close_message_icon_and_check_table_headings(self) -> None:
        """Закрыть сообщение в правом нижнем углу и проверить заголовки таблицы."""
        self.product_version_information_page.click_on_close_message_icon().check_table_headings(
            Lists.TITLES_TABLE_COMPONENT_COMPOSITION
        )

    def _disconnect_network_and_click_yes_button(self) -> None:
        """Отключить сеть и нажать кнопку 'Да'."""
        (
            self.product_version_information_page.disconnect_network()
            .click_on_button_with_text(UITextElements.YES)
            .check_visibility_indication(Colors.RED)
            .check_text(self._GROUP_MARKUP)
            .check_text(self._ERROR_MESSAGE)
            .check_text(RegularExpressions.PATTERN_STRING_TIME)
        )

    def _click_no_button(self, element_text: str) -> None:
        """Нажать кнопку 'Нет'.

        :param element_text: Текст элемента.
        """
        (
            self.product_version_information_page.click_on_button_with_text(UITextElements.NO)
            .check_text(
                page_text=self._INFORMATION_MESSAGE_ATTACK_SURFACE
                if element_text == UITextElements.ATTACK_SURFACE
                else self._INFORMATION_MESSAGE_SECURITY_FUNCTION,
                visible=False,
            )
            .check_text(page_text=UITextElements.YES, visible=False, nth=1)
            .check_text(page_text=UITextElements.INDIRECTLY, visible=False)
        )
