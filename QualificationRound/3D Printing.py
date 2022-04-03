def select_colour(p1,p2,p3,test_nr):
    print("Case #" + str(test_nr + 1)+":",end = ' ')
    max_ink = [0 for i in range(4)]
    how_much = [0 for i in range(4)]
    max_ink[0] = min(p1[0],p2[0],p3[0])
    max_ink[1] = min(p1[1], p2[1], p3[1])
    max_ink[2] = min(p1[2], p2[2], p3[2])
    max_ink[3] = min(p1[3], p2[3], p3[3])
    if max_ink[0] + max_ink[1] + max_ink[2] + max_ink[3] < 1000000:
        print("IMPOSSIBLE")
        return
    res = 0
    if max_ink[0] < 1000000:
        res += max_ink[0]
        how_much[0] = max_ink[0]
        if max_ink[1] + res < 1000000:
            res += max_ink[1]
            how_much[1] = max_ink[1]
            if max_ink[2] + res < 1000000:
                res += max_ink[2]
                how_much[2] = max_ink[2]
                how_much[3] = 1000000 - res
            else:
                how_much[2] = 1000000 - res
        else:
            how_much[1] = 1000000 - res

    else:
     how_much[0] = 1000000

    print(str(how_much[0])+' '+str(how_much[1])+' '+str(how_much[2])+' '+str(how_much[3]))





cases = int(input())

for i in range(cases):
    p1 = [int(item) for item in input().split()]
    p2 = [int(item) for item in input().split()]
    p3 = [int(item) for item in input().split()]
    select_colour(p1,p2,p3,i)