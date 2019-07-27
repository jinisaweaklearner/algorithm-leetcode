def reverseString(s):


    for n in range(len(s)//2):

        s[n],s[len(s)-n-1] = s[len(s)-n-1],s[n]
    print(s)
    return s

reverseString(["h","e","l","l","o"])