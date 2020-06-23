import re

txt = "The rain in Spain"
x = re.sub(r"\s", "9", txt)
print(x)