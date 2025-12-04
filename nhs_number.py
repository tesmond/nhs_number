def is_valid_nhs_number(nhs_number: str, ignore_formatting: bool = False) -> bool:
    # NHS numbers are often formatted xxx xxx xxxx or xxx-xxx-xxxx
    # ignore_formatting strips this formatting so that spaces and hyphens
    # are removed and xxxxxxxxxx and xxx xxx xxxx versions can pass validation
    if ignore_formatting:
        nhs_number = nhs_number.translate(str.maketrans("", "", " -"))

    if not len(nhs_number) == 10 or not nhs_number.isdigit():
        return False

    # Multiply each of the first 9 digits by their weighting factor
    # Add the results of each multiplication together
    # ord is used instead of int for performance reasons
    total: int = 0
    for i in range(9):
        total += (ord(nhs_number[i]) - ord("0")) * (10 - i)

    # Divide the total by 11 and establish the remainder
    remainder: int = total % 11

    # Expected check digit should match last digit in a valid NHS number
    expected_check_digit: int = 0 if remainder == 0 else 11 - remainder
    return expected_check_digit == ord(nhs_number[9]) - ord("0")
