#this was my first problem and it was easy on diff
def plaindromefun(x):
    #here we get the abs value of num and then we reverse it and compare it with the actually number
    return x==int( str( abs(x) )[::-1] ) 


print(plaindromefun(121))
print(plaindromefun(56663))
print(plaindromefun(3333))
print(plaindromefun(55))
print(plaindromefun(1))