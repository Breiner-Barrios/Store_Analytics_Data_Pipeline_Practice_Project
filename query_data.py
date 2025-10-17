import pandas as pd
from sqlalchemy import func, desc
from db import SessionLocal, Customers, Products, Sales

def get_total_sales_per_customer(session):
    """
    Calcula el total gastado por cada cliente.
    """
    query = (
        session.query(
            Customers.name.label("customer_name"),
            Customers.city,
            func.sum(Sales.quantity * Products.price).label("total_spent"),
        )
        .join(Sales, Customers.customer_id == Sales.customer_id)
        .join(Products, Sales.product_id == Products.product_id)
        .group_by(Customers.name, Customers.city)
        .having(func.sum(Sales.quantity * Products.price) > 10000)
        .order_by(desc("total_spent"))
    )
    # Convertir el resultado de la consulta a un DataFrame de Pandas
    df = pd.read_sql(query.statement, session.bind)
    return df


def get_top_selling_products(session, limit=5):
    """
    Encuentra los productos más vendidos por cantidad usando el ORM de SQLAlchemy.
    """
    query = (
        session.query(
            Products.name.label("product_name"),
            Products.category,
            func.sum(Sales.quantity).label("total_quantity_sold"),
        )
        .join(Sales, Products.product_id == Sales.product_id)
        .group_by(Products.name, Products.category)
        .order_by(desc("total_quantity_sold"))
        .limit(limit)
    )
    df = pd.read_sql(query.statement, session.bind)
    return df

def get_monthly_sales_trend(session):
    """
    Calcula la tendencia de ventas mensuales usando el ORM de SQLAlchemy.
    """
    # La función to_char es específica de PostgreSQL, la usamos con func
    sales_month = func.to_char(Sales.sale_date, "YYYY-MM").label("sales_month")

    query = (
        session.query(
            sales_month,
            func.sum(Sales.quantity * Products.price).label("total_sales"),
        )
        .join(Products, Sales.product_id == Products.product_id)
        .filter(func.extract("year", Sales.sale_date) == 2025)
        .group_by(sales_month)
        .order_by(desc("total_sales"))
    )
    df = pd.read_sql(query.statement, session.bind)
    return df

def get_total_sales_per_customer_gender(session):
    """
    Calcula el total de ventas agrupado por género del cliente.
    """
    query = (
        session.query(
            Customers.gender.label("customer_gender"),
            func.sum(Sales.quantity * Products.price).label("total_sales"),
        )
        .join(Sales, Customers.customer_id == Sales.customer_id)
        .join(Products, Sales.product_id == Products.product_id)
        .group_by(Customers.gender)
        .order_by(desc("total_sales"))
    )
    df = pd.read_sql(query.statement, session.bind)
    return df


def main():
    print("=== Ejecutando consultas de análisis de datos con SQLAlchemy ORM ===\n")

    # Crear una sesión para esta ejecución
    session = SessionLocal()
    try:
        print("--- 1. Total gastado por cliente ---")
        sales_per_customer = get_total_sales_per_customer(session)
        print(sales_per_customer.head())
        print(sales_per_customer.tail())
        print("-" * 40 + "\n")

        print(f"--- 2. Top {5} productos más vendidos ---")
        top_products = get_top_selling_products(session, limit=5)
        print(top_products)
        print("-" * 40 + "\n")

        print("--- 3. Tendencia de ventas mensuales ---")
        monthly_sales = get_monthly_sales_trend(session)
        print(monthly_sales)
        print("-" * 40 + "\n")
    except Exception as e:
        print(f"Ocurrió un error durante la consulta: {e}")
    finally:
        # Asegurarse de cerrar la sesión al finalizar
        session.close()
        print("Sesión de base de datos cerrada.")

if __name__ == "__main__":
    main()