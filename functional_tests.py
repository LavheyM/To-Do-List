from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # User visits http://localhost:8000/
        self.browser.get('http://localhost:8000')

        # User notices the page title and header mentions To-Do Lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # User is invited to enter a to-do item right away.
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # User types "Buy Peacock Feathers" as an item
        inputbox.send_keys('Buy peacock feathers')

        # When user hits enter, the page updates and now the page Lists
        # "1: Buy peacock feathers" as an item in a to-do list table
        inputbox.send_keys(Keys.ENTER)
        time.sleep(5)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows),
            "New To-Do Item did not appear in the table."
        )

        # There is still a text box inviting the user to add another item.
        # User enters "Use peacock feathers to make a fly"

        self.fail('Finish the Test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
