data=[25,2,6,50,16,100,99,75,80,1]
data.sort()
print(data)
user=eval(input('masukan nilai yang ingin anda cari : '))
def search(x,nums):
    low=0
    high=len(nums)-1
    while low<= high:
        mid=(low+high)//2
        item = nums[mid]
        if x==item:
            return mid
        elif x<item:
            high=mid-1
        else:
            low=mid+1
    return -1
print(search(user,data))
