class Notebook:
    def __init__(self, title, username, likes):
        self.title, self.username, self.likes = title, username, likes
        
    def __repr__(self):
        return 'Notebook <"{}/{}", {} likes>'.format(self.username, self.title, self.likes)
    
def compare_likes(nb1: Notebook , nb2: Notebook) -> str:
    if nb1.likes > nb2.likes:
        return "greater"
    elif nb1.likes == nb2.likes:
        return "equal"
    else:
        return "smaller"
    
def merge_sort(notebooks):
    if len(notebooks) <= 1:
        return notebooks
    
    mid = len(notebooks) // 2
    left = notebooks[:mid]
    right = notebooks[mid:]
    
    return merge(merge_sort(left) , merge_sort(right))

def merge(left , right):
    merged_notebooks = []
    i , j = 0 , 0
    while i < len(left) and j < len(right):
        result = compare_likes(left[i] , right[j])
        
        if result == "greater" or result == "equal":
            merged_notebooks.append(left[i])
            i+=1
        else:
            merged_notebooks.append(right[j])
            j+=1
    
    return merged_notebooks + left[i:] + right[j:]


if __name__ == "__main__":
    nb0 = Notebook('pytorch-basics', 'aakashns', 373)
    nb1 = Notebook('linear-regression', 'siddhant', 532)
    nb2 = Notebook('logistic-regression', 'vikas', 31)
    nb3 = Notebook('feedforward-nn', 'sonaksh', 94)
    nb4 = Notebook('cifar10-cnn', 'biraj', 2)
    nb5 = Notebook('cifar10-resnet', 'tanya', 29)
    nb6 = Notebook('anime-gans', 'hemanth', 80)
    nb7 = Notebook('python-fundamentals', 'vishal', 136)
    nb8 = Notebook('python-functions', 'aakashns', 74)
    nb9 = Notebook('python-numpy', 'siddhant', 92)
    
    notebooks = [nb0, nb1, nb2, nb3, nb4, nb5,nb6, nb7, nb8, nb9]
    
    print("\n\n Before sorting \n\n" , notebooks)
    print("\n\n After sorting \n\n" , merge_sort(notebooks))
    
