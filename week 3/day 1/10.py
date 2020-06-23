import re

pattern = r"^\w*$" #[0-9A-Za-z_]

tests = ["11", "12","AA", "56","1234567890","1","_word","word!"]

for test in tests:
    print(re.search(pattern, test))

