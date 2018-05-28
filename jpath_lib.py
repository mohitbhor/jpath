import re
import json
import sys
import pprint
from itertools import product
import traceback

sys.setrecursionlimit(10000)

def find_jpath(element, JSON, path, all_paths, f_json):
    if element in JSON:
        path = path + element  # + ' = ' + str(JSON[element])
        # print path
        all_paths.append(path)
        del JSON[element]
        find_jpath(element, f_json, '', all_paths, f_json)

    for key in JSON:
        if isinstance(JSON[key], dict):
            find_jpath(element, JSON[key], path + key + '.', all_paths, f_json)
        if isinstance(JSON[key], list):
            for i, each in enumerate(JSON[key]):
                if type(each) == dict:
                    find_jpath(element, each, path + key + "[" + str(i) + "]" + '.', all_paths, f_json)
    return all_paths


def star_tonumber(jpath, jpathlis):
    #global jsondata
    start = jpath.find('[*]')
    if start > 0:
        try:
            end = start + 3
            tempjpath = jpath[:start]
            # print "temppath-->",tempjpath
            val = get_jpath_value(jsondata, tempjpath)

            if val != None:
                for each in range(0, len(val)):
                    precisejpath = tempjpath + "[" + str(each) + "]" + jpath[end:]
                    # print "Precisepath-->", precisejpath
                    if jpath[end:].find('[*]') < 0:
                        jpathlis.append(precisejpath)

                    star_tonumber(precisejpath, jpathlis)
        except AttributeError as e:
            pass


def to_actualnumbers(jpath):
    regfor_to = re.compile("\[\d{,10}\s*to\s*\d{,10}\]")
    searchfor_to = regfor_to.findall(jpath)
    lis = []
    startendlis = []
    for each in regfor_to.finditer(jpath):
        beg = each.group().split("to")[0].replace("[", "")
        end = each.group().split("to")[1].replace("]", "")
        templis = []
        for i in range(int(beg), int(end) + 1):
            # i= i,[each.start(),each.end()]
            templis.append(i)
            # tup=each.start(),each.end(),templis
        lis.append(templis)
        startendlis.append((each.start(), each.end()))
    return lis, startendlis


def get_formated_string(jpath, each, startendlis):
    s = "jpath"
    for i in range(0, len(each)):
        s = s + ".replace('" + jpath[startendlis[i][0]:startendlis[i][1]] + "','[" + str(each[i]) + "]')"
    return eval(s)


def get_jpath_value(JSON, jpath):
    s = "JSON"
    for each in jpath.split("."):
        reg = re.compile("\[\d{,100}\]")
        search = reg.search(each)
        if search:
            index = reg.search(each).group()
            s = s + ".get('{0}'){1}".format(each.replace(index, ""), index)
        else:
            s = s + ".get('{0}')".format(each)
    #print "S-->", s
    #print type(JSON)
    val = eval(s)
    return val


def generate_to_jpath_list(jpath):
    regfor_to = re.compile("\[\d{,10}\s*to\s*\d{,10}\]")
    # regforstar = re.compile("\[\*\]")
    if regfor_to.search(jpath):
        lis = []
        tup = to_actualnumbers(jpath)
        # print "tup---",tup
        actualnumberslis = tup[0]
        startendlis = tup[1]
        for each in product(*actualnumberslis):
            s = get_formated_string(jpath, each, startendlis)
            lis.append(s)
        return lis
    else:
        return [jpath]
    """
    elif regforstar.search(jpath):
        jpathlis = []
        star_tonumber(jpath, jpathlis)
        return jpathlis
    """


def flatten(lisoflis):
    final = []
    for each in lisoflis:
        if isinstance(each, list):
            for item in each:
                final.append(item)
        else:
            final.append(each)
    return final


def generate_star_jpath_list(jpath, jsondata):
    regforstar = re.compile("\[\*\]")
    if regforstar.search(jpath):
        jpathlis = []
        star_tonumber(jpath, jpathlis)
        return jpathlis
    else:
        return jpath


def execute_jpath(jpath, org_jsondata):
	global jsondata
	jsondata=org_jsondata
	final = []
	for eachjpath in jpath.split(";"):
		jpathlist_res = generate_to_jpath_list(jpath)
		jpathlist = flatten([generate_star_jpath_list(each, org_jsondata) for each in jpathlist_res])
		for eachjpath in jpathlist:
			final.append(get_jpath_value(jsondata, eachjpath))
	return final


"""
jsondata={
	"a": {
		"b": [
			{"c":
			[{
					"key": "value10"
				}, {
					"key": "value11"
				}
			]},
			{"c": [{
				"key": "value2"
			}]},
			{"c": [{
				"key": "value3"
			}]}
		]
	}
}

jpath="a.b[1].c[0].key"
print execute_jpath(jpath,jsondata)

jpathlist_res=generate_to_jpath_list(jpath)
print jpathlist_res
jpathlist=flatten([generate_star_jpath_list(each,jsondata) for each in jpathlist_res])
for eachjpath in jpathlist:
	print get_jpath_value(jsondata,eachjpath)
"""

"""	

f_json = jsondata
all_paths_lis = []
keyname="c"
element =keyname
paths = find_jpath(element, f_json, '', all_paths_lis, f_json)
print "\nThe path till '"'{}'"'in the JSON is-".format(keyname)
for each in paths:
	print " >> " + each
"""
"""
jpathlis = []
result = star_tonumber(jpath, jpathlis)

for eachjpath in jpathlis:
value =get_jpath_value(jsondata, eachjpath))
"""

"""	
			
			
def get_jpath_value(JSON, jpath):
    s = "JSON"
    for each in jpath.split("."):
        reg = re.compile("\[\d{,100}\]")
        search = reg.search(each)
        if search:
            index = reg.search(each).group()
            s = s + ".get('{0}'){1}".format(each.replace(index, ""), index)
        else:
            s = s + ".get('{0}')".format(each)
    # print "S-->",s
    val = eval(s)
    return val


"""

"""

jpathlis = []
result = star_tonumber(jpath, jpathlis)

for eachjpath in jpathlis:
value =get_jpath_value(jsondata, eachjpath))


	mykey[2].mychildkey

s= JSON.get("mykey")[2]

JSON.get("mykey")[2].get("mychildkey")
JSON.get("mykey").get("mychildkey")
"""
