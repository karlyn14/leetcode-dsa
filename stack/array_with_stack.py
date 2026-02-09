def buildArray(self, target, n):
        stack=[]
        i=0
        for num in range(1,n+1):
            stack.append("Push")
            if i<len(target) and num==target[i]:
                i+=1
            else:
                stack.append("Pop")
            if i==len(target):
                break
        return stack
        
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
