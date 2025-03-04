from src.models.product import Product
from src.models.category import Category

if __name__ == "__main__":
    # Продукты
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    # Категория "Смартфоны"
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    # Вывод информации о продуктах в категории
    print(category1.products)

    # Добавление нового продукта в категорию
    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)

    # Вывод информации после добавления нового продукта
    print(category1.products)
    print(category1.product_count)

    # Создание нового продукта с помощью метода new_product
    new_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5}
    )

    # Вывод данных нового продукта
    print(new_product.name)
    print(new_product.description)
    print(new_product.price)
    print(new_product.quantity)

    # Изменение цены нового продукта
    new_product.price = 800
    print(new_product.price)

    # Попытка установить некорректную цену с обработкой исключения
    try:
        new_product.price = -100
    except ValueError as e:
        print(f"Ошибка при установке цены: {e}")

    # Попытка установить цену 0
    try:
        new_product.price = 0
    except ValueError as e:
        print(f"Ошибка при установке цены: {e}")

    # Вывод цены после изменения
    print(new_product.price)
