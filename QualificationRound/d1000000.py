def count_longest(tab,test_nr):
    res = 0
    i = 0
    while i < len(tab):
        if tab[i] > res:
            res += 1
        i += 1
    print("Case #"+str(test_nr+1)+": "+str(res))

cases = int(input())

for i in range(cases):
    t_len = int(input())
    tab = [int(item) for item in input().split()]
    tab.sort()
    count_longest(tab,i)

