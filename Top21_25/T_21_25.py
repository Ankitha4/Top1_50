#21.check if a string contains only digits
import re
s="234567189"
num = globals()
for i in s:
    if i.isdigit():
        num = True
    else:
        num = False
        print("String is not numeric")
        break
if num:
    print("String has only digits")

#or

#using regrex
s1="23a4567189"
if re.fullmatch(r'[0-9]+',s1):
    print("string is numeric")
else:
    print("Not numeric")

#using for loop
s1="23a4567189"
only_numeric = True
for i in s1:
    if i < '0' or i > '9':
        only_numeric = False
        break
print("Is numeric",only_numeric)


