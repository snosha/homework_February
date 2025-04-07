import pytest
from src.models.lawn_grass import LawnGrass

@pytest.fixture
def lawn_grass():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", 7, "Зеленый")


def test_lawn_grass_initialization(lawn_grass):
    # Проверка инициализации объекта LawnGrass
    assert lawn_grass.name == "Газонная трава"
    assert lawn_grass.description == "Элитная трава для газона"
    assert lawn_grass.price == 500.0
    assert lawn_grass.quantity == 20
    assert lawn_grass.country == "Россия"
    assert lawn_grass.germination_period == 7
    assert lawn_grass.color == "Зеленый"


def test_lawn_grass_str(lawn_grass):
    # Проверка строкового представления
    assert str(lawn_grass) == "Трава Газонная трава, страна-производитель: Россия, срок прорастания: 7 дней, цвет: Зеленый, 500.0 руб. Остаток: 20 шт."
