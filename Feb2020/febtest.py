test_list = [(3, 4), (4, 5), (3, 4),  
             (3, 4), (4, 5), (6, 7)] 
  
# printing original list  
print("The original list : " + str(test_list)) 
  
# Get duplicate tuples from list 
# Using list comprehension + set() + count() 
res = list(set([ele for ele in test_list 
            if test_list.count(ele) > 1])) 
  
# printing result 
print("All the duplicates from list are : " + str(res)) 
