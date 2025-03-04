from src.models.product import Product


class Category:
    product_count = 0  # Статическая переменная для отслеживания количества продуктов

    def __init__(self, name: str, description: str, products: list = None):
        self.name = name
        self.description = description
        self.__products = products if products is not None else []
        for product in self.__products:
            if isinstance(product, Product):
                Category.product_count += 1  # Увеличиваем счетчик при добавлении продукта

    @property
    def products(self):
        return ", ".join([product.name for product in self.__products])

    def add_product(self, product: Product):
        if isinstance(product, Product):  # Проверка типа
            self.__products.append(product)
            Category.product_count += 1  # Увеличиваем количество товаров в категории
        else:
            raise TypeError("Только объект типа Product может быть добавлен.")

    def __repr__(self):
        return f"Category(name={self.name}, description={self.description}, products={self.products})"
