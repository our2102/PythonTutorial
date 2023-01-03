nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = 3
nums = nums1[:m] + nums2
nums.sort()

for index in range (len(nums1)):
    nums1[index] = nums[index]
print(nums1)    