
# If we need to hash multiple values combined together like 'coordinates' we can using tuples.
# Since tuples are immutable we can use that a keys for hashing.

# Ex: Hashing coordinates (finding frequency of every coordinates)

points = [(1, 2), (3, 4), (1, 2)]
hashmap = {}

for point in points:
    hashmap[point] = hashmap.get(point, 0) + 1

print(hashmap)
