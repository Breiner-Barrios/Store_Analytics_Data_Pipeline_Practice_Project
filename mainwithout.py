import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta
import os

fake = Faker()

def generate_customers_data(n):
    """Genera datos falsos para la tabla de clientes."""
    genders = ['Male', 'Female', 'Other', 'Prefer not to say']
    cities = ["Bogotá", "Medellín", "Cali", "Barranquilla", "Cartagena", "Bucaramanga"]

    data = []
    for _ in range(n):
        name = fake.name()
        gender = random.choice(genders)
        age = random.randint(18, 80)
        city = random.choice(cities)
        data.append([name, gender, age, city])

    df = pd.DataFrame(data, columns=[
        "name", "gender", "age", "city"
    ])
    return df

def generate_products_data(n):
    """Genera datos falsos para la tabla de productos."""
    categories = ["Technology", "Home", "Fashion", "Health", "Sports", "Education", "Books", "Groceries"]
    # Lista de nombres de productos predefinidos para mayor realismo y control.
    product_names = [
        "Laptop Pro 15-inch", "Wireless Mouse", "4K Monitor", "Mechanical Keyboard",
        "Smart Coffee Maker", "Robotic Vacuum Cleaner", "LED Desk Lamp", "Air Purifier",
        "Classic T-Shirt", "Leather Wallet", "Running Shoes", "Winter Jacket",
        "Vitamin C Supplements", "Digital Thermometer", "Yoga Mat", "Electric Toothbrush",
        "Basketball", "Dumbbell Set", "Resistance Bands", "Soccer Ball",
        "Advanced Python Course", "Data Science Handbook", "The Art of Fiction", "Organic Apples"
    ]
    data = []
    for _ in range(n):
        name = random.choice(product_names) # Se elige un nombre de la lista predefinida.
        category = random.choice(categories)
        price = round(random.uniform(5.0, 1500.0), 2)
        stock = random.randint(0, 200)
        data.append([name, category, price, stock])

    df = pd.DataFrame(data, columns=[
        "name", "category", "price", "stock"
    ])
    return df

def generate_sales_data(n, customer_ids, product_ids):
    """Genera datos falsos para la tabla de ventas."""
    data = []
    for _ in range(n):
        customer_id = random.choice(customer_ids)
        product_id = random.choice(product_ids)
        sale_date = fake.date_between(start_date="-1y", end_date="today")
        quantity = random.randint(1, 5)
        data.append([customer_id, product_id, sale_date, quantity])

    df = pd.DataFrame(data, columns=[
        "customer_id", "product_id", "sale_date", "quantity"
    ])
    return df

def get_record_count(entity_name):
    """Solicita al usuario el número de registros a generar para una entidad."""
    while True:
        try:
            n = int(input(f"Enter the number of {entity_name} to generate: "))
            if n < 0: # Permitimos 0 para no generar datos de una entidad si no se desea
                raise ValueError
            return n
        except ValueError:
            print("Please enter a valid non-negative number.\n")

def main():
    print("=== store_analytics ===")
    print("Fake Data Generator for Database Population\n")

    # Solicitar número de registros para cada entidad
    num_customers = get_record_count("customers")
    num_products = get_record_count("products")
    num_sales = get_record_count("sales")

    # Generar datos
    customers_df = generate_customers_data(num_customers)
    products_df = generate_products_data(num_products)

    # Para generar ventas, necesitamos IDs válidos.
    # Como los IDs son SERIAL, podemos asumir que irán de 1 a N.
    customer_ids = list(range(1, num_customers + 1))
    product_ids = list(range(1, num_products + 1))
    
    if num_sales > 0 and (not customer_ids or not product_ids):
        print("\n Cannot generate sales data because there are no customers or products.")
        sales_df = pd.DataFrame()
    else:
        sales_df = generate_sales_data(num_sales, customer_ids, product_ids)

    print(f"\n Successfully generated {len(customers_df)} customers, {len(products_df)} products, and {len(sales_df)} sales.")

    # Save CSV
    save = input("\nWould you like to save the CSV file? (y/n): ").lower()
    if save == 'y':
        # Guardar cada DataFrame en su propio archivo CSV
        customers_df.to_csv("customers.csv", index=False)
        print(f"💾 File saved as: {os.path.abspath('customers.csv')}")
        
        products_df.to_csv("products.csv", index=False)
        print(f"💾 File saved as: {os.path.abspath('products.csv')}")

        sales_df.to_csv("sales.csv", index=False)
        print(f"💾 File saved as: {os.path.abspath('sales.csv')}")
    else:
        print("\nFiles not saved.")

    print("\nProcess completed. Project Insight – Lufemage Labs © 2025")

if __name__ == "__main__":
    main()
