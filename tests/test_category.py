import pytest
from src.models.product import Product
from src.models.category import Category


class ProductMock(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int):
        super().__init__(name, description, price, quantity)


@pytest.fixture
def product1():
    return ProductMock("Product1", "Description1", 100.0, 5)


@pytest.fixture
def product2():
    return ProductMock("Product2", "Description2", 200.0, 10)


@pytest.fixture
def category_with_products(product1, product2):
    category = Category("Category1", "Description1", [product1, product2])
    return category


@pytest.fixture
def empty_category():
    return Category("EmptyCategory", "Description")


def test_add_product(category_with_products, product1):
    # Проверка добавления продукта
    new_product = ProductMock("Product3", "Description3", 150.0, 20)
    category_with_products.add_product(new_product)

    assert len(category_with_products._Category__products) == 3
    assert category_with_products.total_quantity == 35


def test_add_product_invalid_type(category_with_products):
    # Проверка ошибки при добавлении неправильного типа
    with pytest.raises(TypeError):
        category_with_products.add_product("Not a Product")


def test_total_quantity(category_with_products):
    # Проверка правильности вычисления total_quantity
    assert category_with_products.total_quantity == 15


def test_category_representation(category_with_products):
    # Проверка корректности строкового представления
    assert str(category_with_products) == "Category1, количество продуктов: 15 шт."


def test_add_categories(category_with_products, product1, product2):
    # Проверка операции сложения категорий
    category2 = Category("Category2", "Description2", [product1, product2])
    total_quantity = category_with_products + category2

    assert total_quantity == 30  # 15 + 15


def test_add_categories_invalid_type(category_with_products, product1):
    # Проверка ошибки при сложении с некорректным типом
    with pytest.raises(TypeError):
        category_with_products + product1


def test_add_categories_empty_category(category_with_products, empty_category):
    # Проверка ошибки при сложении пустой категории
    with pytest.raises(ValueError):
        category_with_products + empty_category


def test_product_property_access(product1):
    # Проверка доступа к свойствам
    assert product1.name == "Product1"
    assert product1.price == 100.0
    assert product1.quantity == 5
