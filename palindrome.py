def is_palindrome(value: str) -> bool:
    revstring = value[::-1]
    if value.replace(" ", "").lower() == revstring.replace(" ", "").lower():
        return True
    else:
        return False
