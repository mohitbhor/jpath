# jpath
Japth -  helps you navigate the big json, search the key and hierarchy 

Refer the sample_data 

## Evolution 
      We keep on getting huge and complex JSON payloads.
      Life was difficult while navigating through the multilevel complex JSON structures. 
      Unlike XML, JSON doesn’t have the equivalent feature of XPATH.
      So, we thought of building some library which can imitate some basic 
      behaviour of XPATH on XML for our big and multilevel  JSON, if not all. We call it JPATH.
      To start with, three features were on top of our mind:
            1.	Flatten the full JSON Into Key value pair. 
            2.	Search for a key and get the JPATH of it.
            3.	Supply the JPATH and get the value for that JPATH.  


## python jpath.py  --h

      usage: jpath.py [-h] [-m MODE] [-k KEYNAME] [-j JPATH] [-f FILE]

      The script imitates some of the behaviour of Xpath as in xml for json.
          --> It supports absolute path as well as  wildcarded path.
           --> The script will run on getjpath mode ,getelement mode and flatten mode

      optional arguments:
        -h, --help            show this help message and exit
        -m MODE, --mode MODE  This script will run in 3 mode 1."getjpath", 2."getelement" 3."flatten" mode
        -k KEYNAME, --keyname KEYNAME
                              keyname
        -j JPATH, --jpath JPATH
                              jpath
        -f FILE, --file FILE  path to valid json
  
  
  ## USAGE 1:
  
  ### python jpath.py -m flatten -f sample_data.json
  
          {u'batters.batter[0].id': u'1001',
           u'batters.batter[0].someotherinfo.dummykey.name': u'val',
           u'batters.batter[0].someotherinfo.id': u'200',
           u'batters.batter[0].type': u'Regular',
           u'id': u'0002',
           u'name': u'Raised',
           u'ppu': 0.55,
           u'topping[0].id': u'5001',
           u'topping[0].info': u'value',
           u'topping[0].type': u'None',
           u'topping[1].id': u'5002',
           u'topping[1].info': u'value',
           u'topping[1].type': u'Glazed',
           u'topping[2].id': u'5005',
           u'topping[2].type': u'Sugar',
           u'topping[3].id': u'5003',
           u'topping[3].type': u'Chocolate',
           u'topping[4].id': u'5004',
           u'topping[4].name': u'just_like_that',
           u'topping[4].type': u'Maple',
           u'type': u'donut'}
  
  ## USAGE 2:
  
  ### python jpath.py -m getjpath -k id -f sample_data.json

      The path till 'id'in the JSON is-
       >> id
       >> topping[0].id
       >> topping[1].id
       >> topping[2].id
       >> topping[3].id
       >> topping[4].id
       >> batters.batter[0].id
       >> batters.batter[0].someotherinfo.id
 
 
 ## USAGE 3:  
  ### python jpath.py -m getelement -j topping[0].id -f sample_data.json
 
    >>[u'5001']

  ### python jpath.py -m getelement -j topping[1to3].id -f sample_data.json
  
    >>[u'5002', u'5005', u'5003']
    
  ### python jpath.py -m getelement -j topping[*].id -f sample_data.json
  
    >>[u'5001', u'5002', u'5005', u'5003', u'5004']
 
  
  

