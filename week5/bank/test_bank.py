from bank import value


def test_hello_text():
    assert value("Hello there.") == 0


def test_h_text():
    assert value("How are you brother?") == 20


def test_else_text():
    assert value("something definitely not started with 'hello' or even 'h'") == 100
