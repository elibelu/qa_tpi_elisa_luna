# ENTREGA FINAL: Automatización QA - [Elisa Luna]

Este repositorio contiene la automatización de los ejercicios requeridos para el TPI, cubriendo lógica de programación (Python), pruebas de interfaz de usuario (Cypress) y pruebas de servicios API (Python/Requests).

---

## 1. Lógica de Programación y Ejercicios (Python)

Ubicación: `ejercicios_python/`

| Ejercicio | Descripción | Herramientas Clave |
| :--- | :--- | :--- |
| **Número Primo** | Programa que verifica si un número ingresado por el usuario es primo o no. | `def()`, `if/else`, `for`, `range`, Operador `%` |
| **Ecuación Cuadrática** | Función que retorna las raíces (soluciones) de una ecuación cuadrática (`ax² + bx + c = 0`). | `def()`, `if/elif/else`, `math.sqrt()` |

---

## 2. Pruebas de Interfaz (Web - Cypress)

Ubicación: `cypress/e2e/`

**Reporte de Ejecución Final:** Los resultados se encuentran en `mochawesome-report/final-report.html`.

| Caso | Archivo | Descripción de la Prueba | Estado |
| :--- | :--- | :--- | :--- |
| **Caso 1** | `caso1.cy.js` | Logueo con `standard_user` y verificación del ordenamiento de productos (A-Z y Z-A). | PASÓ |
| **Caso 2** | `caso2.cy.js` | Añadir un producto al carrito, verificar el contador y verificar que el producto esté listado en la vista del carrito. | PASÓ |
| **Caso 3** | `caso3.cy.js` | Ciclo completo: Agregar, remover un artículo, verificar la remoción, agregar 2 artículos y finalizar el proceso de checkout. | PASÓ |

---

## 3. Pruebas de API (Servicios REST)

Ubicación: `api_tests/api_tests.py`

| Caso | Endpoint | Validación Realizada | Estado |
| :--- | :--- | :--- | :--- |
| **Caso 1** | `berry/1` | Verifica el `status_code (200)`, `size (20)`, `soil_dryness (15)` y el nombre de `firmness` (`soft`). | PASÓ |
| **Caso 2** | `berry/2` | Verifica `firmness` (`super-hard`), compara que el `size` sea mayor que el Caso 1 y que el `soil_dryness` sea igual que el Caso 1. | PASÓ |
| **Caso 3** | `pokemon/pikachu` | Verifica el `status_code (200)`, el rango de `base_experience` (entre 100 y 150) y que el `type` principal sea `electric`. | PASÓ |
