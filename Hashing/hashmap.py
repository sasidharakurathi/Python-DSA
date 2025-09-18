

# arr = [1, 2, 2, 3, 1, 4]
# hashmap = dict()

# for ele in arr:
#     hashmap[ele] = hashmap.get(ele, 0) + 1

# print(hashmap)


from collections import defaultdict

arr = [1, 2, 2, 3, 1, 4]
hashmap = defaultdict(int)  # using defaultdict to initialize the new keys with default value (0)

for ele in arr:
    hashmap[ele] += 1

print(dict(hashmap))

