__author__ = 'ncp'
import unittest
from selenium import webdriver
import page
import item


test_url = 'http://www.rossmannversand.de'
test_item = 'altapharma'


class GoodsWatch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        #self.driver.get('http://www.rossmannversand.de')
        self.driver.get(test_url)

    def test_search_in_test_url(self):
        main_page = page.MainPage(self.driver)
        #assert main_page.is_title_matches(), "python.org title doesn't match"
        main_page.search_text_element = test_item
        main_page.click_suchen()
        search_results_page = page.SearchResultsPage(self.driver)
        assert search_results_page.is_results_found(), "No results found."
        find_item = item.GoodsItem(self.driver)
        print find_item.find_item()

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
