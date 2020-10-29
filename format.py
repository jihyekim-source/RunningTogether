a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
f=int(input())

print('{}{}{}'.format,a,b,c)
print('{}{}{}'.format,d,e,f)

third=(a*100+b*10+c)*f
print(third)

forth=(a*100+b*10+c)*e
print(forth)

fifth=(a*100+b*10+c)*d
print(fifth)

sixth=(third+forth*10+fifth*100)
print(sixth)