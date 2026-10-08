import re
from typing import Literal

import allure
from playwright.sync_api import Page, expect
from pytest_assume.plugin import assume
from typing_extensions import Self

from settings import settings
from src.constants.colors import Colors
from src.constants.css_keys_and_values import CssKeysAndValues
from src.constants.load_states import LoadStates
from src.constants.products import Products
from src.constants.regular_expressions import RegularExpressions
from src.constants.roles import Roles
from src.constants.ui_text_elements import UITextElements


class BasePage:
    """Базовый класс для работы со страницами."""

    # Селекторы, регулярные выражения и текстовые константы, необходимые для работы класса BasePage.
    _CHECK_MARK_IN_CHECKBOX_COMPONENT_IN_TABLE = "th path"
    """Галка в checkbox'е 'Компонент' в таблице."""
    _ELEMENTS_IN_PRODUCT_FIELD_IN_MARKUP_TRANSFER_WINDOW = ".formControl__control .popover__popover.selectPopover"
    """Элементы списка в поле 'Продукт' или в поле 'Версия' в окне переноса разметки."""
    _ELEMENT_IN_PRODUCT_FIELD_IN_MARKUP_TRANSFER_WINDOW = ".formControl__control li"
    """Элемент списка в поле 'Продукт' или в поле 'Версия' в окне переноса разметки."""
    _PRODUCT_FIELD_IN_MARKUP_TRANSFER_WINDOW = "div:nth-child(2) > .formControl__control"
    """Поле 'Продукт' в окне переноса разметки."""
    _COMBO_BOX_IN_WINDOW_TRANSFER_OF_MARKINGS = ".selectContainer__control"
    """ComboBox'ы в модальном окне переноса разметки."""
    _TR = "tr"
    """Селектор для тега 'tr'."""
    _PATH = "path"
    """Селектор для тега 'path'."""
    _SPAN = "span"
    """Селектор для тега 'span'."""
    _GREEN_INDICATION = ".toast__status_ok"
    """Зеленая индикация у тоста переноса разметки."""
    _RED_INDICATION = ".toast__status_error"
    """Красная индикация у тоста переноса разметки."""
    _YELLOW_INDICATION = ".toast__status_warning"
    """Жёлтая индикация у тоста переноса разметки."""
    _TITLE_MODAL = ".modalTitle.alertModal__title.alertModal__title_warning"
    """Жёлтая индикация у окна подтверждения."""
    _ICON_FLOPPY_DISK = ".icon-example-app.icon-app-save.icon-component"
    """Иконка в виде дискеты."""
    _DT = "dt"
    """Тег 'dt'."""
    _DD = "+ dd"
    """Соседний тег 'dd'."""
    _CHECKBOX = ".checkboxMark__checked"
    """CSS-селектор отмеченного checkbox'а в фильтре."""
    _CHECKBOX_IN_TABLE = ".checkboxMark__border"
    """CSS-селектор checkbox'а в таблице."""
    _CHECKBOX_COMPONENT_IN_TABLE = "th .checkboxMark__indeterminate"
    """CSS-селектор checkbox'а 'Компонент' в таблице."""
    _LABEL = "label"
    """Тег 'label'."""
    _NAVIGATION_BAR = ".navigationBar"
    """Панель навигации."""
    _SEARCH_RESULTS_FULL_NAME = ".menuWrapper, .option"
    """Выпадающая строка с полным именем сотрудника."""
    _TITLE = "h1"
    """Заголовок с названием компонента."""
    _COMPONENT_COMBO_BOX = ".selectContainer__valueContainer"
    """Выпадающий список в компоненте."""
    _COMPONENT_COMBO_BOX_INPUT = "input"
    """Input внутри выпадающего списка в компоненте."""
    _COMPONENT_COMBO_BOX_DIV = "div.selectContainer__selectedValue"
    """Div внутри выпадающего списка в компоненте."""
    _COMBO_BOX_IN_FILTER = ".appSelect"
    """Выпадающий список в фильтре."""
    _COMBO_BOX_WITH_TEXT_OR_PLACEHOLDER_IN_FILTER = (
        ".valueContainer__value, .valueContainer__placeholder, .selectContainer__placeholder"
    )
    """Выпадающий список с текстом или с placeholder'ом в фильтре."""
    _ELEMENT_COMBO_BOX_IN_FILTER = ".checkbox__label"
    """Элемент выпадающего списка в фильтре."""
    _USER_MENU_ICON = ".icon-example-app.icon-app-arrow-down-single.dropdown__chevronIcon.icon-component"
    """Иконка меню профиля в правом верхнем углу страницы."""
    _LOADING = ".loading .loading__svg"
    """Прелоадер страницы."""
    _ITEM_TITLE_LINK = ".navigationBar__itemTitle_link"
    """Ссылка-заголовок страницы."""
    _ACTIVE_TAB = ".tabs__horizontalTab_active"
    """Активная вкладка."""
    _FIRST_COLUMN_OF_TABLE = "dt"
    """Первая колонка таблицы."""
    SECOND_COLUMN_OF_TABLE = "dd"
    """Вторая колонка таблицы."""
    _NAVIGATION_BAR_ITEM_TITLE = ".navigationBar__itemTitle"
    """Название элемента панели навигации."""
    _FAVORITES_INDICATOR_ON = ".icon-app-favourite-on"
    """Включенный индикатор избранного."""
    _FAVORITES_INDICATOR_OFF = ".icon-app-favourite-off"
    """Выключенный индикатор избранного."""
    _FAVORITES_INDICATOR = ".icon-app-favourite-off, .icon-app-favourite-on"
    """Любой индикатор избранного (включенный или выключенный)."""
    _FUNNEL_ICON = ".icon-example-app.icon-app-filter.icon-component"
    """Иконка в виде воронки."""
    _CLOSE_FILTER_BLOCK_ICON = ".icon-example-app.icon-app-close.icon-component"
    """Иконка в виде крестика (закрывает блок фильтра)."""
    _COLUMN_HEADER = f"{_TR} > th"
    """Заголовок столбца."""
    _TABLE_ROW = f"tbody > {_TR}"
    """Строка таблицы."""
    TABLE_COLUMN = "td"
    """Столбец таблицы."""
    _LINK = "a"
    """Тег ссылки."""
    _EXPANDER = ".icon-example-app.icon-app-arrow-right-single.icon-component"
    """Экспандер."""
    _GREY_INDICATOR = ".circleMarker__mark"
    """Серый индикатор."""
    _LINK_PRODUCTS = ".icon-example-app.icon-app-application.navLink__icon.icon-component"
    """Ссылка 'Продукты'."""
    _SEARCH_INPUT = "input[placeholder='Поиск']"
    """Input поиска."""
    _CROSS_ICON = ".selectContainer__clearButton, .selectContainer__clearSelectButton"
    """Иконка в виде крестика."""
    _YELLOW_BACKLIGHT = "mark"
    """Жёлтая подсветка текста."""
    _TITLE_ARCHITECTURAL_REPOSITORY = "Архитектурный репозиторий"
    """Заголовок-ссылка 'Архитектурный репозиторий'."""
    _LOGOUT_BUTTON = "Выйти"
    """Кнопка 'Выйти'."""
    _IMPERSONATION_BUTTON = "Имперсонация"
    """Кнопка 'Имперсонация'."""
    _ACCOUNT_FOR_IMPERSONATION_LABEL = "Учетная запись для имперсонализации"
    """Текст 'Учетная запись для имперсонализации'."""
    _RESET_FILTERS_BUTTON = "Сбросить фильтры"
    """Кнопка 'Сбросить фильтры'."""
    _CLOSE_MESSAGE_ICON = "Закрыть сообщение"
    """Иконка закрытия всплывающего сообщения в правом нижнем углу."""
    _ERROR_MESSAGE = "Выпадающая строка с полным именем сотрудника должна была исчезнуть за 30 секунд"
    """Сообщение об ошибке."""
    _PATTERN_COMPONENTS_FOUND = re.compile(r"Найдено \d+ компонент[а-я]*")
    """Регулярное выражения для поиска текста 'Найдено <любое число> компонент(а/ов)'."""
    _ERROR_MESSAGE_RESPONSIBLE_FOR_IMPLEMENTATION = "Выпадающий список 'Ответственный за реализацию' недоступен."
    _ERROR_MESSAGE_FIRST_COMBO_BOX = "Первый выпадающий список на странице недоступен."
    _ERROR_MESSAGE_OWNER = "Выпадающий список 'Владелец' недоступен."
    _ERROR_MESSAGE_TECHNICAL_EXPERT = "Выпадающий список 'Технический эксперт' недоступен."
    _PLACEHOLDER = "placeholder"

    def __init__(self, page: Page) -> None:
        """Инициализация объекта страницы.

        :param page: Объект страницы playwright Page.
        """
        self.page = page

        # Локаторы, необходимые для работы класса BasePage.
        self._locator_title_architectural_repository = self.page.get_by_role(
            Roles.LINK, name=self._TITLE_ARCHITECTURAL_REPOSITORY
        )
        """Локатор заголовка-ссылки 'Архитектурный репозиторий'."""
        self._locator_column_header = self.page.locator(self._COLUMN_HEADER)
        """Локатор заголовка столбца."""
        self._locator_table_row = self.page.locator(self._TABLE_ROW)
        """Локатор строки таблицы."""
        self._locator_table_first_row_and_column = self._locator_table_row.first.locator(self.TABLE_COLUMN)
        """Локатор столбца в первой строке таблицы."""
        self._locator_table_last_row_and_column = self._locator_table_row.last.locator(self.TABLE_COLUMN)
        """Локатор столбца в последней строке таблицы."""
        self._locator_search_input = self.page.locator(self._SEARCH_INPUT)
        """Локатор input'а поиска."""
        self._locator_table_row_and_column = self._locator_table_row.locator(self.TABLE_COLUMN)
        """Локатор столбца в строке таблицы."""
        self._locator_reset_filters_button = self.page.get_by_role(Roles.BUTTON, name=self._RESET_FILTERS_BUTTON)
        """Локатор кнопки 'Сбросить фильтры'."""
        self._locator_cross_icon = self.page.locator(self._CROSS_ICON)
        """Локатор иконки в виде крестика."""
        self._locator_components_found_pattern = self.page.get_by_text(self._PATTERN_COMPONENTS_FOUND)
        """Локатор для поиска текста 'Найдено <любое число> компонент(а/ов)'."""
        self._locator_first_combo_box = self.page.locator(self._COMPONENT_COMBO_BOX).first
        """Локатор первого выпадающего списка в компоненте."""
        self._locator_first_combo_box_text = self.page.locator(self._COMPONENT_COMBO_BOX_DIV).first
        """Локатор первого div'а внутри выпадающего списка в компоненте."""
        self._locator_responsible_for_implementation = self.page.locator(self._COMPONENT_COMBO_BOX).nth(1)
        """Локатор второго выпадающего списка в компоненте ('Ответственный за реализацию')."""
        self._locator_responsible_for_implementation_text = self.page.locator(self._COMPONENT_COMBO_BOX_DIV).nth(1)
        """Локатор второго div'а внутри выпадающего списка в компоненте."""
        self._locator_component_owner_combo_box = self.page.locator(self._COMPONENT_COMBO_BOX).nth(2)
        """Локатор третьего выпадающего списка в компоненте ('Владелец')."""
        self._locator_component_owner_combo_box_text = self.page.locator(self._COMPONENT_COMBO_BOX_DIV).nth(2)
        """Локатор третьего div'а внутри выпадающего списка в компоненте."""
        self._locator_technical_expert_combo_box = self.page.locator(self._COMPONENT_COMBO_BOX).last
        """Локатор последнего выпадающего списка в компоненте ('Технический эксперт')."""
        self._locator_technical_expert_combo_box_text = self.page.locator(self._COMPONENT_COMBO_BOX_DIV).last
        """Локатор последнего div'а внутри выпадающего списка в компоненте."""
        self._locator_search_results_full_name = self.page.locator(self._SEARCH_RESULTS_FULL_NAME)
        """Локатор выпадающей строки с полным именем сотрудника."""
        self._locator_combo_box = self.page.locator(self._COMBO_BOX_WITH_TEXT_OR_PLACEHOLDER_IN_FILTER)
        """Локатор выпадающего списка с текстом или с placeholder'ом в фильтре."""
        self._locator_favorites_indicator = self.page.locator(self._FAVORITES_INDICATOR)
        """Локатор любого индикатора избранного (включенного или выключенного)."""
        self._locator_close_message_icon = self.page.get_by_title(self._CLOSE_MESSAGE_ICON)
        """Локатор иконки закрытия всплывающего сообщения в правом нижнем углу."""
        self._locator_link = self.page.locator(self._LINK)
        """Локатор тега ссылки."""
        self._locator_funnel_icon = self.page.locator(self._FUNNEL_ICON)
        """Локатор иконки в виде воронки."""

    @allure.step("Ожидать исчезновения последнего локатора LOADING.")
    def wait_for_page_ready(self) -> Self:
        """Ожидать исчезновения последнего локатора LOADING.

        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        # Ожидание в пять секунд
        self.page.wait_for_timeout(5_000)
        self.page.locator(self._LOADING).last.wait_for(state="detached")
        return self

    @allure.step("Обновить страницу.")
    def refresh_page(self) -> Self:
        """Обновить страницу.

        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        self.page.wait_for_load_state(LoadStates.NETWORK_IDLE)
        self.page.reload(wait_until=LoadStates.NETWORK_IDLE)
        return self

    @allure.step("Проверить заголовок-ссылку 'Архитектурный репозиторий'.")
    def check_title(self) -> Self:
        """Проверить заголовок-ссылку 'Архитектурный репозиторий'.

        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            expect(
                self._locator_title_architectural_repository, "Заголовок 'Архитектурный репозиторий' не отображается"
            ).to_be_visible(timeout=settings.DEFAULT_TIMEOUT)
        return self

    @allure.step("Кликнуть на заголовок-ссылку 'Архитектурный репозиторий'.")
    def click_on_title(self) -> Self:
        """Кликнуть на заголовок-ссылку 'Архитектурный репозиторий'.

        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            self.check_title()
            expect(
                self._locator_title_architectural_repository, "Заголовок-ссылка 'Архитектурный репозиторий' недоступен"
            ).to_be_enabled()
            self._locator_title_architectural_repository.click()
        return self

    @allure.step("Нажать иконку меню профиля в правом верхнем углу страницы.")
    def click_on_user_menu_icon(self) -> Self:
        """Нажать иконку меню профиля в правом верхнем углу страницы.

        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        locator_user_menu_icon = self.page.locator(self._USER_MENU_ICON)

        with assume:
            expect(
                locator_user_menu_icon, "Иконка меню профиля в правом верхнем углу страницы не отображается"
            ).to_be_visible(timeout=settings.DEFAULT_TIMEOUT)
            expect(
                locator_user_menu_icon, "Иконка меню профиля в правом верхнем углу страницы недоступна"
            ).to_be_enabled()
            locator_user_menu_icon.click()
        return self

    @allure.step("Нажать кнопку 'Выйти'.")
    def logout(self) -> Self:
        """Нажать кнопку 'Выйти'.

        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        locator_logout_button = self.page.get_by_role(Roles.BUTTON, name=self._LOGOUT_BUTTON)

        with assume:
            expect(locator_logout_button, "Кнопка 'Выйти' не отображается").to_be_visible()
            expect(locator_logout_button, "Кнопка 'Выйти' недоступна").to_be_enabled()
            locator_logout_button.click()
        return self

    @allure.step("Быстро выйти из сервиса.")
    def fast_logout(self) -> Self:
        """Быстро выйти из сервиса.

        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        self.page.wait_for_load_state(LoadStates.NETWORK_IDLE)
        self.page.evaluate("() => window.sessionStorage.clear();")
        self.page.context.clear_cookies()
        return self

    @allure.step("Кликнуть на кнопку 'Имперсонация'.")
    def click_on_impersonation_button(self) -> Self:
        """Кликнуть на кнопку 'Имперсонация'.

        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        locator_impersonation_button = self.page.get_by_role(Roles.BUTTON, name=self._IMPERSONATION_BUTTON)

        with assume:
            expect(locator_impersonation_button, "Кнопка 'Имперсонация' не отображается").to_be_visible()
            expect(locator_impersonation_button, "Кнопка 'Имперсонация' недоступна").to_be_enabled()
            locator_impersonation_button.click()

            expect(
                self.page.get_by_text(self._ACCOUNT_FOR_IMPERSONATION_LABEL),
                "Текст 'Учетная запись для имперсонализации' не отображается",
            ).to_be_visible()
        return self

    @allure.step("Проверить наличие или отсутствие текста на странице.")
    def check_text(
        self,
        page_text: str,
        visible: bool = True,
        exact: bool = True,
        nth: int = 0,
        timeout: int = settings.DEFAULT_TIMEOUT,
    ) -> Self:
        """Проверить наличие или отсутствие текста на странице.

        :param page_text: Текст, который должен присутствовать на странице.
        :param visible: Видимость текста (если 'False', то текст не должен присутствовать на странице).
        :param exact: Частичное совпадение по тексту (если 'True', то будет точное совпадение).
        :param nth: Порядковый номер элемента с текстом.
        :param timeout: Время ожидания появления или исчезновения текста.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            if visible:
                expect(
                    self.page.get_by_text(page_text, exact=exact).nth(nth),
                    f"Текст '{page_text}' не отображается на странице  (timeout = {timeout} миллисекунд)",
                ).to_be_visible(timeout=timeout)
            else:
                expect(
                    self.page.get_by_text(page_text, exact=exact).nth(nth),
                    f"Текст '{page_text}' не должен отображаться на странице (timeout = {timeout} миллисекунд)",
                ).not_to_be_visible(timeout=timeout)
        return self

    @allure.step("Проверить наличие текста на странице 'Всего * компонент(а/ов)'.")
    def check_text_total_components(self, count: int) -> Self:
        """Проверить наличие текста на странице 'Всего * компонент(а/ов)'.

        :param count: Количество компонентов.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            expect(
                self.page.get_by_text(f"Всего {count} компонент"),
                f"Текст 'Всего {count} компонент(а/ов)' не отображается на странице",
            ).to_be_visible(timeout=settings.DEFAULT_TIMEOUT)
        return self

    @allure.step("Проверить наличие текста на странице 'Всего <любое число> компонент(а/ов)'.")
    def check_text_total_components_with_any_number(self) -> Self:
        """Проверить наличие текста на странице 'Всего <любое число> компонент(а/ов)'.

        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        pattern_string = re.compile(r"Всего \d+ компонент")

        with assume:
            expect(
                self.page.get_by_text(pattern_string),
                "Текст 'Всего <любое число> компонент(а/ов)' не отображается на странице",
            ).to_be_visible(timeout=settings.DEFAULT_TIMEOUT)
        return self

    @allure.step("Проверить наличие текста на странице 'Всего <любое число> продукт(а/ов)'.")
    def check_text_total_products_with_any_number(self) -> Self:
        """Проверить наличие текста на странице 'Всего <любое число> продукт(а/ов)'.

        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        pattern_string = re.compile(r"Всего \d+ продукт")

        with assume:
            expect(
                self.page.get_by_text(pattern_string),
                "Текст 'Всего <любое число> продукт(а/ов)' не отображается на странице",
            ).to_be_visible(timeout=settings.DEFAULT_TIMEOUT)
        return self

    @allure.step("Проверить наличие текста на странице 'Всего <любое число> верс(ия/ий/ии)'.")
    def check_text_total_versions_with_any_number(self) -> Self:
        """Проверить наличие текста на странице 'Всего <любое число> верс(ия/ий/ии)'.

        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        pattern_string = re.compile(r"Всего \d+ верс[а-я]*")

        with assume:
            expect(
                self.page.get_by_text(pattern_string),
                "Текст 'Всего <любое число> верс(ия/ий/ии)' не отображается на странице",
            ).to_be_visible(timeout=settings.DEFAULT_TIMEOUT)
        return self

    @allure.step("Проверить наличие текста на странице 'Всего <любое число> сбор(ка/ки/ок)'.")
    def check_text_total_assemblies_with_any_number(self) -> Self:
        """Проверить наличие текста на странице 'Всего <любое число> сбор(ка/ки/ок)'.

        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        pattern_string = re.compile(r"Всего \d+ сбор[а-я]*")

        with assume:
            expect(
                self.page.get_by_text(pattern_string),
                "Текст 'Всего <любое число> сбор(ка/ки/ок)' не отображается на странице",
            ).to_be_visible(timeout=settings.DEFAULT_TIMEOUT)
        return self

    @allure.step("Проверить наличие текста на странице 'Всего <любое число> пакет(а/ов)'.")
    def check_text_total_packages_with_any_number(self) -> Self:
        """Проверить наличие текста на странице 'Всего <любое число> пакет(а/ов)'.

        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        pattern_string = re.compile(r"Всего \d+ пакет[а-я]*")

        with assume:
            expect(
                self.page.get_by_text(pattern_string),
                "Текст 'Всего <любое число> пакет(а/ов)' не отображается на странице",
            ).to_be_visible(timeout=settings.DEFAULT_TIMEOUT)
        return self

    @allure.step("Проверить наличие текста на странице 'Найдено * компонент(а/ов)'.")
    def check_text_components_found(self, count: int) -> Self:
        """Проверить наличие текста на странице 'Найдено * компонент(а/ов)'.

        :param count: Количество компонентов.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            expect(
                self.page.get_by_text(f"Найдено {count} компонент"),
                f"Текст 'Найдено {count} компонент(а/ов)' не отображается на странице",
            ).to_be_visible(timeout=settings.DEFAULT_TIMEOUT)
        return self

    @allure.step("Проверить наличие текста на странице 'Найдено * продукт(а/ов)'.")
    def check_text_products_found(self, count: int) -> Self:
        """Проверить наличие текста на странице 'Найдено * продукт(а/ов)'.

        :param count: Количество продуктов.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            expect(
                self.page.get_by_text(f"Найдено {count} продукт"),
                f"Текст 'Найдено {count} продукт(а/ов)' не отображается на странице",
            ).to_be_visible(timeout=settings.DEFAULT_TIMEOUT)
        return self

    @allure.step("Проверить наличие текста на странице 'Найдено <любое число> продукт(а/ов)'.")
    def check_text_products_found_with_any_number(self) -> Self:
        """Проверить наличие текста на странице 'Найдено <любое число> продукт(а/ов)'.

        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        pattern_string = re.compile(r"Найдено \d+ продукт[а-я]*")

        with assume:
            expect(
                self.page.get_by_text(pattern_string),
                "Текст 'Найдено <любое число> продукт(а/ов)' не отображается на странице",
            ).to_be_visible(timeout=settings.DEFAULT_TIMEOUT)
        return self

    @allure.step("Проверить наличие текста на странице 'Найдено <любое число> верс(ия/ий/ии)'.")
    def check_text_versions_found_with_any_number(self) -> Self:
        """Проверить наличие текста на странице 'Найдено <любое число> верс(ия/ий/ии)'.

        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        pattern_string = re.compile(r"Найдено \d+ верс[а-я]*")

        with assume:
            expect(
                self.page.get_by_text(pattern_string),
                "Текст 'Найдено <любое число> верс(ия/ий/ии)' не отображается на странице",
            ).to_be_visible(timeout=settings.DEFAULT_TIMEOUT)
        return self

    @allure.step("Проверить наличие текста на странице 'Найдено <любое число> сбор(ка/ки/ок)'.")
    def check_text_assemblies_found_with_any_number(self) -> Self:
        """Проверить наличие текста на странице 'Найдено <любое число> сбор(ка/ки/ок)'.

        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        pattern_string = re.compile(r"Найдено \d+ сбор[а-я]*")

        with assume:
            expect(
                self.page.get_by_text(pattern_string),
                "Текст 'Найдено <любое число> сбор(ка/ки/ок)' не отображается на странице",
            ).to_be_visible(timeout=settings.DEFAULT_TIMEOUT)
        return self

    @allure.step("Проверить наличие текста на странице 'Найдено <любое число> компонент(а/ов)'.")
    def check_text_components_found_with_any_number(self) -> Self:
        """Проверить наличие текста на странице 'Найдено <любое число> компонент(а/ов)'.

        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            expect(
                self._locator_components_found_pattern,
                "Текст 'Найдено <любое число> компонент(а/ов)' не отображается на странице",
            ).to_be_visible(timeout=settings.DEFAULT_TIMEOUT)
        return self

    @allure.step("Получить строку 'Найдено <любое число> компонент(а/ов)'.")
    def get_text_components_found_with_any_number(self) -> str:
        """Получить строку 'Найдено <любое число> компонент(а/ов)'.

        :return: Строка 'Найдено <любое число> компонент(а/ов)'.
        """
        # Ожидание в семь секунд
        self.page.wait_for_timeout(7_000)
        return self._locator_components_found_pattern.inner_text(timeout=settings.DEFAULT_TIMEOUT)

    @allure.step("Проверить количество ссылок на странице.")
    def check_links_count(self, link_text: str, count: int, exact: bool = False) -> Self:
        """Проверить количество ссылок на странице.

        :param link_text: Текст ссылки.
        :param count: Ожидаемое количество ссылок.
        :param exact: Частичное совпадение по тексту (если 'True', то будет точное совпадение).
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            expect(
                self.page.get_by_role(Roles.LINK, name=link_text, exact=exact),
                f"Ссылка с текстом '{link_text}' не отображается на странице или количество таких ссылок не "
                f"соответствует ожидаемому (ожидаемое количество: {count})",
            ).to_have_count(count, timeout=settings.DEFAULT_TIMEOUT)
        return self

    @allure.step("Проверить первый выпадающий список на странице.")
    def check_first_combo_box(self, placeholder: str) -> Self:
        """Проверить первый выпадающий список на странице.

        :param placeholder: Ожидаемый placeholder в выпадающем списке.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        error_message_placeholder = (
            f"Первый выпадающий список на странице не содержит ожидаемый placeholder '{placeholder}'."
        )
        error_message_not_displayed = "Первый выпадающий список на странице не отображается."

        with assume:
            if placeholder == UITextElements.ABSENT:
                expect(
                    self._locator_first_combo_box.locator(self._COMPONENT_COMBO_BOX_INPUT),
                    error_message_not_displayed,
                ).to_be_visible(timeout=settings.DEFAULT_TIMEOUT)
                expect(
                    self._locator_first_combo_box.locator(self._COMPONENT_COMBO_BOX_INPUT),
                    self._ERROR_MESSAGE_FIRST_COMBO_BOX,
                ).to_be_enabled()
                expect(
                    self._locator_first_combo_box.locator(self._COMPONENT_COMBO_BOX_INPUT),
                    error_message_placeholder,
                ).to_have_attribute(self._PLACEHOLDER, placeholder, timeout=settings.DEFAULT_TIMEOUT)
            else:
                expect(self._locator_first_combo_box_text, error_message_not_displayed).to_be_visible(
                    timeout=settings.DEFAULT_TIMEOUT
                )
                expect(self._locator_first_combo_box_text, self._ERROR_MESSAGE_FIRST_COMBO_BOX).to_be_enabled()
                expect(
                    self._locator_first_combo_box_text,
                    error_message_placeholder,
                ).to_have_text(placeholder, timeout=settings.DEFAULT_TIMEOUT)
        return self

    @allure.step("Кликнуть на первый выпадающий список на странице.")
    def click_on_first_combo_box(self) -> Self:
        """Кликнуть на первый выпадающий список на странице.

        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            expect(self._locator_first_combo_box, self._ERROR_MESSAGE_FIRST_COMBO_BOX).to_be_enabled()
            self._locator_first_combo_box.click()
        return self

    @allure.step("Проверить выпадающий список 'Ответственный за реализацию'.")
    def check_responsible_for_implementation_of_component_combo_box(self, placeholder: str) -> Self:
        """Проверить выпадающий список 'Ответственный за реализацию'.

        :param placeholder: Ожидаемый placeholder в выпадающем списке.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        error_message_placeholder = (
            f"Выпадающий список 'Ответственный за реализацию' не содержит ожидаемый placeholder '{placeholder}'."
        )
        error_message_not_displayed = "Выпадающий список 'Ответственный за реализацию' не отображается."

        with assume:
            if placeholder == UITextElements.ABSENT:
                expect(
                    self._locator_responsible_for_implementation.locator(self._COMPONENT_COMBO_BOX_INPUT),
                    error_message_not_displayed,
                ).to_be_visible(timeout=settings.DEFAULT_TIMEOUT)
                expect(
                    self._locator_responsible_for_implementation.locator(self._COMPONENT_COMBO_BOX_INPUT),
                    self._ERROR_MESSAGE_RESPONSIBLE_FOR_IMPLEMENTATION,
                ).to_be_enabled()
                expect(
                    self._locator_responsible_for_implementation.locator(self._COMPONENT_COMBO_BOX_INPUT),
                    error_message_placeholder,
                ).to_have_attribute(self._PLACEHOLDER, placeholder, timeout=settings.DEFAULT_TIMEOUT)
            else:
                expect(
                    self._locator_responsible_for_implementation_text,
                    error_message_not_displayed,
                ).to_be_visible(timeout=settings.DEFAULT_TIMEOUT)
                expect(
                    self._locator_responsible_for_implementation_text,
                    self._ERROR_MESSAGE_RESPONSIBLE_FOR_IMPLEMENTATION,
                ).to_be_enabled()
                expect(
                    self._locator_responsible_for_implementation_text,
                    error_message_placeholder,
                ).to_have_text(placeholder, timeout=settings.DEFAULT_TIMEOUT)
        return self

    @allure.step("Кликнуть на выпадающий список 'Ответственный за реализацию'.")
    def click_on_responsible_for_implementation_of_component_combo_box(self) -> Self:
        """Кликнуть на выпадающий список 'Ответственный за реализацию'.

        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            expect(
                self._locator_responsible_for_implementation,
                self._ERROR_MESSAGE_RESPONSIBLE_FOR_IMPLEMENTATION,
            ).to_be_enabled()
            self._locator_responsible_for_implementation.click()
        return self

    @allure.step("Ввести текст в выпадающий список 'Ответственный за реализацию'.")
    def fill_in_responsible_for_implementation_of_component_combo_box(
        self, full_name: str, click_on_tooltip: bool = True
    ) -> Self:
        """Ввести текст в выпадающий список 'Ответственный за реализацию'.

        :param full_name: ФИО технического эксперта компонента.
        :param click_on_tooltip: Кликнуть на tooltip (если 'False', то клик на tooltip не будет производиться).
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            self._locator_responsible_for_implementation.type(full_name)
            self.wait_for_page_ready()

            if click_on_tooltip:
                self._locator_search_results_full_name.click()
                expect(
                    self._locator_search_results_full_name,
                    self._ERROR_MESSAGE,
                ).not_to_be_visible(timeout=settings.DEFAULT_TIMEOUT)
                # Ожидание в одну секунду
                self.page.wait_for_timeout(1_000)
        return self

    @allure.step("Проверить выпадающий список 'Владелец'.")
    def check_component_owner_combo_box(self, placeholder: str) -> Self:
        """Проверить выпадающий список 'Владелец'.

        :param placeholder: Ожидаемый placeholder в выпадающем списке.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        error_message = f"Выпадающий список 'Владелец' не содержит ожидаемый placeholder '{placeholder}'."
        error_message_not_displayed = "Выпадающий список 'Владелец' не отображается."

        with assume:
            if placeholder == UITextElements.ABSENT:
                expect(
                    self._locator_component_owner_combo_box.locator(self._COMPONENT_COMBO_BOX_INPUT),
                    error_message_not_displayed,
                ).to_be_visible(timeout=settings.DEFAULT_TIMEOUT)
                expect(
                    self._locator_component_owner_combo_box.locator(self._COMPONENT_COMBO_BOX_INPUT),
                    self._ERROR_MESSAGE_OWNER,
                ).to_be_enabled()
                expect(
                    self._locator_component_owner_combo_box.locator(self._COMPONENT_COMBO_BOX_INPUT),
                    error_message,
                ).to_have_attribute(self._PLACEHOLDER, placeholder, timeout=settings.DEFAULT_TIMEOUT)
            else:
                expect(self._locator_component_owner_combo_box_text, error_message_not_displayed).to_be_visible(
                    timeout=settings.DEFAULT_TIMEOUT
                )
                expect(self._locator_component_owner_combo_box_text, self._ERROR_MESSAGE_OWNER).to_be_enabled()
                expect(
                    self._locator_component_owner_combo_box_text,
                    error_message,
                ).to_have_text(placeholder, timeout=settings.DEFAULT_TIMEOUT)
        return self

    @allure.step("Кликнуть на выпадающий список 'Владелец'.")
    def click_on_component_owner_combo_box(self) -> Self:
        """Кликнуть на выпадающий список 'Владелец'.

        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            expect(self._locator_component_owner_combo_box, self._ERROR_MESSAGE_OWNER).to_be_enabled()
            self._locator_component_owner_combo_box.click()
        return self

    @allure.step("Ввести текст в выпадающий список 'Владелец'.")
    def fill_in_component_owner_combo_box(self, full_name: str) -> Self:
        """Ввести текст в выпадающий список 'Владелец'.

        :param full_name: ФИО технического эксперта компонента.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            self._locator_component_owner_combo_box.type(full_name)
            self.wait_for_page_ready()
            self._locator_search_results_full_name.click()
            expect(
                self._locator_search_results_full_name,
                self._ERROR_MESSAGE,
            ).not_to_be_visible(timeout=settings.DEFAULT_TIMEOUT)

        # Ожидание в одну секунду
        self.page.wait_for_timeout(1_000)
        return self

    @allure.step("Проверить выпадающий список 'Технический эксперт'.")
    def check_technical_expert_combo_box(self, placeholder: str) -> Self:
        """Проверить выпадающий список 'Технический эксперт'.

        :param placeholder: Ожидаемый placeholder в выпадающем списке.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        error_message = f"Выпадающий список 'Технический эксперт' не содержит ожидаемый placeholder '{placeholder}'."
        error_message_not_displayed = "Выпадающий список 'Технический эксперт' не отображается."

        with assume:
            if placeholder == UITextElements.ABSENT:
                expect(
                    self._locator_technical_expert_combo_box.locator(self._COMPONENT_COMBO_BOX_INPUT),
                    error_message_not_displayed,
                ).to_be_visible(timeout=settings.DEFAULT_TIMEOUT)
                expect(
                    self._locator_technical_expert_combo_box.locator(self._COMPONENT_COMBO_BOX_INPUT),
                    self._ERROR_MESSAGE_TECHNICAL_EXPERT,
                ).to_be_enabled()
                expect(
                    self._locator_technical_expert_combo_box.locator(self._COMPONENT_COMBO_BOX_INPUT),
                    error_message,
                ).to_have_attribute(self._PLACEHOLDER, placeholder, timeout=settings.DEFAULT_TIMEOUT)
            else:
                expect(
                    self._locator_technical_expert_combo_box_text,
                    error_message_not_displayed,
                ).to_be_visible(timeout=settings.DEFAULT_TIMEOUT)
                expect(
                    self._locator_technical_expert_combo_box_text, self._ERROR_MESSAGE_TECHNICAL_EXPERT
                ).to_be_enabled()
                expect(
                    self._locator_technical_expert_combo_box_text,
                    error_message,
                ).to_have_text(placeholder, timeout=settings.DEFAULT_TIMEOUT)
        return self

    @allure.step("Кликнуть на выпадающий список 'Технический эксперт'.")
    def click_on_technical_expert_combo_box(self) -> Self:
        """Кликнуть на выпадающий список 'Технический эксперт'.

        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            expect(self._locator_technical_expert_combo_box, self._ERROR_MESSAGE_TECHNICAL_EXPERT).to_be_enabled()
            self._locator_technical_expert_combo_box.click()
        return self

    @allure.step("Ввести текст в выпадающий список 'Технический эксперт'.")
    def fill_in_technical_expert_combo_box(self, full_name: str) -> Self:
        """Ввести текст в выпадающий список 'Технический эксперт'.

        :param full_name: ФИО технического эксперта компонента.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            self._locator_technical_expert_combo_box.type(full_name)
            self.wait_for_page_ready()
            self._locator_search_results_full_name.click()
            expect(
                self._locator_search_results_full_name,
                self._ERROR_MESSAGE,
            ).not_to_be_visible(timeout=settings.DEFAULT_TIMEOUT)

        # Ожидание в две секунды
        self.page.wait_for_timeout(2_000)
        return self

    @allure.step("Проверить количество выпадающих списков.")
    def check_combo_boxes_count(self, placeholder: str, count: int) -> Self:
        """Проверить количество выпадающих списков.

        :param placeholder: Ожидаемый placeholder в выпадающем списке.
        :param count: Ожидаемое количество выпадающих списков.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            expect(
                self.page.locator(self._COMPONENT_COMBO_BOX).filter(has_text=placeholder),
                f"Выпадающий список с placeholder'ом '{placeholder}' не отображается на странице или "
                f"количество таких выпадающих списков не соответствует ожидаемому (ожидаемое количество: {count})",
            ).to_have_count(count)
        return self

    @allure.step("Кликнуть на ссылку.")
    def click_on_link(self, link_text: str) -> Self:
        """Кликнуть на ссылку.

        :param link_text: Текст ссылки.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        locator_link = self.page.get_by_role(Roles.LINK, name=link_text, exact=True)

        with assume:
            expect(locator_link, f"Ссылка с текстом '{link_text}' не отображается").to_be_visible(
                timeout=settings.DEFAULT_TIMEOUT
            )
            expect(locator_link, f"Ссылка с текстом '{link_text}' недоступна").to_be_enabled()
            locator_link.click()
        return self

    @allure.step("Кликнуть на ссылку 'Продукты'.")
    def click_on_link_products(self) -> Self:
        """Кликнуть на ссылку 'Продукты'.

        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        locator_link = self.page.locator(self._LINK_PRODUCTS)

        with assume:
            expect(locator_link, "Ссылка 'Продукты' не отображается").to_be_visible(timeout=settings.DEFAULT_TIMEOUT)
            expect(locator_link, "Ссылка 'Продукты' недоступна").to_be_enabled()
            locator_link.click()
        return self

    @allure.step("Проверить ссылку-заголовок страницы.")
    def check_item_title_link(self, title: str, nth: int = 0) -> Self:
        """Проверить ссылку-заголовок страницы.

        :param title: Текст ссылки-заголовка страницы.
        :param nth: Порядковый номер ссылки.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            expect(
                self.page.locator(self._ITEM_TITLE_LINK).nth(nth),
                f"Ссылка-заголовок не отображается или не содержит ожидаемый текст '{title}'",
            ).to_have_text(title, timeout=settings.DEFAULT_TIMEOUT)
        return self

    @allure.step("Проверить заголовок страницы.")
    def check_page_title(self, title_text: str) -> Self:
        """Проверить заголовок страницы.

        :param title_text: Текст заголовка.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            expect(
                self.page.locator(self._TITLE),
                f"Текст заголовка страницы '{title_text}' не отображается или отображается другое название",
            ).to_have_text(title_text, timeout=settings.DEFAULT_TIMEOUT)
        return self

    @allure.step("Проверить название активной вкладки.")
    def check_active_tab(self, tab_name: str) -> Self:
        """Проверить название активной вкладки.

        :param tab_name: Название вкладки.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            expect(
                self.page.locator(self._ACTIVE_TAB),
                f"Активная вкладка '{tab_name}' не отображается или отображается другое название",
            ).to_have_text(tab_name)
        return self

    @allure.step("Проверить индикатор/индикаторы избранного.")
    def check_favorites_indicator(self, count: int = 1) -> Self:
        """Проверить индикатор/индикаторы избранного.

        :param count: Количество индикаторов.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            expect(
                self._locator_favorites_indicator,
                f"Индикатор избранного не отображается или количество не соответствует ожидаемому '{count}'",
            ).to_have_count(count, timeout=settings.DEFAULT_TIMEOUT)
        return self

    @allure.step("Проверить индикатор/индикаторы избранного (включенные).")
    def check_count_favorites_indicator_on(self, count: int = 1) -> Self:
        """Проверить индикатор/индикаторы избранного (включенные).

        :param count: Количество индикаторов.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            expect(
                self.page.locator(self._FAVORITES_INDICATOR_ON),
                f"Включенный индикатор избранного не отображается или количество не соответствует ожидаемому '{count}'",
            ).to_have_count(count, timeout=settings.DEFAULT_TIMEOUT)
        return self

    @allure.step("Проверить видимость продукта 'Coordinator IG 4'.")
    def check_visibility_coordinator_ig_4(self) -> Self:
        """Проверить видимость продукта 'Coordinator IG 4'.

        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            expect(
                self.page.get_by_text(Products.COORDINATOR_IG_4),
                f"Продукт '{Products.COORDINATOR_IG_4}' должен был исчезнуть за 30 секунд",
            ).not_to_be_visible(timeout=settings.DEFAULT_TIMEOUT)
        return self

    @allure.step("Получить количество индикаторов избранного.")
    def get_count_favorites_indicator(self) -> int:
        """Получить количество индикаторов избранного.

        :return: Количество индикаторов избранного.
        """
        with assume:
            self.check_visibility_coordinator_ig_4()
            self.page.wait_for_timeout(1_500)

            expect(
                self._locator_favorites_indicator.first,
                "Ни один индикатор избранного не отображается",
            ).to_be_visible(timeout=settings.DEFAULT_TIMEOUT)
        return self._locator_favorites_indicator.count()

    @allure.step("Проверить название элемента панели навигации.")
    def check_navigation_bar_item_title(self, item_title_text: str) -> Self:
        """Проверить название элемента панели навигации.

        :param item_title_text: Название элемента панели навигации.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            expect(
                self.page.locator(self._NAVIGATION_BAR_ITEM_TITLE),
                f"Название элемента панели навигации не отображается или не соответствует ожидаемому значению "
                f"'{item_title_text}'",
            ).to_have_text(item_title_text)
        return self

    @allure.step("Проверить видимость иконки в виде воронки.")
    def check_visibility_funnel_icon(self) -> Self:
        """Проверить видимость иконки в виде воронки.

        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            expect(self._locator_funnel_icon, "Иконка в виде воронки не отображается").to_be_visible(
                timeout=settings.DEFAULT_TIMEOUT
            )
        return self

    @allure.step("Кликнуть на иконку в виде воронки.")
    def click_on_funnel_icon(self) -> Self:
        """Кликнуть на иконку в виде воронки.

        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            self.check_visibility_funnel_icon()
            expect(self._locator_funnel_icon, "Иконка в виде воронки недоступна").to_be_enabled(
                timeout=settings.DEFAULT_TIMEOUT
            )
            self._locator_funnel_icon.click()
        return self

    @allure.step("Проверить кнопку 'Сбросить фильтры'.")
    def check_reset_filters_button(self, visible_and_enabled: bool = True) -> Self:
        """Проверить кнопку 'Сбросить фильтры'.

        :param visible_and_enabled: Видимость и доступность кнопки (если 'False', то должна быть невидимой).
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            if visible_and_enabled:
                expect(
                    self._locator_reset_filters_button, f"Кнопка '{self._RESET_FILTERS_BUTTON}' не отображается"
                ).to_be_visible()
                expect(
                    self._locator_reset_filters_button, f"Кнопка '{self._RESET_FILTERS_BUTTON}' недоступна"
                ).to_be_enabled()
            else:
                expect(
                    self._locator_reset_filters_button, f"Кнопка '{self._RESET_FILTERS_BUTTON}' не должна отображаться"
                ).not_to_be_visible()
        return self

    @allure.step("Кликнуть на кнопку 'Сбросить фильтры'.")
    def click_on_reset_filters_button(self) -> Self:
        """Кликнуть на кнопку 'Сбросить фильтры'.

        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            self.check_reset_filters_button()
            self._locator_reset_filters_button.click()
        return self

    @allure.step("Проверить выпадающий список в фильтре.")
    def check_combo_box_in_filter(self, placeholder: str, visible: bool = True) -> Self:
        """Проверить выпадающий список в фильтре.

        :param placeholder: Placeholder combobox'а.
        :param visible: Видимость выпадающего списка в фильтре (если 'False', то список должен отсутствовать).
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            if visible:
                error_message_first = f"Выпадающий список с placeholder'ом '{placeholder}' не отображается"

                try:
                    expect(
                        self._locator_combo_box.filter(has_text=placeholder),
                        error_message_first,
                    ).to_be_visible()
                except Exception:
                    expect(
                        self.page.get_by_placeholder(placeholder),
                        error_message_first,
                    ).to_be_visible()
            else:
                error_message_second = f"Выпадающий список с placeholder'ом '{placeholder}' не должен отображаться"

                try:
                    expect(
                        self._locator_combo_box.filter(has_text=placeholder),
                        error_message_second,
                    ).not_to_be_visible()
                except Exception:
                    expect(
                        self.page.get_by_placeholder(placeholder),
                        error_message_second,
                    ).not_to_be_visible()
        return self

    @allure.step("Проверить элементы и текст в выпадающем списке фильтра.")
    def check_combo_box_list_and_text_in_filter(
        self, text_in_combo_box: str, list_combo_box_elements: list[str]
    ) -> Self:
        """Проверить элементы и текст в выпадающем списке фильтра.

        :param text_in_combo_box: Текст combobox'а.
        :param list_combo_box_elements: Список элементов combobox'а.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            locator_combo_box_with_text_in_filter = self.page.locator(
                self._COMBO_BOX_WITH_TEXT_OR_PLACEHOLDER_IN_FILTER
            ).filter(has_text=text_in_combo_box)

            expect(
                locator_combo_box_with_text_in_filter,
                f"Выпадающий список с текстом '{text_in_combo_box}' не отображается",
            ).to_be_visible()

            for i, element in enumerate(list_combo_box_elements):
                expect(
                    self.page.locator(self._COMBO_BOX_IN_FILTER)
                    .filter(has=locator_combo_box_with_text_in_filter)
                    .locator(self._ELEMENT_COMBO_BOX_IN_FILTER)
                    .nth(i),
                    f"Элемент combobox'а в строке номер {i + 1} не отображается или значение не соответствует "
                    f"ожидаемому '{element}'",
                ).to_have_text(element)
        return self

    @allure.step("Кликнуть на выпадающий список в фильтре.")
    def click_on_combo_box_in_filter(self, placeholder: str) -> Self:
        """Кликнуть на выпадающий список в фильтре.

        :param placeholder: Placeholder combobox'а.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        error_message = f"Выпадающий список с placeholder'ом '{placeholder}' недоступен"

        with assume:
            try:
                locator_combo_box_with_filter = self._locator_combo_box.filter(has_text=placeholder)

                expect(
                    locator_combo_box_with_filter,
                    error_message,
                ).to_be_enabled()
            except Exception:
                locator_combo_box_with_filter = self.page.get_by_placeholder(placeholder)

                expect(
                    locator_combo_box_with_filter,
                    error_message,
                ).to_be_enabled()

            locator_combo_box_with_filter.click()
        return self

    @allure.step("Ввести текст в выпадающий список в фильтре.")
    def fill_in_combo_box_in_filter(self, placeholder: str, text: str) -> Self:
        """Ввести текст в выпадающий список в фильтре.

        :param placeholder: Placeholder combobox'а.
        :param text: Текст вводимый в combobox.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            locator_combo_box_with_filter = self._locator_combo_box.filter(has_text=placeholder)

            locator_combo_box_with_filter.type(text)
        return self

    @allure.step("Кликнуть на элемент выпадающего списка в фильтре.")
    def click_on_element_in_combo_box_in_filter(self, element_name: str, nth: int = 0) -> Self:
        """Кликнуть на элемент выпадающего списка в фильтре.

        :param element_name: Название элемента.
        :param nth: Порядковый номер элемента.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        locator_element = (
            self.page.locator(self._ELEMENT_COMBO_BOX_IN_FILTER).get_by_text(element_name, exact=True).nth(nth)
        )

        with assume:
            expect(
                locator_element,
                f"В выпадающем списке элемент '{element_name}' не отображается",
            ).to_be_visible()
            expect(
                locator_element,
                f"В выпадающем списке элемент '{element_name}' недоступен",
            ).to_be_enabled()
            locator_element.click()
        return self

    @allure.step("Кликнуть на иконку в виде крестика (закрывает блок фильтра).")
    def click_on_close_filter_block_icon(self) -> Self:
        """Кликнуть на иконку в виде крестика (закрывает блок фильтра).

        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        locator_close_filter_block_icon = self.page.locator(self._CLOSE_FILTER_BLOCK_ICON)

        with assume:
            expect(
                locator_close_filter_block_icon,
                "Иконка в виде крестика, которая закрывает блок фильтра, не отображается",
            ).to_be_visible()
            expect(
                locator_close_filter_block_icon, "Иконка в виде крестика, которая закрывает блок фильтра, недоступна"
            ).to_be_enabled()
            locator_close_filter_block_icon.click()
        return self

    @allure.step("Проверить заголовки таблицы.")
    def check_table_headings(self, titles: list[str]) -> Self:
        """Проверить заголовки таблицы.

        :param titles: Список заголовков.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            for i, title in enumerate(titles):
                expect(
                    self._locator_column_header.nth(i),
                    f"Заголовок в столбце номер {i + 1} не отображается или значение не соответствует ожидаемому "
                    f"'{title}'",
                ).to_have_text(title, timeout=settings.DEFAULT_TIMEOUT)
        return self

    @allure.step("Проверить текстовые значения таблицы в первой или в последней строке.")
    def check_table_text_values(self, values: list[str], first_string: bool = True) -> Self:
        """Проверить текстовые значения таблицы в первой или в последней строке.

        :param values: Список текстовых значений таблицы в первой или в последней строке.
        :param first_string: Проверяется первая строка (если 'False', то проверяется последняя строка).
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            for i, value in enumerate(values):
                expect(
                    self._locator_table_first_row_and_column.nth(i)
                    if first_string
                    else self._locator_table_last_row_and_column.nth(i),
                    f"Значение в первой строке в столбце номер {i + 1} не отображается или значение не соответствует "
                    f"ожидаемому '{value}'",
                ).to_contain_text(value, timeout=settings.DEFAULT_TIMEOUT)
        return self

    @allure.step("Проверить видимость input'а поиска.")
    def check_visibility_search_input(self) -> Self:
        """Проверить видимость input'а поиска.

        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            expect(self._locator_search_input, "Поле поиска не отображается").to_be_visible()
        return self

    @allure.step("Ввести значение в input поиска.")
    def fill_in_search_input(self, text: str) -> Self:
        """Ввести значение в input поиска.

        :param text: Текст, который будет введён в поле поиска.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            self.check_visibility_search_input()
            expect(self._locator_search_input, "Поле поиска недоступно").to_be_enabled()
            self._locator_search_input.fill(text)

        self.page.wait_for_load_state(LoadStates.LOAD)
        return self

    @allure.step("Проверить атрибут 'href' у ссылки.")
    def check_href(self, link_text: str, href: str, in_table: bool = True, exact: bool = False, nth: int = 0) -> Self:
        """Проверить атрибут 'href' у ссылки.

        :param link_text: Текст ссылки.
        :param href: URL ссылки.
        :param in_table: Ссылка находится в таблице (если 'False', то будет проверка ссылки вне таблицы).
        :param exact: Частичное совпадение по тексту (если 'True', то будет точное совпадение).
        :param nth: Порядковый номер (по умолчанию первая ссылка (nth = 0)).
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        locator_link = (
            (
                self._locator_table_row_and_column.get_by_role(Roles.LINK, name=link_text, exact=True).nth(nth)
                if exact
                else self._locator_table_row_and_column.get_by_role(Roles.LINK, name=link_text).nth(nth)
            )
            if in_table
            else (
                self.page.get_by_role(Roles.LINK, name=link_text, exact=True).nth(nth)
                if exact
                else self.page.get_by_role(Roles.LINK, name=link_text).nth(nth)
            )
        )

        with assume:
            expect(
                locator_link,
                f"Ссылка с текстом '{link_text}' не отображается или атрибут href не соответствует ожидаемому '{href}'",
            ).to_have_attribute("href", href, timeout=settings.DEFAULT_TIMEOUT)
        return self

    @allure.step("Проверить, что ссылка открывается в новой вкладке.")
    def check_target_blank(self, link_text: str, nth: int = 0) -> Self:
        """Проверить, что ссылка открывается в новой вкладке.

        :param link_text: Текст ссылки.
        :param nth: Порядковый номер (по умолчанию первая ссылка (nth = 0)).
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        locator_link = self.page.get_by_role(Roles.LINK, name=link_text).nth(nth)

        with assume:
            expect(
                locator_link, f"Ссылка с текстом '{link_text}' не отображается или она не открывается в новой вкладке"
            ).to_have_attribute("target", "_blank")
        return self

    @allure.step("Проверить видимость иконки в виде крестика.")
    def check_cross_icon(self, visible: bool = True) -> Self:
        """Проверить видимость иконки в виде крестика.

        :param visible: Видимость иконки (если 'False', то иконка должна отсутствовать на странице).
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            if visible:
                expect(self._locator_cross_icon, "Иконка в виде крестика не отображается.").to_be_visible()
            else:
                expect(self._locator_cross_icon, "Иконка в виде крестика не должна отображаться.").not_to_be_visible()
        return self

    @allure.step("Кликнуть на иконку в виде крестика.")
    def click_on_cross_icon(self) -> Self:
        """Кликнуть на иконку в виде крестика.

        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            self.check_cross_icon()
            expect(self._locator_cross_icon, "Иконка в виде крестика недоступна").to_be_enabled()
            self._locator_cross_icon.click()
        return self

    @allure.step("Кликнуть на все иконки в виде крестика.")
    def click_on_all_cross_icons(self) -> Self:
        """Кликнуть на все иконки в виде крестика.

        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            expect(self._locator_cross_icon.first, "Первая иконка в виде крестика не отображается.").to_be_visible(
                timeout=settings.DEFAULT_TIMEOUT
            )

            while self._locator_cross_icon.count() > 0:
                expect(self._locator_cross_icon.first, "Первая иконка в виде крестика недоступна").to_be_enabled()
                self._locator_cross_icon.first.click()
                # Ожидание в пятьсот миллисекунд
                self.page.wait_for_timeout(500)
        return self

    @allure.step("Проверить видимость иконки для закрытия сообщения в правом нижнем углу.")
    def check_visibility_close_message_icon(self) -> Self:
        """Проверить видимость иконки для закрытия сообщения в правом нижнем углу.

        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            expect(
                self._locator_close_message_icon,
                "Иконка закрытия всплывающего сообщения в правом нижнем углу не отображается.",
            ).to_be_visible(timeout=settings.DEFAULT_TIMEOUT)
        return self

    @allure.step("Закрыть сообщение в правом нижнем углу.")
    def click_on_close_message_icon(self) -> Self:
        """Закрыть сообщение в правом нижнем углу.

        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            self.check_visibility_close_message_icon()
            expect(
                self._locator_close_message_icon,
                "Иконка закрытия всплывающего сообщения в правом нижнем углу недоступна",
            ).to_be_enabled()
            self._locator_close_message_icon.click()
        return self

    @allure.step("Проверить input поиска.")
    def check_search_input(self, input_text: str) -> Self:
        """Проверить input поиска.

        :param input_text: Текст, который должен присутствовать в поле поиска.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            expect(self._locator_search_input, f"Поле поиска не содержит текст '{input_text}'").to_have_value(
                input_text
            )
        return self

    @allure.step("Проверить что текст имеет жёлтую подсветку.")
    def check_yellow_backlight(self, yellow_text: str) -> Self:
        """Проверить что текст имеет жёлтую подсветку.

        :param yellow_text: Текст, который должен быть подсвечен жёлтым цветом.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            expect(
                self.page.locator(self._YELLOW_BACKLIGHT),
                f"Текст '{yellow_text}' не подсвечен жёлтым.",
            ).to_contain_text(yellow_text)
        return self

    @allure.step("Кликнуть на экспандер.")
    def click_on_expander(self, text_with_expander: str) -> Self:
        """Кликнуть на экспандер.

        :param text_with_expander: Текст рядом с которым находится экспандер.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        locator_expander = self._locator_table_row_and_column.filter(has_text=text_with_expander).locator(
            self._EXPANDER
        )

        with assume:
            expect(locator_expander, f"Экспандер рядом с текстом '{text_with_expander}' не отображается").to_be_visible(
                timeout=settings.DEFAULT_TIMEOUT
            )
            expect(locator_expander, f"Экспандер рядом с текстом '{text_with_expander}' недоступен").to_be_enabled()
            locator_expander.click()
        return self

    @allure.step("Кликнуть на иконку избранного (включенную).")
    def click_on_favorites_icon_on(self, text_favorites_icon: str) -> Self:
        """Кликнуть на иконку избранного (включенную).

        :param text_favorites_icon: Текст рядом с иконкой избранного.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        locator_favorites_icon_on = self._locator_table_row.filter(has_text=text_favorites_icon).locator(
            self._FAVORITES_INDICATOR_ON
        )

        with assume:
            expect(
                locator_favorites_icon_on, f"Иконка избранного рядом с текстом '{text_favorites_icon}' не отображается"
            ).to_be_visible(timeout=settings.DEFAULT_TIMEOUT)
            expect(
                locator_favorites_icon_on, f"Иконка избранного рядом с текстом '{text_favorites_icon}' недоступна"
            ).to_be_enabled()
            locator_favorites_icon_on.click()
        return self

    @allure.step("Кликнуть на иконку избранного (выключенную).")
    def click_on_favorites_icon_off(self, text_favorites_icon: str) -> Self:
        """Кликнуть на иконку избранного (выключенную).

        :param text_favorites_icon: Текст рядом с иконкой избранного.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        locator_favorites_icon_off = self._locator_table_row.filter(has_text=text_favorites_icon).locator(
            self._FAVORITES_INDICATOR_OFF
        )

        with assume:
            expect(
                locator_favorites_icon_off, f"Иконка избранного рядом с текстом '{text_favorites_icon}' не отображается"
            ).to_be_visible(timeout=settings.DEFAULT_TIMEOUT)
            expect(
                locator_favorites_icon_off, f"Иконка избранного рядом с текстом '{text_favorites_icon}' недоступна"
            ).to_be_enabled()
            locator_favorites_icon_off.click()
        return self

    @allure.step("Проверить видимость иконки избранного (выключенную).")
    def check_favorites_icon_off(self) -> Self:
        """Проверить видимость иконки избранного (выключенную).

        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            expect(
                self.page.locator(self._FAVORITES_INDICATOR_OFF), "Выключенная иконка избранного не отображается"
            ).to_be_visible(timeout=settings.DEFAULT_TIMEOUT)
        return self

    @allure.step("Проверить видимость иконки избранного (включенную).")
    def check_favorites_icon_on(self) -> Self:
        """Проверить видимость иконки избранного (включенную).

        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            expect(
                self.page.locator(self._FAVORITES_INDICATOR_ON), "Включенная иконка избранного не отображается"
            ).to_be_visible(timeout=settings.DEFAULT_TIMEOUT)
        return self

    @allure.step("Кликнуть на иконку избранного (выключенную или включенную).")
    def click_on_favorites_icon(self) -> Self:
        """Кликнуть на иконку избранного (выключенную или включенную).

        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            expect(self._locator_favorites_indicator, "Иконка избранного не отображается").to_be_visible(
                timeout=settings.DEFAULT_TIMEOUT
            )
            expect(self._locator_favorites_indicator, "Иконка избранного недоступна").to_be_enabled()
            self._locator_favorites_indicator.click()
        return self

    @allure.step("Кликнуть на все иконки избранного и иконки 'Закрыть сообщение' в правом нижнем углу.")
    def click_on_all_favorites_icons_and_all_close_message_icons(self) -> Self:
        """Кликнуть на все иконки избранного и иконки 'Закрыть сообщение' в правом нижнем углу.

        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        self.page.wait_for_load_state(LoadStates.NETWORK_IDLE)

        with assume:
            while self._locator_favorites_indicator.count() > 0:
                self._locator_favorites_indicator.first.click()
                self._locator_close_message_icon.first.click()
        return self

    @allure.step("Проверить, что экспандер в списке не отображается.")
    def check_invisible_expanders(self, list_with_expander: list[str]) -> Self:
        """Проверить, что экспандер в списке не отображается.

        :param list_with_expander: Список рядом с которым проверяется отображение экспандеров.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            for text_with_expander in list_with_expander:
                locator_expander = self._locator_table_row_and_column.filter(has_text=text_with_expander).locator(
                    self._EXPANDER
                )

                expect(
                    locator_expander, f"Экспандер рядом с текстом '{text_with_expander}' не должен отображаться"
                ).not_to_be_visible()
        return self

    @allure.step("Проверить таблицу компонентов или продуктов.")
    def check_table_components_or_products(self, strings: list[str]) -> Self:
        """Проверить таблицу компонентов или продуктов.

        :param strings: Список строк.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            self.check_visibility_coordinator_ig_4()
            # Ожидание в две секунды
            self.page.wait_for_timeout(2_000)

            for i, one_string in enumerate(strings):
                expect(
                    self._locator_table_row_and_column.locator(self._LINK).nth(i),
                    f"Значение в строке номер {i + 1} не отображается или не соответствует ожидаемому "
                    f"'{one_string}'",
                ).to_have_text(one_string, timeout=settings.DEFAULT_TIMEOUT)
        return self

    @allure.step("Кликнуть на элемент с определённым текстом.")
    def click_on_element_with_text(self, element_text: str, nth: int = 0) -> Self:
        """Кликнуть на элемент с определённым текстом.

        :param element_text: Текст элемента.
        :param nth: Порядковый номер элемента.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        locator_element = self.page.get_by_text(element_text, exact=True).nth(nth)

        with assume:
            expect(locator_element, f"Элемент с текстом '{element_text}' не отображается").to_be_visible(
                timeout=settings.DEFAULT_TIMEOUT
            )
            expect(locator_element, f"Элемент с текстом '{element_text}' недоступен").to_be_enabled()
            locator_element.click()

        self.page.wait_for_load_state(LoadStates.NETWORK_IDLE)
        return self

    @allure.step("Перейти на предыдущую страницу.")
    def go_to_previous_or_next_page(self, count: int = 1, previous: bool = True) -> Self:
        """Перейти на предыдущую страницу.

        :param count: Количество итераций цикла.
        :param previous: Переход на предыдущую страницу (если значение False, тогда переход будет на следующую).
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        for _ in range(count):
            self.page.go_back(wait_until=LoadStates.NETWORK_IDLE) if previous else self.page.go_forward(
                wait_until=LoadStates.NETWORK_IDLE
            )
        return self

    @allure.step("Проверить checkbox с текстом.")
    def check_checkbox_with_text_in_combo_box_in_filter(self, text: str, marked: bool = True, nth: int = 0) -> Self:
        """Проверить checkbox с текстом.

        :param text: Текст рядом с которым расположен checkbox.
        :param marked: Отмечен checkbox или нет (если 'False', то checkbox должен быть не отмечен).
        :param nth: Порядковый номер checkbox'а.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        locator_checkbox = self.page.locator(self._LABEL).filter(has_text=text).locator(self._CHECKBOX).nth(nth)

        with assume:
            if marked:
                expect(
                    locator_checkbox,
                    f"Checkbox '{text}' не отмечен",
                ).to_be_visible()
            else:
                expect(
                    locator_checkbox,
                    f"Checkbox '{text}' не должен быть отмечен",
                ).not_to_be_visible()
        return self

    @allure.step("Проверить текст в панели навигации.")
    def check_text_in_navigation_bar(self, text: str) -> Self:
        """Проверить текст в панели навигации.

        :param text: Текст, который отображается в панели навигации.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            expect(
                self.page.locator(self._NAVIGATION_BAR),
                f"Текст не отображается в панели навигации или не соответствует ожидаемому '{text}'",
            ).to_have_text(text)
        return self

    @allure.step("Проверить заголовок и текст на вкладке 'Общая информация'.")
    def check_title_and_text_in_tab_general_information(self, title: str, text: str) -> Self:
        """Проверить заголовок и текст на вкладке 'Общая информация'.

        :param title: Заголовок строки в таблице.
        :param text: Текст в строке, который соответствует заголовку.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            expect(
                self.page.locator(self._DT).filter(has_text=title).locator(self._DD),
                f"Заголовок или текст во вкладке 'Общая информация' не отображаются или не соответствуют ожидаемым "
                f"(заголовок: '{title}', текст: '{text}')",
            ).to_have_text(text)
        return self

    @allure.step("Получить текст на вкладке 'Общая информация' по заголовку строки.")
    def get_text_in_tab_general_information(self, title: str) -> str:
        """Получить текст на вкладке 'Общая информация' по заголовку строки.

        :param title: Заголовок строки в таблице.
        :return: Текст на вкладке 'Общая информация' по заголовку строки.
        """
        locator_title_and_text_in_tab_general_information = (
            self.page.locator(self._DT).filter(has_text=title).locator(self._DD)
        )

        with assume:
            expect(
                locator_title_and_text_in_tab_general_information,
                f"Заголовок строки во вкладке 'Общая информация' не отображается или не соответствует ожидаемому "
                f"(заголовок: '{title}')",
            ).to_be_visible()
        return locator_title_and_text_in_tab_general_information.inner_text()

    @allure.step("Кликнуть на иконку в виде дискеты.")
    def click_on_icon_floppy_disk(self) -> Self:
        """Кликнуть на иконку в виде дискеты.

        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        locator_icon_floppy_disk = self.page.locator(self._ICON_FLOPPY_DISK)

        # Ожидание в одну секунду
        self.page.wait_for_timeout(1_000)

        with assume:
            expect(locator_icon_floppy_disk, "Иконка в виде дискеты не отображается").to_be_visible(
                timeout=settings.DEFAULT_TIMEOUT
            )
            expect(locator_icon_floppy_disk, "Иконка в виде дискеты недоступна").to_be_enabled()
            locator_icon_floppy_disk.click()
        return self

    @allure.step("Проверить жёлтую индикацию у окна подтверждения.")
    def check_title_modal(self, visible: bool = True) -> Self:
        """Проверить жёлтую индикацию у окна подтверждения.

        :param visible: Элемент должен присутствовать на странице или нет (если 'False', то должен отсутствовать).
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        locator_title_modal = self.page.locator(self._TITLE_MODAL)

        with assume:
            if visible:
                expect(locator_title_modal, "Жёлтая индикация у окна подтверждения не отображается").to_be_visible(
                    timeout=settings.DEFAULT_TIMEOUT
                )
            else:
                expect(
                    locator_title_modal, "Жёлтая индикация у окна подтверждения не должна отображаться"
                ).not_to_be_visible(timeout=settings.DEFAULT_TIMEOUT)
        return self

    @allure.step("Проверить сортировку ссылок на странице.")
    def check_links_sorting(self, number_of_first_element: int = 0, reverse: bool = False) -> Self:
        """Проверить сортировку ссылок на странице.

        :param number_of_first_element: С какой ссылки начать проверку (по умолчанию: с первой (с 0)).
        :param reverse: Сортировка в порядке возрастания или в порядке убывания (по умолчанию 'False': по возрастанию).
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        # TODO подумать, как сделать другие проверки сортировки без хардкода, как в этом методе
        # Ожидание в одну секунду
        self.page.wait_for_timeout(1_000)
        list_links = self._locator_link.evaluate_all("elements => elements.map(el => el.innerText.trim())")
        list_links = list_links[number_of_first_element:]
        list_links_reverse = sorted(list_links, reverse=reverse)

        assert list_links == list_links_reverse, "Ссылки неправильно отсортированы"
        return self

    @allure.step("Кликнуть на checkbox в таблице.")
    def click_on_checkbox_in_table(self, nth: int) -> Self:
        """Кликнуть на checkbox в таблице.

        :param nth: Порядковый номер checkbox'а.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        locator_checkbox_in_table = self.page.locator(self._CHECKBOX_IN_TABLE).nth(nth)

        with assume:
            expect(locator_checkbox_in_table, f"Checkbox с порядковым номером '{nth}' не отображается").to_be_visible(
                timeout=settings.DEFAULT_TIMEOUT
            )
            expect(locator_checkbox_in_table, f"Checkbox с порядковым номером '{nth}' недоступен").to_be_enabled()
            locator_checkbox_in_table.click()
        return self

    @allure.step("Кликнуть на checkbox в таблице (по тексту).")
    def click_on_checkbox_by_text_in_table(self, text: str) -> Self:
        """Кликнуть на checkbox в таблице (по тексту).

        :param text: Текст в таблице справа от checkbox'а.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        # Локатор checkbox'а в таблице (слева от ссылки на компонент)
        locator_checkbox_by_text_in_table = self.page.get_by_role(Roles.LINK, name=text, exact=True).locator(
            "xpath=../preceding-sibling::td[1]/label"
        )

        with assume:
            expect(locator_checkbox_by_text_in_table, f"Checkbox с текстом '{text}' не отображается").to_be_visible(
                timeout=settings.DEFAULT_TIMEOUT
            )
            expect(locator_checkbox_by_text_in_table, f"Checkbox с текстом '{text}' недоступен").to_be_enabled()
            locator_checkbox_by_text_in_table.click()
        return self

    @allure.step("Проверить галочку у checkbox'а в таблице.")
    def check_checkbox_in_table(self, nth: int) -> Self:
        """Проверить галочку у checkbox'а в таблице.

        :param nth: Порядковый номер checkbox'а.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            expect(
                self.page.locator(self._TR).nth(nth).locator(self.TABLE_COLUMN).first.locator(self._PATH),
                f"Checkbox с порядковым номером '{nth}' не отмечен галочкой",
            ).to_have_css(CssKeysAndValues.DISPLAY, CssKeysAndValues.INLINE)
        return self

    @allure.step("Проверить закрашен или нет checkbox 'Компонент' в таблице.")
    def check_checkbox_component_in_table(self, marked: bool = True) -> Self:
        """Проверить закрашен или нет checkbox 'Компонент' в таблице.

        :param marked: Checkbox 'Компонент' должен быть закрашен или нет (если 'False', то не закрашен).
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        locator_checkbox_component_in_table = self.page.locator(self._CHECKBOX_COMPONENT_IN_TABLE)

        with assume:
            if marked:
                expect(
                    locator_checkbox_component_in_table,
                    "Checkbox 'Компонент' не закрашен",
                ).to_be_visible()
            else:
                expect(
                    locator_checkbox_component_in_table,
                    "Checkbox 'Компонент' не должен быть закрашен",
                ).not_to_be_visible()
        return self

    @allure.step("Проверить галку в checkbox'е 'Компонент' в таблице.")
    def check_check_mark_in_checkbox_component_in_table(self, marked: bool = True) -> Self:
        """Проверить галку в checkbox'е 'Компонент' в таблице.

        :param marked: Если 'False', то галка не отображается.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        locator_check_mark = self.page.locator(self._CHECK_MARK_IN_CHECKBOX_COMPONENT_IN_TABLE)

        with assume:
            if marked:
                expect(locator_check_mark, "Галка в checkbox'е 'Компонент' в таблице не отображается").to_be_visible()
            else:
                expect(
                    locator_check_mark, "Галка в checkbox'е 'Компонент' в таблице не должна отображаться"
                ).not_to_be_visible()
        return self

    @allure.step("Кликнуть на элемент с определённым placeholder'ом.")
    def click_on_element_with_placeholder(self, placeholder: str) -> Self:
        """Кликнуть на элемент с определённым placeholder'ом.

        :param placeholder: Placeholder элемента.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        locator_element_by_placeholder = self.page.get_by_placeholder(placeholder)

        with assume:
            expect(
                locator_element_by_placeholder, f"Элемент с placeholder'ом '{placeholder}' не отображается"
            ).to_be_visible(timeout=settings.DEFAULT_TIMEOUT)
            expect(
                locator_element_by_placeholder, f"Элемент с placeholder'ом '{placeholder}' недоступен"
            ).to_be_enabled()
            locator_element_by_placeholder.click()
        return self

    @allure.step("Кликнуть на элемент с определённым titl'ом.")
    def click_on_element_with_title(self, title: str, nth: int = 0) -> Self:
        """Кликнуть на элемент с определённым titl'ом.

        :param title: Title элемента.
        :param nth: Порядковый номер элемента (по умолчанию `nth = 0`).
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        locator_element_by_title = self.page.get_by_title(title).nth(nth)

        with assume:
            expect(locator_element_by_title, f"Элемент с titl'ом '{title}' не отображается").to_be_visible(
                timeout=settings.DEFAULT_TIMEOUT
            )
            expect(locator_element_by_title, f"Элемент с titl'ом '{title}' недоступен").to_be_enabled()
            locator_element_by_title.click()
        return self

    @allure.step("Отключить сеть.")
    def disconnect_network(self, offline: bool = True) -> Self:
        """Отключить сеть.

        :param offline: Сеть отключена (если 'False', то сеть будет включена).
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        self.page.context.set_offline(offline)
        return self

    @allure.step("Проверить видимость индикации у тоста переноса разметки.")
    def check_visibility_indication(self, color: Literal["green", "red", "yellow"]) -> Self:
        """Проверить видимость индикации у тоста переноса разметки.

        :param color: Цвет индикации у тоста (возможные значения: green, red, yellow)
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        colors = {Colors.GREEN, Colors.RED, Colors.YELLOW}

        assert color in colors, f"Недопустимое значение ('{color}'). Выберите из: {colors}"

        with assume:
            if color == Colors.GREEN:
                expect(
                    self.page.locator(self._GREEN_INDICATION),
                    "Зеленая индикация у тоста переноса разметки не отображается",
                ).to_be_visible(timeout=settings.DEFAULT_TIMEOUT)
            elif color == Colors.RED:
                expect(
                    self.page.locator(self._RED_INDICATION),
                    "Красная индикация у тоста переноса разметки не отображается",
                ).to_be_visible(timeout=settings.DEFAULT_TIMEOUT)
            else:
                expect(
                    self.page.locator(self._YELLOW_INDICATION),
                    "Жёлтая индикация у тоста переноса разметки не отображается",
                ).to_be_visible(timeout=settings.DEFAULT_TIMEOUT)
        return self

    @allure.step("Кликнуть ComboBox 'Версия' в модальном окне переноса разметки")
    def click_on_combo_box_version_transfer_of_markings(self) -> Self:
        """Кликнуть ComboBox 'Версия' в модальном окне переноса разметки.

        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        locator_combo_box_version = self.page.locator(self._COMBO_BOX_IN_WINDOW_TRANSFER_OF_MARKINGS).last

        with assume:
            expect(locator_combo_box_version, "ComboBox 'Версия' не отображается").to_be_visible(
                timeout=settings.DEFAULT_TIMEOUT
            )
            expect(locator_combo_box_version, "ComboBox 'Версия' недоступен").to_be_enabled()
            locator_combo_box_version.click()
        return self

    @allure.step("Проверить видимость и доступность кнопки с определённым текстом.")
    def check_button_with_text(self, button_text: str) -> Self:
        """Проверить видимость и доступность кнопки с определённым текстом.

        :param button_text: Текст кнопки.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        locator_button = self.page.get_by_role(Roles.BUTTON, name=button_text, exact=True)

        with assume:
            expect(locator_button, f"Кнопка с текстом '{button_text}' не отображается").to_be_visible(
                timeout=settings.DEFAULT_TIMEOUT
            )
            expect(locator_button, f"Кнопка с текстом '{button_text}' недоступна").to_be_enabled()
        return self

    @allure.step("Кликнуть на кнопку с определённым текстом.")
    def click_on_button_with_text(self, button_text: str) -> Self:
        """Кликнуть на кнопку с определённым текстом.

        :param button_text: Текст кнопки.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        self.check_button_with_text(button_text)
        self.page.get_by_role(Roles.BUTTON, name=button_text, exact=True).click()
        return self

    @allure.step("Ввести текст в поле продукт в окне переноса разметки.")
    def fill_in_product_field_in_markup_transfer_window(self, text: str) -> Self:
        """Ввести текст в поле продукт в окне переноса разметки.

        :param text: Текст вводимый в combobox.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        self.page.locator(self._PRODUCT_FIELD_IN_MARKUP_TRANSFER_WINDOW).type(text)
        return self

    @allure.step("Проверить вертикальный скролл в списке элементов в окне переноса разметки.")
    def check_vertical_scrolling(self) -> Self:
        """Проверить вертикальный скролл в списке элементов в окне переноса разметки.

        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        with assume:
            expect(
                self.page.locator(self._ELEMENTS_IN_PRODUCT_FIELD_IN_MARKUP_TRANSFER_WINDOW),
                "Вертикальный скролл в списке элементов в окне переноса разметки не отображается",
            ).to_have_class(RegularExpressions.PATTERN_CLASS_SCROLL_THIN)
        return self

    @allure.step("Проверить элементы списка в поле 'Продукт' или в поле 'Версия' в окне переноса разметки.")
    def check_elements_in_field_in_markup_transfer_window(self, list_elements: list[str]) -> Self:
        """Проверить элементы списка в поле 'Продукт' или в поле 'Версия' в окне переноса разметки.

        :param list_elements: Список элементов.
        :return: Текущий объект страницы 'self' (для цепочки вызовов).
        """
        locator_element = self.page.locator(self._ELEMENT_IN_PRODUCT_FIELD_IN_MARKUP_TRANSFER_WINDOW)

        with assume:
            for i, element in enumerate(list_elements):
                expect(
                    locator_element.nth(i),
                    f"Элемент в строке номер {i + 1} не отображается или значение не соответствует "
                    f"ожидаемому '{element}'",
                ).to_have_text(element, timeout=settings.DEFAULT_TIMEOUT)
        return self
