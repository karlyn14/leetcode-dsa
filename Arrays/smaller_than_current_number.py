def smallerNumbersThanCurrent(self, nums):
        result=[]
        for i in nums:
            count=sum(1 for n in nums if n<i)
            result.append(count)
        return result
