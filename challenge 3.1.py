def linearSearchProduct(productList, targetProduct):
  indices = []

  for index, product in enumerate(productList):
    if product == targetProduct:
      indices.append(index)

  return indices


products = ["salt" , "chilli powder" , "salt"]
target = "salt"
target2 = 'orange'
result = linearSearchProduct(products, target)
print(result)