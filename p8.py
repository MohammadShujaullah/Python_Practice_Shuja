# 8.PYTHON PROGRAM TO PRINT ALL  prime in an interval
 
def prime(starting_range,ending_range):
    list=[]
    flag=0
    for i in range(starting_range,ending_range):
         for j in range(2,i):
             if i%j==0:
                 flag=1
                 break
             else:
                 flag=0 
             
         if flag==0:
               list.append(i)
                 
    return list
            ## driver program
starting_range= 2
ending_range= 17

list=prime(starting_range,ending_range)
if len(list) == 0:
    print("there are no prime no. in this range ")
else:
    print("the prime no. in this range are ",list)    
