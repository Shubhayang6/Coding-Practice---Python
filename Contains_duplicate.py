# Leetcode - 217

def containsDuplicate(): 
    new_set = set()
    for i in range(len(nums)):
        if nums[i] in new_set:
            return True
        else:
            new_set.add(nums[i])
    return False


if __name__ == "__main__":
    nums = [1,2,3,1]
    output = containsDuplicate()
    print(output)