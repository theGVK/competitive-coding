#starters 97 q2
for tc in range(int(input())):
    li=list(map(int,input().split()))
    al=[li[0],li[1],li[2]]
    bo=[li[3],li[4],li[5]]
    al.sort()
    bo.sort()
    a=sum(al[1:])
    b=sum(bo[1:])
    if(a>b):
        print("Alice")
    elif(a==b):
        print("Tie")
    else:
        print("Bob")
        
