def compress(s):
    result = ""
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result += s[i - 1] + (str(count) if count > 1 else "")
            count = 1

    result += s[-1] + (str(count) if count > 1 else "")
    return result
def decompress(s):
    result = ""
    i = 0

    while i < len(s):
        ch = s[i]
        i += 1

        num = ""
        while i < len(s) and s[i].isdigit():
            num += s[i]
            i += 1

        result += ch * (int(num) if num else 1)

    return result

text = "AAACCCBBD"

compressed = compress(text)
print(compressed)  
print(decompress(compressed))  
