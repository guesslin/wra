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
        if option.text == option_text:
            option.click()
            break


def small_month(month):
    if month == 2 or month == 4 or month == 6 or month == 9 or month == 11:
        return True
    return False


def main():
    browser = define_browser(wra_url)
    """
    query_method = browser.find_element_by_id('cphMain_cboSearch')
    select_dropdown_option(query_method, 'option', u'所有水庫')
    """
    for year in range(2003, 2015):
        query_year = browser.find_element_by_id('cphMain_ucDate_cboYear')
        select_dropdown_option(query_year, 'option', str(year))
        for month in range(1, 13):
            query_month = browser.find_element_by_id('cphMain_ucDate_cboMonth')
            select_dropdown_option(query_month, 'option', str(month))
            for day in range(1, 32):
                query_day = browser.find_element_by_id('cphMain_ucDate_cboDay')
                select_dropdown_option(query_day, 'option', str(day))

                excel_download = browser.find_element_by_id('cphMain_btnExcel')
                excel_download.click()

    for month in range(1, 5):
        query_month = browser.find_element_by_id('cphMain_ucDate_cboMonth')
        select_dropdown_option(query_month, 'option', str(month))
        for day in range(1, 32):
            query_day = browser.find_element_by_id('cphMain_ucDate_cboDay')
            select_dropdown_option(query_day, 'option', str(day))

            excel_download = browser.find_element_by_id('cphMain_btnExcel')
            excel_download.click()


if __name__ == '__main__':
    main()
