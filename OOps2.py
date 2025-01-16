class computer :
    def _init_(self,CPU,ram):
        self.CPU=CPU
        self.ram=ram

    def config(self):
        print('the configuration is ',self.CPU,self.ram)

c1=computer()
c2=computer()

c1.CPU='i5'
c1.ram=16

print(c1.config())


    
        