import xmltodict

with open('data3.xml') as fd:
    doc = xmltodict.parse(fd.read())


print(doc["mydocument"]["@has"])
print(doc["mydocument"]["and"]["many"])