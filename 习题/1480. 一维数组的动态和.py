# 给你一个数组 nums 。数组「动态和」的计算公式为：runningSum[i] = sum(nums[0]…nums[i]) 。
# 请返回 nums 的动态和。
nums = [1, 2, 3, 4]
ls = []
a = 0
for i in range(len(nums)):
    a = a + nums[i]
    ls.append(a)
print(ls)
