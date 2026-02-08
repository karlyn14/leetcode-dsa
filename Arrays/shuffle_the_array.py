def shuffle(self, nums, n):
        return [val for x, y in zip(nums[:n], nums[n:]) for val in (x, y)]
