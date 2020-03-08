def two_sum(srt_lst, target):
    bot = 0
    top = len(srt_lst) - 1
    for i in range (len(srt_lst)):
        tempSum = srt_lst[bot] + srt_lst[top]
        if (tempSum == target):
            return (bot,top)
        elif (tempSum > target):
            top -= 1
        else:
            bot += 1
    return None

def main():
    srt_lst=[-2,7,11,15,20,21]
    target=22
    print(two_sum(srt_lst,target))
