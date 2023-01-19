from bank import Account
import pytest


@pytest.fixture
def account():
    return Account(1000)


# Le nom de la fonction en fixture passe en paramètre
def test_deposit(account):
    account.deposit(amount=1000)
    assert account.balance == 2000


def test_withdraw(account):
    account.withdraw(amount=1000)
    assert account.balance == 0


# Faire un test spécifique pour détecter l'erreur
def test_withdraw_no_money():
    account = Account(200)
    with pytest.raises(ValueError):
        account.withdraw(500)


def test__create_identifier_length(account):
    assert len(account.identifier) == 25


def test__create_identifier_isalnum(account):
    assert account.identifier.isalnum() is True
