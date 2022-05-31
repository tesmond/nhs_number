import re


def is_valid_nhs_number(nhs_number: str, ignore_formatting: bool = False) -> bool:
    # NHS numbers are often formatted xxx xxxx xxxx or xxx-xxx-xxxx
    # ignore_formatting strips this formatting so that spaces and hyphens
    # are removed and xxxxxxxxxx and xxx xxx xxxx versions can pass validation
    if ignore_formatting:
        nhs_number = "".join(c for c in nhs_number if c not in " -")

    if not re.match(r"^\d{10}$", nhs_number):
        return False

    # Step 1
    # Multiply each of the first nine digits by a weighting factor
    check_digit: int = 0
    for i, digit in enumerate(nhs_number):
        # Step 2
        # Add the results of each multiplication together.
        check_digit += int(digit) * (10 - i)

    # Step 3
    # Divide the total by 11 and establish the remainder.
    remainder = check_digit % 11

    # Step 4
    # Subtract the remainder from 11 to give the check digit.
    check_digit = 11 - remainder
    if check_digit == 11:
        check_digit = 0

    # Step 5
    # Check the remainder matches the check digit.
    # If it does not, the NHS NUMBER is invalid.
    if remainder != check_digit:
        return False

    return True