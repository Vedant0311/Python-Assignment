def find_duplicates(nums):
    seen = set()
    duplicates = set()
    
    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)

input_string = input("Enter numbers separated by spaces: ")

nums = list(map(int, input_string.split()))

output = find_duplicates(nums)

print("Duplicate numbers are:", output)

input("Press Enter to exit...")
