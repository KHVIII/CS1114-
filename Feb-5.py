#Iteration

#Representation of a List Iteration.
class list_iter:
    def __init__(self,ls):
        self.ls = ls;
        self.index = 0;
    def next():
        if self.index < len(self.ls):
            index = self.index;
            self.index+=1;
            return self.ls[index];
        else:
            raise StopIteration;
#List_iter uses index as a pointer, each time next is called, pointer moves down, until len is reached.
        
        

def func():
    ls=[1];
    for item in ls:
        print(item);
        ls.append(item+1);

def main():
    func();
#main();
#This gives an infinite loop because the pointer is always one step behind the len of the list.
    #As we learned, for is just a fancy while loop which acts as a pointer/iterator that stops at StopIteration (pointer index = len).


#Python - C++
#try - try
#raise - throw
#except - catch
#We can use the C++ terminology to remember their functionalities better.
#Raise(throw) expects an Error and Except (catch) will catch that Error and the program jumps to the Except of the type of error 'raise' have threw.
#This makes it easier across different functions / main.


#-------------------------------Asymptotic Analysis---------------------------------------
#How do we measure / compare algorithms with each other.
#We use n as the amount of work we do, relative to time
#If n work cost x time, then how much does n+1 work cost?


#Primality Testing
    #Version I: Checks n numbers to find a divisor
    #Version II: Checks n/2 numbers to find a divisor (cuz no integer compliment divisor once we go more than n/2)
        #1,2,3,.....n/2{.....num}
        #               ^this is k
        #Let k be a divisor of num in the second half of the range. That is, k> num/2
        #Let d be k's complementary divisor, therefore d = num/k
        #We have: d=num/k < num/(num/2) = num * 2/num = 2.
        #Therefore d<2, since d is a divisor, we get that d = 1;
        #So k = n and d = 1.
    #Version III:
        #1,2,3,...sqrt(num){....,num}
        #                   ^assume k and d in here
        #It is impossible for k and d both be bigger than sqrt(num) as
        #k * d = n, [k > sqrt(n)] & [d > sqrt(n)], so k*d > [sqrt(n)]^2, so k*d > n.
            #k and d, one needs to be bigger than sqrt(num), the other one is smaller. **********************
        #So we just need to find divisors smaller than sqrt(n), then we can use math to find all of their compliment divisors.


#Runtime Analysis
    #The running time depends on the input
        #If time = x when input size = n, then would the time for 2n be 2x?
        #We parameterize the running time by the size of the input.
    #The running time depends on the operators we use, and on the types of the data they are applied on.
        #Our analysis uses an abstract model, that ignores machine-dependent constants.
            #   ***We count each primitive operation as 1***
                #Primitive operations like addition, comparison, multiplication and stuff.
    #The running time depennds on the machine's hardware technology
        
