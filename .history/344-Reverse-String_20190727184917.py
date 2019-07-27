def reverseString(s):
    length = len(s)
    for n in range(length//2):
        j = length - n - 1
        s[n],s[j] = s[j],s[n]
    print(s)
    return s

reverseString(["h","e","l","l","o"])