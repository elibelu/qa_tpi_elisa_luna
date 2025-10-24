
# Definir la función que realiza la verificación
def es_primo(numero):
    """
    Retornar True si el número es primo, y False en caso contrario.
    """
    
    # 1 y números menores no son primos
    if numero <= 1:
        return False
    
    # Ciclo for para verificar divisores desde 2 hasta (numero - 1)
    for i in range(2, numero):
        # Si el resto es 0, 'i' es un divisor, y no es primo.
        if (numero % i) == 0:
            return False 
            
    # Si el ciclo termina sin encontrar divisores, es primo.
    return True

# --- Lógica principal del programa ---

# Variables para control de entrada
entrada_valida = False
numero_ingresado = 0
entrada_usuario = "" # Usaremos una cadena vacía inicialmente

# Ciclo while para solicitar la entrada hasta que el usuario ingrese un valor aceptable
while not entrada_valida:
    
    entrada_usuario = input("Por favor, ingresar un número entero: ")

    
    if len(entrada_usuario) > 0: # Asegurar que la entrada no esté vacía
        
        # Caso 1: Es un número positivo (solo dígitos)
        if entrada_usuario.isdigit():
            numero_ingresado = int(entrada_usuario)
            entrada_valida = True
            
        # Caso 2: Es un número negativo (empieza con - y el resto es dígito)
        elif entrada_usuario.startswith('-') and entrada_usuario[1:].isdigit():
            numero_ingresado = int(entrada_usuario)
            entrada_valida = True
            
        else:
            # Si contiene letras, decimales, etc.
            print("Entrada inválida. Debe contener solo números enteros y opcionalmente un signo (-).")

    else:
        print("La entrada no puede estar vacía. Intentar de nuevo.")

# Llamar a la función y mostrar el resultado
if es_primo(numero_ingresado):
    print(f"El número {numero_ingresado} ES primo.")
else:
    print(f"El número {numero_ingresado} NO es primo.")