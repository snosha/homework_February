from src.models.product import Product

class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product):
        """Добавляет товар в категорию и увеличивает счетчик товаров."""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """Возвращает список товаров в виде строк."""
        return "\n".join(
            [f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт." for p in self.__products]
        )
