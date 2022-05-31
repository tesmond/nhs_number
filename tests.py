import pytest
from nhs_number import is_valid_nhs_number


@pytest.mark.parametrize(
    "input,valid,ignore_formatting",
    [
        ("000000000", False, False),
        ("00000 0000", False, False),
        ("000000000A", False, False),
        ("0000000000", True, False),
        ("0000000001", False, False),
        ("479 748 5957", True, True),
        ("479-748-5957", True, True),
        ("479 748 5957", False, False),
        ("479-748-5957", False, False),
        ("929 863 3734", True, True),
        ("929 863 3734", False, False),
        ("9999999999", True, False),
    ],
)
def test_is_valid_nhs_number(input, valid, ignore_formatting):
    assert is_valid_nhs_number(input, ignore_formatting) == valid
