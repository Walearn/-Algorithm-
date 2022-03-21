"""
我们遍历第一次列表 寻找最大的值 将其放到最后
第二次遍历 寻找第二大的值 将其放到倒数第二的位置
……
其实 “放” 并不是很合理 应该是把最大值和最后一个位置的数交换位置
不然我们会把最后一个位置的数给 “吃掉”
"""
mylist = [9,8,1,2,3,4,5,7,6]
for i in range(len(mylist)-1): # 最小的值无序排序 因为它就是在第一个
    min_index = 0
    for j in range(len(mylist)-i): # 
        if mylist[j]>mylist[min_index]:
            min_index = j
    mylist[j],mylist[min_index] = mylist[min_index],mylist[j]
    print(mylist,f"把{mylist[j]}放到倒数第{9-j}个位置")
    
