import re

txt = "The rain in Spain"
x = re.sub(r"[a-z]", "*", txt)
print(x)