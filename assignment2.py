# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 02:15:56 2019

@author: shekhar
"""
import matplotlib.pyplot as plt 
import csv

list_all = []
token_length = 0
with open('E:/NLP/Assignment_1/tweets-dataset.csv','rt', encoding="utf8") as f:
    data = csv.reader(f)
    for row in data:
        token_row = str(row).split()
        token_length = token_length+len(token_row)
        list_all.append(str(row))
        
type_size = len(set(str(list_all).split()))

print('The number of tokens is: ', token_length)
print('The number of types is: ', type_size)
print('The TTR is: ', type_size/token_length)
        
"""
The stats come out to be
The number of tokens is:  341628
The number of types is:  66528
The TTR is:  0.19473813621834277
"""
#Plotting Zipf's law for words lost, like, night, social, comment, wait,love, match, show, and, for, one, man
frequency = [3069, 1751, 1131, 1038, 412, 305, 256, 217, 170, 139, 71, 48, 21]
meaning = [8, 13, 15, 16, 30, 30, 34, 40, 45, 21, 46, 50, 55]
plt.plot(frequency, meaning) 
plt.xlabel('frequency') 
plt.ylabel('meaning') 
plt.title("Zipf's Law") 
plt.show()

#Plotting Heaps' Law
token_length1 = 0
token_count = []
type_length = []
for count in range(522, len(list_all)+1, 2000):
    for row in list_all[0:count]:
        token_row1 = str(row).split()
        token_length1 = token_length1+len(token_row1)
    type_interval = len(set(str(list_all[0:count]).split()))    
    token_count.append(token_length1)
    type_length.append(type_interval)
    token_length1 = 0
    
plt.plot(token_count, type_length) 
plt.xlabel('text size') 
plt.ylabel('number of distinct vocabulary elements') 
plt.title("Heaps' Law") 
plt.show()

# beta for Heaps' Law comes out to be approximately 0.74
# K for Heaps's Law comes out to be approximately 5.54    
    
    
    
    

    



        