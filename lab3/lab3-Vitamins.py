#1a:  8n^2 > (n^2 + 5n -2)
#1b: 2n > (n^2-1)/(n+1)
#1c: 10n> (\sqrt(5n^2 - 3n + 2)) > n

#2a: True, 8n^3 > 8n^2(\sqrt(n))
#2b: False
#2c: True, 18log(n) > (16log(n^2) +2)

#3a: n
#3b: n
#3c: n^3
#3d: n^(3/2)
#3e: n^2

#1
def reverse_list(lst):
    for i in range(len(lst)//2):
        lst[i],lst[-i-1]=lst[-i-1],lst[i]

#2
def move_zeros(nums):
    for i in range(len(nums)):
        if nums[i] == 0: nums.append(nums.pop(i));

#3a: n^2
#3b:
def find_missing(lst):
    n = len(lst)
    return((n*(n+1)//2)-sum(lst))
        
            
    
