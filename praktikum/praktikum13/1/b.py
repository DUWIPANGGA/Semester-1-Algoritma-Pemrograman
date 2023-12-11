def search(x,nums):
    for i in range(len(nums)):
        if nums[i]==x:
            return i
    return -1
print(search(2,[1,2,3,4,5]))