import pytest

from main import add, divide


# Préfixer les fonctions avec le mot test

def test_add():
    assert add(5, 10) == 15


def test_add_with_two_letters():
    assert add("a", "b") == "ab"


def test_add_with_booleans():
    assert add(True, False) == 1
    assert add(True, True) == 2
    assert add(False, False) == 0


# Test si la fonction renvoie bien une erreur
# > Le test fonctionne bien mais la fonction renvoi une erreur dans ce cas de figure
def test_add_with_two_none():
    with pytest.raises(TypeError):
        add(None, None)


def test_divide():
    assert divide(50, 10) == 5
