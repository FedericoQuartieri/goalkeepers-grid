import json
with open('fanta_bigD.json') as json_file:  
    bigD = json.load(json_file)

'''
					"Juventus",
					"Napoli",
					"Atalanta",
					"Inter",
					"Milan",	
					"Roma",	
					"Torino",
					"Lazio",
					"Sampdoria",
					"Bologna",
					"Sassuolo",	
					"Udinese",
					"SPAL",
					"Parma",
					"Cagliari",
					"Fiorentina",	
					"Genoa",
					"Brescia", 
					"Lecce",
					"Verona" 
'''



Fdicto = {}

for e in bigD:
	a = bigD[e]

	for x in a:
		for y in bigD:
			if e != y:
				b = bigD[y]
				if x in b:
					chiavi = []
					chiavi_interm = Fdicto.keys()
					for r in chiavi_interm:
						chiavi.append(r)
					if len(chiavi) == 0:
						Fdicto["{} {}".format(e,y)] = 0	
					else:
						if "{} {}".format(e,y) not in Fdicto :
							Fdicto["{} {}".format(e,y)] = 0	
					c = Fdicto["{} {}".format(e,y)]
					c += 1 
					Fdicto["{} {}".format(e,y)] = c 
				c = 0


for e in bigD:
	for y in bigD:
		if e != y:
			k = "{} {}".format(e,y)
			if k not in Fdicto:
				Fdicto["{} {}".format(e,y)] = 0	



Finale = {}
	


for e in Fdicto:
	a = Fdicto[e]
	if a == 4:
		Finale[e] = a 


#print(Finale)
print(Fdicto["Atalanta Lazio"])
print(Fdicto["Atalanta Udinese"])



'''with open('Output_4.json', 'w') as outfile:  
    json.dump(Finale, outfile)'''










