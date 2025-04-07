from src.models.base_product import BaseProduct
from src.models.mixin import Mixin


class Product(BaseProduct, Mixin):  # Добавляем mixin
    def __init__(self, name: str, description: str, price: float, quantity: int):
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")

        super().__init__(name, description, price, quantity)  # Вызов конструктора родительского класса

        # Добавляем вывод, который будет перехвачен в тестах
        print(
            f"Создан объект Product с параметрами: ('{self.name}', '{self.description}', {self.price}, {self.quantity})")

    def get_product_info(self):
        """Метод для получения информации о продукте."""
        return f"Продукт: {self.name}, Описание: {self.description}, Цена: {self.price} руб., Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Сложение продуктов (стоимости и количества)."""
        if not isinstance(other, Product):
            raise TypeError("Невозможно сложить объекты разных классов (например, Smartphone и LawnGrass).")
        return self.price * self.quantity + other.price * other.quantity

    @property
    def price(self):
        """Геттер для цены."""
        return self._price

    @price.setter
    def price(self, value):
        """Сеттер для цены. Проверяет, что цена положительная."""
        if value <= 0:
            raise ValueError("Цена должна быть положительным числом")
        self._price = value

    @classmethod
    def new_product(cls, data: dict):
        """Метод для создания нового продукта из словаря."""
        if not all(key in data for key in ["name", "description", "price", "quantity"]):
            raise ValueError("В данных должны быть ключи: 'name', 'description', 'price', 'quantity'.")
        return cls(data["name"], data["description"], data["price"], data["quantity"])
