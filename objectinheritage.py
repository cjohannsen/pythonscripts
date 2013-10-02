import copy

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

class Person(Mensch):
	nation = "Weltbuerger"
	def __init__(self,vorname,name,geschlecht,nation):
		Mensch.__init__(self,vorname,name,geschlecht)
		self.nation = nation
	def __str__(self):
		str = "{} Nation: {}".format(Mensch.__str__(self),self.nation)
		return str


otto = Mensch("Hans","Otto","maennlich")
print otto

otto.setName("Meier")
otto.ausgabe()
		
schmidt = Person("Arne","Schmidt","maennlich","Deutschland")
print schmidt

schulz = copy.deepcopy(schmidt)
schulz.name = "Schulz"
print schulz

listePerson = []
listePerson.insert(0,schulz)
listePerson.insert(0,schmidt)
print listePerson
print listePerson[1]
print listePerson[1].vorname
