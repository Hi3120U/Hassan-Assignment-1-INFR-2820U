import time


class Product:

  def __init__(self, product_id, name, price, category):
    self.product_id = product_id
    self.name = name
    self.price = price
    self.category = category


def load_data(file_path):
  products = []
  with open(file_path, 'r') as file:
    for line in file:
      data = line.strip().split(', ')
      product = Product(int(data[0]), data[1], float(data[2]), data[3])
      products.append(product)
  return products


def insert_product(products, new_product):
  products.append(new_product)
  print(f"Inserted new product: {new_product.name}")


def update_product(products, product_id, new_price):
  for product in products:
    if product.product_id == product_id:
      product.price = new_price
      print(f"Updated price for product {product_id} to {new_price}")
      break


def delete_product(products, product_id):
  products[:] = [
      product for product in products if product.product_id != product_id
  ]
  print(f"Deleted product with ID: {product_id}")


def search_product(products, key, value):
  results = []
  for product in products:
    if getattr(product, key) == value:
      results.append(product)
  return results


def bubble_sort(products):
  n = len(products)
  for i in range(n - 1):
    for j in range(0, n - i - 1):
      if products[j].price > products[j + 1].price:
        products[j], products[j + 1] = products[j + 1], products[j]


def measure_sorting_time(sort_function, data, sort_type):
  start_time = time.time()
  sort_function(data)
  end_time = time.time()
  elapsed_time = end_time - start_time
  print(f"Sorting {sort_type} data took {elapsed_time:.6f} seconds")


def display_products(products):
  for product in products:
    print(
        f"{product.product_id}, {product.name}, {product.price}, {product.category}"
    )


# Example usage:
file_path = 'product_data.txt'
product_data = load_data(file_path)

while True:
  print("\nOptions:")
  print("1. Insert a new product")
  print("2. Update a product's price")
  print("3. Delete a product")
  print("4. Search for products")
  print("5. Sort products by price")
  print("6. Exit")

  choice = input("Enter your choice (1-6): ")

  if choice == '1':
    new_product = Product(int(input("Enter product ID: ")),
                          input("Enter product name: "),
                          float(input("Enter product price: ")),
                          input("Enter product category: "))
    insert_product(product_data, new_product)

  elif choice == '2':
    product_id = int(input("Enter product ID to update: "))
    new_price = float(input("Enter new price: "))
    update_product(product_data, product_id, new_price)

  elif choice == '3':
    product_id = int(input("Enter product ID to delete: "))
    delete_product(product_data, product_id)

  elif choice == '4':
    key = input("Enter attribute to search (e.g., 'category'): ")
    value = input("Enter value to search for: ")
    search_results = search_product(product_data, key, value)
    print("\nSearch results:")
    display_products(search_results)

  elif choice == '5':
    measure_sorting_time(bubble_sort, product_data.copy(), 'random')
    print("\nSorted product data:")
    display_products(product_data)

  elif choice == '6':
    print("Exiting the program.")
    break

  else:
    print("Invalid choice. Please enter a number between 1 and 6.")
