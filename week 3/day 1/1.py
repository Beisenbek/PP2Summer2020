import untangle

obj = untangle.parse("data.xml")

print(obj.root.child['name'])

