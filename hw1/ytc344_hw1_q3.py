n = 5
#a
def sumOfSmallerSq(n):
    sSum = 0;
    for num in range(1,n):
        sSum += num**2
    return sSum

#b
sum([i**2 for i in range(1,n)])


#c
def sumOfSmallerOddSq(n):
    sSum = 0;
    for num in range(1,n,2):
        sSum += num**2
    return sSum

#d
sum([i**2 for i in range(1,n,2)])

