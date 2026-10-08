from enum import StrEnum


class RadarAreaValues(StrEnum):
    """Константы значений зоны технического радара."""

    RECOMMENDED = "Рекомендуется"
    PILOTED_BY = "Пилотируется"
    INTERESTED_IN = "Интересует"
    AVOID = "Избегать"
    UNKNOWN = "Неизвестна"
