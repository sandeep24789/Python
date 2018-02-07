import json

jsonData='{"PID":"11203094","Name":"Mohan","Project":"LKM","Designation":"TL"}'

data = json.loads(jsonData)

print(data)
