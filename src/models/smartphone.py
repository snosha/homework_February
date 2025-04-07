from src.models.product import Product


class Smartphone(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int, efficiency: float, model: str, memory: int, color: str):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self):
        return f"Смартфон {self.name}, модель {self.model}, эффективность: {self.efficiency:.1f}, память: {self.memory}ГБ, цвет: {self.color}, {self.price} руб. Остаток: {self.quantity} шт."
