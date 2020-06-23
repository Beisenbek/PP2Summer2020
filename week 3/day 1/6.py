import re

pattern = "^[01234]{1,2}$"

tests = ["0", "1", "5", "11", "12"]

for test in tests:
    print(re.search(pattern, test))

