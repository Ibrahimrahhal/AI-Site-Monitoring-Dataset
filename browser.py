from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class controller:
    def __init__(self):
        chrome_driver_path = "/Users/irahhal/Downloads/chromedriver"
        s = Service(chrome_driver_path)
        options = Options()
        options.headless = True
        options.add_argument('window-size=1366x768')
        self.browser = webdriver.Chrome(service=s, options=options)
    
    def get(self, url):
        self.browser.get(url)
    
    def take_screenshot(self, path, name):
        self.browser.save_screenshot(path+ "/" + name + ".png")
    
    def remove_styles_from_page(self):
        self.browser.execute_script("document.querySelectorAll('style, link[rel]').forEach(s => s.remove())")
        self.browser.execute_script("document.querySelectorAll('[style]').forEach(e => e.setAttribute('style', ''))")
    
    def abort(self):
        self.browser.close()
        
    