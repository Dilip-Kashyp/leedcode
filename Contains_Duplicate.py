def cantainsDuplicate( nums):
    nums.sort()
    for  i in range(len(nums)-1):
        if(nums[i]==nums[i+1]):
            return True
            
    return False
              





nums = [1,2,3,1]

print(cantainsDuplicate(nums))