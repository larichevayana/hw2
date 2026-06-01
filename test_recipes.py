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
import pytest
from recipes import Recipe, Ingredient

def testrsozdanie():
    r = Recipe("Карбонара", [])
    assert r.title == "Карбонара"
    assert r.ingredients == []

def testaddni():
    r = Recipe("Карбонара", [])
    i = Ingredient("Бекон", 200.0, "г")
    r.add_ingredient(i)
    assert len(r) == 1
    assert r.ingredients[0].name == "Бекон"
    assert r.ingredients[0].quantity == 200.0

def testaddsi():
    r = Recipe("Карбонара", [])
    i = Ingredient("Бекон", 150.0, "г")
    ii = Ingredient("Бекон", 50.0, "г")
    r.add_ingredient(i)
    r.add_ingredient(ii)
    assert len(r) == 1
    assert r.ingredients[0].quantity == 200.0

def testscaleno():
    r = Recipe("Карбонара", [])
    r.add_ingredient(Ingredient("Бекон", 200.0, "г"))
    r2 = r.scale(2)
    assert r2 is not r

def testscalekoef():
    r = Recipe("Карбонара", [])
    r.add_ingredient(Ingredient("Бекон", 200.0, "г"))
    r.add_ingredient(Ingredient("Сливки", 100.0, "мл"))
    r2 = r.scale(2)
    for i in r2.ingredients:
        if i.name == "Бекон":
            assert i.quantity == 400.0
        if i.name == "Сливки":
            assert i.quantity == 200.0

def test_scale_invalid_ratio():
    r = Recipe("Карбонара", [])
    r.add_ingredient(Ingredient("Бекон", 200.0, "г"))
    try:
        r.scale(0)
    except ValueError:
        pass
    else:
        assert False, "Исключение не сработало: ratio=0"
    try:
        r.scale(-3)
    except ValueError:
        pass
    else:
        assert False, "Исключение не сработало: ratio=-3"

def test_len():
    r = Recipe("Карбонара", [])
    assert len(r) == 0
    r.add_ingredient(Ingredient("Яйца", 3, "шт"))
    r.add_ingredient(Ingredient("Сливки", 100.0, "г"))
    r.add_ingredient(Ingredient("Бекон", 200.0, "г"))
    assert len(r) == 3
