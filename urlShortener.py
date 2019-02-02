#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 12:44:01 2019

@author: supaul
"""


from DatabaseConnector import *
from BrowserOpener import *
from LargeBaseEncoder import *

def main():
    db_path ='/Users/supaul/Documents/url.db'
    databaseConnector=DatabaseConnector(db_path)
    databaseConnector.createTable()
    url=input("Enter large url\n")
    key=databaseConnector.insertURL(url)
    print(key)
    largeBaseEncoder=LargeBaseEncoder()
    shortenedURL=largeBaseEncoder.encode(key)
    print(shortenedURL) 
    browserOpener=BrowserOpener(databaseConnector)
    browserOpener.openURL(largeBaseEncoder.decode(shortenedURL))
    
    
if __name__ == '__main__':
    main()
    