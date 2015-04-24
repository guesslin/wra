#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


wra_url = 'http://fhy.wra.gov.tw/ReservoirPage_2011/StorageCapacity.aspx'
save_dir = '/home/guesslin/Downloads'


def define_browser():
    fp = webdriver.FirefoxProfile()
    fp.set_preference("browser.helperApps.neverAsk.saveToDisk",
                      "application/vnd.xls")
    browser = webdriver.Firefox(fp)
    return browser


def write_file(year, month, day, page_source):
    with open(os.path.join(save_dir, '{}-{}-{}.html'.format(year, month, day)),
              'w') as fout:
        fout.write(page_source.encode('utf-8'))


def main():
    browser = define_browser()
    browser.get(wra_url)
    year = sys.argv[1]
    month = sys.argv[2]
    day = sys.argv[3]
    Select(browser.find_element_by_id('cphMain_ucDate_cboYear')
           ).select_by_visible_text(year)
    Select(browser.find_element_by_id('cphMain_ucDate_cboMonth')
           ).select_by_visible_text(month)
    for day in range(int(day), 32):
        try:
            el = WebDriverWait(browser, 10).until(
                ec.presence_of_element_located((By.ID,
                                                'cphMain_ucDate_cboDay'))
            )
        except Exception as e:
            print str(e)
            browser.quit()
            sys.exit(-1)
        else:
            Select(el).select_by_visible_text(str(day))
        try:
            submit = WebDriverWait(browser, 10).until(
                ec.presence_of_element_located((By.ID, 'cphMain_btnQuery'))
            )
        except Exception as e:
            print str(e)
            browser.quit()
            sys.exit(-1)
        else:
            submit.click()
            write_file(year, month, day, browser.page_source)
    browser.quit()

if __name__ == '__main__':
    main()
