import sys

try:
 csv = open("test1.csv", "r")
except:
 print "No file found!"
 sys.exit(0)

lines = csv.readlines()
csv.close()

for l in lines:
 la = l.split(";")
 if len(la) != 3:
  raise NameError('HiThere')
 print ("Modell {}, Marke {}, Hersteller {}".format(la[0],la[1],la[2])) 
