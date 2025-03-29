from abc import ABC, abstractmethod

class BaseProduct(ABC):
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @abstractmethod
    def get_product_info(self):
        """Абстрактный метод для получения информации о продукте."""
        pass

    def __str__(self):
        return f"{self.name}, {self._price} руб. Остаток: {self.quantity} шт."
