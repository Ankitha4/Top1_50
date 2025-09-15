#8.longest substrings without repeats

def longest_unique_substring(s):
    seen = {}          # Store last seen index of each character
    start = 0          # Start index of current substring window
    max_len = 0        # Length of longest substring
    max_substr = ""    # The longest substring

    for i in range(len(s)):
        char = s[i]

        # If the character is repeated inside the current window
        if char in seen and seen[char] >= start:
            start = seen[char] + 1  # Move start to after the previous index of char

        seen[char] = i  # Update last seen index
        window_len = i - start + 1

        if window_len > max_len:
            max_len = window_len
            max_substr = s[start:i+1]

    return max_substr
print(longest_unique_substring("abcdeabfghu"))
#or
def longest_substring_without_repeat(s):
    char_set = set()
    l = 0
    max_len = 0
    start_idx = 0  # To remember where the longest substring starts

    for r in range(len(s)):
        while s[r] in char_set:
            char_set.remove(s[l])
            l += 1
        char_set.add(s[r])

        if (r - l + 1) > max_len:
            max_len = r - l + 1
            start_idx = l

    # Extract the substring from start_idx with length max_len
    longest_substr = s[start_idx:start_idx + max_len]
    print("Longest substring without repeats:", longest_substr)
    print("Length:", max_len)
# Test the function
longest_substring_without_repeat("abcdaed")



#9.get all the substrings in the string and get print the palindrome
s= "Programming"
sub_s=[]
count = 0
for i in range(0,len(s)):
    for j in range(i+1,len(s)+1):
        sub_s.append(s[i:j])
        count +=1
        print(f"substring \"{s[i:j]}\" with {count}")
print(sub_s)
print(f"The total substring count is {count}")



#10.Implement your own atoi
def my_atoi(s: str) -> int:
    i = 0
    n = len(s)
    result = 0
    sign = 1

    # 1️⃣ Skip leading spaces
    while i < n and s[i] == ' ':
        i += 1

    # 2️⃣ Handle sign if present
    if i < n and (s[i] == '+' or s[i] == '-'):
        sign = -1 if s[i] == '-' else 1
        i += 1

    # 3️⃣ Convert characters to integer until a non-digit
    while i < n and s[i].isdigit():
        digit = ord(s[i]) - ord('0')
        result = result * 10 + digit
        i += 1

    return sign * result
print(my_atoi("-1256vbY4"))


#OR

def myAtoi(s:str)->int:
    # strip the white space
    s = s.strip()
    if not s:
        return  0
    #Handle sign if present
    i=0
    sign = 1
    if s[i]=="+":
        i+=1
    elif s[i]=="-":
        i +=1
        sign = -1
    parsed = 0
    while i <len(s):
        cur = s[i]
        if not cur.isdigit():
            break
        else:
            parsed = parsed *10 + int(cur)
        i=i+1
    return  parsed*sign


print(myAtoi("-12343vbg78"))
