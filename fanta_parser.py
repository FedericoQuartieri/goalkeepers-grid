import json
with open('fanta_input_modify.json') as json_file:  
    dicto = json.load(json_file)


with open('fanta_squadreA_modify.json') as json_file:  
    squadre_interm = json.load(json_file) 
squadreA = squadre_interm["squadreA"]

print(squadreA, '\n')


squadre = {}
for e in squadreA:
	squadre[e] = []

chiavi = dicto.keys()


for i in range(len(chiavi)):
	a = dicto['giornata_{}'.format(i+1)]
	c = []
	for j in range(len(a)):
		b = a[j].split(" ")
		c.append(b)
	a = c 
	for e in a:
		d = squadre[e[0]]
		d.append(e[1])
		squadre[e[0]] = d
	for x in a:
		d = squadre[x[1]]
		d.append(x[0])
		squadre[x[1]] = d

with open('fanta_pars_out.json', 'w') as outfile:  
    json.dump(squadre, outfile)



print("Done")

