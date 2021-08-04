from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("http://127.0.0.1:8000/")
        self.user = "fake_user"
        self.first_name = "fake_first_name"
        self.last_name = "fake_last_name"
        self.email = "fake_email@email.fr"
        self.password1 = "fake_password1"
        self.password2 = "fake_password1"
        

    def click_on_button(self, name):
        button = self.driver.find_element_by_name(name)
        button.click()

    def click_on_link(self, name):
        link = self.driver.find_element_by_name(name)
        link.click()

    def click_on_link_text(self, text):
        text = self.driver.find_element_by_link_text(text)
        text.click()

    def write_user_text(self, name, user_text):
        element = self.driver.find_element_by_name(name)
        element.clear()
        element.send_keys(user_text)

    def test_result_page_show(self):
        self.driver
        self.assertEqual(
            self.driver.title,
            "Pur Beurre - Plateforme pour amateur de nutella"
        )

    def test_search_top_nutella(self):
        element = self.driver.find_element_by_id("query_top")
        element.clear()
        element.send_keys("nutella")
        element.send_keys(Keys.RETURN)
        self.assertEqual(
            self.driver.current_url,
            "http://127.0.0.1:8000/search_product?query=nutella"
        )

    def test_search_nutella(self):
        element = self.driver.find_element_by_id("query")
        element.clear()
        element.send_keys("nutella")
        element.send_keys(Keys.RETURN)
        self.assertEqual(
            self.driver.current_url,
            "http://127.0.0.1:8000/search_product?query=nutella"
        )

    def test_search_pizza_key_enter(self):
        element = self.driver.find_element_by_id("query")
        element.clear()
        element.send_keys("pizza" + Keys.ENTER)
        self.assertEqual(
            self.driver.current_url,
            "http://127.0.0.1:8000/search_product?query=pizza"
        )

    def test_registrer(self):
        self.click_on_link("login")
        self.assertEqual(
            self.driver.current_url,
            "http://127.0.0.1:8000/accounts/login/"
        )
        self.click_on_link_text("Pas encore inscrit?")
        self.assertEqual(
            self.driver.current_url,
            "http://127.0.0.1:8000/registrer"
        )
        self.write_user_text("username", self.user)
        self.write_user_text("first_name", self.first_name)
        self.write_user_text("last_name", self.last_name)
        self.write_user_text("email", self.email)
        self.write_user_text("password1", self.password1)
        self.write_user_text("password2", self.password2)
        self.click_on_button("submit_form")
        #errorlist = user already exists
        self.assertTrue(self.driver.find_element_by_class_name("errorlist"))

    def test_select_product_and_save(self):
        self.driver.get("http://127.0.0.1:8000/substitute?query=3017620402678")
        self.click_on_link_text("Se connecter")
        self.assertEqual(
            self.driver.current_url,
            "http://127.0.0.1:8000/accounts/login/?next=/substitute?query=3017620402678"
        )
        self.write_user_text("username", self.user)
        self.write_user_text("password", self.password1)
        self.click_on_button("validate")
        self.assertEqual(
            self.driver.current_url,
            "http://127.0.0.1:8000/substitute?query=3017620402678"
        )
        self.click_on_link_text("Sauvegarder")
        self.assertEqual(
            self.driver.current_url,
            "http://127.0.0.1:8000/product_save?substitute=3175681854482"
        )

    def test_myprofile(self):
        self.click_on_link("login")
        self.assertEqual(
            self.driver.current_url,
            "http://127.0.0.1:8000/accounts/login/"
        )
        self.write_user_text("username", self.user)
        self.write_user_text("password", self.password1)
        self.click_on_button("validate")
        self.assertEqual(
            self.driver.current_url,
            "http://127.0.0.1:8000/"
        )
        self.click_on_link("myprofile")
        self.assertEqual(
            self.driver.current_url,
            "http://127.0.0.1:8000/myprofile"
        )

    def test_myfood(self):
        self.click_on_link("login")
        self.assertEqual(
            self.driver.current_url,
            "http://127.0.0.1:8000/accounts/login/"
        )
        self.write_user_text("username", self.user)
        self.write_user_text("password", self.password1)
        self.click_on_button("validate")
        self.assertEqual(
            self.driver.current_url,
            "http://127.0.0.1:8000/"
        )
        self.click_on_link("myfood")
        self.assertEqual(
            self.driver.current_url,
            "http://127.0.0.1:8000/myfood"
        )



    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()


