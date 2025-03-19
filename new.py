# def product_without_self(nums):
#     n = len(nums)
#     left_products = [1] * n
#     right_products = [1] * n
#     result = [1] * n

#     # Calculate left products
#     left_product = 1
#     for i in range(1, n):
#         left_product *= nums[i - 1]
#         left_products[i] = left_product
#     print(left_products)

#     # Calculate right products
#     #right_products = [1] * n
#     right_product = 1
#     for i in range(n - 2, -1, -1):
#         right_product *= nums[i + 1]
#         right_products[i] = right_product
#     print(right_products)

#     # Calculate final product array
#     for i in range(n):
#         result[i] = left_products[i] * right_products[i]

#     return result

# # Test the function
arr = [1, 2, 3, 4, 5, 6]
# result = product_without_self(arr)
# print(result)  # Output: [24, 12, 8, 6]
n = len(arr)
right_products = [1] * n
right_product = 1
for i in range(n - 2, -1, -1):
    right_product *= arr[i + 1]
    right_products[i] = right_product
    print(right_products)
print(right_product)