class Ingredient:
    def __init__(self, name, quantity, unit):
        self.name = name
        self.quantity = quantity
        self.unit = unit

    @property
    def quantity(self):
        return self.quan

    @quantity.setter
    def quantity(self, quan):
        quan = float(quan)
        if quan <= 0:
            raise ValueError("Количество должно быть положительным")
        self.quan = quan

    def __str__(self):
        return f"{self.name}: {self.quantity} {self.unit}"

    def __repr__(self):
        return f"Ingredient('{self.name}', {self.quantity}, '{self.unit}')"

    def __eq__(self, other):
        if type(other) == Ingredient:
            if self.name == other.name and self.unit == other.unit:
                return True
            else:
                return False
        else:
            return False
class Recipe:
    def __init__(self, title, ingredients):
        self.title = title
        self.ingredients = ingredients

    def add_ingredient(self, ingredient):
        yes = 0
        for i in self.ingredients:
            if i.name == ingredient.name and i.unit == ingredient.unit:
                i.quantity = i.quantity + ingredient.quantity
                yes = 1
        if yes == 0:
            self.ingredients.append(ingredient)

    @staticmethod
    def is_valid_ratio(ratio):
        if ratio > 0:
            if type(ratio) == int or type(ratio) == float:
                return True
            else:
                return False
        else:
            return False

    def scale(self, ratio):
        m = []
        i = 0
        s = len(self.ingredients)
        while i < s:
            x = self.ingredients[i]
            kolvo = x.quantity * ratio
            nx = Ingredient(x.name, kolvo, x.unit)
            m.append(nx)
            i = i + 1
        return Recipe(self.title, m)

    def __len__(self):
        return len(self.ingredients)

    def __str__(self):
        ans = "Рецепт: " + self.title + "\nИнгредиенты:\n"
        for i in self.ingredients:
            ans = ans + "  " + str(i) + "\n"
        return ans
