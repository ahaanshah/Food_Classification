from selenium import webdriver
import time
import urllib.request
import os
from selenium.webdriver.common.keys import Keys

categories = ['banana', 'burger', 'butter_chicken', 'chocolate_cake', 'dal', 'donut', 'dosa', 'fish_curry', 'fried_rice', 'hakka_noodles', 'icecream', 'idli', 'naan', 'paratha', 'penne_alfredo', 'pesto_pasta', 'pizza', 'salad', 'tacos', 'waffles']

path = os.getcwd() + '\\selenium_pictures'

for category in categories:
    browser = webdriver.Chrome('C:\\path\\to\\chromedrive.exe')
    browser.get("https://www.google.com/")

    search = browser.find_element_by_name('q')
    search.send_keys(category, Keys.ENTER)  # "" contains the  query

    elem = browser.find_element_by_link_text('Images')
    elem.get_attribute('href')
    elem.click()

    value = 0
    for i in range(20):
        browser.execute_script('scrollBy(' + str(value) + ',+1000);')
        value += 1000
        time.sleep(3)

    elem1 = browser.find_element_by_id('islrg')
    sub = elem1.find_elements_by_tag_name('img')
    folder = "\\"+category
    try:
        os.mkdir(path + folder)
    except FileExistsError:
        pass

    count = 0
    for i in sub:
        src = i.get_attribute('src')
        try:
            if src != None:
                src = str(src)
                # print(src)
                count += 1
                urllib.request.urlretrieve(src, os.path.join(path + folder, 'image' + str(count) + '.jpg'))
            else:
                raise TypeError
        except TypeError:
            print('fail')

    browser.close()
