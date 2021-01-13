# -*- encoding: utf-8 -*-
'''
Filename         :practice.py
Description      :
Time             :2021/01/08 16:58:37
Author           :tab gui
Version          :1.0
'''

# 1题
# 暴力法
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
# hashmap
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            if hashmap.get(target - nums[i]) is not None: # 返回对应的索引
                return [i, hashmap.get(target - nums[i])]
            else:
                hashmap[nums[i]] = i

# 2题 链表相加
# 思路 比较简单 注意创建链表之后的操作需要用新变量替代进行操作,否则一直是空链表
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        re = ListNode(0)
        r = re
        carry = 0
        while(l1 or l2):
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            s = a + b + carry
            carry = s//10
            r.next = ListNode(s%10)
            print(re)
            print(r)
            r = r.next
            if(l1!=None):
                l1 = l1.next
            if(l2!=None):
                l2 = l2.next
        if(carry>0):
            r.next = ListNode(1)
        return re.next
                
# 动态规划部分

# 72题
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(n+1):
            dp[0][i] = i
        for i in range(m+1):
            dp[i][0] = i
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1] == word2[j-1]: # 当位置相同的字符相同时，不需要进行操作
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        return dp[-1][-1] 
