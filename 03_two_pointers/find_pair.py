#two pointers method, assume we want to find pairs that can sum up to 60
# using this method where we push the index position to the front and compare it with the end allows us to efficiently get an answer in a less computational matter

durations = [10, 15 , 20, 30, 45]
target = 60

def find_pair(nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return f"{nums[left]} and {nums[right]} are sum to target: {target}"
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return "No pair found"

print(find_pair(durations, target))
