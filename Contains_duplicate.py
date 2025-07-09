# Leetcode - 217

def containsDuplicate(): 
    # Time - O(n)
    # Space - O(n)
    new_set = set()
    for i in range(len(nums)):
        if nums[i] in new_set:
            return True
        else:
            new_set.add(nums[i])
    return False

    # Time - O(n)
    # Space - O(n)
    nums.sort()
    for i in range(len(nums)):
        if nums[i] == nums[i-1]:
            return True
    return False



if __name__ == "__main__":
    nums = [1,2,3,1]
    output = containsDuplicate()
    print(output)