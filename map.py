import os

list1 = [1, 2, 3, 4]

dict1 = {"items":list1}

body = {
"success": True,
"totalrecords": 1,
"page": 1,
"status": "success",
"rows": 1,
"totalpages": 1,
"data": [
            {
                "friendly_name": "Jacky-T50-Cloud",
                "inactive": 0,
                "data_retention": 30,
                "uptime": 189195,
                "serial_number": "70AF02E3CEF24",
                "folder_id": 0,
                "account_id": "WGC-1-68303a0ce5a149159932",
                "current_version": "12.6.B594291",
                "managed": 0,
                "ip_address": None,
                "end_date": "2020-05-05",
                "cluster_id": 0,
                "id": 10562,
                "short_model_name": "T50-W",
                "mfg_version": "12.0.1",
                "long_model_name": "Firebox T50-W",
                "full_count": 1,
                "logging": 1,
                "connected": 1
            },
            {
                "friendly_name": "Jacky-T50-Cloud",
                "inactive": 0,
                "data_retention": 30,
                "uptime": 189195,
                "serial_number": "70AF02E3CEF24",
                "folder_id": 0,
                "account_id": "WGC-1-68303a0ce5a149159932",
                "current_version": "12.6.B594291",
                "managed": 0,
                "ip_address": None,
                "end_date": "2020-05-05",
                "cluster_id": 0,
                "id": 10563,
                "short_model_name": "T50-W",
                "mfg_version": "12.0.1",
                "long_model_name": "Firebox T50-W",
                "full_count": 1,
                "logging": 1,
                "connected": 1
            }
        ]
}

dev_list = list(map(lambda x: x['id'], body["data"]))


print(dev_list)

print(dict1)
