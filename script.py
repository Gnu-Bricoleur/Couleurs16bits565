
fichier = open("wiki", "r")
toutesleslignes = fichier.readlines()

listecouleurs = []
listergb = []
lister = []
listeg = []
listeb = []
listehexa = []
couleur = False

for ligne in toutesleslignes[9:]:
	print ligne
	
	if couleur == True:
		couleur = False
		col = ligne.split(" || ")
		listergb.append(col[2])
		

	if ligne[0] == "!":
		couleur = True
		col = ligne[2:].split(",")
		col2 = col[0].split(" ")
		listecouleurs.append(col2[0])


fichier.close()
print listecouleurs



for elt in listergb:
	num = elt[4:]
	num = num[:-1]
	num2 = num.split(",")
	print num2
	lister.append(num2[0])
	listeg.append(num2[1][1:])
	listeb.append(num2[2][1:])


for i in range(len(lister)):
	r = lister[i]
	g = listeg[i]
	b = listeb[i]
	r = 255 - int(r)
	b = 255 - int(b)
	g = 255 - int(g)

	#r = bin(r%32)[2:].zfill(5)
	#g = bin(g%64)[2:].zfill(6)
	#b = bin(b%32)[2:].zfill(5)
	
	r = int((r/255.0)*31)
	g = int((g/255.0)*63)
	b = int((b/255.0)*31)
	
	r = bin(r)[2:].zfill(5)
	g = bin(g)[2:].zfill(6)
	b = bin(b)[2:].zfill(5)
	
	binaire = r + g + b
	hexa = hex(int(binaire, 2))[2:].zfill(4)
	hexa = "0x" + hexa.upper()
	listehexa.append(hexa)

fichier = open("couleurs.h", "w")
for i in range(len(listecouleurs)):
	fichier.write("#define " + listecouleurs[i].upper() + " " + listehexa[i] + "\n")
fichier.close


