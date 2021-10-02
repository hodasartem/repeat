"""
milk == 3
butter == 5
bread == 7
"""

product = input('Insert the product:\n')

shop_items = {
    'milk' : 3,
    'butter' : 5,
    'bread' : 7
}
print(shop_items.get(product.lower(), -1))

# if product == 'milk':
#     print(3)
# elif product =='butter':
#     print(5)
# elif product == 'bread':
#     print(7)
# else:
#     print(-1)


# print(product)
print(product)