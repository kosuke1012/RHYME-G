#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MeCab
#import word_converter

def StringJa2Katakana(String):
    mecab = MeCab.Tagger()
    text = String.encode('utf-8')
    res =  mecab.parseToNode(text)
    
    hira = ""
    
    while res:
    #        print res.surface
            ar = res.feature.split(",")
            print ar
            hira += ar[0]
            res = res.next
    return hira


string = u"あいうえお"
print StringJa2Katakana(string)
