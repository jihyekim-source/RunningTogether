T=int(input())

for i in range(T):
    a, b=input().split()
    a=int(a)
    b=int(b)
    result=a+b
    print('Case #%d: %d' %(i+1, result))
    