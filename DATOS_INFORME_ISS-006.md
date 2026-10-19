# DATOS PARA EL INFORME ENTREGABLE - TAREA ISS-006

**Módulo asignado:** `utils.py`  
**Integrante:** Juan Mateo Soruco  
**Objetivo:** Cobertura de pruebas (100% Branch Coverage) y análisis de Grafos de Flujo de Control (CFG) para `utils.py`.

---

## 1. Sección 7: Análisis de Caja Blanca y Complejidad Ciclomática

### 7.15. Función `is_number(num)`
* **Descripción:** Verifica si una entrada puede interpretarse como un número real. Intenta convertir el valor recibido a punto flotante (`float(num)`). Si la conversión tiene éxito retorna `True`; si se produce una excepción `ValueError`, la captura y retorna `False`.
* **Métricas del Grafo de Flujo de Control (CFG):**
  * Nodos ($N$): 4
  * Aristas/Arcos ($E$): 4
  * Nodos de decisión / predicados ($P$): 1
  * Regiones cerradas + abierta ($R$): 2
* **Cálculo formal de Complejidad Ciclomática ($V(G)$):**
  * Por aristas y nodos: $V(G) = E - N + 2P = 4 - 4 + 2(1) = 2$
  * Por nodos predicados: $V(G) = P + 1 = 1 + 1 = 2$
  * Por regiones: $V(G) = R = 2$
  * **Complejidad Ciclomática confirmada:** $V(G) = 2$
* **Conjunto Básico de Caminos Independientes:**
  * **Camino 1:** Inicio $\to$ `float(num)` exitoso $\to$ `return True` $\to$ Fin.
  * **Camino 2:** Inicio $\to$ `float(num)` lanza `ValueError` $\to$ captura `except ValueError` $\to$ `return False` $\to$ Fin.
* **Diseño de Casos de Prueba:**
  | ID | Condición de prueba / Entrada | Resultado esperado |
  | :--- | :--- | :--- |
  | TC-029 | Entrada convertible a número: `"123"` | Retorna `True` |
  | TC-030 | Entrada no convertible / inválida: `"abc"` | Retorna `False` |

---

### 7.16. Función `is_valid_category(cat)`
* **Descripción:** Comprueba que una categoría no sea un valor numérico ni coincida con el nombre o abreviatura de un mes. Primero invoca `is_number(cat)`; si es numérico retorna `False`. Luego normaliza la cadena con `cat.capitalize()` y verifica si pertenece a las claves (`MONTHS.keys()`) o a los valores (`MONTHS.values()`) del diccionario de meses; si coincide con alguno retorna `False`. En cualquier otro caso retorna `True`.
* **Métricas del Grafo de Flujo de Control (CFG):**
  * Nodos ($N$): 7
  * Aristas/Arcos ($E$): 9
  * Nodos de decisión / predicados ($P$): 3 (`is_number(cat)`, `in MONTHS.keys()`, `in MONTHS.values()`)
  * Regiones ($R$): 4
* **Cálculo formal de Complejidad Ciclomática ($V(G)$):**
  * Por aristas y nodos: $V(G) = E - N + 2P = 9 - 7 + 2(1) = 4$
  * Por nodos predicados: $V(G) = P + 1 = 3 + 1 = 4$
  * Por regiones: $V(G) = R = 4$
  * **Complejidad Ciclomática confirmada:** $V(G) = 4$
* **Conjunto Básico de Caminos Independientes:**
  * **Camino 1:** Inicio $\to$ `is_number(cat) == True` $\to$ `return False` $\to$ Fin.
  * **Camino 2:** Inicio $\to$ `is_number == False` $\to$ `cat.capitalize() in MONTHS.keys() == True` $\to$ `return False` $\to$ Fin.
  * **Camino 3:** Inicio $\to$ `is_number == False` $\to$ no está en keys $\to$ `cat.capitalize() in MONTHS.values() == True` $\to$ `return False` $\to$ Fin.
  * **Camino 4:** Inicio $\to$ `is_number == False` $\to$ no está en keys $\to$ no está en values $\to$ `return True` $\to$ Fin.
* **Diseño de Casos de Prueba:**
  | ID | Condición de prueba / Entrada | Resultado esperado |
  | :--- | :--- | :--- |
  | TC-031 | Categoría numérica: `"120"` | Retorna `False` |
  | TC-032 | Nombre completo de mes: `"January"` | Retorna `False` |
  | TC-033 | Abreviatura de mes: `"Jan"` | Retorna `False` |
  | TC-034 | Categoría válida arbitraria: `"Food"` | Retorna `True` |

