#!/usr/bin/env python  
# -*- coding: utf-8 -*-
import os
import urllib
import re
import csv
import codecs
import sys
from pinyin import PinYin


def writeCityName():
    if not os.path.exists('cityName.csv'):
        url="http://www.zxinc.org/gb2260.htm"
        print 'start reading ...'
        response=urllib.urlopen(url)
        page=response.read()
        page = page.decode('utf8')
        print 'reading done...'
        pattern = re.compile(ur'([\u4e00-\u9fa5]{2,5}市)')
        match = pattern.findall(page)  
        if match:
            try:
                with open('cityName.csv', 'wb') as csvfile:
                    csvWrite = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    csvfile.write(codecs.BOM_UTF8)
                    test = PinYin()
                    test.load_word()
                    for result in match :
                        result = result.encode('utf8')
                        py = test.hanzi2pinyin(string = result[:-3])
                        csvWrite.writerow([result[:-3],py[-1]])
                print 'write done!'
            except Exception as e:
                print e
            finally:
                csvfile.close()
    else:
        print 'cityName.csv detected'




