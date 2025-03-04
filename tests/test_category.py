import pytest
from src.models.product import Product
from src.models.category import Category

def test_add_product():
    """Проверяет, что продукт добавляется в категорию и увеличивает счетчик товаров."""
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    category = Category("Смартфоны", "Смартфоны для людей", [product1])

    initial_count = Category.product_count
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    category.add_product(product2)

    assert Category.product_count == initial_count + 1  # Проверяем, что количество продуктов увеличилось

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
