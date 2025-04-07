from src.models.product import Product


class Category:
    def __init__(self, name: str, description: str, products: list = None):
        self.name = name
        self.description = description
        self.__products = products if products is not None else []

    @property
    def products(self):
        return ", ".join([product.name for product in self.__products])

    def add_product(self, product: Product):
        # Проверка, что добавляем только объект типа Product или его наследников
        if not isinstance(product, Product):
            raise TypeError("Только объект типа Product или его наследники могут быть добавлены.")

        self.__products.append(product)

    def __repr__(self):
        return f"{self.name}, количество продуктов: {self.total_quantity} шт."

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    @property
    def total_quantity(self):
        """Считает общее количество товаров (с учетом их количества)"""
        return sum(product.quantity for product in self.__products)

    def __add__(self, other):
        # Магический метод сложения
        if not isinstance(other, Category):
            raise TypeError("Можно сложить только объекты одного класса Category.")

        # Проверка, что обе категории содержат продукты
        if not self.__products or not other.__products:
            raise ValueError("Обе категории должны содержать продукты для выполнения операции сложения.")

        # Проверка, что все продукты в обеих категориях одного класса
        if not all(isinstance(product, type(self.__products[0])) for product in self.__products):
            raise TypeError("Продукты в категории должны быть одного типа.")

        # Суммирование количеств продуктов
        total_quantity = sum(product.quantity for product in self.__products) + sum(
            product.quantity for product in other.__products)
        return total_quantity

    def middle_price(self) -> float:
        """Подсчет средней цены товаров в категории."""
        try:
            total_price = sum(product.price for product in self.__products)
            return total_price / len(self.__products)
        except ZeroDivisionError:
            return 0
