#!/usr/bin/env python  
# -*- coding: utf-8 -*-
import os
import urllib
import re
import csv
import codecs
import sys
import random
from pinyin import PinYin
import grabCity as gc


def idiomFind(x):
    if x == None:
        raise Exception
    else:
        with open('idiom.txt','r') as f:
            base = f.readlines()
            random.shuffle(base)
            j = 0
            for i in base:
                
                c = i[:3].decode('utf8')
                if len(i)>1:
                    try:
                        test = PinYin()
                        test.load_word()
                        py = test.hanzi2pinyin(c)[0]
                        if (py == x):
                            return i
                    except:
                        continue
        return None



if __name__ == "__main__":
    gc.writeCityName()
    print('start main()')
    while True:
        cityName = raw_input('please input Chinese City name:'.decode('utf-8')).decode(sys.stdin.encoding) 
        if cityName:
            with open('cityName.csv', 'rb') as csvfile:
                csvReader = csv.reader(csvfile, delimiter=' ', quotechar='|')
                flag_city = True
                for row in csvReader:
                    if(row[0].decode('utf8') ==  cityName):
                        print 'city found! start searching idom...'
                        print idiomFind(row[1]).decode('utf8')
                        
                        flag_city = False
                        break
                if flag_city:
                    print 'no matching city!'
                
