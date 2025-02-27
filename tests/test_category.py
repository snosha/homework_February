import pytest
from src.models.category import Category
from src.models.product import Product

def test_category_init():
    product1 = Product("Test Product 1", "Description", 100.0, 10)
    product2 = Product("Test Product 2", "Description", 200.0, 5)
    category = Category("Test Category", "Test Description", [product1, product2])

    assert category.name == "Test Category"
    assert category.description == "Test Description"
    assert len(category.products) == 2

def test_category_counts():
    Category.category_count = 0
    Category.product_count = 0

    product1 = Product("Test Product 1", "Description", 100.0, 10)
    product2 = Product("Test Product 2", "Description", 200.0, 5)
    category = Category("Test Category", "Test Description", [product1, product2])

    assert Category.category_count == 1
    assert Category.product_count == 2
