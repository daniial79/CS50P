from plates import is_valid


def test_inappropriate_length():
    assert is_valid("AA") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("C") == False
    assert is_valid("ASDFGHJK") == False


def test_start_with_two_chars():
    assert is_valid("AA") == True
    assert is_valid("A1") == False
    assert is_valid("2A") == False
    assert is_valid("11") == False


def test_digits_at_end():
    assert is_valid("AA123") == True
    assert is_valid("CS50") == True
    assert is_valid("CA15SC") == False


def test_first_digit_is_non_zero():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False


def test_only_alphanumeric():
    assert is_valid("CS>)") == False
    assert is_valid("CS 50") == False