from src.models.category import Category
from src.models.product import Product

def test_add_product():
    product1 = Product("Test Product 1", "Description", 100.0, 10)
    category = Category("Test Category", "Test Description", [product1])

    product2 = Product("Test Product 2", "Description", 200.0, 5)
    category.add_product(product2)

    assert "Test Product 2, 200.0 руб. Остаток: 5 шт." in category.products

def test_products_getter():
    product1 = Product("Test Product 1", "Description", 100.0, 10)
    category = Category("Test Category", "Test Description", [product1])

    expected_output = "Test Product 1, 100.0 руб. Остаток: 10 шт."
    assert category.products == expected_output
