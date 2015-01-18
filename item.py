__author__ = 'ncp'


class GoodsItem(object):
    def __init__(self, driver):
        self.driver = driver

    def find_item(self):
        elem = self.driver.find_element_by_id('ctl00_Main_ProductListControl_repProdGal_ctl01_ProductControlGrid_priceLabel_litPrice')
        return elem.text
