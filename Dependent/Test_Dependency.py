import pytest
class Test_Dependency:
    @pytest.mark.dependency()
    # def test_testcae1(self):
    #     print("this is testcase1")
    #     assert False
    #
    # @pytest.mark.dependency(depends=['Test_Dependency::test_testcae1'])
    # def test_testcae2(self):
    #     print("this is testcase2")

    @pytest.mark.dependency()
    def test_add_product_to_cart(self):
        assert False
        print('product is added into cart successfully')


class Test_BuyProduct:

    @pytest.mark.dependency(depends=['Test_Dependency::test_add_product_to_cart'])
    def test_buy_product(self):
        print('product is ready to shipment')
