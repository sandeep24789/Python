abook={}
abook['mathan']={
    'name':'mathan',
    'address':'CDC',
    'Phno':9003769147
}

abook['sam']={
    'name':'sam',
    'address':'CDC',
    'Phno':9003769147
}

import json
s=json.dumps(abook)
type(s)
print(s)

with open("c:/test/abook.txt","w")as f:
    f.write(s)

fob=open("c:/test/abook.txt","r")
ob=fob.read()
ob
import json
abook=json.loads(ob)

for person in abook:
    print(abook[person])

    
