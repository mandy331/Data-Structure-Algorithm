class Solution:
    def findErrorNums(self, nums):
        ans = []
        if nums:
            s = set()
            for x in nums:
                print(x)
                if x in s:
                    ans.append(x)
                    print(ans)
                s.add(x)
                print(s)
            n = len(nums)

            ans.append(sum(range(1,n+1)) - sum(s))

        return ans