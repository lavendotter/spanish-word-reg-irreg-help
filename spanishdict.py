#! /usr/bin/env python

import re
from selenium import webdriver

browser = webdriver.Chrome() #replace with .Firefox(), or with the
wordlist = "deber"


words = re.split(" +", wordlist)

for word in words:
  url = "http://www.spanishcentral.com/translate/{0}".format(word)
  browser.get(url)

  reg_or_irreg = browser.find_element_by_css_selector(".cpat").text

  print word, reg_or_irreg
