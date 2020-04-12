import os
import json

os.mkdir('pages')
inp_file = open('data1.json','r')
data = json.loads(inp_file.read())
inp_file.close()

f = open('pages/index.md','w')
#f.write("##Hello World!!!")
f.write("##Hello {}. Your Age is {}.".format(data["Name"],data["Age"]))
f.close()
