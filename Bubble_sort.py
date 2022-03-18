'''讲解部分：冒泡排序 （升序为例）
遍历列表 如果第一个值大于第二个值 两者交换位置
第一次遍历可以做到把该列表中的最大值 放到列表的末尾
第二次遍历把第二大的值放到倒数第二的位置
'''
mylist = [9,1,2,8,3,7,4,6,5]
count = 0
for i in range(len(mylist)-1):
    for j in range(len(mylist)-1-i):  # 第几次遍历 就放到倒数第几的位置
        if mylist[j]>mylist[j+1]:
            mylist[j],mylist[j+1] = mylist[j+1],mylist[j]
        count+=1
    print(f"第{i+1}次遍历,{mylist},计算次数{count}")

""" 不难看出 我们在第4次遍历就已经把列表排序完成了
所以我们可以改进一下
"""
mylist = [9,1,2,8,3,7,4,6,5]
count = 0
for i in range(len(mylist)-1):
    flag = 0
    for j in range(len(mylist)-1-i):
        if mylist[j]>mylist[j+1]:
            mylist[j],mylist[j+1] = mylist[j+1],mylist[j]
            flag+=1
        count += 1
    if flag == 0:
        break
    print(f"第{i+1}次遍历,{mylist},计算次数{count}")