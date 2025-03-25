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
        if isinstance(product, Product):
            self.__products.append(product)
        else:
            raise TypeError("Только объект типа Product может быть добавлен.")

    def __repr__(self):
        return f"{self.name}, количество продуктов: {self.total_quantity} шт."

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)  # Исправлено __products
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    @property
    def total_quantity(self):
        """Считает общее количество товаров (с учетом их количества)"""
        return sum(product.quantity for product in self.__products)
