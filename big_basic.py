import json
import os
with open('teams_modify.json') as json_file:  
    squadre = json.load(json_file)
    squadreA = squadre["squadreA"]


with open('ranking_modify.json') as json_file:  
    classifica_interm = json.load(json_file)
    classifica1 = classifica_interm["classifica"]


classifica = {}
for e in squadreA:
	classifica[e] = []

for i in range(len(classifica1)):
	a = classifica1[i]
	b = classifica[a]
	for j in range(i):
		b.append(classifica1[j])


for e in classifica:
	a = classifica[e]
	b = {"B" : a, "M" : []}
	classifica[e] = b 

print(classifica, '\n')


with open('big_basic.json', 'w') as outfile:  
    json.dump(classifica, outfile)


print("Done")




		