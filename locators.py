__author__ = 'ncp'
from selenium.webdriver.common.by import By


class MainPageLocators(object):
    GO_BUTTON = (By.ID, 'submit')
    SUCHEN = (By.ID, 'ctl00_ctl00_SearchBoxTop_bSearch')


class SearchResultsPageLocators(object):
    pass
