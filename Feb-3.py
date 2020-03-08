#Iterators and Generators

#Iterable-Collection: An object that produces an iterator via the syntax iter(iterable_collection)
#Example 1 - List
lst = [1,2,3]
lst_iter = iter(lst)
#If we call 'lst_iter' on console
#We get <list_iterator object at xxxxxxxxx>

#Example 2 - string
str ='abc'
s_iter = iter(s)
#If we call 's_iter' on console
#We get <str_iterator object at xxxxxxxxx>
#Key takeaway: list different from list_iterator different from str_iterator different from strings.




#Iterator: An object that exposes a series of values
#Purpose for Iterators is so we can access elements of an iterator from each subsequent call, however we can access the object itself at all (for security).

#Example 1 - List
print(next(lst_iter))
#1
print(next(lst_iter))
#2

#Example 2 - Iterator as a Pointer
#Both iter1 and iter2 will be iterating over the same list
lst_iter1 = iter(lst)
lst_iter2 = iter(lst)
#They are independent of each other and does not affect each other as they have independent indexes of that list lst.
next(lst_iter1)
#1
next(lst_iter1)
#2
next(lst_iter2)
#1

#Example 3 - Simulating a for loop
for item in s:
    print(item)
#We can simulate this for loop by the s_iter.
end = False
while (end == False):
    try: 
        item = next(s_iter)
        print(item)
    except StopIteration:
        end = True
#Simulating a for loop with iterator is a lot more complicated though.

#Example 4 - Simultaing the range(...) function
for elem in range(3,10,0.5):
    print(elem)
#WE can simulate this range function by using function
def my_range(start,stop,step):
    res = []
    curr = start
    while (curr < stop):
        res.append(curr)
        curr += step
    return res
#In the implementation of the range, the ENTIRE sequence:
#Was generated first
#Then stored.
#-------------------------------------------------------Generator----------------------------------------------------------
#So a better way to do this is through Generators:
def f():
    x = 1
    yield x
    x+= 1
    yield x
    x+= 1
    yield x
g =f()
#call g on console
#<generator object f at 0x1045611b0>
print(next(g))
#1
print(next(g))
#2
#Generator is an iterator, that allows us to break the execution.
#When yield is reached, a snapshot of the active data frame is taken and stored.The next call of the generator will resume from that snpshot until yield is reached again.

#Now let's redo the range function with a generator
def my_range(start,stop,step):
    curr = start
    while (curr < stop):
        yield curr
        curr += step 
#With each call, we start from right after the last yield.
#When using generators, we perform *lazy evaluation*


#Now, let's consider the random library
import random;
print(random.randint(0,100))
print(random.randint(0,100))
#With random number GENERATOR, it is a GENERATOR as it holds a conceptually infinite amount of values, it does not create all of them at once and store it.
#Instead, with each call, it produces the next 'pseudo random number' with the given seed.

