def is_anagram(first_string: str, second_string: str) -> bool:
    """
    Given two strings, this functions determines if they are an anagram of one another.
    """
    first = sorted(first_string)
    second = sorted(second_string)
    if first == second:
        return True
    else:
        return False
