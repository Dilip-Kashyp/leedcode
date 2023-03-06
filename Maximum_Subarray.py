def maxSubArray(nums):
    maxx =  nums[0]
    sum =0
    for i in range(len(nums)):
        sum = sum + nums[i]
        print(sum)
        if (sum >= maxx):
            maxx = sum
        print(maxx)

        if (sum < 0):
            sum = 0

    return maxx




nums = [-3, -2, -2,-3]

print(maxSubArray(nums))
