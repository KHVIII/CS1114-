def demo1(): #theta(N^2)
    ls = [];
    for i in range(100):
        ls.append(i);
    while (len(ls)>0):
        print(ls.pop(0); #theta(N)

def demo2(): #theta(N)
    ls = []
    for i in range(100):
        ls.append(i);
    ls.reverse();
    while (len(ls)>0):
        print(ls.pop()); #theta (1)

def main():
    t = Timer();
    for i in range(10000,1000000,10000):
        t.reset();
        demo1(i);
        elapsed = t.elapsed
