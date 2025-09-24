#26.reverse array in place
ar = ["A", "N", "K", "I", "T", "H", "A"]
ar = ar[::-1]
print(ar)

def reverse_array(a:list):
    left,right = 0, len(a)-1
    while left<right:
        a[left], a[right]= a[right],a[left]
        left +=1
        right -=1
    print(a)


reverse_array(["A", "N", "K", "I", "T", "H", "A"])
