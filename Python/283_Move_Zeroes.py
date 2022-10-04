class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        front = 0
        back = len(nums)

        while front < back:
            if nums[front] != 0:
                front +=1
            else:
                nums.insert(len(nums),0)
                nums.pop(front)
                back -=1
