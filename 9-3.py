N=int(input())
grade=map(int, input().split())

grade_list=list(grade)
grade_list.sort()
M=grade_list[-1]

average=0

for i in range(len(grade_list)):
    grade_list[i]=grade_list[i]/M*100
    average=average+grade_list[i]

print(average/N)