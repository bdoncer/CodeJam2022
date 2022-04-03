def print_card(R,C,test_nr):

    print("Case #" + str(test_nr + 1)+":")

    #top left cell
    print("..", end='')
    for j in range(C-1):
        print("+-", end='')
    print("+")
    print("..", end='')
    for j in range(C-1):
        print("|.", end='')
    print("|")


    for i in range(1,R):
        for j in range(C):
            print("+-",end='')
        print("+")
        for j in range(C):
            print("|.",end='')
        print("|")
    for j in range(C):
        print("+-", end='')
    print("+")




cases = int(input())

for i in range(cases):
    R, C = input().split()
    R = int(R)
    C = int(C)
    print_card(R,C,i)