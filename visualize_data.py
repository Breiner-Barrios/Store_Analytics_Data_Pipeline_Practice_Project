import matplotlib.pyplot as plt
import seaborn as sns
from db import SessionLocal
from query_data import (
    get_total_sales_per_customer,
    get_top_selling_products,
    get_monthly_sales_trend,
    get_total_sales_per_customer_gender
)

def visualize_top_selling_products(df):
    """Genera un gráfico de barras para los productos más vendidos."""
    if df.empty:
        print("No hay datos de productos para visualizar.")
        return
        
    plt.figure(figsize=(10, 6))
    sns.barplot(x='total_quantity_sold', y='product_name', data=df, palette='viridis')
    plt.title('Top 5 Productos Más Vendidos por Cantidad')
    plt.xlabel('Cantidad Total Vendida')
    plt.ylabel('Producto')
    plt.tight_layout()
    plt.show()

def visualize_monthly_sales_trend(df):
    """Genera un gráfico de líneas para la tendencia de ventas mensuales."""
    if df.empty:
        print("No hay datos de ventas mensuales para visualizar.")
        return

    plt.figure(figsize=(12, 6))
    sns.lineplot(x='sales_month', y='total_sales', data=df, marker='o', color='royalblue')
    plt.title('Tendencia de Ventas Mensuales')
    plt.xlabel('Mes')
    plt.ylabel('Ventas Totales ($)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def visualize_sales_by_gender(df):
    """Genera un gráfico de pastel para las ventas por género."""
    if df.empty:
        print("No hay datos de ventas por género para visualizar.")
        return

    plt.figure(figsize=(8, 8))
    plt.pie(df['total_sales'], labels=df['customer_gender'], autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
    plt.title('Distribución de Ventas por Género del Cliente')
    plt.ylabel('') # Ocultar la etiqueta del eje y
    plt.show()

def main():
    """
    Función principal para ejecutar las consultas y generar las visualizaciones.
    """
    print("=== Iniciando la visualización de datos ===")
    
    # Configurar un estilo visual atractivo para los gráficos
    sns.set_theme(style="whitegrid")

    session = SessionLocal()
    try:
        # 1. Visualizar los productos más vendidos
        print("📊 Generando gráfico de productos más vendidos...")
        top_products_df = get_top_selling_products(session, limit=5)
        visualize_top_selling_products(top_products_df)

        # 2. Visualizar la tendencia de ventas mensuales
        print("📈 Generando gráfico de tendencia de ventas mensuales...")
        monthly_sales_df = get_monthly_sales_trend(session)
        visualize_monthly_sales_trend(monthly_sales_df)

        # 3. Visualizar la distribución de ventas por género
        print("🧑‍🤝‍🧑 Generando gráfico de distribución por género...")
        gender_sales_df = get_total_sales_per_customer_gender(session)
        visualize_sales_by_gender(gender_sales_df)

    except Exception as e:
        print(f"❌ Ocurrió un error durante la visualización: {e}")
    finally:
        session.close()
        print("Sesión de base de datos cerrada.")

if __name__ == "__main__":
    main()