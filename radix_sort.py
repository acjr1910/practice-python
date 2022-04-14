import math


def get_digit(num, i):
    return math.floor(abs(num) / math.pow(10, i)) % 10


def digit_count(num):
    if num == 0:
        return 1
    return math.floor(math.log10(abs(num))) + 1


def most_digits(nums):
    max_digits = 0
    for i in range(len(nums) - 1):
        max_digits = max(max_digits, digit_count(nums[i]))
    return max_digits


def radix_sort(nums):
    max_digit_count = most_digits(nums)
    for k in range(max_digit_count):
        digit_buckets = [[] for digit in range(max_digit_count)]
        for i in range(len(nums)):
            digit = get_digit(nums[i], k)
            digit_buckets[digit].append(nums[i])
        nums = [num for buckets in digit_buckets for num in buckets]
    return nums


print(radix_sort([293, 29, 219231, 1231231023, 48596, 1]))
