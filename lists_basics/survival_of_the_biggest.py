nums = input().split(' ')
copy_nums = list(map(int, nums))    # We create list and then with map walk throuh the list - from str to int
count = int(input())                # map() is like for loop

for _ in range(count):
    current_min_element = min(copy_nums)         # we take the min value from the int list
    nums.remove(str(current_min_element))
    copy_nums.remove(current_min_element)

print(', '.join(nums))
