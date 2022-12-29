# Append a dictionary to a list. Iterate over Json.
# [{"name": "sdd","st":900},{"name":"ttt","st": 76}]
import json
with open('files.json') as fl:
    data = json.load(fl)

def append_dict_to_list(data):
    newlist = []

    for i in data['incidents'][:4]:
        dict = {}
        dict["name"] = i['name']
        dict["status"] = i['status']
        dict["impact"] = i['impact']
        newlist.append(dict)
    return newlist

print(append_dict_to_list(data))

