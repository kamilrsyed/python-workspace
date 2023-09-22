#########################################################################################
###########################+++++++++++++++++++++++++++++++++++###########################
###########################++++++++++   LEET CODE   ++++++++++###########################
###########################++++++   Top Interview 150   ++++++###########################
###########################+++++++++++++++++++++++++++++++++++###########################
#####################+++++++++++++++++++++++++++++++++++++++++++++++#####################
##############+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++##############



#########################################################################################
# Two Sum
#########################################################################################

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

#########################################################################################
# Merge Two Sorted Arrays
#########################################################################################

# You are given two integer arrays nums1 and nums2, 
# sorted in non-decreasing order, and two integers m and n,
# representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

def merge_two_arrays(nums1, m, nums2, n):
    i = m - 1
    j = n - 1
    k = m + n - 1
    
    while (j >= 0):
        if (nums1[i] > nums2[j]):
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    print(nums1)
        
merge_two_arrays([1, 4, 6, 7, 8, 9, 0, 0, 0, 0], 6, [2, 3, 5, 5], 4)