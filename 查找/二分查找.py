# 二分查找 就和简单
import sys

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def bin_search(ele):
    max_index = len(mylist)
    min_index = 0
    count = 0
    while 1:
        count += 1
        mid = (max_index + min_index) // 2
        if min_index > max_index:
            break
        if ele == mylist[mid]:
            print(f"{ele}在列表{mid + 1}")
            break
        elif ele > mylist[mid]:
            min_index = mid
        else:
            max_index = mid
    return count
print(bin_search(1))
#
# # 递归的二分查找
def bin_search_new(ele,min_index,max_index):
    if min_index>=max_index:
        return None
    mid = (max_index+min_index)//2

    # if min_index> max_index:
    #     print("no")
    #     return 0
    if ele == mylist[mid]:
        return mid
    elif ele < mylist[mid]:
        bin_search_new(ele,min_index,mid)
    else:
        bin_search_new(ele,mid,max_index)
print(f"在第{bin_search_new(10,0,len(mylist))}个位置")
