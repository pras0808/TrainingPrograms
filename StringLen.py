def longest_substring(s):
    seen = {}
    start = 0
    max_len = 0
    for end in range(len(s)):
        if s[end] in seen and seen[s[end]] >= start:
            start = seen[s[end]] + 1
        seen[s[end]] = end
        max_len = max(max_len, end - start + 1)
    return max_len

s = input("Enter string: ")
print(longest_substring(s))
