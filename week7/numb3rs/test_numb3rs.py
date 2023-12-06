from numb3rs import validate


def test_format():
    assert validate(r"1.2.3.4") == True
    assert validate(r"1.1.0") == False
    assert validate(r"1.1") == False
    assert validate(r"1") == False


def test_range():
    assert validate(r"127.0.0.1") == True
    assert validate(r"256.0.0.0") == False
    assert validate(r"0.256.0.0") == False
    assert validate(r"0.0.256.0") == False
    assert validate(r"0.0.0.256") == False