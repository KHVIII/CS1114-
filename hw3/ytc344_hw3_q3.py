def find_duplicates(lst):
    check = [0] * (len(lst))
    dups = []
    for i in lst:
        if check[i] ==0:
            check[i]=1;
        elif check[i] ==1:
            check [i] =2;
            dups.append(i);
    return dups

#worst case run time: n

