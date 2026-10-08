import re
from typing import Final


class RegularExpressions:
    """Константы регулярных выражений."""

    PATTERN_STRING_TIME: Final = re.compile(r"(?:[01]\d|2[0-3]):[0-5]\d")
    PATTERN_WINDOWS: Final = re.compile(r"Windows")
    PATTERN_CLASS_SCROLL_THIN: Final = re.compile(r"scrollThin")
