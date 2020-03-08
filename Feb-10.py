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

def linear_search(lst,val):
    for i in range (len(list)):
        if (lst[i] == val):
            return i;
    return None;
#None is a special object

def binary_search(lst,val):
    #ASSUMING ST IS SORTED
    left = 0;
    right = len(lst) - 1
    ind = None;
    found = false;
    while ((found == false) and left <=right):
        mid = (left+right)//2
        if (lst[mid] == val):
            ind = mid;
            found=True;
        elif (val<lst[mid]):
            right = mid -1;
        else:
            left = mid + 1;
    return ind;



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
# str + str -> THETA (N)
# int + int -> THETA (1)

#However, if we make a copy of a list of CONSTANT SIZE, e.g.
lst4 = (lst1.copy()) * 10
#It is THETA (1), because there are always 10 elements in the list we copy, with each extra N, we increase 10 operations CONSTANTLY.
##Same thing with string

#We seperate our operations into different parts for better results.

#When doing a search, since we 'depend' on luck, we have 3 different cases.- THIS IS FOR LINEAR SEARCH
#Best Case: THETA (1) - The first thing I search, I find it.
#Worst Case THETA (N) - I search everything and it's not in there.
#Average Case: THETA (N/2 -> N) - On average, we need to search through half the list

#- FOR BINARY SEARCH
#Best Case: THETA (1)
#Worst Case: THETA (Log base 2 of N)
#Average Case: THETA (Log base 2 of N)




