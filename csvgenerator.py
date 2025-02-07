import pandas as pd

# Datos de prueba
datos = {
    "id": [1, 2, 3, 4, 5],
    "texto": [
        "La inteligencia artificial está transformando el mundo.",
        "Los modelos de lenguaje son una herramienta poderosa.",
        "Python es un lenguaje de programación muy popular.",
        "El aprendizaje automático es una rama de la IA.",
        "La ciencia de datos combina estadística y programación."
    ]
}

# Crear un DataFrame
df = pd.DataFrame(datos)

# Guardar el DataFrame en un archivo CSV
df.to_csv('data/datos.csv', index=False, encoding='utf-8')

print("Archivo CSV generado en 'data/datos.csv'.")