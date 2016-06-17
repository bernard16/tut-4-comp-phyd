
#COMPLEX POWERS TO COMPLEX NUMBERS.
import numpy as ben
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def __pow__(self,other): 
        r = ben.sqrt(self.real**2 + self.imag**2) 
        if (self.real==0 and self.imag==0):
            print ('Error: comp1 can not be zero, ZeroDivisionError')
            return 'nan'
        if self.real==0.0: 
            tet = ben.pi/2
        else:
            tet = ben.arctan(self.imag/self.real)
        return Complex(ben.exp(other.real*ben.log(r)-other.imag*tet)*ben.cos(other.real*tet + other.imag*ben.log(r)),
                       ben.exp(other.real*ben.log(r)-other.imag*tet)*ben.sin(other.real*tet + other.imag*ben.log(r)))
    
    def __str__(self):
        return '(%g,%g)'%(self.real,self.imag)
    
    
comp1 = Complex(5.0,8.0)
comp2 = Complex(3.0,-1.0)
thepow = comp1**comp2
print 'complex number comp1 is ', comp1
print 'complex number comp2 is ', comp2
print 'complex comp1 the power of comp2 is ', thepow
