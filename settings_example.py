from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    """Константы базовых настроек."""

    LOGIN: str = ""
    """Логин для авторизации."""
    PASSWORD: str = ""
    """Пароль для авторизации."""
    URL: str = ""
    """URL сервиса."""
    IGNORE_HTTPS_ERRORS: bool = True
    """Игнорировать любые ошибки SSL-сертификатов при посещении веб-сайтов."""
    SCREENSHOTS: bool = True
    """Делать снимки экрана при выполнении автотестов."""
    SNAPSHOTS: bool = True
    """Сохранять полные слепки состояния DOM (HTML и CSS) для каждого действия."""
    SOURCES: bool = True
    """Включить исходный код автотестов в файл трассировки."""
    INIT_SCRIPT: str = ";"
    """JavaScript-код, который будет выполняться до встроенных скриптов сайта и до загрузки самой страницы."""
    DEFAULT_TIMEOUT: int = 15_000
    """Таймаут для всех действий по умолчанию."""


settings = Settings()
