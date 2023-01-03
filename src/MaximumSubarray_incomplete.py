nums = [-2, 1, -3, 4, -1, 2, 1, 5, -5, 4]
max = nums[0]
max_index = 0
def max_subarray(max_index):
    #max to left
    max_sum = 0
    sum = 0
    left = max_index - 1
    max_left = max_index
    while left >= 0 and left < len(nums):
        sum += nums[left] 
        if sum > max_sum:
            max_sum = sum
            max_left = left
        left -= 1    
    #max to right
    right = max_index + 1
    max_right = max_index
    sum = 0
    max_sum = 0
    while right >= 0 and right < len(nums):
        sum += nums[right] 
        if sum > max_sum:
            max_sum = sum
            max_right = right
        right += 1
    #sum of subarray
    sum = 0
    for index in range(max_left, max_right + 1):
        sum += nums[index]
    return sum

max_sum = max_subarray(max_index)

for index in range(len(nums)):
    if nums[index] > max:
        max = nums[index]
        max_index = index
        if max_sum < max_subarray(max_index):
            max_sum = max_subarray(max_index)
print(max_sum)            
