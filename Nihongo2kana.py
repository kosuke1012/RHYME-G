#!/usr/bin/env python
# -*- coding:utf-8 -*-

import MeCab

### Constants
MECAB_MODE = 'mecabrc'
PARSE_TEXT_ENCODING = 'utf-8'

### Functions
def main():
    sample_u = u"センサ漢字せんさ"
    word_dict = parse(sample_u)
    print word_dict
    #print "Nouns:", ",".join(words_dict['nouns'])
    #print "Verbs:", ",".join(words_dict['verbs'])
    #print "Adjs:", ",".join(words_dict['adjs'])
    return


def parse(unicode_string):
    tagger = MeCab.Tagger(MECAB_MODE)
    # str 型じゃないと動作がおかしくなるので str 型に変換
    text = unicode_string.encode(PARSE_TEXT_ENCODING)
    node = tagger.parseToNode(text)
    
    words = []
    nouns = []
    verbs = []
    adjs = []
    pos = u""
    while node:
        st = node.feature.split(",")
               # unicode 型に戻す
        if len(st)==7:  #katakana
            word = node.surface.decode("utf-8")
            pos +=word
        elif len(st)==9: #kanji or hiragana
            pos += st[8].decode("utf-8")
        node = node.next

    return pos

### Execute
if __name__ == "__main__":
    main()