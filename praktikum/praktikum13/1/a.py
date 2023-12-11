def search(x, nums):
        try:      
            return nums.index(x)    
        except:
             return -1
print(search(2,[1,2,4,6]))