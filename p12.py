## python program to find positon of nth multiple of number k in febunacci series 
# SHVAIB KHAN(22BEE035)

def findposition(k,n):
    a=0
    b=1

    i=2
    while i!=0:
        c=a+b
        a=b
        b=c

        if b % k == 0:
            return n*i
        
        i+=1

    return    
 # multiple number 
n=5;
# number of whose multiple we are finding 
k=4;
text='position of { 4}th multiple of {5 } in fibunacci series is:'
print(text,findposition(k,n))


