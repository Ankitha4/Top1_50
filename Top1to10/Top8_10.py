#longest substrings without repeats
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