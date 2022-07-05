## Leetcode: https://leetcode.com/problems/richest-customer-wealth/

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for account in accounts:
            sum_bank = 0
            for bank in account:
                sum_bank += bank
            if sum_bank > max_wealth:
                max_wealth = sum_bank
        return max_wealth
  
# Time Complexity: o(m*n)
# Space Complexity: o(1)
