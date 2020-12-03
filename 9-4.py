N=int(input())
num=input()

list=list(num)

add=0
for i in range(N):
    add=add+int(list[i])

print(add)