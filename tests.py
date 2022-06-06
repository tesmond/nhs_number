import pytest
from nhs_number import is_valid_nhs_number


@pytest.mark.parametrize(
    "input,valid,ignore_formatting",
    [
        ("000000000", False, False),
        ("1111111111", True, False),
        ("00000 0000", False, False),
        ("000000000A", False, False),
        ("0000000000", True, False),
        ("0000000001", False, False),
        ("479 748 5957", True, True),
        ("479-748-5957", True, True),
        ("479 748 5957", False, False),
        ("479-748-5957", False, False),
        ("929 863 3734", True, True),
        ("929 863 3735", False, True),
        ("929 863 3734", False, False),
        ("9999999999", True, False),
        ("370 601 7695", True, True),
        ("405 951 4497", True, True),
        ("503 729 2530", True, True),
        ("170 981 2044", True, True),
        ("456 299 4754", True, True),
        ("362 170 3861", True, True),
        ("564 035 8580", True, True),
        ("851 475 7091", True, True),
        ("221 425 4889", True, True),
        ("090 959 4635", True, True),
        ("370 601 7696", False, True),
        ("405 951 4498", False, True),
        ("503 729 2531", False, True),
        ("170 981 2045", False, True),
        ("456 299 4755", False, True),
        ("362 170 3862", False, True),
        ("564 035 8581", False, True),
        ("851 475 7092", False, True),
        ("221 425 4880", False, True),
        ("090 959 4636", False, True),
    ],
)
def test_is_valid_nhs_number(input, valid, ignore_formatting):
    assert is_valid_nhs_number(input, ignore_formatting) == valid
