class student:
    def _init_(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def average(self):
        return (self.m1+self.m2+self.m3)/3
    
s1=student ()
s2=student ()
s1.m1=14
s1.m2=13
s1.m3=19
print(s1.average())

