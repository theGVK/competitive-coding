#starters 97 q3
li=[i for i in "abcdefghijklmnopqrstuvwxyz"]
for tc in range(int(input())):
    n=int(input())
    x1=[i for i in input()]
    x2=[i for i in input()]
    x3=[i for i in input()]
    k=li.index(x2[0])-li.index(x1[0])
    res=""
    for i in x3:
        res=res+li[(li.index(i)+k)%26]
    print(res)
