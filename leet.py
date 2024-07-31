# problem:2616

# problem
# nums = [-1,2,1,-4]
# target = 1
# def soham(nums, target):
    
#     for i in range(0, len(nums)-2):
#         sum = nums[i] + nums[i+1] + nums[i+2]
#         if(sum == target):
#             sum = sum
        

#     return sum
# print(soham(nums, target))

# problem:518
# coins = [1,2,5]
# amount = 5





# problem7
# import sys
# x = 1534236469
# size = sys.getsizeof(x)
# if(size >= 32):
#     print("Soham")
#     print(0)    

# elif(x >= 0):
#     y = str(x)
#     x = y[::-1]
#     x = int(x)
#     print(x)
# else:
#     y = str(x)
#     x = y[::-1]
#     x = x[0:len(x)-1]
#     x = int(x)
#     x = -x
#     print(x)


# problem8
# s = "sohaknk56sdcs46cs"
# a = ""
# for i in range(len(s)):
#     if(s[i] == "-" or s[i] == "+" or s[i] == "0" or s[i] == "1" or s[i] == "2" or s[i] == "3" or s[i] == "4" or s[i] == "5" or s[i] == "6" or s[i] == "7" or s[i] == "8" or s[i] == "9" ):
#         a = a + s[i]
#     else:
#         continue
# a = int(a)
# if -2**31 <= a <= 2**31 - 1:
#     return a
# else:
#     return 0



# problem49
# strs = ["eat","tea","tan","ate","nat","bat"]
# result = []
# for i in range(len(strs)):
#     for j in range(len(strs)):
#         for k in range(len(strs[i])):

# problem45
# nums = [2,3,1,1,4]
# count = 1
# i = 2
# print(len(nums))
# while(i != len(nums)):
#     count = count + 1
#     # print(nums[i])
#     for j in range(nums[i] - len(nums) ):
#         i = i + 1


# print("count", count)

# def soham(dividend, divisor):
#     return(dividend/divisor)


# print(soham(10, 3))

# problem28
# haystack ="hello"
# needle = "ll"
# haystack = "sadbutsad"
# needle = "sad"
# haystack = "leetcode"
# needle = "leeto"
# haystack = "ssoham"
# needle = "soham"
# haystack = "soham"
# needle = "soham"
# haystack = "a"
# needle = "a"



# problem: 20

# s = "(){"
# def soham(s):
#     arr = []
#     j = -1
#     for i in s:
#         if(i == '(' or i == '{' or i == '[' or i == '<' ):
#             arr.append(i)
#             j = j + 1
#         else:
#             if(j>=0):
#                 arr.remove(arr[j])
#             else:
#                 return False
#     return True  

# print(soham(s))


# problem: 121
# prices = [7,1,5,3,6,4]
# prices = [7,6,4,3,1]
# prices = [1, 2]
# def soham(prices):
#     min_price = min(prices)

#     for i in range(len(prices)):
#         if(prices[i] == min_price):
#             print("here for min price", i)
#             min_price_position = i
#         else:
#             continue
#     arr = prices[min_price_position: len(prices)]
#     max_price = max(arr)
#     print(max_price)

#     for i in range(len(arr)):
#         if(arr[i] == max_price):
#             print("here for max price", i)
#             max_price_position = i
#         else:
#             continue

#     if(max_price_position > min_price_position):
#         return min_price_position + max_price_position + 1
#     else:
#         return 0
# print(soham(prices))



# # problem:118
# rowIndex = 0
# def soham(rowIndex):
    
# print(soham(rowIndex))






# 6
# s = "PAYPALISHIRING"
# def soham(s, numRows):
#     ans = "soham"
#     for i in range(0, len(s)):
#         print(i)
#     return ans
# print(soham(s, 3))




# 41 memory
# nums = [1,2,0]
# nums = [3,4,-1,1]
# nums = [7,8,9,11,12]
# def soham(nums):
#     for i in range(1, max(nums)):
#         if(i in nums and i>0):
#             continue
#         else:
#             return i
#     return max(nums) + 1

# print("ans",soham(nums))    


# 2482 time
# grid = [[1,1,1],[1,1,1]]
# grid = [[0,1,1],[1,0,1],[0,0,1]]
# def soham(grid):
#     row = len(grid)
#     col = len(grid[0])
#     ans = [[0] * col for _ in range(row)]
#     for i in range(0, row):
#         for j in range(0, col):
#             val = 0

#             # col
#             for m in range(0, col):
#                 if(grid[i][m] == 0):
#                     val = val - 1
#                 else:
#                     val = val + 1

#             # row
#             for m in range(0, row):
#                 if(grid[m][j] == 0):
#                     val = val - 1
#                 else:
#                     val = val + 1
#             ans[i][j] = val
#     return ans


# print("ans",soham(grid))


# 10

# s = "aa"
# p = "aa"
# def soham(s, p):
#     if((len(p) == len(s)) and (p in ['.'])):
#         print(p is not ['*', '.'])
#         print("soham")
#         if(p == s):
#             return True
#         else:
#             return False
#     else:
        # value = True
        # i = 0
        # while(value):
        #     point = 0
        #     if(p[i] == s[i] or point == s[i]):
        #         continue
        #     elif(p[i] == '*' or point == s[i]):
        #         point = s[i]
        #     elif(p[i] == '.' or point == s[i]):
        #         continue
        #     else:
        #         return False
        #     i = i + 1
