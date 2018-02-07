
import re

passwordValue="As2c";
result=None;
length=len(passwordValue);
print(length);
if(length>=6 and length<=20):
    print("hello");
    result=re.search("^[A-Z].*(\\d)+.*[@#$]+.*[a-z]$", passwordValue);
print(result);

