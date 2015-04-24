#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver


wra_url = 'http://fhy.wra.gov.tw/ReservoirPage_2011/StorageCapacity.aspx'


def define_browser(url):
    fp = webdriver.FirefoxProfile()
    fp.set_preference("browser.helperApps.neverAsk.saveToDisk",
                      "application/vnd.xls")
    browser = webdriver.Firefox(fp)
    browser.get(url)
    return browser


def select_dropdown_option(driver, select_locator, option_text):
    for option in driver.find_elements_by_tag_name(select_locator):
        if option.text == option_text.encode('utf-8'):
            option.click()
            break


def main():
    browser = define_browser(wra_url)
    query_method = browser.find_element_by_id('cphMain_cboSearch')
    select_dropdown_option(query_method, 'option', u'所有水庫')

    query_year = browser.find_element_by_id('cphMain_ucDate_cboYear')
    select_dropdown_option(query_year, 'option', '2009')

    query_month = browser.find_element_by_id('cphMain_ucDate_cboMonth')
    select_dropdown_option(query_month, 'option', '11')

    query_day = browser.find_element_by_id('cphMain_ucDate_cboDay')
    select_dropdown_option(query_day, 'option', '28')
    excel_download = browser.find_element_by_id('cphMain_btnExcel')
    excel_download.click()

if __name__ == '__main__':
    main()
