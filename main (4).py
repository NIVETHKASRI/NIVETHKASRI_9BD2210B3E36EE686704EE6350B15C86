def linear_search_product(products,target_product):
 indices=[]
 for i in range(len(products)):
  if products[i]==target_product:
     indices.append(i)
 return indices

products=["apple","banana","orange","banana","grape"]
target="banana"
result=linear_search_product(products,target)
print(result)
