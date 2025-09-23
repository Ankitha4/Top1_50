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

#22.Count words in a sentence
sen = "I love python programming"
word_list = sen.split()
count = len(word_list)
count1 = sum([1 for ch in word_list])
print(count)
print(count1)

#without split

in_word = False
con = 0
for ch in sen:
    if ch != " " and not in_word:
        con +=1
        in_word = True
    elif ch == " ":
        in_word = False
print(con)


#23.Remove the specific character
def rem_character(s,ch):
    new_word = ''
    for i in s:
        if i != ch:
            new_word += i
    print(new_word)

rem_character("ankitha","i")

#24.Find the shortest word in the sentence:
def short_word(s):
    s_words = s.split(" ")
    short_w = s_words[0]
    for words in s_words:
        if len(short_w) > len(words):
            short_w = words
    print(short_w)
short_word("Find the shortest word in the sentence")

def short_words(s):
    s_words = s.split()
    min_len = min(len(words) for words in s_words)
    shrt_word = [words for words in s_words if len(words)== min_len]
    print(shrt_word)

short_words("I am at a bar")


def short_words(s):
    s_words = s.split()
    min_len= float("inf")
    for words in s_words:
        if min_len > len(words):
            min_len = len(words)
    short_w = [words for words in s_words if len(words)== min_len]
    print(short_w)

short_words("I am at a bar")

#25.Longest palindromic substring:



