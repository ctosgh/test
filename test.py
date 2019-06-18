import os
from boto3.dynamodb.conditions import Key, Attr
from functools import reduce

mydict = {"name":"jsun", "age":18, "gender":"male", "delta":{"age":"19", "name":"jsun"}}

if "delta" in mydict:
    print("have delta")
else:
    print("no delta")

record = dict()
record["name"] = "jacky"
record["age"] = "18"

mylist = list()

mylist.append("name")

print(record.get('name'))
print(record.get('aaa'))
print(mylist)

kce = Key("account").eq(1928)
print(type(kce))
print(str(kce))

print(reduce(lambda x,y : x + y, mylist))


print("name" in record)
