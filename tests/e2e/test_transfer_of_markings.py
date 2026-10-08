import allure
from allure_commons.types import LinkType

from src.constants.agreement_values import AgreementValues
from src.constants.colors import Colors
from src.constants.components import Components
from src.constants.lists import Lists
from src.constants.products import Products
from src.constants.radar_area_values import RadarAreaValues
from src.constants.regular_expressions import RegularExpressions
from src.constants.test_inputs import TestInputs
from src.constants.ui_text_elements import UITextElements
from src.constants.versions import Versions
from tests.base.base_test import BaseTest


@allure.parent_suite("Перенос разметки.")
@allure.epic("Перенос разметки.")
@allure.sub_suite("Перенос разметки.")
# TODO раскомментировать функционал связанный с проверкой прогресс-бара, когда починят баг и когда восстановят разметку
class TestTransferOfMarkings(BaseTest):
    """Перенос разметки."""

    # transfer_to_product = "Перенос в продукт "
    _VERSION_FIVE_NINE = "4.5.9"
    _VERSION_SIX_ZERO = "4.6.0"
    _RELOCATE = "Перенести"
    _EXPAND = "Раскрыть"
    _TRANSFERRING_MARKUP = "Перенос разметки"
    _MESSAGE = "Выберите версию продукта с которой необходимо перенести разметку."
    _TRANSFER_ERROR = "Ошибка переноса. Выбранные компоненты отсутствуют в исходной версии."

    @allure.suite("Паспорт продукта, ручной перенос разметки по статусу согласования.")
    @allure.title("Паспорт продукта, ручной перенос разметки по статусу согласования.")
    @allure.id("1585524")
    @allure.description("Баги: прогресс-бар и неверная разметка.")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1607284", LinkType.LINK, "TASK 1607284"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1585524", "TestCase 1585524")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_product_passport_manual_transfer_of_markings_according_to_approval_status(self) -> None:  # noqa: C901
        """Паспорт продукта, ручной перенос разметки по статусу согласования."""
        message = "Выберите продукт из которого необходимо перенести разметку."
        select_product = "Выберите продукт"
        amqp_cpp = "AMQP-CPP"
        markup_has_been_successfully_migrated = "Разметка успешно перенесена."
        transfer_error = "Ошибка переноса. Выбранные компоненты отсутствуют в исходном продукте."
        markup_has_been_partially_moved = (
            "Разметка частично перенесена. Некоторые компоненты отсутствуют в исходном продукте."
        )
        titles = [
            " ",
            UITextElements.COMPONENT,
            UITextElements.TECHNICAL_RADAR_AREA,
            UITextElements.AGREEMENT,
            "Обоснование/Комментарий",
        ]

        with allure.step(
            "1. Пользователь с правами на редактирование паспортов компонентов и продуктов авторизован в сервисе. "
            "Открыт паспорт продукта назначения 'Coordinator HW 5', вкладка 'Компонентный состав' (паспорт продукта в "
            "который переносим разметку). В продукте назначения разметка отсутствует. В используемых компонентах "
            "исходного продукта 'Coordinator HW 4' есть компоненты со следующими свойствами - см. 'Summary'. Есть "
            "различия в компонентном составе у исходного продукта и продукта назначения"
        ):
            components = [
                Components.UTIL_LINUX,
                Components.BZIP2,
                Components.CRYPTO_UNDERGROUND_V2,
                Components.ZLIB1G,
                Components.CRYPT_CPU_FEATURES,
                Components.ACCORDSDK,
                Components.ACETAO,
                Components.ACPID,
            ]

            self.component_page.click_on_link_products()
            self.product_page.click_on_link(UITextElements.ALL_PRODUCTS).click_on_link(Products.COORDINATOR_HW_5)
            self.product_information_page.click_on_link(UITextElements.COMPONENT_COMPOSITION)

            for component in components:
                self._clearing_markup(component)

            (
                self.product_information_page.fill_in_search_input(Components.ATOP)
                .click_on_element_with_text(UITextElements.EDIT)
                .check_checkbox_agreement_and_click()
                .fill_in_textarea_justification_comment(UITextElements.TEXT_JUSTIFICATION)
                .click_on_icon_floppy_disk()
                .click_on_element_with_text(UITextElements.YES)
                .check_text(page_text=UITextElements.QUESTION, visible=False)
                .click_on_close_message_icon()
            )

            self.component_page.click_on_link_products()
            self._click_on_links()

            components = [
                Components.LIBC6,
                Components.CRYPT_CPU_FEATURES,
                Components.ACPID,
            ]

            for component in components:
                (
                    self.product_information_page.fill_in_search_input(component)
                    .click_on_element_with_text(UITextElements.EDIT)
                    .check_checkbox_agreement_and_click()
                    .fill_in_textarea_justification_comment(UITextElements.TEXT_JUSTIFICATION)
                    .click_on_icon_floppy_disk()
                    .click_on_element_with_text(UITextElements.YES)
                    .check_text(page_text=UITextElements.QUESTION, visible=False)
                    .click_on_close_message_icon()
                )

            components = [
                Components.UTIL_LINUX,
                Components.ZLIB1G,
                Components.ACETAO,
            ]

            for component in components:
                (
                    self.product_information_page.fill_in_search_input(component)
                    .click_on_element_with_text(UITextElements.EDIT)
                    .check_checkbox_agreement_and_click(marked=False)
                    .fill_in_textarea_justification_comment(UITextElements.TEXT_JUSTIFICATION)
                    .click_on_icon_floppy_disk()
                    .click_on_element_with_text(UITextElements.YES)
                    .check_text(page_text=UITextElements.QUESTION, visible=False)
                    .click_on_close_message_icon()
                )

            components = [
                Components.BZIP2,
                Components.CRYPTO_UNDERGROUND_V2,
                Components.ACCORDSDK,
                Components.ATOP,
            ]

            for component in components:
                self._clearing_markup(component)

            self.component_page.click_on_link_products()
            self.product_page.click_on_link(UITextElements.ALL_PRODUCTS).click_on_link(Products.COORDINATOR_HW_5)
            self.product_information_page.click_on_link(UITextElements.COMPONENT_COMPOSITION)

        with allure.step(
            "2. В компонентном составе продукта назначения 'Coordinator HW 5' выбрать все компоненты из 'Summary'"
        ):
            components = [
                Components.BASH,
                Components.LIBC6,
                Components.UTIL_LINUX,
                Components.BZIP2,
                Components.CRYPTO_UNDERGROUND_V2,
                Components.ZLIB1G,
                Components.CRYPT_CPU_FEATURES,
                Components.ACCORDSDK,
                Components.ACETAO,
                Components.ACPID,
            ]
            selected = f"выбрано: {len(components)}"

            for component in components:
                self.product_information_page.click_on_checkbox_by_text_in_table(component)

            (
                self.product_information_page.check_checkbox_component_in_table()
                .check_text(page_text=UITextElements.EDIT, visible=False)
                .check_text(selected)
            )

        with allure.step("3. Нажать 'Перенести разметку'"):
            (
                self.product_information_page.click_on_element_with_text(UITextElements.TRANSFER_MARKUP)
                .check_text(message)
                .check_button_with_text(UITextElements.CANCEL)
            )

        with allure.step("4. В поле Продукт выбрать исходный продукт 'Coordinator HW 4'"):
            (
                self.product_information_page.click_on_element_with_placeholder(select_product)
                .click_on_element_with_text(Products.COORDINATOR_HW_4)
                .check_text(Products.COORDINATOR_HW_4)
            )

        with allure.step("5. Нажать 'Перенести'"):
            self.product_information_page.click_on_button_with_text(self._RELOCATE).check_text(
                page_text=message, visible=False
            )
            # self._check_of_transfer_to_product()
            (
                self.product_information_page.check_visibility_indication(Colors.GREEN)
                .check_text(self._TRANSFERRING_MARKUP)
                .check_text(markup_has_been_successfully_migrated)
                .check_text(RegularExpressions.PATTERN_STRING_TIME)
                .check_visibility_close_message_icon()
                .check_text(page_text=markup_has_been_successfully_migrated, visible=False, timeout=6_000)
                .check_text(page_text=selected, visible=False)
                .check_text(page_text=UITextElements.TRANSFER_MARKUP, visible=False)
                .check_text(UITextElements.EDIT)
                .check_checkbox_component_in_table(marked=False)
            )

        with allure.step("6. Проверить корректность переноса разметки по статусу согласования"):
            self.product_information_page.check_table_headings(titles)

            list_values = [
                Lists.VALUES_BASH,
                [
                    " ",
                    Components.UTIL_LINUX,
                    RadarAreaValues.PILOTED_BY,
                    AgreementValues.DEVIATION_IS_NOT_AGREED_UPON,
                    UITextElements.TEXT_JUSTIFICATION,
                ],
                [
                    " ",
                    Components.BZIP2,
                    RadarAreaValues.INTERESTED_IN,
                    AgreementValues.DEVIATION_IS_NOT_AGREED_UPON,
                    "",
                ],
                Lists.VALUES_CRYPTO_UNDERGROUND_V2,
                [
                    " ",
                    Components.ZLIB1G,
                    RadarAreaValues.AVOID,
                    AgreementValues.DEVIATION_IS_NOT_AGREED_UPON,
                    UITextElements.TEXT_JUSTIFICATION,
                ],
                Lists.VALUES_CRYPT_CPU_FEATURES,
                Lists.VALUES_ACCORDSDK,
                [
                    " ",
                    Components.ACETAO,
                    RadarAreaValues.UNKNOWN,
                    AgreementValues.CHOICE_IS_NOT_AGREED_UPON,
                    UITextElements.TEXT_JUSTIFICATION,
                ],
                Lists.VALUES_ACPID,
            ]

            second_element_of_list = 1
            for values in list_values:
                self.product_information_page.fill_in_search_input(
                    values[second_element_of_list]
                ).check_table_text_values(values)

            values_libc6 = [
                " ",
                Components.LIBC6,
                RadarAreaValues.PILOTED_BY,
                AgreementValues.DEVIATION_IS_AGREED,
                UITextElements.TEXT_JUSTIFICATION,
            ]
            self.product_information_page.fill_in_search_input(Components.LIBC6).check_table_text_values(
                values=values_libc6, first_string=False
            )

            self.product_information_page.click_on_link_products()
            self._click_on_links()

            for values in list_values:
                self.product_information_page.fill_in_search_input(values[1]).check_table_text_values(values)

            self.product_information_page.fill_in_search_input(Components.LIBC6).check_table_text_values(
                values_libc6, False
            )

            self.product_information_page.click_on_link_products()
            self.product_page.click_on_link(UITextElements.ALL_PRODUCTS).click_on_link(Products.COORDINATOR_HW_5)
            self.product_information_page.click_on_link(UITextElements.COMPONENT_COMPOSITION)

        with allure.step(
            "7. В компонентном составе продукта назначения 'Coordinator HW 5' выбрать компонент 'AMQP-CPP'"
        ):
            selected = "выбран: 1"

            self.product_information_page.click_on_checkbox_by_text_in_table(amqp_cpp).check_text(selected)

        with allure.step("8. Повторить шаги 3, 4, 5 для переноса разметки компонента 'AMQP-CPP'"):
            (
                self.product_information_page.click_on_element_with_text(UITextElements.TRANSFER_MARKUP)
                .click_on_element_with_placeholder(select_product)
                .click_on_element_with_text(Products.COORDINATOR_HW_4)
                .click_on_button_with_text(self._RELOCATE)
            )
            # self._check_of_transfer_to_product()
            (
                self.product_information_page.check_visibility_indication(Colors.RED)
                .check_text(self._TRANSFERRING_MARKUP)
                .check_text(transfer_error)
                .check_text(RegularExpressions.PATTERN_STRING_TIME)
                .check_visibility_close_message_icon()
                .check_text(page_text=transfer_error, visible=False, timeout=6_000)
                .check_text(page_text=selected, visible=False)
                .check_text(page_text=UITextElements.TRANSFER_MARKUP, visible=False)
                .check_text(UITextElements.EDIT)
                .check_checkbox_component_in_table(marked=False)
            )

        with allure.step(
            "9. Проверить корректность переноса разметки по статусу согласования для компонента 'AMQP-CPP'"
        ):
            self.product_information_page.click_on_link_products()
            self._click_on_links()
            (
                self.product_information_page.fill_in_search_input(amqp_cpp)
                .check_text(UITextElements.NOTHING_FOUND)
                .click_on_link_products()
            )
            self.product_page.click_on_link(UITextElements.ALL_PRODUCTS).click_on_link(Products.COORDINATOR_HW_5)
            self.product_information_page.click_on_link(UITextElements.COMPONENT_COMPOSITION)

        with allure.step(
            "10. В компонентном составе продукта назначения 'Coordinator HW 5' выбрать компонент 'AMQP-CPP' и "
            "компонент 'atop' (компонент не размечен в исходной версии, но размечен в версии назначения) "
        ):
            self.product_information_page.click_on_checkbox_by_text_in_table(
                amqp_cpp
            ).click_on_checkbox_by_text_in_table(Components.ATOP)

        with allure.step("11. Повторить шаги 3, 4, 5 для переноса разметки компонентов 'AMQP-CPP' и 'atop'"):
            (
                self.product_information_page.click_on_element_with_text(UITextElements.TRANSFER_MARKUP)
                .click_on_element_with_placeholder(select_product)
                .click_on_element_with_text(Products.COORDINATOR_HW_4)
                .click_on_button_with_text(self._RELOCATE)
            )
            # self._check_of_transfer_to_product()
            (
                self.product_information_page.check_visibility_indication(Colors.YELLOW)
                .check_text(self._TRANSFERRING_MARKUP)
                .check_text(markup_has_been_partially_moved)
                .check_text(RegularExpressions.PATTERN_STRING_TIME)
                .check_visibility_close_message_icon()
                .check_text(page_text=markup_has_been_partially_moved, visible=False, timeout=6_000)
                .check_text(page_text=selected, visible=False)
                .check_text(page_text=UITextElements.TRANSFER_MARKUP, visible=False)
                .check_text(UITextElements.EDIT)
                .check_checkbox_component_in_table(marked=False)
            )

        with allure.step(
            "12. Проверить корректность переноса разметки по статусу согласования  для компонентов 'AMQP-CPP' и 'atop'"
        ):
            values = [
                " ",
                Components.ATOP,
                RadarAreaValues.UNKNOWN,
                AgreementValues.CHOICE_IS_NOT_AGREED_UPON,
                "",
            ]

            (
                self.product_information_page.fill_in_search_input(Components.ATOP)
                .check_table_text_values(values)
                .click_on_link_products()
            )
            self._click_on_links()
            (
                self.product_information_page.fill_in_search_input(amqp_cpp)
                .check_text(UITextElements.NOTHING_FOUND)
                .fill_in_search_input(Components.ATOP)
                .check_table_text_values(values)
            )

    @allure.suite("Ручной перенос ПА и ФБ, окно 'Перенос разметки', Отмена.")
    @allure.title("Ручной перенос ПА и ФБ, окно 'Перенос разметки', Отмена.")
    @allure.id("1545358")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1618077", LinkType.LINK, "TASK 1618077"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1545358", "TestCase 1545358")
    @allure.severity(allure.severity_level.MINOR)
    def test_transfer_of_markings_cancel(self) -> None:
        """Ручной перенос ПА и ФБ, окно 'Перенос разметки', Отмена."""
        # Ручной перенос ПА и ФБ_Окно Перенос разметки_Отмена
        with allure.step(
            "1. Пользователь с правами на редактирование паспортов компонентов и продуктов авторизован в сервисе. "
            "Открыт паспорт версии продукта, вкладка 'Компонентный состав'"
        ):
            self._setup_version_of_product_component_composition()

        with allure.step("2. В списке компонентов выбрать не менее одного компонента"):
            for i in range(1, 4):
                self.product_version_information_page.click_on_checkbox_in_table(i)

            self.product_information_page.check_checkbox_component_in_table().check_text(UITextElements.THREE_CHOSEN)
            self._check_checkboxes_in_table()

        with allure.step("3. Нажать 'Перенести разметку'"):
            self._click_transfer_markup()

        with allure.step("4. Заполнить обязательные поля валидными значениями"):
            (
                self.product_version_information_page.click_on_combo_box_version_transfer_of_markings()
                .click_on_element_with_text(Versions.FIVE_FIVE_ZERO)
                .check_text(Versions.FIVE_FIVE_ZERO)
            )

        with allure.step("5. Нажать 'Отмена'"):
            self.product_version_information_page.click_on_button_with_text(UITextElements.CANCEL).check_text(
                page_text=self._MESSAGE, visible=False
            )
            self._check_checkboxes_in_table()

        with allure.step("6. Повторно нажать 'Перенести разметку'"):
            (
                self.product_version_information_page.click_on_element_with_text(UITextElements.TRANSFER_MARKUP)
                .check_text(self._MESSAGE)
                .check_text(Products.COORDINATOR_HW_5)
                .check_text(page_text=Versions.FIVE_FIVE_ZERO, visible=False)
                .click_on_combo_box_version_transfer_of_markings()
            )

    @allure.suite("Ручной перенос ПА и ФБ в рамках версии одного продукта, ошибка переноса.")
    @allure.title("Ручной перенос ПА и ФБ в рамках версии одного продукта, ошибка переноса.")
    @allure.id("1545341")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1618940", LinkType.LINK, "TASK 1618940"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1545341", "TestCase 1545341")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_transfer_of_markings_within_version_of_one_product_transfer_error(self) -> None:
        """Ручной перенос ПА и ФБ в рамках версии одного продукта, ошибка переноса."""
        # Ручной перенос ПА и БФ в рамках версии одного продукта_ошибка переноса
        with allure.step(
            "1. Пользователь с правами на редактирование паспортов компонентов и продуктов авторизован в сервисе. "
            "Открыт паспорт версии продукта, вкладка 'Компонентный состав' (паспорт версии в которую переносим "
            "разметку). В исходной версии отсутствуют компоненты, которые есть в версии назначения"
        ):
            self._setup_version_of_product_component_composition()

        with allure.step(
            "2. В списке компонентов версии назначения выбрать компоненты, которые ОТСУТСТВУЮТ в исходной версии"
        ):
            for i in range(1, 4):
                self.product_version_information_page.click_on_checkbox_in_table(i)

            self.product_information_page.check_checkbox_component_in_table().check_text(UITextElements.THREE_CHOSEN)
            self._check_checkboxes_in_table()

        with allure.step("3. Нажать 'Перенести разметку'"):
            (
                self.product_version_information_page.click_on_element_with_text(UITextElements.TRANSFER_MARKUP)
                .check_text(self._MESSAGE)
                .check_button_with_text(self._RELOCATE)
                .check_button_with_text(UITextElements.CANCEL)
            )

        with allure.step(
            "4. Поле 'Продукт' оставить без изменений (перенос осуществляется в рамках разных версий одного продукта)"
        ):
            self.product_version_information_page.check_text(Products.COORDINATOR_HW_5)

        with allure.step("5. В поле 'Версия' указать номер версии продукта из которой будет перенесена разметка"):
            (
                self.product_version_information_page.click_on_combo_box_version_transfer_of_markings()
                .click_on_element_with_text(Versions.ONE_ONE)
                .check_text(Versions.ONE_ONE)
            )

        with allure.step("6. Нажать 'Перенести'"):
            self.product_version_information_page.click_on_button_with_text(self._RELOCATE).check_text(
                page_text=self._MESSAGE, visible=False
            )
            # self._check_of_transfer_to_version()
            (
                self.product_version_information_page.check_visibility_indication(Colors.RED)
                .check_text(self._TRANSFERRING_MARKUP)
                .check_text(self._TRANSFER_ERROR)
                .check_text(RegularExpressions.PATTERN_STRING_TIME)
                .check_visibility_close_message_icon()
                .check_text(page_text=self._TRANSFER_ERROR, visible=False, timeout=6_000)
                .check_text(page_text=UITextElements.THREE_CHOSEN, visible=False)
                .check_text(page_text=UITextElements.TRANSFER_MARKUP, visible=False)
                .check_text(UITextElements.EDIT)
                .check_checkbox_component_in_table(marked=False)
            )

    @allure.suite("Перенос разметки, поля 'Продукт' и 'Версия', валидация.")
    @allure.title("Перенос разметки, поля 'Продукт' и 'Версия', валидация.")
    @allure.id("1561972")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1619600", LinkType.LINK, "TASK 1619600"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1561972", "TestCase 1561972")
    @allure.severity(allure.severity_level.MINOR)
    def test_transfer_of_markings_fields_product_and_version_validation(self) -> None:
        """Перенос разметки, поля 'Продукт' и 'Версия', валидация."""
        # Паспорт версии продукта, вкладка Компонентный состав_Окно Перенос разметки_ поле Продукт/Версия_ валидация
        with allure.step(
            "1. Пользователь с правами на редактирование  паспортов компонентов и  продуктов авторизован в "
            "сервисе. Открыт паспорт версии продукта, вкладка 'Компонентный состав', выбраны компоненты для "
            "переноса разметки"
        ):
            self._setup_version_of_product_component_composition()

            for i in range(1, 4):
                self.product_version_information_page.click_on_checkbox_in_table(i)

            self.product_information_page.check_checkbox_component_in_table().check_text(UITextElements.THREE_CHOSEN)
            self._check_checkboxes_in_table()

        with allure.step("2. Нажать 'Перенести разметку'"):
            self._click_transfer_markup()

        with allure.step("3. Нажать 'Перенести'"):
            (
                self.product_version_information_page.click_on_button_with_text(self._RELOCATE)
                .check_text("Выберите версию продукта")
                .check_visibility_red_backlight_field_version()
                .check_visibility_red_font_error()
            )

    @allure.suite("Перенос разметки, поле 'Продукт'.")
    @allure.title("Перенос разметки, поле 'Продукт'.")
    @allure.id("1545374")
    @allure.description("Баг: 'Ничего НА найдено'")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1620259", LinkType.LINK, "TASK 1620259"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1545374", "TestCase 1545374")
    @allure.severity(allure.severity_level.NORMAL)
    def test_transfer_of_markings_field_product(self) -> None:
        """Перенос разметки, поле 'Продукт'."""
        # Паспорт версии продукта, вкладка Компонентный состав_Окно Перенос разметки_ поле Продукт
        # TODO проверить тест-кейс (его должны актуализировать), возможно нужно будет изменить автотест после этого
        with allure.step(
            "1. Пользователь с правами на редактирование ВСЕХ паспортов компонентов и ВСЕХ продуктов авторизован в "
            "сервисе. Открыт паспорт версии продукта, вкладка 'Компонентный состав', выбраны компоненты для переноса "
            "разметки, открыто окно 'Перенос разметки'"
        ):
            self._setup_version_of_product_component_composition()

            for i in range(1, 4):
                self.product_version_information_page.click_on_checkbox_in_table(i)

            self.product_information_page.check_checkbox_component_in_table().check_text(UITextElements.THREE_CHOSEN)
            self._check_checkboxes_in_table()
            self._click_transfer_markup()

        with allure.step("2. Установить курсор в поле 'Продукт'"):
            self.product_version_information_page.click_on_element_with_title(self._EXPAND).check_vertical_scrolling()

        with allure.step("3. Ввести название несуществующего продукта"):
            (
                self.product_version_information_page.fill_in_product_field_in_markup_transfer_window(
                    TestInputs.SPECIAL_CHARACTERS
                )
                .check_text(UITextElements.NOTHING_FOUND)
                .click_on_button_with_text(UITextElements.CANCEL)
            )

        with allure.step("4. Ввести часть названия продукта в нижнем/верхнем/смешанном регистре"):
            list_products = [Products.COORDINATOR_HW_4, Products.COORDINATOR_HW_5]

            (
                self.product_version_information_page.click_on_element_with_text(UITextElements.TRANSFER_MARKUP)
                .click_on_element_with_title(self._EXPAND)
                # Вводим название продукта в верхнем регистре и без последнего символа
                .fill_in_product_field_in_markup_transfer_window(Products.COORDINATOR_HW_5.upper()[:-1])
                .check_elements_in_field_in_markup_transfer_window(list_products)
                .click_on_button_with_text(UITextElements.CANCEL)
            )

        with allure.step("5. Ввести название продукта, поставить пробел до/после названия"):
            (
                self.product_version_information_page.click_on_element_with_text(
                    UITextElements.TRANSFER_MARKUP
                ).click_on_element_with_title(self._EXPAND)
                # Вводим название с пробелами до и после названия
                .fill_in_product_field_in_markup_transfer_window(f" {Products.COORDINATOR_HW_4} ")
            )

        with allure.step("6. Выбрать искомый продукт"):
            self.product_version_information_page.click_on_element_with_text(Products.COORDINATOR_HW_4).check_text(
                Products.COORDINATOR_HW_4
            )

    @allure.suite("Перенос разметки, поле 'Версия'.")
    @allure.title("Перенос разметки, поле 'Версия'.")
    @allure.id("1545375")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1620758", LinkType.LINK, "TASK 1620758"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1545375", "TestCase 1545375")
    @allure.severity(allure.severity_level.NORMAL)
    def test_transfer_of_markings_field_version(self) -> None:
        """Перенос разметки, поле 'Версия'."""
        # Паспорт версии продукта, вкладка Компонентный составОкно Перенос разметки_ поле Версия

        version_four_eight = "4.4.8"

        with allure.step(
            "1. Пользователь с правами на редактирование паспортов компонентов и продуктов авторизован в "
            "сервисе. Открыт паспорт версии продукта, вкладка 'Компонентный состав', выбраны компоненты для "
            "переноса разметки"
        ):
            self._setup_version_of_product_component_composition()

            for i in range(1, 4):
                self.product_version_information_page.click_on_checkbox_in_table(i)

            self.product_information_page.check_checkbox_component_in_table().check_text(UITextElements.THREE_CHOSEN)
            self._check_checkboxes_in_table()

        with allure.step("2. Нажать 'Перенести разметку'"):
            self._click_transfer_markup()

        with allure.step("3. Нажать на экспандер в поле 'Версия'"):
            list_versions = [self._VERSION_SIX_ZERO, self._VERSION_FIVE_NINE, "4.5.8"]

            (
                self.product_version_information_page.click_on_element_with_title(self._EXPAND)
                .click_on_element_with_text(Products.COORDINATOR_HW_4)
                .click_on_combo_box_version_transfer_of_markings()
                .check_elements_in_field_in_markup_transfer_window(list_versions)
            )

        with allure.step("4. В поле 'Продукт' выбрать любой другой продукт"):
            (
                self.product_version_information_page.click_on_element_with_title(self._EXPAND)
                .click_on_element_with_text(Products.CSP_WINDOWS_4)
                .check_text(Products.CSP_WINDOWS_4)
            )

        with allure.step("5. Нажать на экспандер в поле 'Версия'"):
            list_versions = ["4.4.10", version_four_eight, "4.4.4"]

            self.product_version_information_page.click_on_combo_box_version_transfer_of_markings()
            self.product_version_information_page.check_elements_in_field_in_markup_transfer_window(list_versions)

        with allure.step("6. Выбрать любую версию"):
            self.product_version_information_page.click_on_element_with_text(version_four_eight).check_text(
                version_four_eight
            )

    @allure.suite("Ручной перенос разметки ПА и ФБ в рамках разных продуктов.")
    @allure.title("Ручной перенос разметки ПА и ФБ в рамках разных продуктов.")
    @allure.id("1561935")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1621962", LinkType.LINK, "TASK 1621962"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1561935", "TestCase 1561935")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_transfer_of_markings_within_different_products(self) -> None:
        """Ручной перенос разметки ПА и ФБ в рамках разных продуктов."""
        # Ручной перенос разметки ПА и ФБ в рамках разных продуктов
        # TODO проверить тест-кейс (его должны актуализировать), возможно нужно будет изменить автотест после этого
        checkbox_first = 0
        chosen = "выбрано: 309"
        markup_has_been_partially_moved = (
            "Разметка частично перенесена. Некоторые компоненты отсутствуют в исходной версии."
        )

        with allure.step(
            "1. Предусловие: Пользователь с правами на редактирование паспортов компонентов и продуктов авторизован "
            "в сервисе. Открыт паспорт версии продукта, вкладка 'Компонентный состав' (паспорт версии в которую "
            "переносим разметку). В исходной версии продукта есть только часть компонентов от версии назначения."
        ):
            self._setup_version_of_product_component_composition()

        with allure.step("2. Выбрать ВСЕ используемые компоненты в версии назначения"):
            (
                self.product_version_information_page.click_on_checkbox_in_table(nth=checkbox_first)
                .check_text(chosen)
                .check_check_mark_in_checkbox_component_in_table()
            )
            self._check_checkboxes_in_table()

        with allure.step("3. Нажать 'Перенести разметку'"):
            self._click_transfer_markup()

        with allure.step("4. В поле 'Продукт' указать название продукта отличного от текущего"):
            (
                self.product_version_information_page.click_on_element_with_title(self._EXPAND)
                .click_on_element_with_text(Products.COORDINATOR_HW_4)
                .check_text(Products.COORDINATOR_HW_4)
            )

        with allure.step("5. В поле 'Версия' указать версию из которой будем переносить разметку"):
            (
                self.product_version_information_page.click_on_combo_box_version_transfer_of_markings()
                .click_on_element_with_text(self._VERSION_FIVE_NINE)
                .check_text(self._VERSION_FIVE_NINE)
            )

        with allure.step("6. Нажать 'Перенести'"):
            (
                self.product_version_information_page.click_on_button_with_text(self._RELOCATE)
                .check_visibility_indication(Colors.YELLOW)
                .check_text(self._TRANSFERRING_MARKUP)
                .check_text(markup_has_been_partially_moved)
                .check_text(RegularExpressions.PATTERN_STRING_TIME)
                .check_visibility_close_message_icon()
                .check_text(page_text=markup_has_been_partially_moved, visible=False, timeout=6_000)
                .check_text(page_text=chosen, visible=False)
                .check_text(page_text=UITextElements.TRANSFER_MARKUP, visible=False)
                .check_text(UITextElements.EDIT)
                .check_checkbox_component_in_table(marked=False)
                .check_check_mark_in_checkbox_component_in_table(marked=False)
            )

        with allure.step(
            "7. Повторить шаги тест-кейса для переноса разметки между версиями разных продуктов для получения тостов "
            "'Разметка успешно перенесена.' и 'Ошибка переноса. Выбранные компоненты отсутствуют в исходной версии.'"
        ):
            # Ошибка переноса. Выбранные компоненты отсутствуют в исходной версии.
            self.product_version_information_page.click_on_link_products()
            self.product_page.click_on_link(UITextElements.ALL_PRODUCTS).click_on_link(Products.COORDINATOR_HW_5)
            self.product_information_page.click_on_link(UITextElements.VERSIONS_TAB).click_on_link(
                Versions.COORDINATOR_HW_5
            )
            (
                self.product_version_information_page.click_on_link(UITextElements.COMPONENT_COMPOSITION)
                .click_on_checkbox_in_table(nth=checkbox_first)
                .click_on_element_with_text(UITextElements.TRANSFER_MARKUP)
                .click_on_element_with_title(self._EXPAND)
                .click_on_element_with_text(Products.COORDINATOR_HW_4)
                .click_on_combo_box_version_transfer_of_markings()
                .click_on_element_with_text(self._VERSION_SIX_ZERO)
                .click_on_button_with_text(self._RELOCATE)
                .check_text(self._TRANSFER_ERROR)
            )

    def _click_transfer_markup(self) -> None:
        """Нажать 'Перенести разметку'."""
        (
            self.product_version_information_page.click_on_element_with_text(UITextElements.TRANSFER_MARKUP)
            .check_text(self._MESSAGE)
            .check_text(Products.COORDINATOR_HW_5)
            .check_button_with_text(self._RELOCATE)
            .check_button_with_text(UITextElements.CANCEL)
        )

    def _click_on_links(self) -> None:
        """Кликнуть по ссылкам: 'Все продукты', 'Coordinator HW 4' и 'Компонентный состав'."""
        self.product_page.click_on_link(UITextElements.ALL_PRODUCTS).click_on_link(Products.COORDINATOR_HW_4)
        self.product_information_page.click_on_link(UITextElements.COMPONENT_COMPOSITION)

    def _clearing_markup(self, component_name: str) -> None:
        """Очистка разметки компонента.

        :param component_name: Название компонента.
        """
        (
            self.product_information_page.fill_in_search_input(component_name)
            .click_on_element_with_text(UITextElements.EDIT)
            .check_checkbox_agreement_and_click(marked=False)
            .fill_in_textarea_justification_comment("")
            .click_on_icon_floppy_disk()
            .click_on_element_with_text(UITextElements.YES)
            .check_text(page_text=UITextElements.QUESTION, visible=False)
            .click_on_close_message_icon()
        )

    # def _check_of_transfer_to_version(self) -> None:
    #     """Проверка прогресс-бара 'Перенос в версию 5.4.0'."""
    #     transfer_to_version = "Перенос в версию "
    #
    #     (
    #         self.product_information_page.check_text(transfer_to_version + Versions.COORDINATOR_HW_5)
    #         .check_text(RegularExpressions.PATTERN_STRING_TIME)
    #         .check_visibility_close_message_icon()
    #         .check_text(
    #         page_text=transfer_to_version + Versions.COORDINATOR_HW_5, visible=False, timeout=6_000
    #         )
    #     )

    #
    # def _check_of_transfer_to_product(self) -> None:
    #     """Проверка прогресс-бара 'Перенос в продукт Coordinator HW 5'."""
    #     (
    #         self.product_information_page.check_text(self.transfer_to_product + Products.COORDINATOR_HW_5)
    #         .check_text(RegularExpressions.PATTERN_STRING_TIME)
    #         .check_visibility_close_message_icon()
    #     )
