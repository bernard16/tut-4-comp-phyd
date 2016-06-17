# POWERS OF COMPLEX NUMBERS.
import numpy as ben
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __pow__(self,r): 
        self.r = ben.sqrt(self.real**2 + self.imag**2)
        if self.real==0.0:
            tet = ben.pi/2
        else:
            tet = ben.arctan(self.imag/self.real)
        return Complex(self.r**power*ben.cos(power*tet),
                       self.r**power*ben.sin(power*tet))

    def __str__(self):
        return '(%g,%g)'%(self.real,self.imag)

comp = Complex(5.0,8.0)
power = 3
thepow = comp**power
print 'the complex number is comp', comp
print 'complex number comp the power of ', repr(power)
print 'is ', (thepow)
power = 1/2.0  
thepow1 = comp**power
print 'complex number z the power of ', repr(power)
print 'is ', (thepow1)
