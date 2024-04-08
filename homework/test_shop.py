import pytest

from homework.models import Product, Cart

@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)

@pytest.fixture
def cart():
    return Cart()

class TestProducts:
    """
    Тестовый класс для класса Product
    """

    def test_product_check_quantity(self, product):
        assert product.check_quantity(500) == True
        assert product.check_quantity(1500) == False

    def test_product_buy(self, product):
        product.buy(500)
        assert product.quantity == 500

    def test_product_buy_more_than_available(self, product):
        with pytest.raises(ValueError):
            product.buy(1500)

class TestCart:
    """
    Тестовый класс для класса Cart
    """

    def test_add_product(self, product, cart):
        cart.add_product(product, 5)
        assert product in cart.products
        assert cart.products[product] == 5

    def test_remove_product(self, product, cart):
        cart.add_product(product, 5)
        cart.remove_product(product, 7)
        assert product not in cart.products.keys()

        cart.add_product(product, 5)
        cart.remove_product(product, 5)
        assert product not in cart.products.keys()

    def test_clear(self, product, cart):
        cart.add_product(product, 5)
        cart.clear()
        assert not cart.products

    def test_get_total_price(self, product, cart):
        cart.add_product(product, 2)
        assert cart.get_total_price() == 200

    def test_buy(self, product, cart):
        cart.add_product(product, 2)
        # Пытаемся купить больше товара, чем есть на складе
        cart.add_product(product, 2000)
        with pytest.raises(ValueError):
            cart.buy()
