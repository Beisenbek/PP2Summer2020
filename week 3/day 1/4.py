import re

pattern = "^The.*Spain$"

test1 = "The rain in Spain"
test2 = "The rain in Italy Spain"
test3 = "TheSpain"

x1 = re.search(pattern, test1)
x2 = re.search(pattern, test2)
x3 = re.search(pattern, test3)

print(x1)
print(x2)
print(x3)

