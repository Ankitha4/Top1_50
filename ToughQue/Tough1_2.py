#1.remove only integer repeateing values from string
#2.first write the string in alphabetic then in number then add the special characyer if any

import  re
s="an#$%nkk23it222333665556678hhhh32aa#$%1a"
seen_int = []
new_string = ""
for char in s:
    if char.isdigit():
        if char not in seen_int:
            seen_int.append(char)
            new_string += char
    else:
        new_string += char
print(new_string)
char_string= ""
num_string =""
spec_string = ""

for char in new_string:
    if char.isalpha():
        char_string += char
    elif char.isdigit():
        num_string += char
    else:
        spec_string += char
num_string = (sorted(num_string))
num_string = "".join(num_string)

print(char_string+num_string+spec_string)




