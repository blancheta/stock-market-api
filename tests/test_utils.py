from utils.Order import Order


class TestOrderUtil:

    def test_place_order_good(self):
        output = Order.place_order()
        assert output == {"status": "created"}
