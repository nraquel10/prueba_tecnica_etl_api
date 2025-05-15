import pandas as pd
import mysql.connector
from dotenv import load_dotenv
import os

# Cargar variables del archivo .env
load_dotenv()

# Conexión a la base de datos MySQL
db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

cursor = db.cursor()

# Leer archivo CSV
df = pd.read_csv("data_prueba_tecnica.csv")

# Normalizar columnas: minúsculas y sin espacios
df.columns = [c.strip().lower() for c in df.columns]

# Transformaciones necesarias
df["amount"] = df["amount"].astype(float)
df["created_at"] = pd.to_datetime(df["created_at"])
df["paid_at"] = pd.to_datetime(df["paid_at"], errors="coerce")  # Puede haber NaT

# Renombrar "paid_at" a "updated_at"
df.rename(columns={"paid_at": "updated_at"}, inplace=True)

# Crear tabla de compañías (únicas)
companies = df[["company_id", "name"]].drop_duplicates()
companies.columns = ["id", "company_name"]  # renombrar para coincidir con la tabla

# Insertar compañías
print("Insertando compañías...")
for _, row in companies.iterrows():
    cursor.execute("""
        INSERT INTO companies (id, company_name)
        VALUES (%s, %s)
        ON DUPLICATE KEY UPDATE company_name = VALUES(company_name)
    """, (row["id"], row["company_name"]))

# Insertar transacciones
print("Insertando cargos...")
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO charges (id, company_id, amount, status, created_at, updated_at)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        row["id"],
        row["company_id"],
        row["amount"],
        row["status"],
        row["created_at"].to_pydatetime(),
        row["updated_at"].to_pydatetime() if pd.notna(row["updated_at"]) else None
    ))

# Confirmar cambios
db.commit()

# Cerrar conexión
cursor.close()
db.close()

print("✅ ETL finalizado correctamente.")
