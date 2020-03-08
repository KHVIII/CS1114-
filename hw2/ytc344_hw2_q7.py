def findChange(lst01):
    bot = 0
    top = len(lst01) - 1
    while (top>=bot):
        mid = (top+bot)//2
        if lst01[mid] == 1:
            top = mid
        elif lst01[mid] == 0 and top-bot == 1:
            return mid+1
        elif lst01[mid] == 0:
            bot = mid
    return None;

def main():
    lst01 = [0,0,0,0,0,1,1,1]
    print(findChange(lst01))
