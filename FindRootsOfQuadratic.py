import math 
a,b,c=1,-5,6
disc=b*b-4*a*c
d=math.sqrt(disc)

if d==0:
    x1=x2=-b/(2*a)


elif   d>0:
        x1=(-b-d)/(2*a)
        x2=(-b+d)/(2*a)
        print('the roots are real and unequal',x1,x2)

else:
      print('the roots are complex ')