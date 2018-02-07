'''
Created on Mar 15, 2017

@author: suneetha.muvva
'''
import re
print(re.search("^A.*e$", "Accenture"));
print(re.search("[rmc]at","mat"));
print(re.search("(r|m)at","rat"));
print(re.search("a*","baa"));
print(re.search("a+","bbb"));
print(re.search("b?", "bbb"));
print(re.search("^a{3,}$","aaaa"));
print(re.search("a{0,3}","aa"));

