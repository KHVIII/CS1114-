#A: Different ways of creating a list based off another List -------------------------------

#say we have 
lst1=[1,2,3]
#We have 2 ways of creating 2 lists based off of it, a copy(deep or shallow) or a reference.

#1: Copy, which means changes to either list will not affect the other
lst2=lst1.copy()

#2: Reference, which means changes to either list WILL affect the other
lst3=lst1

'''
Try modifying lst1 and see the effect it has on both lst2 and lst3.
Key Concept: the '=' operator assigns value while 'copy' duplicates.
'''

#B: Deepcopy vs Shallow Copy -------------------------------

#say we have
lst1=[1,2,3]
lst2=[4,5,6]
lst3=[lst1,lst2]
#In the copy method, we also have two ways to duplicate - Shallow vs Deep.

#1: Shallow, which just duplicates the content in the referenced list.This means changes to the content inside the referenced list could still impact the shallow copy.
lst4 = lst3.copy() #When lst1 & lst2 changes, lst4 will change as well.

#2: Deep, which goes down all the way to int. This means changes to the content inside the referenced list WILL NOT impact the deep copy.
import copy
lst5=copy.deepcopy(lst3)

'''
For the purpose of this course, deepcopy is more resource & cpu intensive than shallowcopy.
'''

#C: Squares List -------------------------------

def squares_list(n):
    ls=[];
    for i in range(1,n+1):
        ls.append(i*i);
    return ls;

def squares_list2(n):
    return[i*i for i in range(1,n+1)]; # list comprehension

#squares_list and squares_list2 will produce the same result.
#But squares_list2 is a lot easier to write,

'''
List Comprehensive is GENERALLY faster
'''

#D: List Comprehension Exercise-------------------------------

def tens_list(n):
    return [10*i for i in range (1,i+1)];

def shallow_copy(ls):
    return [elem for elem in ls];

#E: More Complex List Comprehension -------------------------------

def factors_list(n):
    ls=[];
    for i in range(1,n+1):
        if (n%i == 0):
            ls.append(i);
    return i;

def factors_list2(n):
    return ([i for i in range(1,n+1) if (n%i==0)])

#F: List COmprehension Formula **** ------------------------------- ****
#From above exercises, we can conclude a general formula for list comprehensions.

# [ (values) for (values2) in (data structure) if (conditional) ] The 'if (conditional)' is optional
    #values  and  values2 does not have to be the same.

#G: 'List Comprehension'in Created Objects -------------------------------
class Counter:
    def __init__(self):
        self.value=0;
    def inc(self):
        self.value+=1;
    def __repr__(self):
        return str(self.value);
def main():
    c1 = Counter();
    c1.inc();
    print('C1:',c1);
    c1.inc();
    c1,inc();
    print('C1:',c1);
    c2 = Counter();
    c2.inc();
    print('C2:',c2);

    A = [Counter()]*3
    for c in A:
        c.inc();
        print ('C:',c);
    #printing this will give C:1 C:2 C:3.
    #Because there is only one Counter object created and all others are merely COPIES.

    
    A = [Counter()] + [Counter()] + [Counter()]
    for c in A:
        c.inc()
	print('C',c)
    #Printing this will give C:1 C:1 C:1.
    #Because there is 3 Counters seperately created.
    #Another way to write this is by List Comprehension
    B = [Counter() for i in range(3)]
    for c in A:
        c.inc();
        print('C',c)
    #C:1 C:1 C:1


#H: DeepCopy & ShallowCopy with List Comprehension -------------------------------
A=[1,[2,3],[4,5]]
B=[item for item in A]; #Creates a shallow Copy
C=copy.deepcopy(A); #Creates a deep Copy

A[0]=10 #changes value, no change to B and C
A[1]=[20,30] #changes reference, no change to B and C
A[2,1]=50 #changes the value inside REFERENCE, change to B but not C.

#I: ENUMERATURE **** ------------------------------- ****
mat = [[1,2,3],
       [4,5,6],
       [7,8,9]];
diag = [mat[i][i] for i in range(len(mat))]
#or
diag2 = [row[ind] for (ind,row) in enumerate(mat)]; #enumerate gives a data struct containing tuples of (index,content) from a list
#Enumerate is slower because it creates sort of creates a seperate list.














