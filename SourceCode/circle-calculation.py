'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2024-03-19 21:26:31
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2024-03-23 23:29:23
FilePath: \fuck-python-in-school\0-use.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#终端写圆
from time import sleep

import os
import time
from tqdm import tqdm



sleep(0.5)
print('','')
print('','')
print('','')
PI = 3.14    
a = input('please put a fucking nummber here:')
b1 = False
try:
    b = float(a)
    b1 = isinstance(b,float)
except ValueError:
   pass

if  b1 == True : 
 # happly ending
    a = float(a)
    FuckC = a*2*PI
    FuckS = a**2*PI
    print('正在计算中')
    
    #等待几秒更有感觉
    for i in tqdm(range(3, 10)):
        sleep(0.1)
    sleep(1)
    
    print('周长是',FuckC)
    print('面积是',FuckS)
    sleep(1)
    print('---------------------------')
    print('10秒后自动关闭')
    sleep(10)
else:
    
    sleep(0.3)
    print('...')
    sleep(0.5)
    print('你滴,大大滴坏!!!')
    sleep(0.5)
    c = input('在这里打666就不把你电脑炸了-->')
    d =c.isdigit()
    
    if d == True and c == '666'  :
     # still  a decent ending
     sleep(0.4)
     print('这次就饶了你')
     sleep(0.4)
     print('-------------------------')
     print('15秒后自动关闭')
     sleep(15)
    else:
       #you die or i die
       sleep(0.5)
       i = 0
       while i < 60:
         i += 1
         print('开炮!!!')
         os.system("start cmd")
         sleep(0.1)   

#如若报错,请检查是否下载三方库 os , threading ,tqdm和 time.
#下载指令  'pip install XXX'  <--cmd中运行该命令  -> eg: T>pip install os  
#如果实在不清楚为何报错,可以联系作者 "https://github.com/bearkid6/FuckSchoolPYHomework"
#打不开请百度一下 '为什么打不开"GitHub"'

