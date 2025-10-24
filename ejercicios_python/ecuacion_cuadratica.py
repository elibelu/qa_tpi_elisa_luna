
# Importación del módulo 'math' para usar la función de raíz cuadrada
import math

def calcular_raices_cuadratica(a, b, c):
    """
    Retornar las raíces (soluciones) de una ecuación cuadrática ax^2 + bx + c = 0.
    """
    
    # Validar el caso en que 'a' es cero (no es una ecuación cuadrática)
    if a == 0:
        return {"estado": "Error", "mensaje": "El coeficiente 'a' no puede ser cero."}
    
    # Calcular el Discriminante (Delta = b^2 - 4ac)
    discriminante = (b**2) - (4 * a * c)
    
    # Estructura If-Elif-Else para manejar los tres casos
    
    # Caso 1: Dos raíces reales distintas (Discriminante > 0)
    if discriminante > 0:
        
        # Fórmula cuadrática: (-b +- sqrt(Delta)) / (2a)
        raiz1 = (-b + math.sqrt(discriminante)) / (2 * a)
        raiz2 = (-b - math.sqrt(discriminante)) / (2 * a)
        
        # Retornar un diccionario con las dos raíces
        return {
            "estado": "Dos raíces reales distintas",
            "x1": raiz1,
            "x2": raiz2
        }
        
    # Caso 2: Una raíz real doble (Discriminante = 0)
    elif discriminante == 0:
        
        # Fórmula simplificada: -b / 2a
        raiz = (-b) / (2 * a)
        
        # Retornar un diccionario con la raíz doble
        return {
            "estado": "Una raíz real doble",
            "x": raiz
        }
        
    # Caso 3: No hay raíces reales (Discriminante < 0)
    else: 
        
        # Retornar un diccionario con el mensaje de error
        return {
            "estado": "No hay raíces reales",
            "mensaje": "El discriminante es negativo, no hay soluciones reales."
        }

# --- Ejemplo de Uso ---

# Coeficientes de la ecuación: x^2 - 5x + 6 = 0 (Raíces esperadas: x=3 y x=2)
a_val = 1
b_val = -5
c_val = 6 

resultado = calcular_raices_cuadratica(a_val, b_val, c_val)

print(f"\nEcuación: {a_val}x^2 + {b_val}x + {c_val} = 0")
print("Resultado del cálculo:")

print(resultado)