---

### 7.17. Función `find_month(month, is_num = False)`
* **Descripción:** Identifica y devuelve la abreviatura de tres letras de un mes a partir de su nombre o de su número cronológico ($1$ a $12$). Si `str(month).capitalize()` se encuentra en `MONTHS.keys()`, devuelve su abreviatura. Si no coincide, pero el parámetro booleano `is_num` es `True` y `int(month)` se encuentra entre las claves de `month_number` ($1$ al $12$), devuelve la abreviatura respectiva. En caso contrario devuelve `None`.
* **Métricas del Grafo de Flujo de Control (CFG):**
  * Nodos ($N$): 8
  * Aristas/Arcos ($E$): 10
  * Nodos de decisión / predicados ($P$): 3 (`in MONTHS.keys()`, `is_num == True`, `in month_number.keys()`)
  * Regiones ($R$): 4
* **Cálculo formal de Complejidad Ciclomática ($V(G)$):**
  * Por aristas y nodos: $V(G) = E - N + 2P = 10 - 8 + 2(1) = 4$
  * Por nodos predicados: $V(G) = P + 1 = 3 + 1 = 4$
  * Por regiones: $V(G) = R = 4$
  * **Complejidad Ciclomática confirmada:** $V(G) = 4$
* **Conjunto Básico de Caminos Independientes:**
  * **Camino 1:** Inicio $\to$ `str(month).capitalize() in MONTHS.keys()` es `True` $\to$ `return MONTHS[...]` $\to$ Fin.
  * **Camino 2:** Inicio $\to$ no está en `MONTHS.keys()` $\to$ `is_num == False` $\to$ `return None` $\to$ Fin.
  * **Camino 3:** Inicio $\to$ no está en `MONTHS.keys()` $\to$ `is_num == True` $\to$ `int(month) in month_number.keys()` es `True` $\to$ `return month_number[...]` $\to$ Fin.
  * **Camino 4:** Inicio $\to$ no está en `MONTHS.keys()` $\to$ `is_num == True` $\to$ `int(month)` fuera del rango $[1, 12]$ $\to$ `return None` $\to$ Fin.
* **Diseño de Casos de Prueba:**
  | ID | Condición de prueba / Entrada | Resultado esperado |
  | :--- | :--- | :--- |
  | TC-035 | Nombre de mes válido: `"January"` (is_num por defecto False) | Retorna abreviatura (`"Jan"`) |
  | TC-036 | Nombre inválido con `is_num=False`: `"NotAMonth"` | Retorna `None` |
  | TC-037 | Número válido con `is_num=True`: `10` | Retorna abreviatura (`"Oct"`) |
  | TC-038 | Número fuera de rango con `is_num=True`: `13` | Retorna `None` |

---

### 7.18. Función `sort_months_with_data(months_data: dict)`
* **Descripción:** Organiza cronológicamente los datos de gastos por mes según la secuencia del calendario gregoriano (`Jan` a `Dec`). Recorre la lista de orden predefinida `month_order` e incluye en `sorted_months` solo aquellos meses que figuren como claves en el diccionario `months_data`. Luego genera la lista `sorted_values` extrayendo los importes correspondientes y retorna ambas listas en una tupla `(sorted_months, sorted_values)`.
* **Métricas del Grafo de Flujo de Control (CFG):**
  * Nodos ($N$): 8
  * Aristas/Arcos ($E$): 10
  * Nodos de decisión / predicados ($P$): 3 (Iterador de `month_order`, filtro condicional `if mnth in months_data`, iterador de `sorted_months`)
  * Regiones ($R$): 4
* **Cálculo formal de Complejidad Ciclomática ($V(G)$):**
  * Por aristas y nodos: $V(G) = E - N + 2P = 10 - 8 + 2(1) = 4$
  * Por nodos predicados: $V(G) = P + 1 = 3 + 1 = 4$
  * Por regiones: $V(G) = R = 4$
  * **Complejidad Ciclomática confirmada:** $V(G) = 4$
* **Conjunto Básico de Caminos Independientes:**
  * **Camino 1:** Diccionario vacío `{}` (no se incorporan meses y el segundo bucle no itera) $\to$ Retorna `([], [])`.
  * **Camino 2:** Diccionario con meses en orden aleatorio $\to$ Comprueba el reordenamiento cronológico estricto según `month_order`.
  * **Camino 3:** Diccionario con claves arbitrarias que no son nombres de mes $\to$ Filtra y excluye las claves no válidas.
  * **Camino 4:** Diccionario con los 12 meses completos $\to$ Cada mes evalúa la condición verdadera y se ordenan del 1 al 12.
