## 11 number is fibonacci or not
 
import math 
def isperfectSquare(number):
    s=int(math.sqrt(number))       ##(5*n*n+4)or (5*n*n-4) must be 
                                    ##  a perfect square ,then number is fibbunacci
    return s*s==number



def isfibunacci(number):
    if isperfectSquare(5*number**2+4) or isperfectSquare(5*number**2-4):
        return True
    else:
        return False
    


number=int(input("enter the value of number to check:"))
if isfibunacci(number):
    print(number,"is afibunacci number")
else:
    print(number,"is not a fibunacci number")
