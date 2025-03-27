class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self._price = price  # Приватный атрибут
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self._price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        # Проверяем, что складываются объекты одного и того же класса
        if type(self) != type(other):
            raise TypeError("Невозможно сложить объекты разных классов (например, Smartphone и LawnGrass).")

        return self._price * self.quantity + other._price * other.quantity

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Цена должна быть положительным числом")
        self._price = value

    @classmethod
    def new_product(cls, data: dict):
        if not all(key in data for key in ["name", "description", "price", "quantity"]):
            raise ValueError("В данных должны быть ключи: 'name', 'description', 'price', 'quantity'.")
        return cls(
            data["name"],
            data["description"],
            data["price"],
            data["quantity"]
        )
