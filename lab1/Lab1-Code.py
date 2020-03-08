import math
import secrets
def add_binary(bin_num1, bin_num2):
    decSum = int(bin_num1,2) + int(bin_num2,2)
    times = math.floor((math.log(decSum,2))) + 1
    digList = [str(((decSum//(2**i)) % 2)) for i in range (times)]
    digList.reverse()
    binSum = ''.join(digList)
    return binSum


def can_construct (word, letters):
    word = [i for i in word]
    for letter in letters:
        if letter in word:
            word.remove(letter)
    if word == []:
        return True
    return False

class Complex:
    def __init__(self, a, b):
        self.real = a
        self.imag = b
    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)
    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)
    def __mul__(self,other):
        tempImag = self.real * other.imag + other.real * self.imag
        tempReal = self.real * other.real + other.imag * self.imag * -1
        return Complex(tempReal,tempImag)
    def __repr__(self):
        sign = '+'
        if self.imag < 0:
            sign = '-'
        cNumber = '{} {} {}i'.format(str(self.real),sign,str(abs(self.imag)))
        return cNumber



def create_permutation (n):
    ogList = [i for i in range(n)]
    newList = []
    while ogList != []:
        tempInt = (secrets.choice(ogList))
        ogList.remove(tempInt)
        newList.append(tempInt)
    return newList

def scramble_word(word):
    newWord=''
    for index in create_permutation(len(word)):
        newWord += word[index]
    return newWord

def main(word='pokemon'):
    
    print('Unscramble the word:  {}'.format((' '.join([i for i in (scramble_word(word))]))))
    tryNum = 1
    guess = input('Try #{}: '.format(str(tryNum)))
    while (guess != word):
        print('Wrong!')
        tryNum += 1;
        guess = input('Try #{}: '.format(str(tryNum)))
        
    print('Yay, you got it!')
    
    
