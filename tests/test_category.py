import pytest
from src.models.product import Product
from src.models.category import Category


def test_add_product():
    """Проверяет, что продукт добавляется в категорию и увеличивает счетчик товаров."""
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    category = Category("Смартфоны", "Смартфоны для людей", [product1])

    initial_count = category.product_count  # Используем атрибут, а не свойство
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    category.add_product(product2)

    assert category.product_count == initial_count + 1  # Проверяем, что количество продуктов увеличилось


def test_add_invalid_product():
    """Проверяет, что при попытке добавить не продукт (например, строку), возникает ошибка."""
    category = Category("Смартфоны", "Смартфоны для людей")
    with pytest.raises(TypeError):
        category.add_product("Not a product")  # Пытаемся добавить строку вместо продукта


def test_product_output():
    """Проверяет, что метод products правильно возвращает строку с названиями продуктов."""
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    category = Category("Смартфоны", "Смартфоны для людей", [product1, product2])

    assert category.products == "Samsung Galaxy S23 Ultra, Iphone 15"  # Проверяем строковое представление продуктов


def test_category_str():
    """Проверяет строковое представление категории."""
    products = [Product(f"Product {i}", f"Описание {i}", 100.0, 1) for i in range(1, 14)]  # 13 продуктов
    category = Category("Смартфоны", "Смартфоны для людей", products)

    # Проверяем, что строковое представление категории включает количество продуктов
    assert str(category) == "Смартфоны, количество продуктов: 13 шт."


def test_product_addition():
    """Проверяет магический метод сложения для продуктов."""
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

    # Проверяем, что сложение продуктов возвращает правильную сумму стоимости
    assert product1 + product2 == 2580000.0  # 180000 * 5 + 210000 * 8 = 2580000


def test_product_str():
    """Проверяет строковое представление продукта."""
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

    # Проверяем, что строковое представление продукта возвращает правильную строку
    assert str(product1) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_product_price_setter():
    """Проверяет установку цены у продукта и обработку ошибок."""
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

    # Проверяем, что цена устанавливается правильно
    product1.price = 200000.0
    assert product1.price == 200000.0

    # Проверяем, что при установке отрицательной цены возникает ошибка
    with pytest.raises(ValueError):
        product1.price = -100

    # Проверяем, что при установке нулевой цены возникает ошибка
    with pytest.raises(ValueError):
        product1.price = 0
