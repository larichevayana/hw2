import pytest
from recipes import Ingredient
def testsozdanie():
    i = Ingredient("Яблоки", 200.0, "г")
    assert i.name == "Яблоки"
    assert i.quantity == 200.0
    assert i.unit == "г"

def teststr():
    i = Ingredient("Мука", 500.0, "г")
    assert str(i) == "Мука: 500.0 г"

def testodinak():
    i = Ingredient("Яблоки", 200.0, "г")
    ii = Ingredient("Яблоки", 300.0, "г")
    assert i == ii

def testraznname():
    i = Ingredient("Яблоки", 300.0, "г")
    ii = Ingredient("Мука", 300.0, "г")
    assert i != ii

def testraznunit():
    i = Ingredient("Яблоки", 1.0, "г")
    ii = Ingredient("Яблоки", 1.0, "кг")
    assert i != ii