#         return True

# print(soham(s, p))



# 15 solved
# nums = [0,1,1]
# nums = [-1,0,1,2,-1,-4]
# def soham(nums):
#     ans = []
#     bns = []
#     for i in range(0, len(nums)):
#         for j in range(i+1, len(nums)):
#             for k in range(j+1, len(nums)):
#                 if(nums[i] + nums[j] + nums[k] == 0 and (i!=j!=k)):
#                     ans.append([nums[i], nums[j], nums[k]])
#                     bns.append([i, j, k])
#                     break
#                 else:
#                     continue

#     print(ans)
#     print(bns)
#     # return ans, bns

# print(soham(nums))

# 1155
# 1897


# 1578
# colors = "abaac"
# neededTime = [1,2,3,4,5]
# colors = "abc"
# neededTime = [1,2,3]
# colors = "aabaa"
# neededTime = [1,2,3,4,1]
# colors = "aaabbbabbbb"
# neededTime = [3,5,10,7,5,3,5,5,4,8,1]
# def soham(colors, neededTime):
#     ans = 0
#     for i in range(1, len(colors)):
#         if(colors[i - 1] == colors[i]):
#             print(neededTime[i-1:i+1], min(neededTime[i-1:i+1]), ans)
#             ans  = ans + min(neededTime[i - 1: i + 1])
#         #     neededTime.remove(min(neededTime[i-1:i+1]))
#     return ans
    
# print(soham(colors, neededTime))



# def soham(colors, neededTime):
#     ans = 0
    
#     return ans
    
# print(soham(colors, neededTime))


# 997
# def soham():
#         n = 3
#         trust = [[1,3],[2,3],[5,3]]
#         judge = trust[0][1]
#         for i in range(0, len(trust)):
#                 if(trust[i][1] == judge and trust[i][0] != judge):
#                         continue
#                 else:
#                         return -1
#         return judge
# print(soham())

# chatgpt
# 2125
# 2870
# 1235
# 446
# 872
# 1026
# 1347
# 1657
# 931
# 1457
# 1143
# 49
# 2096
# 1110
# 1530






# 228
# nums = [0,1,2,4,5,7, 8, 9]
# def soham(nums):
#     ans = []
#     start = nums[0]
#     for i in range(0, len(nums) - 1):
#         if(nums[i + 1] - nums[i] == 1):
#             end = nums[i + 1]
#             if(i == len(nums) - 2):
#                 if(start == end):
#                     ans.append("{}".format(start))
#                 else:    
#                     ans.append("{}->{}".format(start, end))
#         else:
#             ans.append("{}->{}".format(start, end))
#             start = nums[i + 1]
#             end = nums[i + 1]
#             if(i == len(nums) - 2):
#                 if(start == end):
#                     ans.append("{}".format(start))
#                 else:    
#                     ans.append("{}->{}".format(start, end))
#     return ans

# print(soham(nums))



# Example usage:v
# sol = Solution()
# k = 3
# rowConditions = [[1, 2], [3, 2]]
# colConditions = [[2, 1], [3, 2]]
# print(sol.buildMatrix(k, rowConditions, colConditions))




# class Node:
#     def __init__(self, data=None):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = new_node


#     def display(self):
#         current = self.head
#         while current:
#             print(current.data, end=" -> ")
#             current = current.next
#         print("None")

#     def display(self):
#         current = self.head
#         if(current):
#             while current:
#                 if(current.next is None):
#                     print(current.data)
#                 else:
#                     print(current.data, "->", end="")
#                 current = current.next
#         else:
#             print("linkedlist is empty")

# # Usage
# linked_list = LinkedList()
# linked_list.append(1)
# linked_list.append(2)
# linked_list.append(3)
# linked_list.display()  # Output: 1 -> 2 -> 3 -> None



# js logic for prject
# data={
#     "vrusharth":"60",
#     "soham":"40",
#     "sharvesh":"90",
#     "dhrub":"10",
# }
# def soham(data):
#     ans = data.copy()
#     total = 0
#     for key in data:
#         total = total + int(data[key])
#     payable = total/len(data)
#     for key in ans:
#         if(float(ans[key]) >= payable):
#             ans[key] = str(float(ans[key]) - payable) + "++"
#         else:
#             ans[key] = str(payable - float(ans[key])) + "--"
#     return ans

# print(soham(data))




nums = [-1,0,1,2,-1,-4]
nums = [-2, 0, 1, 1, 2]
nums = [-1, 0, 1, 2, -1, -4, 2, 2]
nums = [-4, -2, -1, 0, 1, 2, 3, 4]
nums = [-1, 0, 1, 2, -1, -4]
def soham(nums):
    nums.sort()  # Sort the list to use two-pointer technique
    print(nums)
    ans = []
    for i in range(0, len(nums) - 2):
        for j in range(i+1, len(nums) - 1):
            val = nums[i] + nums[j]
            for k in range(j+1, len(nums)):
                # print(i, j, k)
                if(nums[k] == -val):
                    # print("!!!!!")
                    # data = sorted([nums[i], nums[j], nums[k]])
                    if([nums[i], nums[j], nums[k]] in ans):
                        continue
                    else:
                        # print("-------")
                        ans.append([nums[i], nums[j], nums[k]])
                    break
                else:
                    continue
    return ans
print(soham(nums))