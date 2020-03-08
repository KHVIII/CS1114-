class Vector:
    def __init__(self, d):
        #a
        if isinstance(d,int): 
            self.coords = [0]*d
        else:
            self.coords = d[:]
        
    def __len__(self):
        return len(self.coords)
    def __getitem__(self, j):
        return self.coords[j]
    def __setitem__(self, j, val):
        self.coords[j] = val
    def __add__(self, other):
        if (len(self) != len(other)):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    #b
    def __sub__(self, other):
        if (len(self) != len(other)):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    #d
    def __mul__(self,m):
        if isinstance(m,int):
            result = Vector(len(self))
            for j in range (len(self)):
                result[j] = self[j]*m
            return result
        elif (len(self) != len(m)): #assume other is Vector object
            raise ValueError('dimensions must agree')
        else:
            tempLst = [m[j]*self[j] for j in range(len(self))]
            return sum(tempLst)
                

    #e
    def __rmul__(self,m):
            return (self.__mul__(m));
    
    def __eq__(self, other):
        return self.coords == other.coords
    def __ne__(self, other):
        return not (self == other)
    def __str__(self):
        return '<'+ str(self.coords)[1:-1] + '>'
    def __repr__(self):
        return str(self)
    #c
    def __neg__(self):
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = -self[j]
        return result

    
    
