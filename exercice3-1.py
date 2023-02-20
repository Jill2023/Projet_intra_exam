#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
import requests
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys


# In[ ]:


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.ebay.com/")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.XPATH,'//a[@href="https://www.ebay.com/sch/ebayadvsearch"]').click()
time.sleep(3)

