class A():
    def talk(self):
        print ('hi from A')

class AA:
    def talk(self):
        print ('hi from AA')
class B(A):
    def talk(self):
        print ('hi from B')
        
class C(AA, A):
    def talk(self):
        print ('hi from C')
        
class D(B):
    def talk(self):
        print ('hi from D')

class O(A):
    def talk(self):
        print ('hi from O')
                
class F(C, O):
    def talk(self):
        print ('hi from F')


class G(F, D):
    def talk(self):
        print ('hi from G')

g=G()

g.talk()

print(G.mro())

A.talk(g)
       
