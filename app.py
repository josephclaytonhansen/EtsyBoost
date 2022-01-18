#Use searches.txt to hold search terms, and shop_name.txt to hold the shop name
#Will not function without these two files in working directory

from selenium import webdriver
import time
driver = webdriver.Chrome()
with open("searches.txt", "r") as k:
    searches = k.readlines()
    print(searches)

shop_name_location = 'wt-mb-xs-1'
names = []

with open("shop_name.txt", "r") as p:
    shop_name = p.read().split("\n")[0].strip()

page_count = 2
for search in searches:
    next_page = True
    try:
        search_q = "+".join(search.split(" "))
        driver = webdriver.Chrome()
        driver.get('https://www.etsy.com/')
        search_input = '//*[@id="global-enhancements-search-query"]'
        search_button = '//*[@id="gnav-search"]/div/div[1]/button'

        driver.find_element_by_xpath(search_input).send_keys(search)
        driver.find_element_by_xpath(search_button).click()
        while next_page:
            next_page_path = 'https://www.etsy.com/search?q='+search_q+'&page='+str(page_count)+'&ref=pagination'
            tree = driver.find_elements_by_class_name(shop_name_location)
            for i in tree:
               names.append(i.text)
               if i.text == shop_name:
                   i.click()

            if shop_name not in names:
                page_count += 1
                driver.get(next_page_path)
            else:
                next_page = False
    except Exception as e:
        print(e)
    if next_page == False:        
        time.sleep(2)
        driver.quit()
driver.quit()
