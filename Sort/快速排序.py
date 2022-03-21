# # # 结合二分法
import time
import threading
mylist = [9,1,2,3,8,7,6,5,4]
# # 我的天哪 这个也太还有递归的用法这也
# def quicksort(mylist):
#     if len(mylist)<=1:
#         return mylist
#     pivot = mylist[0]
#     bigger_list = [i  for  i in mylist if i>pivot]
#     small_lsit = [i  for i in mylist if i <pivot]
#     return quicksort(small_lsit) + [pivot] + quicksort(bigger_list)
# print(quicksort(mylist))
# # 但是这使用了新的列表 我们可不可以只使用原先的列表呢？
def quicksort(mylist, begin, end):
    if begin>=end:
        return mylist
    i=begin
    j=begin+1
    while j<=end-1:
        print(mylist,i,j)
        if mylist[j]<mylist[i]:
            mylist[j],mylist[i+1] = mylist[i+1],mylist[j]
            i+=1
        j+=1
    mylist[begin],mylist[i] = mylist[i],mylist[begin]
    quicksort(mylist,0,i-1)
    quicksort(mylist,i+1,end)
    return  mylist
print(quicksort(mylist,0,9))


# def quick_sort(lists,i,j):
#     if i >= j:
#         return list
#     pivot = lists[i]
#     low = i
#     high = j
#     while i < j:
#         while i < j and lists[j] >= pivot:
#             j -= 1
#         lists[i]=lists[j]
#         while i < j and lists[i] <=pivot:
#             i += 1
#         lists[j]=lists[i]
#     lists[j] = pivot
#     quick_sort(lists,low,i-1)
#     quick_sort(lists,i+1,high)
#     return lists
#
# if __name__=="__main__":
#     lists=[30,24,5,58,18,36,12,42,39]
#     print("排序前的序列为：")
#     for i in lists:
#         print(i,end =" ")
#     print("\n排序后的序列为：")
#     for i in quick_sort(lists,0,len(lists)-1):
#         print(i,end=" ")

# 探寻函数的返回值
# 返回多个值
# def sum(ele):
#     return [ele*2,ele,[10,2]]
#
# def check(obj):
#     print(obj)
#     print(type(obj))
# check(sum(3))
