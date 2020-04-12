import os
import json

os.mkdir('pages')
inp_file = open('data1.json','r')
data = json.loads(str(inp_file.read()))
inp_file.close()

f = open('pages/index.html','w')
#f.write("##Hello World!!!")
f.write("<h2> Hello {}. Your Age is {}. </h2>".format(data["Name"],data["Age"]))
f.close()
