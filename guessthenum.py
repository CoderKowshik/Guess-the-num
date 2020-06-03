# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 17:08:04 2018

@author: Kowshik
"""

import random
a= random.randint(1,101)


while(True):
    b=int(input("Enter a number"))
    if(b==a):
        print("guessed num is correct")
        break
    elif(b>a):
        print("The  num is less than guessed num")
    elif(b<a):
        print("The num is greater than guessed num")
        


            

