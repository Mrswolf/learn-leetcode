# -*- coding: utf-8 -*-
#
# Sort从小到大
# Leetcode: 912
from typing import List
# 快速排序(in-place)
# 将元素分为两部分，左边小于等于pivot，右边都比pivot大, 递归进行

# 用最后一个元素作为pivot
# Lomuto partition scheme
# 快慢指针
# 慢指针i指向决策边界，快指针指向扫描的元素
def partition(nums: List[int], left, right):
    pivot = nums[right] # 去见[left, right]
    i = left # i指向第一个比pivot大的元素
    for j in range(left, right): # [left, right-1]
        if nums[j] <= pivot:
            # 此时j指向小于等于pivot的元素
            nums[j], nums[i] = nums[i], nums[j]
            # 若i==j，这是自己交换自己
            i += 1
    # 交换pivot
    nums[i], nums[right] = nums[right], nums[i]
    return i

def quicksort(nums: List[int], left, right):
    # nums只有一个元素或无元素的情况
    if left >= right:
        return
    pi = partition(nums, left, right)
    quicksort(nums, left, pi-1)
    quicksort(nums, pi+1, right)

# time: ave O(nlogn), bad O(n^2) space: O(logn)




