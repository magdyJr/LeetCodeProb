class Solution:
    def myAtoi(self, s: str) -> int:
        #output list
        output=[]
        #flag for positive or negative sign
        PosOrNeg=True
        # flag for uniqueness of the sign 
        uniqSign=False
        # flag for uniqueness of floatng point 
        uniqFloatingPoint=False
        #removing white spaces
        newStr=s.strip()

        #checking if the string is empty
        if len(newStr) < 1:
            return 0
        
        #else if the new string 1 char then we check if its a digit then we add it
        elif len(newStr) < 2:
            if newStr.isdigit():
                return int(newStr)
            else :
                return 0
        
        #else if the new string 2 char then 
        # we check if the first char is digit then we check if the second char is digit then we add them
        # else if the first char is a sign the we check the second is a digit then we add them
        elif len(newStr) < 3:
            if newStr[0].isdigit():
                output.append(newStr[0])
                if newStr[1].isdigit():
                    output.append(newStr[1])
            elif newStr[0]=='+' :
                if newStr[1].isdigit():
                    output.append(newStr[1])
                else : return 0
            elif newStr[0]=='-' :
                PosOrNeg=False
                if newStr[1].isdigit():
                    output.append(newStr[1])
                else : return 0
            else : return 0
        
        #else if the string is more than 2 chars we loop throw them
        #if we see any chars we break the loop
        # if a digit we add it to the list
        # if a its a sign we rise a unique flag and positive or negative flag
        # if its a "." we add it and rise unique flag
        else :
            for char in newStr:
                if char=='+' and not output:
                    #if uniqSign flag is raised then we break the loop and skip all remaining chars
                    if uniqSign:
                        break
                    PosOrNeg=True
                    uniqSign=True
                elif char=='-'and not output:
                    #if uniqSign flag is raised then we break the loop and skip all remaining chars
                    if uniqSign:
                        break
                    PosOrNeg=False
                    uniqSign=True
                elif char.isdigit() or (char =='.'and output):
                    if char=='.' and  not uniqFloatingPoint:
                        output.append(char)
                        uniqFloatingPoint=True
                    elif char.isdigit():
                        output.append(char)
                    else : break
                    
                else: break
        # we check if output list empty if its then return 0
        if output :
            finalOutput=0
            #if the PosOrNeg flag is raised the output is positive
            if not PosOrNeg:
                finalOutput=int(float('-'+''.join(output)))
                # if the output <-2**31 we make it equals to -2**31
                if finalOutput < -2**31 :
                    return -2**31
                else : return finalOutput
            else:
                finalOutput=int(float(''.join(output)))
                # if the output > 2**31 -1 we make it equals to 2**31 -1
                if finalOutput > (2**31) -1 :
                    return (2**31) -1
                else : return finalOutput
        else : return 0



#TestCases
sol =Solution()
print(sol.myAtoi('42'))
print(sol.myAtoi('      -42'))
print(sol.myAtoi('4193 with words'))
