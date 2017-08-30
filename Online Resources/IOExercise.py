# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 13:25:38 2017

@author: Chris
"""
import re



def sum_Numbers():
    f_sum = 0
    with open(r'C:/Users/Chris/Documents/GitHub/Python-Learning/Online Resources/f1.txt', 'r') as x:
        for line in x:
            num = float(line)
            f_sum += num
    print(f_sum)
    
sum_Numbers()

def filter_Sum():
    f_sum = 0
    with open(r'C:\Users\Chris\Documents\GitHub\Python-Learning\Online Resources\f2.txt', 'r') as x:
        x = x.read()
        numbers = re.findall(r"[-+]?\d*\.\d+|\d+", x)
    for x in numbers:
        f_sum += int(x)
    print(f_sum)
    
filter_Sum()