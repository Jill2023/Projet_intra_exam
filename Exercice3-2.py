#!/usr/bin/env python
# coding: utf-8

# In[14]:


import time
import requests
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys


# In[16]:


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver = webdriver.Chrome()
driver.get("https://www.ebay.com/")
elem=driver.find_element(By.NAME,"_nkw")
elem.send_keys("iPhone 11")
driver.find_element(By.ID,"gh-btn").click()
time.sleep(3)
url_actuel=driver.current_url
response=requests.get(url_actuel)
response.content
response.status_code
Soup=BeautifulSoup(response.content,"html.parser")
list=Soup.find_all("div",{"class":"lister-item"})
if(len(list))<=1000:
    print("au moins de 1000 elements de recherche presents")
else:
    print("au plus de 1000 elements de recherche presents")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




