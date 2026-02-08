def findErrorNums(self, nums):
        n=len(nums)
        sets=set()
        duplicate=0
        for i in nums:
            if i in sets:
                duplicate=i
            else:
                sets.add(i)
        missing_number=(n*(n+1)//2-sum(sets))
        return [duplicate,missing_number]
