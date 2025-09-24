#26.reverse array in place
from typing import Tuple, Any

ar = ["A", "N", "K", "I", "T", "H", "A"]
ar = ar[::-1]
print(ar)


def reverse_array(a: list):
    left, right = 0, len(a) - 1
    while left < right:
        a[left], a[right] = a[right], a[left]
        left += 1
        right -= 1
    return a


reverse_array(["A", "N", "K", "I", "T", "H", "A"])


#27.Find the largest and smallest element in array

def lar_small(num_arr: list):
    largest = smallest = num_arr[0]
    for num in num_arr:
        if smallest > num:
            smallest = num
        elif largest < num:
            largest = num
    print(f"largest : {largest} , smallest : {smallest}")


num_arr = [25, 78, 89, 90, 20, -3, 0]
lar_small(num_arr)

#28.Check for duplicates in array
ary = [200, "d", "900", "d", 90, 200, 8, 77]
non_dup = []
for i in ary:
    if i not in non_dup:
        non_dup.append(i)
print(non_dup)
