import sys
SMALL="abcdefghijklmnopqrstuvwxyz"
BIG="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUM="0123456789"
while True:
    small, big, num, space= 0,0,0,0
    string=sys.stdin.readline().rstrip('\n')

    if not string:
        break
    
    for i in string:
        if i in SMALL:
            small+=1
        elif i in BIG:
            big+=1
        elif i in NUM:
            num+=1
        elif i in " ":
            space+=1
            
    print(small, big, num, space)