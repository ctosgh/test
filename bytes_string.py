import os
import json

base_str = "我是个坏人"
print(type(base_str))
print(base_str)
print(len(base_str))

bytes_utf8 = base_str.encode(encoding="utf-8")
print(type(bytes_utf8))
print(bytes_utf8)
print(len(bytes_utf8))

bytes_gb2312 = base_str.encode(encoding="gb2312")
print(type(bytes_gb2312))
print(bytes_gb2312)


oristr = bytes_utf8.decode(encoding="utf-8")
print(oristr)

try:
    oristr = bytes_utf8.decode(encoding="gb2312")
    print(oristr)
except Exception as e:
    print("exception caught {}".format(e))

test = {"name":"我是个好人"}
json_str = json.dumps(test, ensure_ascii=False)
print(json_str)
