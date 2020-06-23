import re

pattern = "^[^01234]{2}$"

tests = ["11", "12","AA", "56"]

for test in tests:
    print(re.search(pattern, test))

