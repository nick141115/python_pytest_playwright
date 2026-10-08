import allure
import pytest
from allure_commons.types import LinkType

from src.constants.components import Components
from src.constants.packages import Packages
from src.constants.regular_expressions import RegularExpressions
from src.constants.test_inputs import TestInputs
from src.constants.ui_text_elements import UITextElements
from src.constants.versions import Versions
from tests.base.base_test import BaseTest


@allure.parent_suite("Пакет компонента.")
@allure.epic("Пакет компонента.")
@allure.sub_suite("Пакет компонента.")
class TestComponentPackage(BaseTest):
    """Пакет компонента."""

    _TEXT_IN_DEVELOPMENT = " В разработке "
    _TEXT_ASSEMBLY_BY_CONFIGURATION = "Сборка по конфигурации"
    _TEXT_PACKAGE_ACCORDSDK = "Пакет 1.0.0.14"
    _RUBY = "Ruby"
    _C_SHARP = "C#"
    _YA_RU = "http://ya.ru/"
    _LINK_REMOVED = "Ссылка удалена."
    _SOURCE_CODE_IS_EXTERNAL = "Исходный код внешний"
    _SOURCE_CODE_IS_INTERNAL = "Исходный код внутренний"
    _LINK_SAVED = "Ссылка сохранена."
    _RETURN_LINK_FROM_SOURCE = "Вернуть ссылку из источника"
    _LINK_CHANGED = "Ссылка изменена."
    _COPY = "Копировать"
    _TEAM_CITY = "TeamCity"
    _SOURCE_CODE_IS_EXTERNAL_LINK_NOT_PROVIDED = "Исходный код внешний (ссылка не указана)"
    _SOURCE_CODE_INTERNAL_ARTIFACTORY_LINK_SOURCE = "Исходный код внутренний (источник ссылки Artifactory)"
    _SIX_POINT_TWO = "6.2"
    _PACKAGE_NUMBER_ACETAO = "6.2.7.15"

    @pytest.fixture
    def remove_links(self) -> None:
        """Фикстура удаления ссылок."""
        yield

        with allure.step("Возвращаем стенд к первоначальному состоянию"):
            self._impersonate_as_user_with_read_or_write_permissions(write_permissions=True)
            (
                self.component_page.click_on_title()
                .click_on_link(UITextElements.ALL_COMPONENTS_TAB)
                .click_on_link(Components.ACETAO)
            )
            self.component_information_page.click_on_link(UITextElements.VERSIONS_TAB).click_on_link(
                self._SIX_POINT_TWO
            )
            self.product_version_information_page.click_on_link(UITextElements.PACKAGES_TAB).click_on_link(
                self._PACKAGE_NUMBER_ACETAO
            )

            for _ in range(2):
                with allure.step("Нажать на меню ссылки"):
                    self.component_package_information_page.click_on_icon_menu()

                with allure.step("Нажать 'Удалить'"):
                    self.component_package_information_page.click_on_element_with_text("Удалить")

                with allure.step("Нажать 'Да'"):
                    (
                        self.component_package_information_page.click_on_element_with_text(UITextElements.YES)
                        .check_text(self._LINK_REMOVED)
                        .refresh_page()
                    )

    @pytest.fixture
    def return_link_from_source_fixture(self) -> None:
        """Фикстура для возвращения ссылки из источника."""
        yield

        with allure.step("Возвращаем стенд к первоначальному состоянию"):
            with allure.step("Нажать на меню ссылки"):
                self._impersonate_as_user_with_read_or_write_permissions(write_permissions=True)
                (
                    self.component_page.click_on_title()
                    .click_on_link(UITextElements.ALL_COMPONENTS_TAB)
                    .click_on_link(Components.ACCORDSDK)
                )
                self.component_information_page.click_on_link(UITextElements.VERSIONS_TAB).click_on_link(
                    Versions.ACCORDSDK
                )
                self.product_version_information_page.click_on_link(UITextElements.PACKAGES_TAB).click_on_link(
                    Packages.ACCORDSDK
                )
                self.component_package_information_page.click_on_icon_menu()

            with allure.step("Нажать 'Вернуть ссылку из источника'"):
                self.component_package_information_page.click_on_element_with_text(self._RETURN_LINK_FROM_SOURCE)

            with allure.step("Нажать 'Да'"):
                self.component_package_information_page.click_on_element_with_text(UITextElements.YES).check_text(
                    self._LINK_CHANGED
                )

    @pytest.fixture
    def delete_programming_languages(self, request: pytest.FixtureRequest) -> None:
        """Фикстура удаления языков программирования.

        :param request: Значения передаваемые в фикстуру.
        """
        yield
        programming_languages = request.param

        with allure.step("Возвращаем стенд к первоначальному состоянию"):
            self._impersonate_as_user_with_read_or_write_permissions(write_permissions=True)
            self._setup()

            for programming_language in programming_languages:
                self.component_package_information_page.delete_programming_language(programming_language)

    @allure.suite("Пакет компонента, посмотреть сведения.")
    @allure.title("Пакет компонента, посмотреть сведения.")
    @allure.id("1513331")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1540462", LinkType.LINK, "TASK 1540462"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1513331", "TestCase 1513331")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_component_package_view_information(self) -> None:
        """Пакет компонента, посмотреть сведения."""
        # Пакет компонента_посмотреть сведения
        with allure.step(
            "1. Предусловие: Пользователь авторизован в сервисе, открыта страница 'Компоненты', выбран один из "
            "компонентов списка, выбрана версия компонента, выбран пакет."
        ):
            self._impersonate_as_user_with_read_or_write_permissions(write_permissions=False)
            self._setup()

        with allure.step("2. Проверить отображение информации по выбранному пакету компонента"):
            with allure.step("Вкладка 'Общая информация'"):
                (
                    self.component_package_information_page.check_active_tab(UITextElements.GENERAL_INFORMATION)
                    .check_text_in_navigation_bar(
                        UITextElements.COMPONENTS
                        + Components.ACCORDSDK
                        + UITextElements.VERSION_ONE
                        + self._TEXT_PACKAGE_ACCORDSDK
                    )
                    .check_links_count(link_text=UITextElements.COMPONENTS, count=3)
                    .check_links_count(link_text=Components.ACCORDSDK, count=1)
                    .check_links_count(link_text=UITextElements.VERSION_ONE, count=1)
                    .check_favorites_indicator()
                    .check_text(page_text=self._TEXT_PACKAGE_ACCORDSDK, nth=1)
                    .check_title_and_text_in_tab_general_information(
                        title=UITextElements.TEXT_VERSION, text=Versions.ACCORDSDK + self._TEXT_IN_DEVELOPMENT
                    )
                    .check_title_and_text_in_tab_general_information(
                        title=UITextElements.PACKAGE_MANAGER, text=UITextElements.ANT_IVY
                    )
                    .check_title_and_text_in_tab_general_information(
                        title=UITextElements.PLATFORMS, text=RegularExpressions.PATTERN_WINDOWS
                    )
                    .check_title_and_text_in_tab_general_information(
                        title=UITextElements.TEXT_PROGRAMMING_LANGUAGE, text="Bourne ShellCC/C++ HeaderDOS BatchPython"
                    )
                    .check_text(UITextElements.LINKS)
                    .check_links_count(link_text=UITextElements.ARTIFACTORY, count=2)
                    .check_links_count(link_text=self._TEAM_CITY, count=1)
                    .check_links_count(link_text=self._SOURCE_CODE_INTERNAL_ARTIFACTORY_LINK_SOURCE, count=1)
                    .check_links_count(link_text=self._SOURCE_CODE_IS_EXTERNAL, count=1)
                )

            with allure.step("Вкладка 'Сборки'"):
                title = [self._TEXT_ASSEMBLY_BY_CONFIGURATION]
                value = [UITextElements.DEFAULT_BRAND_TRUNK]

                (
                    self.component_package_information_page.click_on_link(UITextElements.ASSEMBLIES_BY_CONFIGURATION)
                    .check_active_tab(UITextElements.ASSEMBLIES_BY_CONFIGURATION)
                    .check_table_headings(title)
                    .check_table_text_values(value)
                )

            with allure.step("Вкладка 'Компоненты-потребители'"):
                (
                    self.component_package_information_page.click_on_link(UITextElements.CONSUMER_COMPONENTS_TAB)
                    .check_active_tab(UITextElements.CONSUMER_COMPONENTS_TAB)
                    .check_links_count(link_text=Components.CRYPT_PASSWORD_FORGE, count=1)
                    .check_links_count(link_text=Versions.ONE_FOUR, count=1, exact=True)
                    .check_links_count(link_text="1.4.7.10", count=1)
                )

    @allure.suite("Паспорт пакета компонента, отображение ЯП, нет ссылки на исходный код.")
    @allure.title("Паспорт пакета компонента, отображение ЯП, нет ссылки на исходный код.")
    @allure.id("1521345")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1566864", LinkType.LINK, "TASK 1566864"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1521345", "TestCase 1521345")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.multiple_streams
    def test_component_package_no_link_to_source_code(self) -> None:
        """Паспорт пакета компонента, отображение ЯП, нет ссылки на исходный код."""
        # Паспорт пакета компонента_ отображение ЯП_Нет сылки на исходный код
        with allure.step(
            "1. Предусловие: Пользователь с правами на редактирование паспортов компонентов авторизован в сервисе. "
            "Открыт паспорт пакета компонента, нет ссылки на исходный код"
        ):
            self._setup(
                component_name=Components.ADDRESSBOOK, version=Versions.ADDRESSBOOK, package=Packages.ADDRESSBOOK
            )

        with allure.step("2. Проверить отображение ЯП"):
            self.component_package_information_page.check_input_no_link_to_source_code()

    @allure.suite("Паспорт пакета компонента, отображение ЯП, есть ссылка на исходный код.")
    @allure.title("Паспорт пакета компонента, отображение ЯП, есть ссылка на исходный код.")
    @allure.id("1521344")
    @allure.description("Баг: при добавлении ЯП иногда удаляются все ЯП из списка вместо добавления.")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1567739", LinkType.LINK, "TASK 1567739"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1521344", "TestCase 1521344")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_component_package_there_is_link_to_source_code(self) -> None:
        """Паспорт пакета компонента, отображение ЯП, есть ссылка на исходный код."""
        # Паспорт пакета компонента_ отображение ЯП_есть ссылка на исходный код
        with allure.step(
            "1. Предусловие: Пользователь с правами на редактирование паспортов компонентов авторизован в сервисе. "
            "Открыт паспорт пакета компонента, есть ссылка на исходный код"
        ):
            self._setup()

        with allure.step("2. Проверить отображение ЯП"):
            (
                self.component_package_information_page.check_text_in_chips_input(
                    UITextElements.PROGRAMMING_LANGUAGE_INPUT_PLACEHOLDER
                )
                .check_text_in_chips_input(UITextElements.BOURNE_SHELL)
                .check_text_in_chips_input("C/C++ Header")
                .check_text_in_chips_input("DOS Batch")
                .check_text_in_chips_input(UITextElements.PYTHON)
                .check_titles_count(title_text="Удалить из списка", count=5)
            )

    @allure.suite("Паспорт пакета компонента, добавить ЯП.")
    @allure.title("Паспорт пакета компонента, добавить ЯП.")
    @allure.id("1521346")
    @allure.description("Баг: при добавлении ЯП иногда удаляются все ЯП из списка вместо добавления.")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1567748", LinkType.LINK, "TASK 1567748"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1521346", "TestCase 1521346")
    @pytest.mark.parametrize("delete_programming_languages", [[_C_SHARP, _RUBY]], indirect=True)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_component_package_add_programming_language(self, delete_programming_languages: None) -> None:
        """Паспорт пакета компонента, добавить ЯП.

        :param delete_programming_languages: Фикстура удаления языков программирования.
        """
        # Паспорт пакета компонента_ добавить ЯП
        with allure.step(
            "1. Предусловие: Пользователь с правами на редактирование паспортов компонентов авторизован в сервисе. "
            "Открыт паспорт пакета компонента, есть ссылка на исходный код"
        ):
            self._setup()

        with allure.step("2. В поле 'Язык программирования' ввести часть названия ЯП"):
            self.component_package_information_page.fill_in_chips_input("C")

        with allure.step("3. Выбрать любой ЯП из списка"):
            self.component_package_information_page.click_on_element_with_text(self._C_SHARP)

        with allure.step("4. Повторить шаги 2 и 3 для добавления нескольких ЯП"):
            (
                self.component_package_information_page.fill_in_chips_input("ru")
                .click_on_element_with_text(self._RUBY)
                .check_titles_count(title_text="Удалить из списка", count=7)
                .check_text_in_chips_input(
                    "Bourne ShellCC/C++ HeaderDOS BatchPythonC#RubyНачните вводить и выберите из списка"
                )
            )

        with allure.step("5. Обновить страницу сервиса"):
            self.component_package_information_page.refresh_page().check_text_in_chips_input(
                "Bourne ShellCC#C/C++ HeaderDOS BatchPythonRubyНачните вводить и выберите из списка"
            )

    @allure.suite("Паспорт пакета компонента, удалить ручную ссылку на исходный код, подтвердить удаление.")
    @allure.title("Паспорт пакета компонента, удалить ручную ссылку на исходный код, подтвердить удаление.")
    @allure.id("1567136")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1580679", LinkType.LINK, "TASK 1580679"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1567136", "TestCase 1567136")
    @allure.severity(allure.severity_level.NORMAL)
    def test_component_package_remove_manual_source_code_link_confirm_deletion(self) -> None:
        """Паспорт пакета компонента, удалить ручную ссылку на исходный код, подтвердить удаление."""
        # Паспорт пакета компонента_Удалить ручную ссылку на исходный код_подтврдить удаление
        # TODO когда сервис станет работать стабильно добавить фикстуру проверки удаления ссылки после теста
        with allure.step(
            "1. Пользователь с правами на редактирование паспортов компонентов и продуктов авторизован в сервисе. "
            "Открыт паспорт пакета компонента, ссылка на внешний исходный код введена вручную"
        ):
            (
                self.component_page.click_on_link(UITextElements.ALL_COMPONENTS_TAB)
                .fill_in_search_input(Components.ADDRESSBOOK)
                .click_on_link(Components.ADDRESSBOOK)
            )
            self.component_information_page.click_on_link(UITextElements.VERSIONS_TAB).click_on_link(
                Versions.ADDRESSBOOK
            )
            self.product_version_information_page.click_on_link(UITextElements.PACKAGES_TAB).click_on_link(
                Packages.ADDRESSBOOK
            )
            (
                self.component_package_information_page.click_on_icon_plus_in_circle(nth=1)
                .fill_in_input_url(self._YA_RU)
                .check_text_in_input_url(self._YA_RU)
                .click_on_icon_floppy_disk()
            )

        with allure.step("2. Нажать на меню ссылки"):
            self.component_package_information_page.click_on_icon_menu().check_text(self._COPY).check_text(
                UITextElements.EDIT
            )

        with allure.step("3. Нажать 'Удалить'"):
            (
                self.component_package_information_page.click_on_element_with_text("Удалить")
                .check_title_modal()
                .check_text("Удалить ссылку?")
                .check_text(UITextElements.NO)
            )

        with allure.step("4. Нажать 'Да'"):
            (
                self.component_package_information_page.click_on_element_with_text(UITextElements.YES)
                .check_text(self._LINK_REMOVED)
                .check_text(self._SOURCE_CODE_IS_EXTERNAL_LINK_NOT_PROVIDED)
            )

    @allure.suite("Паспорт пакета компонента, ручной ввод ссылки на исходный код.")
    @allure.title("Паспорт пакета компонента, ручной ввод ссылки на исходный код.")
    @allure.id("1567133")
    @allure.description("Паспорт пакета компонента, ручной ввод ссылки на исходный код.")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1580689", LinkType.LINK, "TASK 1580689"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1567133", "TestCase 1567133")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_component_package_manually_entering_link_to_source_code(self, remove_links: None) -> None:
        """Паспорт пакета компонента, ручной ввод ссылки на исходный код.

        :param remove_links: Фикстура удаления ссылок.
        """
        # Паспорт пакета компонента_Ручной ввод ссылки на исходный код
        with allure.step(
            "1. Пользователь с правами на редактирование паспортов компонентов и продуктов авторизован в "
            "сервисе. Открыт паспорт пакета компонента, ссылка на внешний исходный код отсутствует"
        ):
            self.component_page.click_on_link(UITextElements.ALL_COMPONENTS_TAB).click_on_link(Components.ACETAO)
            self.component_information_page.click_on_link(UITextElements.VERSIONS_TAB).click_on_link(
                self._SIX_POINT_TWO
            )
            self.product_version_information_page.click_on_link(UITextElements.PACKAGES_TAB).click_on_link(
                self._PACKAGE_NUMBER_ACETAO
            )

        with allure.step("2. Нажать на иконку в виде плюса в кружочке"):
            self.component_package_information_page.click_on_icon_plus_in_circle(nth=1).check_button_cancel()

        with allure.step("3. Ввести валидную ссылку на внешний репозиторий"):
            self.component_package_information_page.fill_in_input_url(self._YA_RU).check_text_in_input_url(self._YA_RU)

        with allure.step("4. Нажать 'Сохранить'"):
            (
                self.component_package_information_page.click_on_icon_floppy_disk()
                .check_text(self._LINK_SAVED)
                .click_on_close_message_icon()
                .check_text(self._SOURCE_CODE_IS_EXTERNAL)
                .check_href(link_text=self._SOURCE_CODE_IS_EXTERNAL, href=self._YA_RU, in_table=False)
            )

        with allure.step("5. Повторить шаги тест-кейса для внутренней ссылки"):
            with allure.step("Нажать на иконку в виде плюса в кружочке"):
                self.component_package_information_page.click_on_icon_plus_in_circle().check_button_cancel()

            with allure.step("Ввести валидную ссылку на репозиторий"):
                self.component_package_information_page.fill_in_input_url(self._YA_RU).check_text_in_input_url(
                    self._YA_RU
                )

            with allure.step("Нажать 'Сохранить'"):
                (
                    self.component_package_information_page.click_on_icon_floppy_disk()
                    .check_text(self._LINK_SAVED)
                    .check_text(self._SOURCE_CODE_IS_INTERNAL)
                    .check_href(link_text=self._SOURCE_CODE_IS_INTERNAL, href=self._YA_RU, in_table=False)
                )

    @allure.suite("Паспорт пакета компонента, редактирование ссылки на исходный код (Исходный код внутренний).")
    @allure.title("Паспорт пакета компонента, редактирование ссылки на исходный код (Исходный код внутренний).")
    @allure.id("1567134")
    @allure.description("Паспорт пакета компонента, редактирование ссылки на исходный код (Исходный код внутренний).")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1581521", LinkType.LINK, "TASK 1581521"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1567134", "TestCase 1567134")
    @allure.severity(allure.severity_level.NORMAL)
    def test_component_package_editing_source_code_link_source_code_is_internal(
        self, return_link_from_source_fixture: None
    ) -> None:
        """Паспорт пакета компонента, редактирование ссылки на исходный код (Исходный код внутренний).

        :param return_link_from_source_fixture: Фикстура для возвращения ссылки из источника.
        """
        # Паспорт пакета компонента_Редактирование ссылки на исходный код
        # TODO проверить тест-кейс (его должны актуализировать), возможно нужно будет изменить автотест после этого
        link_tfs = (
            "http://tfs.example.ru/tfs/exampletc1/TDCode/_versionControl?path=%24%2FTDCode%2Fcontrib"
            "%2Faccordsdk%2Ftrunk"
        )

        with allure.step(
            "1. Пользователь с правами на редактирование паспортов компонентов и продуктов авторизован в сервисе. "
            "Открыт паспорт пакета компонента, ссылка на исходный код получена автоматически"
        ):
            self._setup()

        with allure.step("2. Нажать на меню справа от ссылки"):
            self.component_package_information_page.click_on_icon_menu()

        with allure.step("3. Нажать 'Редактировать'"):
            (
                self.component_package_information_page.check_href(
                    link_text=self._SOURCE_CODE_IS_INTERNAL,
                    href=link_tfs,
                    in_table=False,
                    exact=False,
                )
                .click_on_element_with_text(UITextElements.EDIT)
                .check_text_in_input_url(link_tfs)
            )

        with allure.step("4. Внести изменения в URL"):
            self.component_package_information_page.fill_in_input_url(self._YA_RU).check_text_in_input_url(self._YA_RU)

        with allure.step("5. Нажать 'Сохранить'"):
            (
                self.component_package_information_page.click_on_icon_floppy_disk()
                .check_text(self._LINK_SAVED)
                .check_text(self._SOURCE_CODE_IS_INTERNAL)
                .check_href(link_text=self._SOURCE_CODE_IS_INTERNAL, href=self._YA_RU, in_table=False)
            )

        with allure.step("6. Снова нажать меню ссылки"):
            self.component_package_information_page.click_on_icon_menu().check_text(self._RETURN_LINK_FROM_SOURCE)

    @allure.suite(
        "Паспорт пакета компонента, вернуть автоссылку на исходный код, подтвердить изменение (Исходн. код внутренний)."
    )
    @allure.title(
        "Паспорт пакета компонента, вернуть автоссылку на исходный код, подтвердить изменение (Исходн. код внутренний)."
    )
    @allure.id("1567135")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1581520", LinkType.LINK, "TASK 1581520"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1567135", "TestCase 1567135")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_component_package_return_autolink_to_source_code_confirm_change_source_code_is_internal(self) -> None:
        """Паспорт пакета компонента, вернуть автоссылку на исходный код, подтвердить изменение (Исход. код внутр.)."""
        # Паспорт пакета компонента_Вернуть автоссылку на исходный код_подтвердить изменение
        # TODO проверить тест-кейс (его должны актуализировать), возможно нужно будет изменить автотест после этого
        with allure.step(
            "1. Пользователь с правами на редактирование паспортов компонентов и продуктов авторизован в сервисе. "
            "Открыт паспорт пакета компонента, ссылки на исходный код полученные автоматически были изменены вручную"
        ):
            self._setup()
            (
                self.component_package_information_page.click_on_icon_menu()
                .click_on_element_with_text(UITextElements.EDIT)
                .fill_in_input_url(self._YA_RU)
                .click_on_icon_floppy_disk()
                .check_text(self._LINK_SAVED)
                .check_text(self._SOURCE_CODE_IS_INTERNAL)
                .check_href(link_text=self._SOURCE_CODE_IS_INTERNAL, href=self._YA_RU, in_table=False)
                .refresh_page()
            )

        with allure.step("2. Нажать на меню справа от ссылки"):
            self.component_package_information_page.click_on_icon_menu().check_text(self._COPY).check_text(
                UITextElements.EDIT
            )

        with allure.step("3. Нажать 'Вернуть ссылку из источника'"):
            (
                self.component_package_information_page.click_on_element_with_text(self._RETURN_LINK_FROM_SOURCE)
                .check_title_modal()
                .check_text("Будет подставлена ссылка полученная из источника.")
                .check_text("Вернуть ссылку?")
                .check_text(UITextElements.NO)
            )

        with allure.step("4. Нажать 'Да'"):
            (
                self.component_package_information_page.click_on_element_with_text(UITextElements.YES)
                .check_title_modal(visible=False)
                .check_text(self._LINK_CHANGED)
                .check_text(self._SOURCE_CODE_IS_INTERNAL, exact=False)
                .check_text("(источник ссылки Artifactory)")
            )

    @allure.suite("Паспорт пакета компонента, посмотреть сведения (все вкладки).")
    @allure.title("Паспорт пакета компонента, посмотреть сведения (все вкладки).")
    @allure.id("1565463")
    @allure.link(
        "https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1583242", LinkType.LINK, "TASK 1583242"
    )
    @allure.testcase("https://tfs.example.ru/tfs/exampletc1/DEP_PMO/_workitems/edit/1565463", "TestCase 1565463")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_component_package_view_details_all_tabs(self) -> None:
        """Паспорт пакета компонента, посмотреть сведения (все вкладки)."""
        # Паспорт пакета компонента_посмотреть сведения (все вкладки)
        package = "6.2.7.18"
        first_package_in_table = "1.5.285"
        assembly = "debian9.amd64.buildd_trunk"
        version_1_5 = "1.5"

        with allure.step(
            "1. Предусловие: Пользователь авторизован в сервисе, открыта страница 'Компоненты', выбран один из "
            "компонентов списка, выбрана версия компонента, выбран пакет"
        ):
            self._impersonate_as_user_with_read_or_write_permissions(write_permissions=False)
            self._setup(component_name=Components.ACETAO, version=self._SIX_POINT_TWO, package=package)

        with allure.step("2. Проверить отображение информации по выбранному пакету компонента"):
            with allure.step("Вкладка 'Общая информация'"):
                (
                    self.component_package_information_page.check_active_tab(UITextElements.GENERAL_INFORMATION)
                    .check_text_in_navigation_bar(
                        UITextElements.COMPONENTS
                        + Components.ACETAO
                        + f"{UITextElements.TEXT_VERSION} {self._SIX_POINT_TWO}"
                        + UITextElements.TEXT_PACKAGE
                        + " "
                        + package
                    )
                    .check_links_count(link_text=UITextElements.COMPONENTS, count=3)
                    .check_links_count(link_text=Components.ACETAO, count=1)
                    .check_links_count(link_text=f"{UITextElements.TEXT_VERSION} {self._SIX_POINT_TWO}", count=1)
                    .check_favorites_indicator()
                    .check_text(f"{UITextElements.TEXT_PACKAGE} {package}", nth=1)
                    .check_title_and_text_in_tab_general_information(
                        title=UITextElements.TEXT_VERSION, text=self._SIX_POINT_TWO + self._TEXT_IN_DEVELOPMENT
                    )
                    .check_title_and_text_in_tab_general_information(
                        title=UITextElements.PACKAGE_MANAGER, text=UITextElements.ANT_IVY
                    )
                    .check_title_and_text_in_tab_general_information(title=UITextElements.PLATFORMS, text="Debian")
                    .check_title_and_text_in_tab_general_information(
                        title=UITextElements.TEXT_PROGRAMMING_LANGUAGE,
                        text="BashBourne ShellCC#C++C/C++ HeaderC ShellDenizenScriptDOS BatchJavaLispLLVM IRPerlPython",
                    )
                    .check_text(UITextElements.LINKS)
                    .check_text(UITextElements.LINKS_ARTIFACTORY, exact=False)
                    .check_text(self._TEAM_CITY + " " + UITextElements.LICENSES_LINK, exact=False)
                    .check_links_count(link_text=UITextElements.REGULATIONS, count=2)
                    .check_links_count(link_text=self._SOURCE_CODE_INTERNAL_ARTIFACTORY_LINK_SOURCE, count=1)
                    .check_text(self._SOURCE_CODE_IS_EXTERNAL)
                )

            with allure.step("Вкладка 'Сборки'"):
                title = [self._TEXT_ASSEMBLY_BY_CONFIGURATION]
                value = [assembly]

                (
                    self.component_package_information_page.click_on_link(UITextElements.ASSEMBLIES_BY_CONFIGURATION)
                    .check_active_tab(UITextElements.ASSEMBLIES_BY_CONFIGURATION)
                    .check_text_total_assemblies_with_any_number()
                    .check_table_headings(title)
                    .check_table_text_values(value)
                    .check_links_count(link_text=assembly, count=1)
                    .fill_in_search_input(TestInputs.SPECIAL_CHARACTERS)
                )

            with allure.step("Вкладка 'Компоненты-потребители'"):
                titles = [UITextElements.COMPONENT, UITextElements.TEXT_VERSION, UITextElements.TEXT_PACKAGE]
                values = [Components.IPS, version_1_5, first_package_in_table]

                (
                    self.component_package_information_page.click_on_link(UITextElements.CONSUMER_COMPONENTS_TAB)
                    .check_active_tab(UITextElements.CONSUMER_COMPONENTS_TAB)
                    .check_text_total_components_with_any_number()
                    .check_table_headings(titles)
                    .check_table_text_values(values)
                    .check_links_count(link_text=Components.IPS, count=3)
                    .check_links_count(link_text=version_1_5, count=1, exact=True)
                    .check_links_count(link_text=first_package_in_table, count=1)
                    .fill_in_search_input(TestInputs.SPECIAL_CHARACTERS)
                )

    def _setup(
        self,
        component_name: str = Components.ACCORDSDK,
        version: str = Versions.ACCORDSDK,
        package: str = Packages.ACCORDSDK,
    ) -> None:
        """Предусловие: открыть пакет компонента.

        :param component_name: Название компонента.
        :param version: Версия компонента.
        :param package: Пакет компонента.
        """
        (
            self.component_page.click_on_title()
            .click_on_link(UITextElements.ALL_COMPONENTS_TAB)
            .click_on_link(component_name)
        )
        self.component_information_page.click_on_link(UITextElements.VERSIONS_TAB).click_on_link(version)
        self.product_version_information_page.click_on_link(UITextElements.PACKAGES_TAB).click_on_link(package)
