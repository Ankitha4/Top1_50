#1.reverse a string without built
s= "Programming"
rev=""
#first approach
for i in s:
    rev = i+rev
print(rev)

#secomd approach
rev_str=s[::-1]
print(rev_str)


#2.Is it a palindrome
#string
s1 = "MalayalaM"
if s1 == s1[::-1]:
    print("It is a palindrome")
else:
    print("Not a palindrome")
#number
rev_num = 0
num1= 4565
tem_num = 45654
while tem_num>0:
    digit = tem_num %10
    rev_num = rev_num*10 + digit
    tem_num //= 10
if num1 == rev_num:
    print("palindrome")
else:
    print("Not a palindrome")

#second method
num1 = str(num1)
if num1==num1[::-1]:
    print("Is a palindrome")
else:
    print("Not a palindrome")


#3.Remove duplicate from string effectively
s="Programming"
s_wd= ""
for char in s:
    if char not in s_wd:
        s_wd +=char
print(s_wd)


#4.Remove only the consecutive from string
s="aabbaabbccdddaaabbeee"
rem_du = ""
for char in s:
    if char not in rem_du or char!= rem_du[-1]:
        rem_du += char
print(rem_du)


#5.Count how many times character appears
s="Characterr"
char_count = {}
for char in s:
    if char in char_count:
        char_count[char] +=1
    else:
        char_count[char] =1
print(char_count)


#6.Flip the words in a sentence, not the letter
s="I like python programming"
s_list=s.split(" ")
s_list=s_list[::-1]
flip_sentence = " ".join(s_list)
print(flip_sentence)


#7.Are two string Anagrams:
s1= "ABCDM"
s2= "CDBMA"

#solution1
len_s1=len(s1)
len_s2=len(s2)
s_s1= sorted(s1.lower())
s_s2= sorted(s2.lower())
if len_s1==len_s2 and s_s1 == s_s2:
    print("Is a anagram")
else:
    print("Not a anagram")

#solution2
def character_count(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] +=1
        else:
            char_count[char]=1
    return char_count
if character_count(s1)==character_count(s2):
    print("Anagram")
else:
    print("Not a Anagram")