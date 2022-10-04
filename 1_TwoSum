class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        self.nums = nums
        self.target = target
        adder = len(nums) - 1
        pointer = 0       
        iterator = int((adder * (adder + 1))/2)
        for i in range(0, iterator):
            sum_of_num = nums[pointer] + nums[adder]
            if sum_of_num == target:                
                return[pointer, adder]
                break
            if adder > pointer:
                adder = adder - 1 
            if adder == pointer: 
                adder = len(nums) - 1
                pointer = pointer + 1
