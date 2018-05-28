import re
import sys
import json
from itertools import product
import traceback
import jpath_lib as lib
from pprint import pprint
from argparse import RawTextHelpFormatter
import argparse


def check_arg(args=None):
    parser = argparse.ArgumentParser(description="""The script imitates some of the behaviour of Xpath as in xml for json.
    --> It supports absolute path as well as  wildcarded path.\r\n \
    --> The script will run on getjpath mode ,getelement mode and flatten mode""", formatter_class=RawTextHelpFormatter)
    parser.add_argument('-m', '--mode',
                        help='This script will run in 3 mode 1."getjpath", 2."getelement" 3."flatten" mode')
    # parser.add_argument('-ge', '--getelement', help='supply the jpath and file name (using -f option)')
    parser.add_argument('-k', '--keyname', help='keyname')
    parser.add_argument('-j', '--jpath', help='jpath')
    parser.add_argument('-f', '--file', help='path to valid json')
    results = parser.parse_args(args)
    return (results.mode, results.keyname, results.jpath, results.file)



if __name__ == '__main__':
    mode, keyname, jpath, file = check_arg(sys.argv[1:])

    # print keyname
    # print getelement
    # print getjpath
    if not mode:
        print """Mode has to be supplied.
Please input getjpath mode or getelement mode or flatten. Using -m option. Try --help for more Info """
        sys.exit(2)
    with open(file) as datafile:
        # for i, each in enumerate(datafile):
        # print i
        # if i == 1:
        #    j_col = each.split("|")[9]
        # file=open()
		jsondata = datafile.read()
		f_json = json.loads(jsondata)
		all_paths_lis = []
		element = keyname

		if mode == "getjpath":
			paths = lib.find_jpath(element, f_json, '', all_paths_lis, f_json)
			print "\nThe path till '"'{}'"'in the JSON is-".format(keyname)
			for each in paths:
				print " >> " + each

		elif mode == "getelement":
			
			result = lib.execute_jpath(jpath, f_json)
			print result

		elif mode == "flatten":
			from subprocess import call
			call(["python", "flattenjson.py",file])
		else:
			print "Mode supplied is not correct check -h or --help "
