'''Given a dictionary of products and their prices, find the product with the highest price.'''
products = {"TV":34000, "Phone":25000, "Laptop":85000, "Car":20000000}

highest_product = max(products, key = products.get)

print("Product with hightest price:", highest_product)
print("price:", products[highest_product])
