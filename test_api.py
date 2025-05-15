from api_numeros_faltantes import Conjunto100

# Simulación: número 42 fue extraído
numeros = list(range(1, 101))
numeros.remove(42)

conjunto = Conjunto100()
faltante = conjunto.extraer(numeros)

print(f"El número faltante es: {faltante}")
