import sys

def read_datei(path):
 try:
  datei = open(path)
 except:
  print("No file found.")
  sys.exit(0)

 zeilen = datei.readlines()
 datei.close()

 for z in zeilen:
  print(z)

def read_all(path):
 try:
  datei = open(path)
 except:
  print("No file found.")
  sys.exit(0)

 datei_inhalt = datei.read()
 return datei_inhalt
 datei.close()

def read_splitted(path):
  try:
   datei = open(path)
  except:
   print("No file found.")
   sys.exit(0)

  lines = datei.readlines()
  datei.close()

  for l in lines:
   la = l.split(";")
   return la[0],la[1],la[2]


#Ausgabe der Zeilen
read_datei("datei.txt")

#Ausgabe des Objektes
output = read_all("datei.txt")
print output 

#Ausgabe mehrerer Ergebnisse
test = read_splitted("test.csv")
print test
