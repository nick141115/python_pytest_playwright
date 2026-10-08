from playwright.sync_api import Page

from src.pages.base_page import BasePage


class ComponentPage(BasePage):
    """Описывает страницу 'Компоненты'."""

    def __init__(self, page: Page) -> None:
        """Инициализация объекта страницы.

        :param page: Объект страницы playwright Page.
        """
        super().__init__(page)
