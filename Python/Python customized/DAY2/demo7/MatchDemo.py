'''
Created on Mar 15, 2017

@author: suneetha.muvva
'''
import re
s1="Accenture global technologies";
result1=re.match(r"Accenture", s1);
print(result1)

if(result1):
    print("found");
else:
    print("not found");
result2=re.match(r"global", s1);
if(result2):
    print("found");
else:
    print("not found");
