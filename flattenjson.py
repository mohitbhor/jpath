import json
import pprint
import sys


def flatten_dict(d, key="", mapp={}, delimeter="."):
    for k, v in d.iteritems():
        value = v
        if type(value) == dict:
            flatten_dict(value, key + delimeter + k)

        elif type(value) == list:
            flatten_lis(value, key + delimeter + k)

        else:
            mapp.update({key + delimeter + k: value})

    return mapp


def flatten_lis(v, k):
    lis = []
    for i, each in enumerate(v):
        index = "[" + str(i) + "]"
        if type(each) == dict:
            result = flatten_dict(each, k + index)
            lis.append(result)

        elif type(each) == list:
            result = flatten_lis(each, k + index)
            lis.append(result)

        else:
            lis.append({k: v})

    return lis


def iterate_on_data(data):
    for k, v in data.iteritems():
        if type(v) == dict:
            data1 = flatten_dict(v, k)
            temp.append(data1)

        elif type(v) == list:
            data2 = flatten_lis(v, k)
            temp.append(data2)
        else:
            data = {k: v}
            temp.append(data)



def flatten(temp):
    new = []
    for entries in temp:
        if type(entries) == list:
            for each in entries:
                new.append(each)
        else:
            new.append(entries)

    d = {}
    for dis in new:
        for k, v in dis.iteritems():
            if type(v) != dict:
                d.update({k: v})
    pprint.pprint(d)
    


fname = sys.argv[1]
# "D:\\vmware\\BIBA\\skyline\\NSX_output\\output_1497022158193_Topology.json"
f = open(fname, "r")
data = json.loads(f.read())
temp = []
iterate_on_data(data)  # will populate the temp list
flatten(temp)  # will flatten the temp list
