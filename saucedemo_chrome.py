__author__ = 'P Rayudu Pasumarthi'

from selenium import webdriver
from selenium.webdriver.support.select import Select
import time


class SauceDemo():
    def test_login(self):
        baseUrl = "https://www.saucedemo.com/"
        # Instantiates the Driver
        self.driver = webdriver.Chrome()
        # Implicit 10 seconds waiting for elements to load
        self.driver.implicitly_wait(10)
        # Load base URL https://www.saucedemo.com/
        self.driver.get(baseUrl)
        # Finding userName element node to input user name.
        self.driver.find_element_by_xpath("//input[@id='user-name']").click()
        self.driver.find_element_by_xpath("//input[@id='user-name']").send_keys("standard_user")
        # Finding password element node to input password.
        self.driver.find_element_by_xpath("//input[@id='password']").click()
        self.driver.find_element_by_xpath("//input[@id='password']").send_keys("secret_sauce")
        # Finding login element node to click login button
        self.driver.find_element_by_xpath("//input[@id='login-button']").click()

    def test_sort(self):
        self.driver.find_element_by_xpath("//select[@class='product_sort_container']").click()
        sort_by = Select(self.driver.find_element_by_xpath("//select[@class='product_sort_container']"))
        sort_by.select_by_visible_text('Price (low to high)')

    def test_add2cart(self):
        # get the list of all inventory items
        inventory_items = self.driver.find_elements_by_xpath("//div[@class='inventory_item_name']")
        shopping_cart = 0    # Initialising shopping cart item count to Zero
        count = 1
        updated_shopping_cart_items = 0
        if len(inventory_items) > 0:
            for item in inventory_items:
                # prepare button ID dynamically, so that it can be used for any items
                button_id = 'add-to-cart-' + '-'.join(item.text.lower().split(' '))
                button_xpath = "//button[@id='" + button_id + "']"
                # find add to cart button for this particular item element and click
                self.driver.find_element_by_xpath(button_xpath).click()
                time.sleep(1)
                # read the updated cart count and compare to check the item is really added or not
                updated_shopping_cart_items = self.driver.find_element_by_xpath("//span[@class='shopping_cart_badge']").text
                if int(shopping_cart) + count == int(updated_shopping_cart_items):
                    print("{} item has been added to shopping cart successfully.".format(item.text))
                else:
                    print("Failed to add {} item to shopping cart.".format(item.text))
                count += 1
            # Finally do an extra check that updated cart count is matching with actual targeted inventory size.
            if len(inventory_items) == int(updated_shopping_cart_items):
                print("Test Case PASS.")
        else:
            print("No items found in the inventory")

    def test_teardown(self):
        self.driver.quit()


if __name__ == '__main__':
    SD = SauceDemo()
    try:
        SD.test_login()
        time.sleep(2)
        SD.test_sort()
        time.sleep(2)
        SD.test_add2cart()
        time.sleep(5)
        SD.test_teardown()
    except Exception as Error:
        print("Exception Occurred while testing the SauceDemo. Error is: {}".format(Error))

