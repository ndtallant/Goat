import unittest
from selenium import webdriver

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
        self.fail('Finish the test!')

if __name__ == '__main__':
    # Runs the unittest test runner!
    unittest.main(warnings='ignore')
