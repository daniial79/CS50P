from twttr import shorten


def test_twitter():
    assert shorten("twitter") == "twttr"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("TwItTeR") == "TwtTR"


def test_punctuations():
    punctuations = list(".,:;'\"")

    for punc in punctuations:
        assert shorten(punc) == punc


def test_numbers():
    numbers = list("1234567890")

    for digit in numbers:
        assert shorten(digit) == digit


