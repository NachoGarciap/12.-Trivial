import re

text = "pink,red,blue,green"

pattern = r"\s+"
result = re.split(pattern, text)
print(result)
