import pytest
from src.models.smartphone import Smartphone

@pytest.fixture
def smartphone():
    return Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый")


def test_smartphone_initialization(smartphone):
    # Проверка инициализации объекта Smartphone
    assert smartphone.name == "Samsung Galaxy S23 Ultra"
    assert smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone.price == 180000.0
    assert smartphone.quantity == 5
    assert smartphone.efficiency == 95.5
    assert smartphone.model == "S23 Ultra"
    assert smartphone.memory == 256
    assert smartphone.color == "Серый"


def test_smartphone_str(smartphone):
    # Проверка строкового представления
    assert str(smartphone) == "Смартфон Samsung Galaxy S23 Ultra, модель S23 Ultra, эффективность: 95.5, память: 256ГБ, цвет: Серый, 180000.0 руб. Остаток: 5 шт."
