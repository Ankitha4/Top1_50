#15.valid shuffle?
def str_shuffle(s:str,indices:list[int])->str:
    n = len(s)
    shuffle = ['']*n
    for i in range(n):
        shuffle[indices[i]] = s[i]
    return "".join(shuffle)

print(str_shuffle("codeleet",[4,5,6,7,0,2,1,3]))

#16.covert the text to title case properly
def title_case(s:str)-> str:
    word_list = s.split()
    title_string = []
    for word in word_list:
        if word:
            title_string.append(word[0].upper()+word[1:].lower())
        else:
            title_string.append(" ")
    return " ".join(title_string)

print(title_case("How is the $cod4e"))

def title_case_without_builtin(s:str):
    words_list= s.split()
    title_string= []

    def upper_case(s):
        upper = ""
        for char in s:
            if 'a'<= char <='z':
                upper += chr(ord(char)-32)
            else:
                upper += char
        return upper

    def lower_case(s):
        lower = ""
        for char in s:
            if 'A'<=char<='Z':
                lower += chr(ord(char)+32)
            else:
                lower += char
        return lower

    for word in words_list:
        if word:
            title_string.append(upper_case(word[0])+lower_case(word[1:]))
        else:
            title_string.append(" ")
    return " ".join(title_string)

print(title_case_without_builtin("How is the $cod4e"))

