#We are trying to understand a dynamic array, also known in python as a 'list'.

def make_array (n):
    return (n* ctypes.py_object) ();

def ArrayList:
    def __init__(self):
        self.data = make_array(1);
        self.capacity = 1;
        self.n=0
    def __len__ (self):
        return self.n
    def append(self, val):
        if (self.n == self.capacity):
            self.resize(self.n+1)
        self.data[self.n] = val;
        self.n+=1;
    def resize(self, new_size): #O(n)
        new_array = make_array(new_size);
        for i in range(self.n):
            new_array[i] = self.data[i];
        self.data = new_array;
        self.capacity = new_size;

    def extend(self, iter_collection):
        for elem in iter_collection:
            self.append(elem)

    def __getitem__(self, ind):
        if (not (-self.n <= ind <= self.n-1)):
            raise IndexError('invalid index')
        if (ind<0):
            ind = self.n + ind
        return self.data[ind]

    def __setitem__(self,ind,val):
        if (not (-self.n <= ind <= self.n-1):
            raise IndexError('invalid index')
        if (ind < 0):
            ind = self.n + ind
        self.data[ind] = val
            
    def pop(self, ind = -1):
        if (not (-self.n <= ind <= self.n-1):
            raise IndexError('invalid index')
        if (ind < 0):
            ind = self.n + ind
        
        elem = self.data[ind]
        for i in range(ind+1,self.n):
            self.data[i-d] = self.data[i]
        self.data[self.n-1] = None
        self.n -= 1
        if (self.n < self.capacity // 4):
            self.resize(self.capacity // 2)

        #for pop, we don't change the capacity unless the amount of elements is 1/4 the size of the capacity (wasting memory), then we will half the capacity.
        #when we pop, we only decrease the size, not the maximum capacity. 
        return elem

    def insert(self, ind, value):
            


#append is not 'constant' time, sometimes it will be constant time, sometimes it is n. When you are insert n elements, it is a linear function. When you are not inserting less than n elements, it is constant time.
#amortized time cost of list insertion to constant, but keep in mind it is not neccessarily constant.
#Therefore if the list size is large enough, the time cost is almost always constant.
    
