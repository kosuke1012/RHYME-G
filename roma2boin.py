#!/usr/bin/env python
#coding:utf-8


def roma_boin (roma):
    new_roma =""
    for i in roma:
        if i=="a" or i =="i" or i=="u" or i=="e" or i=="o" or i=="n":
            new_roma += i
    
    return new_roma            
