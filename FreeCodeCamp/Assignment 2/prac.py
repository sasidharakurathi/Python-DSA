MAX_HASH_TABLE_SIZE = 4096


class BasicHashTable:
    def __init__(self , max_size=MAX_HASH_TABLE_SIZE):
        self.data_list = [None] * max_size
        
    def insert(self , key , value):
        idx = get_index(self.data_list , key)
        self.data_list[idx] = (key , value)
    
    def find(self , key):
        idx = get_index(self.data_list , key)
        
        kv = self.data_list[idx]
        
        if kv is None:
            return None
        
        return kv[1]
    
    def update(self , key , value):
        idx = get_index(self.data_list , key)
        self.data_list[idx] = key , value
        
    
    def list_all(self):
        return [kv[0] for kv in self.data_list if kv is not None]

class ProbingHashTable:
    def __init__(self,max_size = MAX_HASH_TABLE_SIZE):
        self.data_list = [None] * max_size
    
    def insert(self,key,value):
        idx = get_valid_index(self.data_list , key)
        
        if idx == -1:
            print("List is full")
            return
        
        
        self.data_list[idx] = key , value
    
    def find(self , key):
        idx = get_valid_index(self.data_list , key)
        
        if idx == -1:
            print("List is full")
            return
        
        kv = self.data_list[idx]
        
        if kv is None:
            return None
        
        return kv[1]
    
    def update(self , key ,value):
        idx = get_valid_index(self.data_list , key)
        
        if idx == -1:
            print("List is full")
            return
        
        self.data_list[idx] = key , value
    
    def list_all(self):
        return [kv[0] for kv in self.data_list if kv is not None]


    

# data_list = [None] * MAX_HASH_TABLE_SIZE

# print(len(data_list))
# print(data_list[155] == None)
# for i in data_list:
#     assert i == None

def get_index(data_list , a_string):
    """
        Simple Hash Function:  (Collision may occur)
            1. Take a string as input
            2. Convert each character of that string into a number using 'ord()' method.
            3. Sum all thoses numbers to obtain the hash of the string
            4. Return the remainder of the Sum with the length of the data_list
    """
    
    
    result = 0
    
    for a_character in a_string:
        a_number = ord(a_character)
        result += a_number
    
    list_index = result % len(data_list)
    
    return list_index

def get_valid_index(data_list , key):
    idx = get_index(data_list , key)
    
    count = 1
    while True:
        kv = data_list[idx]
        
        if kv is None:
            return idx
        
        k , v = kv
        if k == key:
            return idx
        
        idx += 1
        
        if idx == len(data_list):
            idx = 0
            
        count += 1
        if count == len(data_list):
            return -1
    


# basic_hash_table = BasicHashTable(1024)
# # print(len(basic_hash_table.data_list) == 1024)
# basic_hash_table.insert('Akash' , '9999999999')
# basic_hash_table.insert('Hemanth' , '9999998889')
# basic_hash_table.update('Hemanth' , '8888888888')


# print(basic_hash_table.find('Hemanth') == '8888888888')
# print(basic_hash_table.list_all())


probing_hash_table = ProbingHashTable(1024)
# print(len(basic_hash_table.data_list) == 1024)
probing_hash_table.insert('Akash' , '9999999999')
probing_hash_table.insert('Hemanth' , '9999998889')
probing_hash_table.update('htnameH' , '8888888888')


print(probing_hash_table.find('Hemanth') == '8888888888')
print(probing_hash_table.list_all())