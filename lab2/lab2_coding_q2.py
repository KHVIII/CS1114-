class UnsignedBinaryInteger:

    def __init__(self,bin_num_str):
        self.data = bin_num_str
    def __getitem__(self, j):
        return self.data[j]
    def __setitem__(self, j, val):
        self.data[j] = val
    def __len__(self):
        return len(self.data)
    def __int__(self):
        return int(self.data)
    def __add__(self,other):
        if len(self) >= len(other):
            rSumInBinary =([int(i) for i in str(int(self)+int(other))])
            rSumInBinary.reverse();
            rSumInBinary.append(0)
            for index in range (len(rSumInBinary)-1):
                rSumInBinary[index+1] += (rSumInBinary[index]//2)
                rSumInBinary[index] = str(rSumInBinary[index] % 2)
            nUBI = rSumInBinary[-1::-1]
            if nUBI[0] == 0:
                nUBI.pop(0)
            else:
                nUBI[0] = '1'
            nUBI = ''.join(nUBI)
            nUBI = str(nUBI)
            return(UnsignedBinaryInteger(nUBI))
        else:
            return other.__add__(self);
    def decimal (self):
        return sum([(int(self[-i-1]) * 2**i) for i in range(len(self))])
    def __lt__(self,other):
        if self.decimal() < other.decimal():
            return True
        else:
            return False
    def __eq__(self,other):
        if not (self < other or other < self):
            return True
        else:
            return False
    def __gt__(self,other):
        if not (self == other or self < other):
            return True
        else:
            return  False
    def is_twos_power(self):
        if (self.data).count('1') < 2 :
            return True
        else:
            return False
    def largest_twos_power(self):
        tempBi = '1'+'0'*(len(self)-1)
        return (UnsignedBinaryInteger(tempBi)).decimal();
    def __repr__(self):
        return ('0b'+self.data)
    
