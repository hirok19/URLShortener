#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 13:06:31 2019

@author: supaul
"""
from DatabaseConnector import *
import webbrowser
class BrowserOpener:
    db=None
    def __init__(self,db):
        self.db=db
        return
    def openCompressed(self,compressedStr):
        self.openUncompressed(self.db.getURLFromKey(compressedStr))        
        return
    def openUncompressed(self,uncompressedStr):
        print(uncompressedStr)
        webbrowser.open(uncompressedStr)
        return
    def openURL(self,URL):
        if(self.db.getURLFromKey(URL) is None):
            self.openUncompressed(URL)
        else:
            self.openCompressed(URL)
        return