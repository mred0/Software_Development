product1 = { "name" : "apple", "quantity" : 120, "price" : 600 } 

product2 = { "name" : "banana", "quantity" : 2520, "price" : 1500 } 

product3 = { "name": "orange", "quantity": 100, "price": 400 } 

products = [product1, product2] 

def show_products(): print("\n=== Current Products ===") if not products: print("No products availables") return for i, product in enumerate(products, start=1): print(f"{i}. {product['name']} - Quantity: {product['quantity']}, Price: {product['price']}") print("==============================") 

def add_product(): name = input("Enter product name:").lower() quantity = int(input("Enter quantity: ")) price = int(input("Enter price: ")) 

for product in products:  
    if product["name"] == name: 
        print("Product already exits. Updating quatity instead.") 
        product["quantity"] += quantity 
        product["price"] += price 
        return  
     
new_product = {"name": name, "quantity": quantity, "price": price} 
products.append(new_product) 
print(f"Product '{name}' added successfully!") 
  

def main(): while True: print("\n=== Inventory Management ===") print("1. Display Products") print("2. Add Product") print("3. Remove Product") print("4. Update Product") print("5. Exit") 

choice = input("Enter your choice (1-5): ") 
 
    if choice == "1": 
        show_products() 
    elif choice == "2": 
        add_product() 
    elif choice == "3": 
        remove_product() 
    elif choice == "4": 
        update_product() 
    elif choice == "5": 
        print("Exiting program...") 
        break 
    else: 
        print("Invalid choice. Please try again.") 
  

if name == "main": main() 

 
