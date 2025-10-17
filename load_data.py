import pandas as pd
from sqlalchemy.orm import sessionmaker
from db import engine, Customers, Products, Sales
import os

# Crear una sesión para interactuar con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()

def load_csv_to_db(file_path, model, session):
    """
    Carga los datos de un archivo CSV a una tabla de la base de datos.

    Args:
        file_path (str): La ruta al archivo CSV.
        model: La clase del modelo de SQLAlchemy correspondiente.
        session (Session): La sesión de SQLAlchemy para ejecutar la transacción.
    """
    if not os.path.exists(file_path):
        print(f"❌ Error: El archivo {file_path} no fue encontrado.")
        return

    try:
        # Leer el CSV con pandas
        df = pd.read_csv(file_path)
        # Convertir el DataFrame a una lista de diccionarios
        data = df.to_dict(orient='records')

        # Insertar los datos en bloque para mayor eficiencia
        session.bulk_insert_mappings(model, data)
        session.commit()
        print(f"{len(data)} registros cargados exitosamente en la tabla '{model.__tablename__}'.")

    except Exception as e:
        session.rollback() # Revertir cambios en caso de error
        print(f"❌ Error al cargar {file_path}: {e}")
    

def main():
    print("=== Iniciando la carga de datos a la base de datos ===")

    # Usar os.path.join para construir rutas de archivo de forma segura
    seeders_dir = 'seeders'

    # El orden es importante debido a las claves foráneas (foreign keys)
    # 1. Cargar clientes
    load_csv_to_db(os.path.join(seeders_dir, 'customers.csv'), Customers, db)

    # 2. Cargar productos
    load_csv_to_db(os.path.join(seeders_dir, 'products.csv'), Products, db)

    # 3. Cargar ventas (depende de clientes y productos)
    load_csv_to_db(os.path.join(seeders_dir, 'sales.csv'), Sales, db)

    print("\n=== Proceso de carga finalizado. ===")


if __name__ == "__main__":
    main()
    db.close() # Cerrar la sesión al final
