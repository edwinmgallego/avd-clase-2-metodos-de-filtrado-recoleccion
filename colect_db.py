from sqlalchemy import create_engine
import pandas as pd

# Conexión a SQLite
engine = create_engine('sqlite:///mi_base_de_datos.db')

# Ejecutar consulta
query = "SELECT * FROM usuarios"
data = pd.read_sql(query, engine)
print(data.head())
