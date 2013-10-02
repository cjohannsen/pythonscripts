class Mensch:
 vorname = ""
 name = ""
 geschlecht = ""
 def __init__(self,vorname,name,geschlecht):
  self.name = name 
  self.vorname = vorname
  self.geschlecht = geschlecht
 def setName(self,name):
  self.name = name 
 def ausgabe(self):
  print self.name 
 def __str__(self):
  str = "Vorname: {} Name: {} Geschlecht: {}".format(self.vorname,self.name,self.geschlecht)
  return str

otto = Mensch("Hans","Otto","maennlich")
print otto

otto.setName("Meier")
otto.ausgabe()
