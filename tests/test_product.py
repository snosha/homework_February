import pytest
from src.models.product import Product

# Тестирование класса Product

@pytest.fixture
def product():
    return Product("Product1", "Description1", 100.0, 10)


def test_product_initialization(product):
    # Проверка инициализации объекта Product
    assert product.name == "Product1"
    assert product.description == "Description1"
    assert product.price == 100.0
    assert product.quantity == 10


def test_product_str(product):
    # Проверка строкового представления
    assert str(product) == "Product1, 100.0 руб. Остаток: 10 шт."


def test_product_addition_same_class(product):
    # Проверка правильности сложения объектов одного класса
    other_product = Product("Product2", "Description2", 200.0, 5)
    result = product + other_product
    assert result == 2000.0  # 100.0 * 10 + 200.0 * 5


def test_product_addition_different_class(product):
    # Проверка ошибки при сложении объектов разных классов
    with pytest.raises(TypeError):
        product + "Not a Product"


def test_product_price_setter(product):
    # Проверка правильности сеттера для цены
    product.price = 150.0
    assert product.price == 150.0

    # Проверка ошибки при установке отрицательной цены
    with pytest.raises(ValueError):
        product.price = -50.0


def test_product_new_product_valid_data():
    # Проверка корректного создания нового продукта из словаря
    data = {
        "name": "Product3",
        "description": "Description3",
        "price": 300.0,
        "quantity": 20
    }
    new_product = Product.new_product(data)
    assert isinstance(new_product, Product)
    assert new_product.name == "Product3"
    assert new_product.description == "Description3"
    assert new_product.price == 300.0
    assert new_product.quantity == 20


def test_product_new_product_invalid_data():
    # Проверка ошибки, если в словаре нет обязательных ключей
    data = {
        "name": "Product4",
        "description": "Description4",
        "price": 400.0
    }
    with pytest.raises(ValueError):
        Product.new_product(data)


def test_product_price_getter(product):
    # Проверка геттера для цены
    assert product.price == 100.0
