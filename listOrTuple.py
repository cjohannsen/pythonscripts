t = ("ich","bin","ein","tuple")
print t

l = []
for i in t:
 l.append(i)
l.insert(3, "fake")

print l
