import numpy 

class NBody:
    def __init__(self, m, partno, G=1.0):
        
        self.dat = {}
        self.dat['m'] = m
        self.dat['partno'] = partno
        self.dat['G'] = G
        
        self.m = numpy.ones(self.dat['partno'])*m
        self.xpos = numpy.random.randn(self.dat['partno']) 
        self.ypos = numpy.random.randn(self.dat['partno'])
                    
    def p_energy(self):
        PE = 0
        for i in range(self.dat['partno']):
            PE += self.dada['G']*self.m[i]*self.m[i+1]/(numpy.sqrt(self.xpos[i]**2 + self.ypos[i]**2))
        return PE

if __name__=='__main__':
    sys = NBody(10.0,50,1.0)
    print 'the system has', repr(sys.dat)
    print 'm as array is ', repr(sys.m) 
    print 'the x positions are ', repr(sys.xpos)
    print 'the y positions are ', repr(sys.ypos)
    print 'the method is ', repr(sys.p_energy)
                        
                             
                             

                                                                  
        
