# Part 1
def input_postal_code(prompt, *postalcodes):
    while True:
        value = input(prompt)

        if value.casefold() == 'q':
            return None

        try:
            return _check_postalcode(value, postalcodes)
        except ValueError as error:
            print(error)


def _concatenate(postalcodes):
    return ", ".join(str(code) for code in postalcodes)


def _check_postalcode(value, postalcodes):
    try:
        postalcode = int(value)
    except ValueError:
        raise ValueError(f"Please enter a valid postalcode, e.g., {_concatenate(postalcodes)}. Your input '{value}' "
                         f"was not numerical.")

    if postalcode not in postalcodes:
        raise ValueError(f"Please enter a valid postal code, your input {postalcode} is not in the valid postal code "
                         f"list {_concatenate(postalcodes)}")

    return postalcode


# Part 2
def input_bounded_integer(prompt, description, minimum, maximum):
    while True:
        value = input(prompt)

        if value.casefold() == 'q':
            return None

        try:
            return _check_bounded_integer(value, description, minimum, maximum)
        except ValueError as error:
            print(error)




def _check_bounded_integer(value, description, lower, upper):
    try:
        result = int(value)
    except ValueError:
        raise ValueError(f"Please enter {description}. Your input '{value}' was not numerical.")

    if result < lower or result > upper:
        raise ValueError(f"Please enter a valid {description}, your input {result} is not between {lower} and {upper}.")

    return result


def input_string(prompt):
    while True:
        value = input(prompt)

        if value.casefold() == 'q':
            return None

        else:
            return value