#!/usr/bin/env python
# -*- coding:utf-8 -*-
import MeCab

### Constants
MECAB_MODE = 'mecabrc'
PARSE_TEXT_ENCODING = 'utf-8'

def sentence_word(sentence):
    tagger = MeCab.Tagger(MECAB_MODE)
    text = sentence.encode(PARSE_TEXT_ENCODING)
    node = tagger.parseToNode(text)
    
    d=u"動詞"
    m=u"名詞"
    k=u"感動詞"

    word_list =[]
    while node:
        st =node.feature.split(",")
        pos = st[0]
        if pos==d or pos==m or pos==k :
            word = node.surface.decode("utf-8")
            print word
            word_list.append(word)

        node = node.next
    return word_list
