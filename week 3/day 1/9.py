import re

pattern = r"^\d*$"

tests = ["11", "12","AA", "56","1234567890","1",""]

for test in tests:
    print(re.search(pattern, test))

