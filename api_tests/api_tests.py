
import requests

# Base URL para la PokeAPI
BASE_URL = "https://pokeapi.co/api/v2/"

def test_caso1_berry_validation():
    """Caso 1: Berry 1 - Verificar size, soil_dryness y firmness."""
    print("\n--- Ejecutando Caso 1: Berry 1 ---")
    
    # Hacer la solicitud GET
    response = requests.get(f"{BASE_URL}berry/1")
    
    # Verificar que la respuesta es 200 OK
    assert response.status_code == 200, f"Error en la solicitud: {response.status_code}"
    
    # Convertir la respuesta a JSON
    data = response.json()
    
    # 1. Verificar 'size'
    assert data['size'] == 20, f"Fallo en size: Esperado 20, Obtenido {data['size']}"
    
    # 2. Verificar 'soil_dryness'
    assert data['soil_dryness'] == 15, f"Fallo en soil_dryness: Esperado 15, Obtenido {data['soil_dryness']}"
    
    # 3. Verificar 'firmness' (debe ser "soft")
    firmness_name = data['firmness']['name']
    assert firmness_name == "soft", f"Fallo en firmness: Esperado 'soft', Obtenido '{firmness_name}'"
    
    print("GET y verificaciones del Caso 1 exitosas.")


def test_caso2_berry_comparison():
    """Caso 2: Berry 2 - Verificar firmness y comparar size/soil_dryness con Berry 1."""
    print("\n--- Ejecutando Caso 2: Berry 2 y Comparación ---")
    
    # 1. Obtener datos de Berry 1 (referencia)
    response1 = requests.get(f"{BASE_URL}berry/1")
    data1 = response1.json()
    
    # 2. Obtener datos de Berry 2
    response2 = requests.get(f"{BASE_URL}berry/2")
    data2 = response2.json()
    
    # Verificar que ambas respuestas son 200 OK
    assert response2.status_code == 200, f"Error en la solicitud de Berry 2: {response2.status_code}"

    # 3. Verificar 'firmness' de Berry 2 (debe ser "hard")
    firmness_name2 = data2['firmness']['name']
    assert firmness_name2 == "super-hard", f"Fallo en firmness de Berry 2: Esperado 'super-hard', Obtenido '{firmness_name2}'"
    
    # 4. Comparar 'size' de Berry 2 con Berry 1 (debe ser mayor)
    size1 = data1['size']
    size2 = data2['size']
    assert size2 > size1, f"Fallo en comparación de size: {size2} no es mayor que {size1}"
    
    # 5. Comparar 'soil_dryness' de Berry 2 con Berry 1 (debe ser menor)
    dryness1 = data1['soil_dryness']
    dryness2 = data2['soil_dryness']
    assert dryness2 == dryness1, f"Fallo en comparación de dryness: {dryness2} no es igual que {dryness1}"
    
    print("GET y verificaciones del Caso 2 exitosas.")


def test_caso3_pikachu():
    """Caso 3: Pikachu - Verificar base_experience (rango) y tipo (electric)."""
    print("\n--- Ejecutando Caso 3: Pikachu ---")

    # Hacer la solicitud GET para Pikachu
    response = requests.get(f"{BASE_URL}pokemon/pikachu")
    
    # Verificar que la respuesta es 200 OK
    assert response.status_code == 200, f"Error en la solicitud: {response.status_code}"
    
    data = response.json()
    
    # 1. Verificar 'base_experience' (debe estar entre 100 y 150)
    base_xp = data['base_experience']
    assert 100 <= base_xp <= 150, f"Fallo en base_experience: {base_xp} no está en el rango [100, 150]"
    
    # 2. Verificar que su primer tipo sea 'electric'
    primer_tipo = data['types'][0]['type']['name']
    assert primer_tipo == "electric", f"Fallo en tipo: Esperado 'electric', Obtenido '{primer_tipo}'"

    print("GET y verificaciones del Caso 3 exitosas.")

# --- Ejecución manual (para correr desde terminal) ---
if __name__ == "__main__":
    print("Iniciando pruebas de API...")
    test_caso1_berry_validation()
    test_caso2_berry_comparison()
    test_caso3_pikachu()
    print("\n--- Todas las pruebas de API finalizadas ---")