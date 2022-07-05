## Question: https://leetcode.com/problems/number-of-good-pairs/

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs = 0
        value_store = {}
        
        for num in nums:
            # add to dictionary counter the number of times the num repeated.
            if num in value_store:
                # pairs will be nothing but the combination of all pairs possible:
                # Refer: https://leetcode.com/problems/number-of-good-pairs/discuss/822102/Python-99.27-O(n)-easy-to-understand-(its-math)
                pairs += value_store[num]
                value_store[num] += 1
            else:
            # store value in dictionary with initial value = 1
                value_store[num] = 1
        return pairs
            
        
## Time Complexity: o(n)
## Space Complexity: o(n)
