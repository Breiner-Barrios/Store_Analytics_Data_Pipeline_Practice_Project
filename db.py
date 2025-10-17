import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, Numeric, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener la URL de la base de datos desde las variables de entorno
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
Base = declarative_base()
 
class Customers(Base):
    __tablename__ = 'customers'
    __table_args__ = {'schema': 'store_analytics'} 
    
    customer_id = Column(Integer, primary_key=True)
    name = Column(String)
    gender = Column(String)
    age = Column(Integer)
    city = Column(String)

    def __repr__(self):
        return f"<Customer(id={self.customer_id}, name='{self.name}')>"

class Products(Base):
    __tablename__ = 'products'
    __table_args__ = {'schema': 'store_analytics'}

    product_id = Column(Integer, primary_key=True)
    name = Column(String)
    category = Column(String)
    price = Column(Numeric(10, 2))
    stock = Column(Integer)

    def __repr__(self):
        return f"<Product(id={self.product_id}, name='{self.name}')>"

class Sales(Base):
    __tablename__ = 'sales'
    __table_args__ = {'schema': 'store_analytics'}

    sale_id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('store_analytics.customers.customer_id'))
    product_id = Column(Integer, ForeignKey('store_analytics.products.product_id'))
    sale_date = Column(Date)
    quantity = Column(Integer)

    def __repr__(self):
        return f"<Sale(id={self.sale_id}, customer_id={self.customer_id}, product_id={self.product_id})>"

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
