def factors(num):
    import math
    lst=[0]*(int(math.sqrt(num)))
    for i in range(1,int(math.sqrt(num))+1):
        if (num % i == 0):
            if (i != num//i):
                lst[-i]= num//i
            yield i
    for q in lst:
        if q != 0:
            yield q;
        
