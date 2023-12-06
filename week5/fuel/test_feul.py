from feul import convert, gauge
import pytest


def test_division_err():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_value_err():
    with pytest.raises(ValueError):
        convert("randomstring/anotherrandomstring")


def test_convert():
    assert convert("99/100") == 99
    assert convert("1/100") == 1
    assert convert("3/4") == 75
    assert convert("1/2") == 50


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(75) == "75%"
    assert gauge(50) == "50%"
