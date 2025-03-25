import pytest
from src.models.product import Product
from src.models.category import Category


def test_add_product():
    """Проверяет, что продукт добавляется в категорию и увеличивает количество товаров."""
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    category = Category("Смартфоны", "Смартфоны для людей", [product1])

    initial_count = category.total_quantity  # Используем новый метод
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    category.add_product(product2)

    assert category.total_quantity == initial_count + 8  # Проверяем, что общее количество товаров увеличилось


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
    """Проверяет строковое представление категории с учетом общего количества товаров."""
    products = [
        Product("Телефон A", "Описание A", 50000, 3),
        Product("Телефон B", "Описание B", 60000, 10)
    ]
    category = Category("Смартфоны", "Смартфоны для людей", products)

    assert str(category) == "Смартфоны, количество продуктов: 13 шт."  # 3 + 10


def test_category_repr():
    """Проверяет строковое представление категории через repr()."""
    products = [
        Product("Телефон X", "Описание X", 70000, 4),
        Product("Телефон Y", "Описание Y", 80000, 6)
    ]
    category = Category("Гаджеты", "Современные гаджеты", products)

    assert repr(category) == "Гаджеты, количество продуктов: 10 шт."  # 4 + 6


def test_total_quantity():
    """Проверяет, что метод total_quantity корректно считает количество товаров."""
    products = [
        Product("Гаджет A", "Описание A", 50000, 2),
        Product("Гаджет B", "Описание B", 60000, 5)
    ]
    category = Category("Гаджеты", "Разные гаджеты", products)

    assert category.total_quantity == 7  # 2 + 5
