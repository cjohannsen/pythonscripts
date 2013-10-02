import sys, urllib2, re, json

url = "http://81.173.201.133/test.json"

try:
	json_string = urllib2.urlopen(url).read()
except:
	print ("No website")
	sys.exit()
	
# de-serialize the string so that we can work with it
the_data = json.loads(json_string)
print the_data

# get the list of trends
trends = the_data[0]
print trends

# print the name of each trend
for trend in trends:
    print trend['name']

	