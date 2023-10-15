#!/usr/bin/python3
import re
string = 'User.all()'
string2 = re.split(r'[("").]', string)
string2 = [item for item in string2 if item]
print(string2)
