# Leetcode - 242
from collections import defaultdict
def valid_anagram(): 
    # Time - O(n)
    # Space - O(n)
    count = defaultdict(int)
    
    for i in s:
        count[i] += 1
        
    for i in t:
        count[i] -= 1
        
    for x in count.values():
        if x != 0:
            return False
        
    return True


if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    output = valid_anagram()
    print(output)