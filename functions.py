"""
A playground for functions
"""
number_list = [12, 45, 60, 87, 999, 200, 85, 77, 99, 20]

"""
Returns odd numbers from a list of numbers
"""
def odds(nums):
    odd_nums = [num for num in nums if num % 2 != 0]
    return odd_nums


odds_list = odds(number_list)

print(odds_list)
