import re

text = 'my phone once, my phone twice'

for match in re.finditer('phone',text):
    print(match.group())