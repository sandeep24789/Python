'''
Created on Mar 16, 2017

@author: suneetha.muvva
'''
import re
dateValue="10/4/9999";
result=re.search("^([1-9]|[12][0-9]|3[01])/(\d|1[012])/\d(\d?){3}$", dateValue);
print(result);



