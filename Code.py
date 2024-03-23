class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        l = []
        r = []
        ans = []
        for x in range(len(nums)):
            l.append(sum(nums[0:x]))
            r.append(sum(nums[x+1:len(nums)]))
        for x in range(len(nums)):
            if l[x]-r[x] < 0:
                ans.append((l[x]-r[x])*-1)
            else:
                ans.append(l[x]-r[x])
        return ans
