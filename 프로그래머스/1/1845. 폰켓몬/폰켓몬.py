def solution(nums):
    l = len(nums)//2
    n = len(set(nums))
    return l if n>l else n 