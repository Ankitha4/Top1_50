#11.Compress with run-length encoding
def ecd(s):
    result = ""
    count = 1
    prev = None
    for char in s:
        if char == prev:
            count +=1
        else:
            if prev is not None:
                result += prev + str(count)
            prev = char
            count = 1
    if prev is not None:
        result += prev + str(count)
    return result
print(ecd("Aaabbccddeeeddfffffff"))



#12.Most frequent character in a string
def mostfreq(s,n):
    char_count = {}
    new_string = ""
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    n_char = None
    for i in range(n):
        max_freq = 0
        max_char = ""
        for char,freq in char_count.items():
            if freq > max_freq:
                max_freq = freq
                max_char = char

        if max_char is None:  # Not enough unique characters
            return s, None

        # Remove the current max to find the next in next iteration
        del char_count[max_char]
        n_char = max_char

    new_string = ''.join(c for c in s if c != n_char)
    return new_string, n_char
print(mostfreq("aaaaaabebbbbbcccccddddeeeeeeeeeeeeeee",1))



#13.is one string rotation of another
def find_rotation(s1,s2):
    s = s1+s2
    if s2 in s:
        return print(f"{s2} is a rotation of {s1}")
    return print(f"{s2} is not a rotation of {s1}")

find_rotation("ABC","BAC")

#14.Strip all white space:
def strip_whitespaces(s):
    n = len(s)
    without_space = ""
    i = 1
    while i < n:
        if s[i] != ' ':
            without_space += s[i]
        i += 1
    print(f"without whitespace {without_space}")
strip_whitespaces("   sbh hj   ")

