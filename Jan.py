# -*- encoding: utf-8 -*-
'''
Filename         :Jan.py
Description      :
Time             :2021/01/19 16:07:46
Author           :tab gui
Version          :1.0
'''
# 第三题 无重复字符的最长子串
# 用滑动窗口法 保存滑动过的窗口，新字符如果在该窗口内，应减小窗口范围
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        print(s)
        if len(s) == 0:
            return 0
        max_len = 0
        cur_len = 0
        window = ''
        for i in range(len(s)):
            cur_len += 1
            while s[i] in window:
                cur_len -= 1
                window = window[1:]
            if cur_len > max_len:
                max_len = cur_len
            window += s[i]
        return max_len

# 整数反转
# 注意事项 不能越界 注意正反
class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        if x > 0 :
            while x!= 0:
                num = x % 10
                ans = ans * 10 + num
                x = x // 10
        else:
            x = abs(x)
            while x!= 0:
                num = x % 10
                ans = ans * 10 + num
                x = x // 10
            ans = -ans
        if  ans > 2147483647 or ans < -2147483648 :
            return 0
        return ans