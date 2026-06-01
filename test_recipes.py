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
import pytest
from recipes import Ingredient, Recipe, ShoppingList

def testadd_recipe():
    s = ShoppingList()
    r = Recipe("Карбонара", [])
    r.add_ingredient(Ingredient("Бекон", 200.0, "г"))
    s.add_recipe(r, 2)
    assert len(s.items) == 1
    i = s.items[0][0]
    assert i.quantity == 400.0

def testadd_recipee():
    s = ShoppingList()
    r = Recipe("Карбонара", [])
    try:
        s.add_recipe(r, 0)
        assert False, "Исключение не сработало при 0"
    except ValueError:
        pass
    try:
        s.add_recipe(r, -3)
        assert False, "Исключение не сработало при -3"
    except ValueError:
        pass

def testudalit():
    s = ShoppingList()
    r = Recipe("Карбонара", [])
    r.add_ingredient(Ingredient("Бекон", 200.0, "г"))
    rr = Recipe("Салат", [])
    rr.add_ingredient(Ingredient("Помидор", 300.0, "г"))
    s.add_recipe(r, 1)
    s.add_recipe(rr, 1)
    s.remove_recipe("Карбонара")
    assert len(s.items) == 1
    assert s.items[0][1] == "Салат"

def testudalit_not():
    s = ShoppingList()
    r = Recipe("Карбонара", [])
    r.add_ingredient(Ingredient("Бекон", 200.0, "г"))
    s.add_recipe(r, 1)
    s.remove_recipe("Салат")
    assert len(s.items) == 1

def testsum():
    s = ShoppingList()
    r = Recipe("Карбонара", [])
    r.add_ingredient(Ingredient("Масло", 200.0, "г"))
    rr = Recipe("Салат", [])
    rr.add_ingredient(Ingredient("Масло", 50.0, "г"))
    s.add_recipe(r, 1)
    s.add_recipe(rr, 1)
    m = s.get_list()
    assert len(m) == 1
    assert m[0].name == "Масло"
    assert m[0].quantity == 250.0

def test_get_lists():
    s = ShoppingList()
    r = Recipe("Карбонара", [])
    r.add_ingredient(Ingredient("Бекон", 200.0, "г"))
    r.add_ingredient(Ingredient("Яйца", 3, "шт"))
    r.add_ingredient(Ingredient("Сливки", 100.0, "г"))
    s.add_recipe(r, 1)
    m = s.get_list()
    ans = [i.name for i in m]
    assert ans == ["Бекон", "Сливки", "Яйца"]

def test_add():
    s = ShoppingList()
    r = Recipe("Карбонара", [])
    r.add_ingredient(Ingredient("Бекон", 200.0, "г"))
    s.add_recipe(r, 1)
    ss = ShoppingList()
    rr = Recipe("Салат", [])
    rr.add_ingredient(Ingredient("Морковь", 100.0, "г"))
    ss.add_recipe(rr, 1)
    s3 = s + ss
    assert len(s3.items) == 2
    assert len(s.items) == 1
    assert len(ss.items) == 1
