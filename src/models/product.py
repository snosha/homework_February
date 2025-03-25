class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self._price = price  # Приватный атрибут
        self.quantity = quantity

    def __str__(self):
        # Строковое представление товара
        return f"{self.name}, {self._price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        # Магический метод сложения
        if not isinstance(other, Product):
            raise TypeError("Складывать можно только объекты класса Product")
        return self._price * self.quantity + other._price * other.quantity

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        # Установим цену, проверяя, что она положительная
        if value <= 0:
            raise ValueError("Цена должна быть положительным числом")
        self._price = value

    @classmethod
    def new_product(cls, data: dict):
        # Класс-метод для создания нового продукта из словаря
        return cls(
            data["name"],
            data["description"],
            data["price"],
            data["quantity"]
        )

