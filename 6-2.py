def solve(a:list):
    sum=0
    for i in a:
        sum=sum+i
    return sum



a=map(int, input().split())
n=solve(a)
print(n)


'''다른 풀이
    def solve(a:list):
    sum=0
    for i in a:
        sum+=i
    return sum'''
