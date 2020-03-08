def split_parity(lst):
    oddNums = 0;
    for i in range(len(lst)):
        if lst[i]%2 == 1:
            lst[oddNums],lst[i] = lst[i],lst[oddNums]
            oddNums += 1;

            
