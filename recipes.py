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
        if not self.is_valid_ratio(ratio):
            raise ValueError("Значение коэффициента должно быть положительным")
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
class ShoppingList:
    def __init__(self):
        self.items = []

    def add_recipe(self, recipe, portions):
        if portions <= 0:
            raise ValueError("Количество порций должно быть положительным")
        recipevpor = recipe.scale(portions)
        ingr = recipevpor.ingredients
        for i in ingr:
            self.items.append((i, recipe.title))

    def remove_recipe(self, title):
        m = []
        for i in self.items:
            if i[1] != title:
                m.append(i)
        self.items = m

    def get_list(self):
        s = {}
        for i, j in self.items:
            k = (i.name, i.unit)
            if k in s:
                s[k] = s[k] + i.quantity
            else:
                s[k] = i.quantity
        ans = []
        for (name, unit), quantity in s.items():
            x = Ingredient(name, quantity, unit)
            ans.append(x)
        m = len(ans)
        for i in range(m):
            for k in range(m - i - 1):
                if ans[k].name > ans[k + 1].name:
                    ans[k], ans[k + 1] = ans[k + 1], ans[k]
        return ans

    def __add__(self, other):
        m = ShoppingList()
        m.items = self.items + other.items
        return m
class DietaryRecipe(Recipe):
    def __init__(self, title, diet_type, ingredients):
        super().__init__(title, ingredients)
        self.diet_type = diet_type

    def scale(self, ratio):
        x = super().scale(ratio)
        return DietaryRecipe(x.title, self.diet_type, x.ingredients)

    def __str__(self):
        ans = "[" + self.diet_type + "] " + self.title + "\nИнгредиенты:\n"
        for i in self.ingredients:
            ans = ans + "  " + str(i) + "\n"
        return ans
