class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        stack = []
        for i1,num in enumerate(nums):
            for i2, n in enumerate(stack):
            
                if n + num == target:
                    return [i1, i2]
            stack.append(num)
        

    def twoSum2(self, nums, target):
        map = {}
        for i, num in enumerate(nums):
            map[num] = i
        
        for i, num in enumerate(nums):
            n = target - num
            if map.has_key(n):
                if map[n] != i:
                    return [map[n], i]
    
    def twoSum3(self, nums, target):
        map = {}
        for i, num in enumerate(nums):
            n = target - num
            if map.has_key(n):
                if map[n] != i:
                    return [map[n], i]
            map[num] = i

a = Solution()

print(a.twoSum3([3, 2, 4], 6))