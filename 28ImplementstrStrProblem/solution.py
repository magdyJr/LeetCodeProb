def strStr(haystack: str, needle: str) -> int:
    #checking if the needle is empty and using strip to remove spaces from right and left
    if not needle.strip():
        return 0
    # here we use find fun to get the fist occurence of the needle
    else:
        return haystack.find(needle)

#testcases
print(strStr('hello','ll'))
print(strStr('hello',' '))
print(strStr('aaaaaa','bba'))
print(strStr('hello hello','ll'))