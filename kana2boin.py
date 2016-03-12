#!/usr/bin/env python
#coding:utf-8


# kanaroma.py


import re


def kana_boin(kana):
    
    hepbum = {
    
    'あ' : 'a', 'い' : 'i', 'う' : 'u', 'え' : 'e', 'お' : 'o',
    'か' : 'a', 'き' : 'i', 'く' : 'u', 'け' : 'ke', 'こ' : 'ko',
    'さ' : 'a', 'し' : 'i', 'す' : 'u', 'せ' : 'se', 'そ' : 'so',
    'た' : 'a', 'ち' : 'i', 'つ' : 'u', 'て' : 'te', 'と' : 'to',
    'な' : 'a', 'に' : 'i', 'ぬ' : 'u', 'ね' : 'ne', 'の' : 'no',
    'は' : 'a', 'ひ' : 'i', 'ふ' : 'u', 'へ' : 'he', 'ほ' : 'ho',
    'ま' : 'a', 'み' : 'i', 'む' : 'u', 'め' : 'me', 'も' : 'mo',
    'や' : 'a', 'ゆ' : 'u', 'よ' : 'o',
    'ら' : 'a', 'り' : 'i', 'る' : 'u', 'れ' : 're', 'ろ' : 'ro',
    'わ' : 'a', 'ゐ' : 'i', 'ゑ' : 'e', 'を' : 'wo', 'ん' : 'n',
    'が' : 'a', 'ぎ' : 'i', 'ぐ' : 'u', 'げ' : 'ge', 'ご' : 'go',
    'ざ' : 'a', 'じ' : 'i', 'ず' : 'u', 'ぜ' : 'ze', 'ぞ' : 'zo',
    'だ' : 'a', 'ぢ' : 'i', 'づ' : 'u', 'で' : 'de', 'ど' : 'do',
    'ば' : 'a', 'び' : 'i', 'ぶ' : 'u', 'べ' : 'be', 'ぼ' : 'bo',
    'ぱ' : 'a', 'ぴ' : 'i', 'ぷ' : 'u', 'ぺ' : 'pe', 'ぽ' : 'po',
    
    'きゃ' : 'kya', 'きゅ' : 'kyu', 'きょ' : 'kyo',
    'しゃ' : 'sha', 'しゅ' : 'shu', 'しょ' : 'sho',  
    'ちゃ' : 'cha', 'ちゅ' : 'chu', 'ちょ' : 'cho',
    'にゃ' : 'nya', 'にゅ' : 'nyu', 'にょ' : 'nyo',
    'ひゃ' : 'hya', 'ひゅ' : 'hyu', 'ひょ' : 'hyo',
    'みゃ' : 'mya', 'みゅ' : 'myu', 'みょ' : 'myo',
    'りゃ' : 'rya', 'りゅ' : 'ryu', 'りょ' : 'ryo',
    'ぎゃ' : 'gya', 'ぎゅ' : 'gyu', 'ぎょ' :'gya',
    'じゃ' : 'ja', 'じゅ' : 'ju', 'じょ' : 'jo',
    'びゃ' : 'bya', 'びゅ' : 'byu', 'びょ' : 'byo',
    'ぴゃ' : 'pya', 'ぴゅ' : 'pyu', 'ぴょ' : 'pyo', 
    
    'ア' : 'a', 'イ' : 'i', 'ウ' : 'u', 'エ' : 'e', 'オ' : 'o',
    'カ' : 'ka', 'キ' : 'ki', 'ク' : 'ku', 'ケ' : 'ke', 'コ' : 'ko',
    'サ' : 'sa', 'シ' : 'shi', 'ス' : 'su', 'セ' : 'se', 'ソ' : 'so',
    'タ' : 'ta', 'チ' : 'chi', 'ツ' : 'tsu', 'テ' : 'te', 'ト' : 'to',
    'ナ' : 'na', 'ニ' : 'ni', 'ヌ' : 'nu', 'ネ' : 'ne', 'ノ' : 'no',
    'ハ' : 'ha', 'ヒ' : 'hi', 'フ' : 'fu', 'ヘ' : 'he', 'ホ' : 'ho',
    'マ' : 'ma', 'ミ' : 'mi', 'ム' : 'mu', 'メ' : 'me', 'モ' : 'mo',
    'ヤ' : 'ya', 'ユ' : 'yu', 'ヨ' : 'yo',
    'ラ' : 'ra', 'リ' : 'ri', 'ル' : 'ru', 'レ' : 're', 'ロ' : 'ro',
    'ワ' : 'wa', 'ヲ' : 'wo', 'ン' : 'n',
    
    'ガ' : 'ga', 'ギ' : 'gi', 'グ' : 'gu', 'ゲ' : 'ge', 'ゴ' : 'go',
    'ザ' : 'za', 'ジ' : 'ji', 'ズ' : 'zu', 'ゼ' : 'ze', 'ゾ' : 'zo',
    'ダ' : 'da', 'ヂ' : 'ji', 'ヅ' : 'zu', 'デ' : 'de', 'ド' : 'do',
    'バ' : 'ba', 'ビ' : 'bi', 'ブ' : 'bu', 'ベ' : 'be', 'ボ' : 'bo',
    'パ' : 'pa', 'ピ' : 'pi', 'プ' : 'pu', 'ペ' : 'pe', 'ポ' : 'po,',
    'ヴ' : 'vu',
    
    'キャ' : 'kya', 'キュ' : 'kyu', 'キョ' : 'kyo',
    'シャ' : 'sha', 'シュ' : 'shu', 'ショ' : 'sho',
    'チャ' : 'cha', 'チュ' : 'chu', 'チョ' : 'cho',
    'ニャ' : 'nya', 'ニュ' : 'nyu', 'ニョ' : 'nyo',
    'ヒャ' : 'hya', 'ヒュ' : 'hyu', 'ヒョ' : 'hyo',
    'ミャ' : 'mya', 'ミュ' : 'myu', 'ミョ' : 'myo',
    'リャ' : 'rya', 'リュ' : 'ryu', 'リョ' : 'ryo',
    'ギャ' : 'gya', 'ギュ' : 'gyu', 'ギョ' :'gya',
    'ジャ' : 'ja', 'ジュ' : 'ju', 'ジョ' : 'jo',
    'ビャ' : 'bya', 'ビュ' : 'byu', 'ビョ' : 'byo',
    'ピャ' : 'pya', 'ピュ' : 'pyu', 'ピョ' : 'pyo'
}
    
    
    hepbum_keys = hepbum.keys()        
    hepbum_keys.sort(key=lambda x: len(x), reverse=True)
    re_kanaroma = re.compile("|".join(map(re.escape, hepbum_keys)))
    re_xtu = re.compile("っ(.)")
    re_xtu_katakana = re.compile("ッ(.)")
    re_ltu = re.compile("っ$")
    #re_n = re.compile(r"n(b|p([aiueo])")  
    re_oo = re.compile(r"([aiueo])\1")
    romaji = re_kanaroma.sub(lambda x: hepbum[x.group(0)], kana)
    romaji = re_xtu.sub(r"\1\1", romaji)
    romaji = re_xtu_katakana.sub(r"\1\1", romaji)        
    romaji = re_ltu.sub(r"", romaji)   
    #romaji = re_n.sub(r"m\1\2", romaji)                    
    romaji = re_oo.sub(r"\1", romaji)
                                                                                 
    return romaji
