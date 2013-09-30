import sys

try:
 datei = open("datei.txt", "r")
except:
 print ("No file!")
 sys.exit(0)

zeilen = datei.readlines()

print datei.name

for i in zeilen:
 print(i)

datei.seek(0)

zeile = datei.readline()
while zeile:
 print(zeile)
 zeile = datei.readline()

datei.close()

#call local command
#from subprocess import call
#call("ls")


