#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Priyanka Das
# @Version : 0.1
#
# test cases for ecom_finder
# Standard library imports
import os
import sys

# Third party imports
import pytest

sys.path.append(os.path.abspath(os.path.join("..")))

# Dependency Test
def test_dependencies():
    success = False
    try:
        from bs4 import BeautifulSoup
        import pandas
        import requests
        import re
        import urllib
        import speech_recognition
        success = True
    except Exception as e:
        print(e)
        
    assert success == True
    
# Amazon Crawling Test   
def test_crawler_amazon():
    import ecom_finder.ecom_finder as ef
    mobiles = ef.__get_items_from_amazon__("Mobiles")    
    assert mobiles.shape[0] > 0

# Flipkart Crawling Test
def test_crawler_flipkart():
    import ecom_finder.ecom_finder as ef
    mobiles = ef.__get_items_from_flipkart__("Mobiles")    
    assert mobiles.shape[0] > 0
    