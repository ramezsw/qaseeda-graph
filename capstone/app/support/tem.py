import os

greet = 'Hello'
name = 'url'

filename = "%s.txt" %name
path = "/home/ramez/python/capstone/app"
fullpath = os.path.join(path, filename)
#print(filename)

with open(fullpath,"w") as f:
    f.write(greet)



















'''
{
    "title":"kaza",
    "author":"kaza",
    "abyat":[
        {"sadr":"here","ajez":"here"},
        {"sadr":"here","ajez":"here"}
        ]
}
'''
