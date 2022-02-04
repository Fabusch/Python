#to check if in item in a list use the in command

words = ["spam","hello","nice"]
print("spam" in words) #TRUE
print("tomato" in words) #FALSE


nums = [10,9,8,7,6,5]
nums[0] = nums[1] - 5
if 4 in nums:
    print(nums[3])
else:
    print(nums[4])
    
    
# To check of an item not in a list use the NOT operator 
nums = [1, 2, 3]
print(not 4 in nums) #True
print (4 not in nums) #True
print(not 3 in nums) #False
