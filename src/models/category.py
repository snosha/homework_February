from src.models.product import Product


class Category:
    def __init__(self, name: str, description: str, products: list = None):
        self.name = name
        self.description = description
        self.__products = products if products is not None else []
        # Преобразуем в нормальную длину
        self.product_count = len(self.__products)  # Начальное количество продуктов

    @property
    def products(self):
        return ", ".join([product.name for product in self.__products])

    def add_product(self, product: Product):
        if isinstance(product, Product):  # Проверка типа
            self.__products.append(product)
            self.product_count += 1  # Увеличиваем количество товаров в категории
        else:
            raise TypeError("Только объект типа Product может быть добавлен.")

    def __repr__(self):
        return f"{self.name}, количество продуктов: {self.product_count} шт."

    def __str__(self):
        return f"{self.name}, количество продуктов: {self.product_count} шт."  # Строковое представление категории

