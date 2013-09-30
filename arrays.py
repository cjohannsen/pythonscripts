stadt = [["Hamburg", "Hamburg", 1000000],["Frankfurt", "Hessen", 2000000], ["Berlin", "Berlin", 100000000]]
for city in stadt:
 print ("Die Stadt %s liegt in %s und hat %i Einwohner" %(city[0],city[1],city[2]))

for t in stadt:
 for n in t:
  print(n) 
