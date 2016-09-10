import os.path
import linecache
import json
import linecache
import glob

from py2neo import neo4j, Node, rel

rootdir = '/home/ramez/python/capstone/app/jahili_basic_graph_data'#add jahili_json etc.

fw = open("ping.txt","w")
textfiles = glob.glob(os.path.join(rootdir, '*.txt'))
jsonfiles = glob.glob(os.path.join(rootdir, '*.json'))

#print(textfiles)
#neo4j.authenticate("localhost:7474","neo4j","faisal")
#default for 7474 is empty. can add url.
#graph_db = neo4j.Graph()

for f in textfiles:
    title = linecache.getline(f,1)# filename, line_number
    titles = title[1:-1].split(',')

        #print(type(title.split(',')))

    author = linecache.getline(f,2)
    #authors.append(author[:-1])
            #title = fi.readlines()[0]
            #author = fi.readlines()[1]
            #era = fi.readlines()[2]
    #poet = Node("Poet", name = author)
    #author_node_list.append(poet)

            #graph_db.create(poet)
            #graph_db.create(rel(poet,"BORN_IN", asr))

    for item in titles:
        item = item[2:-1]
        #poem_list.append(item)
        #print(item)
        #item = Node("Title", name = item)
        #poem_node_list.append(item)
        #graph_db.create(item)
        #graph_db.create(rel(poet,"WROTE",item))
        poe = str(item)
        po = poe[15:-3]
        #print(po)
        #poem_list.append(item)
        #print(item)
        for fi in jsonfiles:
            with open(fi,"r") as fa:
                poems = json.load(fa)
                for i in range(len(poems["abyat"])):
                    if(i==0):
                        print(poems["abyat"][0])
                    if(i>0):
                        print("hi")


                        #APPLY THIS TEMPLATE TO NODES InSTEAD OFPRINT HI GIVE REL FOLLOED BY WEWEWEWE

                #print(len(poems["abyat"]))
                #print(poems["title"])
                    #fw.write(item)

#fw.close()



        #item = Node("Title", name = item)
        #poem_node_list.append(item)
                #poe = str(item)
                #print(poe[15:-3])
                #graph_db.create(item)
                #graph_db.create(rel(poet,"WROTE",item))
'''
                if(f.endswith(".json")):
                    with open(f,"r") as fi:
                        poems = json.load(fi)
                        populate_graph(item)'''

#fw = open("ping.txt","w")
'''
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        f = os.path.join(subdir, file)
        if(f.endswith(".json")):
            print(f)

        fw.write(f)
fw.close()
'''


































'''
complete_poem = {}

#auth = linecache.getline(rootdir+'/0.txt', 3)
#print(auth)

def get_complete_poem(f):
    with open("/home/ramez/python/capstone/app/3.txt","r") as fi:
        pname = linecache.getline("/home/ramez/python/capstone/app/3.txt",1)
        pnames = pname[1:-1].split(',')
    #print(pname)
    for item in pnames:
        item = item[2:-1]
        with open(f,"r") as out:
            poems = json.load(out)
            if(item in poems["title"]):
                complete_poem.update({"abyat":poems["abyat"]})

    return complete_poem

                #with open("hi.json","w") as r:
                    #r.write(str(n))
                    #json.dump(n, r, ensure_ascii=False)
        #print(item)

#open the file containing the list of poems. get each poem la7alo, like in the case of poets, then for each poem title, find it in the json file directory, then append to the file that I obtained the poem names from; that way the file will have all the info needed for the graph!@
    #with open(f,"r") as fi:
     #   poems = json.load(fi)
        #if(author_poems == poet):
      #  for item in poems["abyat"]:
       #     complete_poem.update(item)
    #return complete_poem

#get_complete_poem()

fw = open("rimz.txt","w")
for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            f = os.path.join(subdir, file)
            #with open(f,"r") as fi:
            #print(f)
            print(get_complete_poem(f))

            #print(len(poems["author"]))

fw.close()




fx = open("welp.txt","w")
for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            f = os.path.join(subdir, file)

            fi = open(f,"r")
            auth = linecache.getline("0.txt")
            lst = fi.readlines()[0]
            #fx.write(lst)
            for i,item in enumerate(lst):
                lst[i] = function(object)
                fx.write(item)
            print(len(lst))
fx.close()
'''
