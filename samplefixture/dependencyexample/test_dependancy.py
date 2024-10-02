import pytest
class Test_dependency:
    @pytest.mark.dependency()
    def test_testcase1(self):
        print("this  is testcase 1")
        assert 2==3


    @pytest.mark.dependency(depends=["Test_dependency::test_testcase1"])
    def test_testcase2(self):
        print("this is testcase  2")

class Test_Depend:
    @pytest.mark.dependency(depends=["Test_dependency::test_testcase1"])
    def test_testcase3(self):
        print("this is testcase 3")
