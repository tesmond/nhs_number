import re


def is_valid_nhs_number(nhs_number: str, ignore_formatting: bool = False) -> bool:
    # NHS numbers are often formatted xxx xxxx xxxx or xxx-xxx-xxxx
    # ignore_formatting strips this formatting so that spaces and hyphens
    # are removed and xxxxxxxxxx and xxx xxx xxxx versions can pass validation
    if ignore_formatting:
        nhs_number = "".join(c for c in nhs_number if c not in " -")

    if not re.match(r"^\d{10}$", nhs_number):
        return False

    # Multiply each of the first 9 digits by their weighting factor
    # Add the results of each multiplication together
    total: int = sum(int(nhs_number[i]) * (10 - i) for i in range(9))

    # Divide the total by 11 and establish the remainder
    remainder: int = total % 11

    # Expected check digit should match last digit in a valid NHS number
    expected_check_digit: int = 0 if remainder == 0 else 11 - remainder
    return expected_check_digit == int(nhs_number[9])
