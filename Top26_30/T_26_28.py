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

#27.Find the largest and smallest element in array
num_arr = [25,78,89,90,20,-3,0]
def lar_small(num_arr:list):
    largest = smallest = num_arr[0]
    for num in num_arr:
        if smallest >num:
            smallest= num
        elif largest < num:
            largest = num
    print(f"largest : {largest} , smallest : {smallest}")


lar_small(num_arr)