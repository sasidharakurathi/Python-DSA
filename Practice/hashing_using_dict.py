

l = [1,0,2,4,3,5,6,7,9,1,1,2,5,9]
hashtable = dict([[key , 0] for key in range(10)])
for i in l:
    hashtable[i] += 1
print(hashtable) 

