mylist = [9,1,2,8,7,3,4,6,5]
count=0
for i in range(1,len(mylist)):
    point = i
    # 在这个新的序列是一个有序的数列 所以我们直接插入一次就够了
    for j in range(i,0,-1):
        if mylist[j]<mylist[j-1]:
            mylist[j],mylist[j-1] = mylist[j-1],mylist[j]
        count+=1
    print(mylist)
print(count)