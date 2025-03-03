from src.models.product import Product

def test_new_product():
    data = {"name": "Test Product", "description": "Test Desc", "price": 100.0, "quantity": 10}
    product = Product.new_product(data)

    assert product.name == "Test Product"
    assert product.price == 100.0
    assert product.quantity == 10

def test_price_setter():
    product = Product("Test Product", "Description", 100.0, 10)

    product.price = 50.0
    assert product.price == 50.0

    product.price = -10.0  # Ошибка, цена не должна измениться
    assert product.price == 50.0