* **Diseño de Casos de Prueba:**
  | ID | Condición de prueba / Entrada | Resultado esperado |
  | :--- | :--- | :--- |
  | TC-039 | Diccionario vacío: `{}` | Retorna `([], [])` |
  | TC-040 | Meses desordenados: `{"Dec": 120, "Jan": 10, "May": 50, "Feb": 20}` | Retorna `(["Jan", "Feb", "May", "Dec"], [10, 20, 50, 120])` |
  | TC-041 | Claves arbitrarias no reconocidas: `{"Mar": 30, "Unknown": 999, "Aug": 80}` | Retorna `(["Mar", "Aug"], [30, 80])` |
  | TC-042 | Diccionario con los 12 meses del año | Retorna listas completas ordenadas de `Jan` a `Dec` con sus 12 valores |

---

## 2. Sección 8 / Implementación: Total de Complejidad y Estrategia de Pruebas
* **Complejidad Ciclomática Acumulada de ISS-006:**
  $$V(G)_{\text{total}} = V(\text{is\_number}) + V(\text{is\_valid\_category}) + V(\text{find\_month}) + V(\text{sort\_months\_with\_data})$$
  $$V(G)_{\text{total}} = 2 + 4 + 4 + 4 = \mathbf{14}$$
* **Implementación:** Archivo `test_utils.py` mediante `pytest` estructurado en 4 clases de prueba: `TestIsNumber` (2 tests), `TestIsValidCategory` (4 tests), `TestFindMonth` (4 tests) y `TestSortMonthsWithData` (4 tests).
* **Técnica empleada:** Cobertura estricta 1 a 1 de cada camino del conjunto básico de caminos independientes de McCabe, totalizando **exactamente 14 pruebas unitarias automatizadas**.

---

## 3. Sección 11.2: Resultados Finales Correspondientes a ISS-006

* **Pruebas ejecutadas:** 14 de 14 aprobadas (100% de éxito).
* **Sentencias del módulo `utils.py`:** 25 de 25 ejecutadas (100%).
* **Ramas instrumentadas (Branches):** 8 de 8 cubiertas en ambas direcciones (`True` y `False`).
* **Ramas parciales:** 0.
* **Cobertura de ramas reportada por pytest-cov:** **100%**.
* **Tabla de Cobertura de ISS-006:**
  | Archivo | Sentencias (Stmts) | No cubiertas (Miss) | Ramas (Branch) | Ramas parciales (BrPart) | Cobertura final |
  | :--- | :---: | :---: | :---: | :---: | :---: |
  | `utils.py` | 25 | 0 | 8 | 0 | **100%** |

---

## 4. Sección 12.2: Conclusiones de ISS-006

1. La técnica de análisis de Grafo de Flujo de Control (CFG) sobre `utils.py` permitió determinar con exactitud matemática los 14 caminos independientes requeridos para verificar la robustez de las validaciones del sistema.
2. Cada caso de prueba implementado en `test_utils.py` corresponde biunívocamente (1 a 1) a un camino básico identificado en el grafo, alcanzando el 100% de Branch Coverage con el mínimo teórico exacto de 14 pruebas.
3. Se comprobó la efectividad de la métrica de cobertura de ramas (*Branch Coverage*), logrando un 100% sin ramas parciales ni caminos inalcanzables en este módulo.
4. Las pruebas de caja blanca aseguraron que las funciones de utilidad proporcionen datos limpios y filtrados a los módulos dependientes (`data_handler`, `analysis` y `expense_tracker`), previniendo errores en tiempo de ejecución.

---

## 5. Sección 13.2: Instrucciones de Ejecución para ISS-006

### Comandos de ejecución y reporte (Linux / macOS / PowerShell):
```bash
# 1. Activar entorno virtual
source .venv/bin/activate   # En Linux/macOS
# .\venv\Scripts\Activate.ps1 # En Windows PowerShell

# 2. Ejecutar las 14 pruebas unitarias de utils.py en modo detallado
pytest test_utils.py -v

# 3. Medir cobertura de ramas con reporte en terminal
pytest test_utils.py -v --cov=utils --cov-branch --cov-report=term-missing

# 4. Generar reporte HTML interactivo
pytest test_utils.py --cov=utils --cov-branch --cov-report=html
# El reporte se genera en htmlcov/index.html
```
