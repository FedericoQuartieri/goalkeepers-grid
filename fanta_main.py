import json
with open('fanta_calendar_modify.json') as json_file:  
    dicto = json.load(json_file)

with open('fanta_squadreA_modify.json') as json_file:  
    squadre_interm = json.load(json_file) 
squadreA = squadre_interm["squadreA"]

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
		#print(c)
	a = c
	#print(a)
	#print(squadre)
	for e in a:
		d = squadre[e[0]]
		#print(d)
		d.append(e[1])
		#print(d)
		squadre[e[0]] = d
	for x in a:
		d = squadre[x[1]]
		d.append(x[0])
		squadre[x[1]] = d

dicto = squadre

with open('fanta_big.json') as json_file:  
    big = json.load(json_file)

bigD = {}

for e in squadreA:
	bigD[e] = [[],[]]

c = 1

for e in dicto:
	a = dicto[e]
	g = big[e]["B"]
	m = big[e]["M"]
	bignumber = []
	mednumber = []
	for x in a:
		for y in g:
			if x == y:
				bignumber = bigD[e][0]
				#print(bigD)
				bignumber.append(c)
		final = [bignumber,bigD[e][1]]
		bigD[e] = final
		for y in m:
			if x == y:
				mednumber = bigD[e][1]
				#print(bigD)
				mednumber.append(c)
		final = [bigD[e][0],mednumber]
		bigD[e] = final
		c += 1
	c = 1

#print(bigD)

Fdicto = {}

for e in bigD:
	a = bigD[e]

	for x in a[0]:
		for y in bigD:
			if e != y:
				b = bigD[y][0]
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
					c += 3 
					Fdicto["{} {}".format(e,y)] = c 
				c = 0
	for x in a[0]:
		for y in bigD:
			if e != y:
				b = bigD[y][1]
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
					c += 2 
					Fdicto["{} {}".format(e,y)] = c 
				c = 0
	for x in a[1]:
		for y in bigD:
			if e != y:
				b = bigD[y][0]
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
					c += 2 
					Fdicto["{} {}".format(e,y)] = c 
				c = 0
	for x in a[1]:
		for y in bigD:
			if e != y:
				b = bigD[y][1]
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
	
#print(Fdicto)

for e in bigD:
	for y in bigD:
		if e != y:
			k = "{} {}".format(e,y)
			if k not in Fdicto:
				Fdicto["{} {}".format(e,y)] = 0	

Finale = {}

for i in range(6):
	for e in Fdicto:
		a = Fdicto[e]
		if a == i:
			Finale[e] = a 
	with open('Output/Output_{}.json'.format(i), 'w') as outfile:  
		json.dump(Finale, outfile)

to_sort = {}
for e in squadreA:
	squadra = "Juventus"
	a = squadra + " " + e
	if a != squadra + " " + squadra:
		to_sort[a] = Fdicto[a]
sorted_final = sorted(to_sort.items(), key=lambda x: x[1])
print(sorted_final)