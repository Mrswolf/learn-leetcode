# -*- coding: utf-8 -*-
#
# 两指针

# 最长无重复子字符串
# abcabcbb 3 abc
# pwwkew   3 wke
# LeetCode: 3
# 滑动窗法
# 要点是用一个集合维护当前字符串，并删除已遇见字符串之前的字符串
def len_of_longest_substring(s: str) -> int:
    length = 0
    substring_set = set()
    i = 0 # 窗起始位置
    for j in range(len(s)):
        while s[j] in substring_set:
            # 删除重复字符及以前的字符
            substring_set.remove(s[i])
            i += 1
        substring_set.add(s[j])
        # 比较子字符串的大小
        length = max(length, j-i+1)
    return length






