array = [1 , 2, 3, 4, 5, 6, 30, 44, 43, 7, 77, 14]
result = []
# i = 0

# for x in array:
#     if x % 7 == 0:
#         print(x, i)
#     i +=  1

for i, x in enumerate(array):
    if x % 7 == 0:
        result.append((x, i))
        print(x, i)

print(result)