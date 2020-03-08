#1
#a
    #[1,2,[30,4]]
    #[10,2,[30,4]]
#b
    #[10,[2,'ABC'],[3,[4]],7]
    #[1,[2,'abc'],[3,[40]],7]
#c
    #[1,[4,3],['aa','b'],'c']
    #[1,[4,3],['aa','b']]
    #[1,[4,3],['aa','b'],'c']

#2
    #1, 3, 6, 10, 15, 21, 28, 36, 45, 55,

#3
lsta = [(-2)**i for i in range(8)] 
lstb = [int('1'*i) for i in range(1,8)]

my_str = input('Enter a string: ')
length = len(my_str)
print([ my_str[i] for c in range(2) for i in range (len(my_str))]) 
