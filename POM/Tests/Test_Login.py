
from POM.Pages import Login_Page
class Test_Login:

    def test_login(self,driver):
        login_page =Login_Page(driver)

        login_page.