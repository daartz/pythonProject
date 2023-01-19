from unittest import TestCase, main

from main import add, divide


class TestCalculatrice(TestCase):
    def test_add(self):
        self.assertEqual(add(5, 10), 15)

    def test_add_with_two_letters(self):
        self.assertEqual(add("a", "b"), "ab")

    def test_add_with_booleans(self):
        self.assertEqual(add(True, False), 1)
        self.assertEqual(add(True, True), 2)
        self.assertEqual(add(False, False), 0)

    # Test si la fonction renvoie bien une erreur
    # > Le test fonctionne bien mais la fonction renvoi une erreur dans ce cas de figure
    def test_add_with_two_none(self):
        with self.assertRaises(TypeError):
            add(None,None)

    def test_divide(self):
        self.assertEqual(divide(50, 10), 5)



