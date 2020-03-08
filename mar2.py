#recursion
#A problem solving method where the solution is a combination of all smaller instances of the same problem.
#Consider 3 Steps:
    #The 'base' case
        #The ending point, the most simple input to output.
            #Identify how to measure the size of the input
            #Find the condition testing for the smallest possible input
            #Formulate the solution of the problem for the smallest possible input
    #The 'simple' case
        #One small instance that repeats throughout recursion 
    #The reduction of the set by simple case towards the base case.



#E.g.
def count_up(start,finish):
    if end<start:
        return;
    else:
        print(start);
        count_up(start+1,end);
    #theta(N)

def count_down(start, end):
    if end<start:
        return;
    else:
        count_down(start+1, end);
        print(start);

def count_up2(start,end):
    if start==end:
        print(end);
    else:
        mid = (start+end)//2
        count_up2(start,mid)
        count_up2(mid+1,end);

def factorial(n):
    if (n==1 or n==0):
        return 1;
    return n*factorial(n-1);
