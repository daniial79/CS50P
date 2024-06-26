from project import find
from project import character_is_valid
from project import is_session_finished

def test_find():
    assert find("russia", "s") == [2, 3]
    assert find("russia", "s") != [1, 2]
    
    
def test_character_is_valid():
    assert character_is_valid("@") == False
    assert character_is_valid("ab") == False
    assert character_is_valid("a") == True
    
    
def test_session_finished():
    assert is_session_finished("iran", ["i", "r", "a", "n"]) == True
    assert is_session_finished("russia", ["-", "-", "s", "s", "-", "-"]) == False