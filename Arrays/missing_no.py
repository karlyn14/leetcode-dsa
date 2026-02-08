def findDisappearedNumbers(self, nums):
        n=len(nums)
        num=set(nums)
        result=[]
        for i in range(1,n+1):
            if i not in num:
                result.append(i)
        return result 
