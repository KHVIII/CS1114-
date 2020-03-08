def fibs(n):
    n0 = 1
    yield n0
    n1 = 1
    yield n1
    for i in range (n-2):
        result = n0 +n1
        n0 = n1
        n1 = result
        yield result;

def main():
    for curr in fibs(1):
        print(curr)
        
