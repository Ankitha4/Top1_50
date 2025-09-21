#18.Break a string into a character array
s= "Ankitha"
char_array = [ch for ch in s]
print(char_array)
#or
ch_arr=[]
for ch in s:
    ch_arr.append(ch)
print(char_array)

#19.Replace spaces with %20
s1= "I love programming in Python"
replaced_string= ""
s1_replaced=s1.replace(" ","%20")
print(s1_replaced)

#or

for ch in s1:
    if ch == " ":
        ch = "%20"
        replaced_string += ch
    else:
        replaced_string += ch

print(replaced_string)

#20.Turn full sentence into acronyms
sen = "Aster World Trade Center"
sen_word_array = sen.split()
acro = ""
for word in sen_word_array:
    if word[0].isupper():
        acro += word[0]
print(acro)
