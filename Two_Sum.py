class find_pair(object):
  def twoSum(self, nums, target):
    for i, num in enumerate(nums):
        for j in range(i+1, len(nums)):
            if num + nums[j] == target:
                return [i, j]
    return []


# user inputs
nums = [2, 7, 15, 11]
target = 9

# Class Instantiation
obj = find_pair()


result = obj.twoSum(nums, target)  # Pass both nums and target
if result:
    print("Pair found:", result)
else:
    print("No pair found")