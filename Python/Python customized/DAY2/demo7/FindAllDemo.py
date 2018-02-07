'''
Created on Mar 16, 2017

@author: suneetha.muvva
'''
import re
line="tiger lion donkey monkey girafee snake x";
result=re.findall(r"\b\w{\b", line);
print(result);
