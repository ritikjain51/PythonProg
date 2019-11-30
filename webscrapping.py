# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 23:29:34 2019

@author: ATUL SHARMA
"""

import requests 
URL = "https://www.geeksforgeeks.org/data-structures/"
r = requests.get(URL) 
print(r.content) 
