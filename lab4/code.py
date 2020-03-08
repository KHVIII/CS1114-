###1
def is_palindrome(s):
    for i in range(len(s)//2):
        if s[i] != s[-(i+1)] :
            return False
    return True



###2
def reverse_vowels(input_str):
    tempList = list(input_str)
    vowelInd = []
    for i in range(len(input_str)):
        if tempList[i] in 'aeiou':
            vowelInd.append(i)
    for i in range(len(vowelInd)//2):
        tempList[vowelInd[i]],tempList[vowelInd[-(i+1)]] = tempList[vowelInd[-(i+1)]], tempList[vowelInd[i]]

    output = ''.join(tempList)
    return output,vowelInd







###3
def find_shift(lst):
    left = 0
    right = len(lst) - 1

    while left <= right:
        mid = (left + right) //2

        if right - left == 1:
            return right;
        
        elif lst[mid] < lst[left]:
            right = mid
        
        elif lst[mid] > lst[left]:
            left = mid
    
    return None #not in list

def shift_binary_search(lst,val):
    shift = find_shift(lst);
    newLst = lst[shift:] + lst[:shift]
    
    left = 0
    right = len(newLst) - 1

    while left <= right:
        mid = (left + right) //2

        if newLst[mid] == val:
            return ('else',(shift+mid) % len(lst), shift,mid)
        
        elif newLst[mid] < val:
            left = mid + 1
        
        else:
            right = mid - 1

            
    
    return None #not in list


###4
def jump_search(lst, val, k):
    start = 0
    while (start <len(lst)+k):
        if start > len(lst)-1:
            start -=k
            if start < 0:
                return None
            else:
                for i in range(start,len(lst)):
                    if lst[i] ==val:
                        return i
                return None
        elif lst[start] > val:
            start -=k
            if start < 0:
                return None
            else:
                for i in range(start,len(lst)):
                    if lst[i] ==val:
                        return i
                return None
        elif lst[start] <val:
            start +=k
        else:
            return start 
    return None
# worst case time is n/k - 1 + k

def jump_search_opt(lst, val):
    start = 0
    k = math.sqrt(len(lst))
    while (start <len(lst)+k):
        if start > len(lst)-1:
            start -=k
            if start < 0:
                return None
            else:
                for i in range(start,len(lst)):
                    if lst[i] ==val:
                        return i
                return None
        elif lst[start] > val:
            start -=k
            if start < 0:
                return None
            else:
                for i in range(start,len(lst)):
                    if lst[i] ==val:
                        return i
                return None
        elif lst[start] <val:
            start +=k
        else:
            return start 
    return None
#time is sqrt(n)

###5
def exponential_search(lst,val):
    if lst[0] == val:
        return 0;
    start = 1
    while start < len(lst)*2:
        if start > len(lst)-1:
            left = start//2
            right = len(lst)-1
            while left <= right:
                mid = (left + right) //2

                if lst[mid] == val:
                    return mid
                
                elif lst[mid] < val:
                    left = mid + 1
                
                else: #lst[mid] > val
                    right = mid - 1
            
            return None #not in list
        elif lst[start] < val:
            start *= 2;
        elif lst[start] == val:
            return start
        elif lst[start] > val:
            left = start//2
            right = start
            while left <= right:
                mid = (left + right) //2

                if lst[mid] == val:
                    return mid
                
                elif lst[mid] < val:
                    left = mid + 1
                
                else: #lst[mid] > val
                    right = mid - 1
            
            return None #not in list

                    
