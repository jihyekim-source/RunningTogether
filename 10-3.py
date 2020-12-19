T=int(input())
i=0

while i<T:
    i+=1
    a=map(int, input().split())

    a=list(a)
    a.sort()
    print(a[len(a)-3])