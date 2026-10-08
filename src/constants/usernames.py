from enum import StrEnum


class Usernames(StrEnum):
    """Константы с ФИО сотрудников."""

    USER_WITH_READ_PERMISSIONS = "Иванов Иван Иванович"
    """Пользователь с правами на чтение."""
    USER_WITH_WRITE_PERMISSIONS = "Иванова Елена Ивановна"
    """Пользователь с правами на запись."""
