def findMaxConsecutiveOnes(self, nums):
        max_count=0
        current=0
        for i in nums:
            if i==1:
                current+=1
                max_count=max(max_count,current)
            else:
                current=0
        return max_count
