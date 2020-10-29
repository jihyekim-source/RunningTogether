H=int(input())
M=int(input())

print(H, M)


if (M>=45):
    M=M-45

else:
    H=H-1
    M=60+(M-45)

print(H,M)