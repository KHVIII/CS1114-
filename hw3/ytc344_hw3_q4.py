##def remove_all(lst, value):
##    end = False
##    while (end == False):
##        try:
##            lst.remove(value)
##        except ValueError:
##            end = True
    #worst case running time is n^2

def remove_all(lst, value):
    
    point1 = lst.index(value)
    point2 = point1
    while (point2 != len(lst)-1):
        if lst[point2+1] != value:
            lst[point1], lst[point2+1] = lst[point2+1], lst[point1]
            point1 += 1
        point2 += 1
    for i in range(point1, point2+1):
        lst.pop()
    #worst case run time is 2n, O(n). 
            
