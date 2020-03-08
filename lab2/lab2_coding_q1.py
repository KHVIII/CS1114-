class Poly:
    def __init__(self,lst=[0]):
        self.poly = lst
    def __getitem__(self, j):
        return self.poly[j]
    def __setitem__(self, j, val):
        self.poly[j] = val
    def __len__(self):
        return len(self.poly);
    def __add__(self,other):
        if len(self) >= len(other):
            nPoly = Poly([0]*len(self))
            for i in range (len(self)):
                if i < (len(other)):
                    nPoly[i] = self[i]+other[i]
                else:
                    nPoly[i] = self[i]
            return nPoly
        else:
            return other.__add__(self);
    def __call__(self,x):
        return sum([self[i] * (x**i) for i in range(len(self))])
        

    
