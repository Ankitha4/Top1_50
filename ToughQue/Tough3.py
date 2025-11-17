#print the integers as per the count present above
s="A3S4G2"
s=list(s)
alp = ""
digit=0
result=""
for idx,i in enumerate(s):
    if i.isdigit():
        digit=int(i)
        alp = s[idx-1]
        j=0
        while j<digit-1:
            result +=alp
            j +=1
    else:
        result +=i
print(result)

#or

s1="A3B4C2"
letter=""
count=0
res=""

for i in range(0,len(s1),2):
    letter = s1[i]
    count= int(s1[i+1])
    res +=letter* count
print(res)
