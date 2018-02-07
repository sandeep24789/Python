'''
Created on Mar 15, 2017

@author: suneetha.muvva
'''
import re
colorCode="red:green$blue#yellow_orange";
colors=re.split("[:$#_]", colorCode);
print(colors);
