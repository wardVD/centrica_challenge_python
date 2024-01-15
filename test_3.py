def first_non_duplicated_character(item: str) -> str:
    """
    Find the first character that is not duplicated in "item".

    >>> first_non_duplicated_character("abcd")
    "a"

    >>> first_non_duplicated_character("aaabcd")
    "b"

    """
    for i in range(len(item)):
        char = item[i]

        duplicate = False
        for j in range(i + 1, len(item)):
            if char == char[j]:
                duplicate = True
                break

        if not duplicate:
            return char

    return None