
def e_approx(n):
    tempList = [1]*(n+1)
    for i in range (1,n+1):
        tempList[i] = tempList[i-1]*i
    sm = 0
    for num in tempList:
        sm += (1/num);
    return (sm);
    


def main():
    for n in range(15):
        curr_approx = e_approx(n)
        approx_str = '{:.15f}'.format(curr_approx)
        print('n =', n, 'Approximation:', approx_str)
