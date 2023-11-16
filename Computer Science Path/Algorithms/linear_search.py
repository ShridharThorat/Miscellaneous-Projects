def linear_search(search_list, target):
    if search_list == [] :
        return None
    for item in search_list:
        if item == target:
            return True, search_list.index(item)
    
    
    
test = [1,2,3,4,5,6,7]
target = 5
print(linear_search(test,target))