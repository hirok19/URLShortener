#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 15:38:58 2019

@author: supaul
"""
import string
class LargeBaseEncoder:
    dict36={}
    dictlargeBase={}
    map36Str="";
    maplargeStr="";
    largeBase=0
    def __init__(self):
        self.map36Str="0123456789abcdefghijklmnopqrstuvwxyz"
        self.maplargeStr=string.printable
        for i in range(len(self.map36Str)):
            self.dict36[self.map36Str[i]]=i
        for i in range(len(self.maplargeStr)):
            self.dictlargeBase[self.maplargeStr[i]]=i
        
        self.largeBase=len(self.maplargeStr)
        return
    def encode(self,URL):
        encodedStr="";
        decimal=0
        power=0
        URL="".join(reversed(URL))
        for ch in URL:
            digitVal=self.dict36[ch]
            decimal+=(digitVal*(36**power))
            power+=1
        while(decimal>0):
            rem=(decimal%(self.largeBase))
            decimal=decimal//(self.largeBase)
            encodedStr=self.maplargeStr[rem]+encodedStr
        return encodedStr
    def decode(self,URL):
        decodedStr="";
        decimal=0
        power=0
        URL="".join(reversed(URL))
        for ch in URL:
            digitVal=self.dictlargeBase[ch]
            decimal+=(digitVal*(self.largeBase**power))
            power+=1
        while(decimal>0):
            rem=(decimal%(36))
            decimal=decimal//(36)
            decodedStr=self.map36Str[rem]+decodedStr
        return decodedStr
    
    