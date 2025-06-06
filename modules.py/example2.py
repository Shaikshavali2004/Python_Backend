#To print 10 random otp numbers

#import math,os,csv,json,re,random

#help(random)

from random import randint
for ele in range(10):
    print("OTP:",randint(1000,9999))