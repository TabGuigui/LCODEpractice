# -*- encoding: utf-8 -*-
'''
Filename         :Jan.py
Description      :
Time             :2021/01/19 16:07:46
Author           :tab gui
Version          :1.0
'''
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