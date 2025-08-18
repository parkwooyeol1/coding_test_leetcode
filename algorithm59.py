class Solution:
    def intersection(self, nums1, nums2):
        result = []
        a, b = list(set(nums1)), list(set(nums2))
        for i in a:
            if i in b:
                result.append(i)
        return result


s = Solution()
nums1 = [1,2,2,1]
nums2 = [2,2]
print(s.intersection(nums1,nums2))