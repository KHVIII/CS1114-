def mysum(ls):
    acc=0;
    for item in ls:
        acc+=item;
    return acc;

def func(ls):
    acc = mysum(ls);

#func and mysum same runtime, n

def func2():
    ls = [];
    for i in range(10): #THETA (N)
        ls.append(i);

    for item in ls: #THETA (N)
        print(item);
#Even though the exact number of operations is 2N + 1, when we talking about THETA(), we only get the largest order, which is N in this case. 

def func3():
    ls = [];
    for i in range(10): #THETA (N) 
        ls = ls+[i]; #THETA (N) since to add two lists, we need to make a copy of ls everytime, which requires to go through N elements. 
    return ls;
#Since there is a N elements operation inside another N elements operation, the overall THETA() is N^2. 


#func3 is worse than func2,


def print_square(n):
    for i in range(1,n+1):
        line = '*'*n;
        print(line)

def print_triangle(n):
    for i in range(1,n+1):
        line = '*'*i
        print(line);

#print_square is always worse as it is printing n stars for n times ->n*n
#print_triangle is printing 1,2,....n -> 1+2+3+....+ n
#However, the runtime for square is n^2, for triangle is n(n-1)/2
        #which means their theta, are both n^2, so their growth is the same.

def prefix_average1(lst):
    n = len(lst);
    res = [0]*n;
    curr_sum = 0;
    for j in range(n);
        curr_sum += lst[j];
        curr_average = curr_sum/(j+1);
        res[j] = curr_average;
    return res
#n

def prefix_average2(lst):
    n = len(lst);
    res = [0]*n;
    curr_sum = 0;
    for j in range(n):
        curr_sum = sum(lst[0:j+1])
        curr_average = curr_sum/(j+1);
        res[j] = curr_average;
    return res;
#n^2

#average1 has better runtime as every loop we are only adding once
    #for average2, every loop we are adding increasingly more.



#--------------------Big Takeaways---------------
lst1 = [1,2,3]
#if we copy a list, e.g.
lst2 = lst1 + [4]
#We are doing THETA (N) operations, where N is the number of items in lst1

#if we assign a list e.g.
lst3 = lst1
lst3.append(4)
#We are doing a CONSTANT operation, since assignment is one primitive operation, and so is append.

# lst + lst -> THETA (N)
# int + int -> THETA (1)

