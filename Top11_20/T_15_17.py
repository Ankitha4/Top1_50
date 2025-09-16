#15.valid shuffle?
def str_shuffle(s:str,indices:list[int])->str:
    n = len(s)
    shuffle = ['']*n
    for i in range(n):
        shuffle[indices[i]] = s[i]
    return "".join(shuffle)

print(str_shuffle("codeleet",[4,5,6,7,0,2,1,3]))

#16.covert the text to asii


