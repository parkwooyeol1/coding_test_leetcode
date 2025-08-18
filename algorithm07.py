class Solution:
    def trap(self, height):
        list1 = []
        result = 0
        i = 0

        while i < len(height) - 1:
            list1 = []
            if height[i] > 0:
                h = 0
                a = -1
                for j in range(i + 1, len(height)):
                    if height[j] >= height[i]:
                        h = height[i]
                        a = j
                        break
                    elif height[j] > h:
                        h = height[j]
                        a = j
                if a != -1:
                    for k in range(i + 1, a):
                        list1.append(height[k])
                    result += min(height[i], height[a]) * len(list1) - sum(list1)
                    i = a
                else:
                    i += 1
            else:
                i += 1

        return result

                        
                    
                    




    
s = Solution()
height = [4,2,3,2,2]


print(s.trap(height))