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
