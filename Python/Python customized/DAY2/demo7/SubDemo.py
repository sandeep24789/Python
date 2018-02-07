'''
Created on Mar 16, 2017

@author: suneetha.muvva
'''
import re
dateFormat="12/10/2017";
print(dateFormat)
newDateFormat=re.sub("/", "-",dateFormat);
print(newDateFormat);
