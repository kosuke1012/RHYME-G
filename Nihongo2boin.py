#!/usr/bin/env python
#coding:utf-8

import Nihongo2kana
import kana2roma
import roma2boin

text = u"木の脇エーケーエー赤い稲妻"
kana = Nihongo2kana.parse(text).encode('utf-8')
roma = kana2roma.kana_roma(kana)
boin = roma2boin.roma_boin(roma)

print text
print kana
print roma
print boin
