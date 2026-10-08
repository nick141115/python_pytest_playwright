from enum import StrEnum


class AgreementValues(StrEnum):
    """Константы значений согласования."""

    DEVIATION_IS_AGREED = "Отклонение согласовано"
    CHOICE_IS_AGREED = "Выбор согласован"
    CHOICE_IS_NOT_AGREED_UPON = "Выбор не согласован"
    DEVIATION_IS_NOT_AGREED_UPON = "Отклонение не согласовано"
    NOT_REQUIRED = "Не требуется"
