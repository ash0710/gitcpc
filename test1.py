import os
import re
import collections 
z =  collections.defaultdict(list)
d=[]
dic={}
for i in os.listdir(r'C:\Users\ashray\Desktop\New folder'):#workspace path
    
    result = os.path.splitext(i)[0]
    #print(" ===",result)
    d.append(result)
#print(d)

my_str = ','.join(d)
       
#print(my_str)
l=my_str.split(',')
#print(l)

for keyAndValue in l:
     record=keyAndValue.split('#')
     if record[0] in dic:
        dic[record[0]].append(record[1])
     else:
        dic[record[0]]=[record[1]]
print(dic)

for key in dic:
    sortedVals=sorted(dic[key],reverse=True)
    print(key,sortedVals[0])