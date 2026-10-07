"""
Write a command to match the sum of pairs in the list is equal to given target number.
Use Hash set also called as set in python that does not allow duplicasy.
"""
def find_pairs_with_sum(numbers, target):
    seen = set()
    pairs = set()

    for num in numbers:
        complement = target - num
        if complement in seen:
            # Store the pair as sorted tuple.
            pairs.add(tuple(sorted((num, complement))))
        seen.add(num)
    return list(pairs)

nums = [3,4,2,6,8,2,1]
target_sum = 10
result = find_pairs_with_sum(nums, target_sum)
print(f"Pairs that add up to {target_sum}: {result}")