import time

from selenium import webdriver


browser = webdriver.Firefox()
browser.get('https://docs.djangoproject.com/en/3.2/')

print(browser.title)

try:
    assert 'pythonn'== browser.title
except AssertionError:
    print(f"page title not matching with actual page{browser.title}, expect title is {'pythonn'}")

browser.maximize_window()
time.sleep(5)
browser.minimize_window()
time.sleep(5)
browser.maximize_window()
time.sleep(5)
browser.close()