# -*- coding: utf-8 -*-
# Binary Search
from typing import List

# Description: 给定排序数组从小到大排列，找到目标数字;
# Note: 无重复元素
def binary_search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) # 右边界不包含在内[left, right)
    while left < right: # 注意判断条件
        mid = (left + right) // 2 #这种是否OK?有没有循环无法终止的情况？
        # python总是向下取整， 因此对于长度为1的区间一定落在left
        # 但是对于较大的left和right会有溢出的问题，比如left=max_int-1, right=max_int
        # 但对Python无所谓
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid # 注意右边界是可检查元素的后一个元素（不包括在区间内）
        elif nums[mid] < target:
            left = mid + 1 #这里需要排除已检查过的mid
    return -1

def binary_search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) # [left, right)
    while left < right:
        mid = left + (right-left)//2 # 防溢出，取上位中位数
        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            right = mid
        elif target > nums[mid]:
            left = mid + 1
    return -1
# time: O(logN) space: O(1)

# 变体，若有重复元素，给出左边界或右边界
# [1,2,2,2,3], target=2
# 也就是说要改动第一次找到target的代码
def binary_search_left_bound(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) #[left, right)
    while left < right:
        mid = left + (right-left) // 2
        if nums[mid] == target:
            right = mid # 继续搜索左边界[left, mid)
            # 此时left会慢慢移动到right，最后一次出现target的地方
        elif nums[mid] > target:
            right = mid
        elif nums[mid] < target:
            left = mid + 1
    # 退出条件是left和right相等，那么left代表什么
    # [2,3,4,5] 8, left=length=4=right
    # [3,4,5,6] 2, left=0=right
    # [2,4,5,6] 2, left=0=right
    # left是第一个不小于target的位置
    if left == len(nums): return -1
    return left if nums[left] == target else -1

def binary_search_right_bound(nums: List[int], target: int) -> int:
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right-left)//2
        if nums[mid] == target:
            left = mid + 1 #继续搜索右边界[mid+1, right)
        elif nums[mid] > target:
            right = mid
        elif nums[mid] < target:
            left = mid + 1
    # [2,3,4,5] 8, left=length=right=4
    # [2,3,4,8] 8, left=length=right=4
    # [2,3,4,6] 1, left=right=0
    # left是第一个大于target的数
    if left == 0: return -1
    return left-1 if nums[left-1] == target else -1