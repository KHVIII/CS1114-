def shift(lst, k, d='left'):
    for i in range(k):
        if d == 'left':
            lst.append(lst.pop(0))
        if d == 'right':
            lst.insert(0, (lst.pop()))
    return(lst)

def main():
    lst = shift([1,2,3,4,5,6],2,'right')
    print (lst)             
