class HashTable:
    def __init__(self , max_size=4096):
        self.data_list = [None] * max_size
        self.max_size = max_size
    
    def __setitem__(self,key , value):
        self._insert_or_update(key , value)
        
    def __getitem__(self , key):
        return self._find(key)
    
    def __iter__(self):
        return (kv for kv in self.data_list if kv is not None)
    
    def list_all(self):
        return [kv[0] for kv in self.data_list if kv is not None]
    
    
    def _insert_or_update(self , key , value):
        idx = self._get_valid_index(key)
        
        if idx == -1:
            print("List is full")
            return
        
        self.data_list[idx] = key , value
        
    
    def _find(self , key):
        idx = self._get_valid_index(key)
        
        if idx == -1:
            print("List is full")
            return
        
        kv = self.data_list[idx]
        
        if kv is None:
            return None
        
        return kv[1]        
        
    
    # def _update(self , key , value):
    #     idx = self._get_valid_index(key)
    
    #     if idx == -1:
    #         print("List is full")
    #         return
 
    #     self.data_list[idx] = key , value
    
    
    def _get_valid_index(self , string):
        idx = self._get_index(string)
        count = 1
        while True:
            
            kv = self.data_list[idx]
            
            if kv is None:
                return idx
            
            if kv[0] == string:
                return idx
            
            idx += 1
            count += 1
            
            if idx == len(self.data_list):
                idx = 0
                
            if count == len(self.data_list):
                return -1
    
    def _get_index(self , string):
        return hash(string) % len(self.data_list)

if __name__ == "__main__":
    hashtable = HashTable()
    # print(hashtable._get_index("ash"))
    hashtable["ASH"] = 95
    hashtable["LEO"] = 35
    hashtable["SAM"] = 63
    hashtable["POP"] = 101
    hashtable["DANNY"] = 26
    
    hashtable["ASH"] = 59
    
    # print(hashtable["ASH"])
    # print(list(hashtable))
    # print(hashtable["ASH"])
    
    # for key,value in hashtable:
    #     print(key , value)