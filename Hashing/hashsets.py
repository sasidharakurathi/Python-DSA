
# We use hashsets to handle data structures realted to unique values (Ex: check if duplicates are there in an array)

nums = [1, 2, 3, 4, 2]
hashset = set()

for num in nums:
    if num in hashset:
        print("Duplicate found")
    hashset.add(num)
