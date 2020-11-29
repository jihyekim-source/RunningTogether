num1=set(range(1, 10001))
num2=set()

for i in range(1, 10001):
    for j in str(i):
        i=i+int(j)
    num2.add(i)

self_number=sorted(num1-num2)
for i in self_number:
    print(i)
