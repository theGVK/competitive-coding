#starters 97 q4
for tc in range(int(input())):
    n=int(input())
    s=[i for i in input()]
    count=0
    flag=0
    for i in range(n):
        if(flag==2 and s[i]==':'):
            count+=1
        if(s[i]=="("):
            flag=0
        if s[i]==':':
            flag=1
        if s[i]==')' and flag>0:
            flag=2
    print(count)
