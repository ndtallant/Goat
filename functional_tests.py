import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        '''Special method that works like try.'''
        self.browser = webdriver.Firefox()

    def tearDown(self):
        '''Special method that works like finally.'''
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Our user goes to the home page
        self.browser.get('http://localhost:8000')

        # They notice the title has to-do list stuff
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # They are invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a to-do item'
        )
        # They type buy peakcock feathers lol
        inputbox.send_keys('Buy peacock feathers')

        # They hit enter, and the page updates
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
                any(row.text == '1: Buy peackock feathers' for row in rows)
        )

        self.fail('Finish the test!')

if __name__ == '__main__':
    # Runs the unittest test runner!
    unittest.main(warnings='ignore')
