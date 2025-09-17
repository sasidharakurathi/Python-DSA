class HashTable:
    """A from-scratch implementation of a hash table with separate chaining."""

    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.buckets = [ [] for _ in range(self.capacity)]

    def _hash(self, key):
        """A simple hash function."""
        return hash(key) % self.capacity

    def __setitem__(self, key, value):
        """Insert or update a key-value pair. Handles resizing."""
        if self.size / self.capacity >= 0.75: # Load factor threshold
            self._resize()

        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value) # Update existing key
                return
        
        bucket.append((key, value)) # Add new key-value pair
        self.size += 1

    def __getitem__(self, key):
        """Retrieve a value by its key."""
        index = self._hash(key)
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == key:
                return v
        raise KeyError(key)

    def __delitem__(self, key):
        """Delete a key-value pair."""
        index = self._hash(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                return
        raise KeyError(key)

    def _resize(self):
        """Double the capacity and rehash all items."""
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [ [] for _ in range(self.capacity)]
        self.size = 0

        for bucket in old_buckets:
            for key, value in bucket:
                self[key] = value # Re-insert using __setitem__

#  --- Python way ---
# l = [1,0,2,4,3,5,6,7,9,1,1,2,5,9]
# hashtable = dict([[key , 0] for key in range(10)])
# for i in l:
#     hashtable[i] += 1
# print(hashtable)           


if __name__ == "__main__":
    hashtable = HashTable()
    hashtable["a"] = 1
    
    
    