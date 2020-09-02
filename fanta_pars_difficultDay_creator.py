import json
with open('fanta_pars_out.json') as json_file:  
    dicto = json.load(json_file)


with open('fanta_big.json') as json_file:  
    big = json.load(json_file)



with open('fanta_squadreA_modify.json') as json_file:  
    squadreA_interm = json.load(json_file)
squadreA = squadreA_interm["squadreA"]



#big = ["Juventus", "Napoli", "Atalanta", "Inter", "Milan", "Roma", "Torino"]

bigD = {}


for e in squadreA:
	bigD[e] = []



c = 1

for e in dicto:
	a = dicto[e]
	g = big[e]["B"]
	m = big[e]["M"]
	for j in m:
		g.append(j)
	b = []
	for x in a:
		for y in g:
			if x == y:
				b = bigD[e]
				b.append(c)
		bigD[e] = b
		c += 1
	c = 1


print(bigD)


with open('fanta_bigD.json', 'w') as outfile:  
    json.dump(bigD, outfile)


print("Done")







