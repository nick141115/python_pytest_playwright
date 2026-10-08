from src.constants.agreement_values import AgreementValues
from src.constants.components import Components
from src.constants.radar_area_values import RadarAreaValues
from src.constants.ui_text_elements import UITextElements
from typing import Final


class Lists:
    """Константы списков."""

    TITLES_TABLE_CONSUMER_PRODUCTS: Final = [UITextElements.PRODUCT, UITextElements.TEXT_VERSION]

    TITLES_TABLE_COMPONENT_COMPOSITION: Final = [
        " ",
        UITextElements.COMPONENT,
        UITextElements.TECHNICAL_RADAR_AREA,
        UITextElements.TEXT_PACKAGE,
        UITextElements.SECURITY_FUNCTION,
        UITextElements.JUSTIFICATION_COMMENT,
        UITextElements.ATTACK_SURFACE,
        UITextElements.JUSTIFICATION_COMMENT,
    ]

    VALUES_BASH: Final = [
        " ",
        Components.BASH,
        RadarAreaValues.RECOMMENDED,
        AgreementValues.NOT_REQUIRED,
        "",
    ]

    VALUES_ACPID: Final = [
        " ",
        Components.ACPID,
        RadarAreaValues.UNKNOWN,
        AgreementValues.CHOICE_IS_AGREED,
        UITextElements.TEXT_JUSTIFICATION,
    ]

    VALUES_ACCORDSDK: Final = [
        " ",
        Components.ACCORDSDK,
        RadarAreaValues.UNKNOWN,
        AgreementValues.CHOICE_IS_NOT_AGREED_UPON,
        "",
    ]

    VALUES_CRYPT_CPU_FEATURES: Final = [
        " ",
        Components.CRYPT_CPU_FEATURES,
        RadarAreaValues.AVOID,
        AgreementValues.DEVIATION_IS_AGREED,
        UITextElements.TEXT_JUSTIFICATION,
    ]

    VALUES_CRYPTO_UNDERGROUND_V2: Final = [
        " ",
        Components.CRYPTO_UNDERGROUND_V2,
        RadarAreaValues.AVOID,
        AgreementValues.DEVIATION_IS_NOT_AGREED_UPON,
        "",
    ]
