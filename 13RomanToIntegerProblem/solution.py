def romanToInt( s: str) -> int:
    symboldict={'I':1, 'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    total=0
    for pos , ch in enumerate(s):
        if(pos+1!=len(s)):
            #we just checking if the next char is bigger than current if true we add if false we subtract
            if symboldict[s[pos+1]] > symboldict[s[pos]]:
                total-=symboldict[ch]
            else:
                total+=symboldict[ch]
        else:
            total+=symboldict[ch]
    return total



print(romanToInt('III'))
print(romanToInt('LVIII'))
print(romanToInt('MCMXCIV'))
