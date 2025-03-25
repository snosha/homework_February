import pytest
from src.models.product import Product


def test_product_creation():
    """Проверяет создание продукта с корректными параметрами."""
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_product_price_setter():
    """Проверяет, что цена продукта может быть изменена через setter."""
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

    product.price = 200000.0
    assert product.price == 200000.0


def test_product_price_setter_invalid():
    """Проверяет, что установка отрицательной или нулевой цены вызывает ошибку."""
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

    with pytest.raises(ValueError):
        product.price = -1000.0  # Попытка установить отрицательную цену

    with pytest.raises(ValueError):
        product.price = 0.0  # Попытка установить цену 0


def test_product_str():
    """Проверяет строковое представление продукта."""
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    assert str(product) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_product_addition():
    """Проверяет работу оператора сложения продуктов (складывает стоимость всех продуктов)."""
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

    assert product1 + product2 == 180000.0 * 5 + 210000.0 * 8  # Стоимость двух продуктов


def test_new_product():
    """Проверяет создание нового продукта через класс-метод new_product."""
    data = {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
    }
    product = Product.new_product(data)

    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5
