# Two Sum

# brute force approach (O(n^2))
# def two_sum(list, target):    
#     #target = 5
#     #list = [2,5,7,3,4,9]
#     for i in range(len(list)):
#         for j in range(i + 1, len(list)):
#             if list[i] + list[j] == target:
#                 return [i, j]
            
# optimized 
def two_sum(list, target):
    map = {}
    for i in range(len(list)):
        compliment = target - list[i]
        if (compliment in map):
            return [i, map[compliment]]
        else:
            map[list[i]] = i
            
            
print(two_sum([2,5,7,3,4,9], 16))