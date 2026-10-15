# Informe de Pruebas Unitarias y Corrección de Bugs

## 1. Datos
* **Nombre:** Juan David Henao Jimenez
* **Grupo:** DevOps 
* **Fecha:** 14 de octubre de 2026

---

## 2. Análisis por Módulo

### Módulo `calculadora.py`
* **¿Qué hace?:** Realiza operaciones matemáticas fundamentales como suma, resta, multiplicación, división y raíz cuadrada.
* **Casos probados y justificación:** Se probaron operaciones estándar para verificar la exactitud de los resultados. Se decidió incluir casos de borde y manejo de excepciones (como división por cero y raíces de números negativos) para garantizar la robustez del código y evitar fallos no controlados en tiempo de ejecución.

### Módulo `descuentos.py`
* **¿Qué hace?:** Calcula el precio final de un producto aplicando un porcentaje de descuento determinado.
* **Casos probados y justificación:** Se evaluaron valores representativos de descuento (0%, 100% y valores intermedios) para confirmar la lógica del negocio. También se probaron valores fuera del rango permitido (menores a 0% o mayores a 100%) para asegurar que se lancen las excepciones adecuadas frente a datos de entrada no válidos.

### Módulo `conversor.py`
* **¿Qué hace?:** Realiza conversiones entre distintas unidades físicas de temperatura, distancia, masa y volumen.
* **Casos probados y justificación:** Se validaron las equivalencias matemáticas entre unidades de uso común. Se enfatizó la prueba de límites físicos (como valores en grados Kelvin menores al cero absoluto) y fórmulas de precisión para detectar posibles errores algebraicos o de validación de entradas.

---

## 3. Tabla de Bugs Encontrados y Corregidos

| Función | Entrada de prueba | Resultado erróneo vs Esperado | Corrección realizada |
| :--- | :--- | :--- | :--- |
| `raiz_cuadrada` | `a = -4` | **Erróneo:** Retornaba un número complejo `2j` sin arrojar excepción.<br>**Esperado:** Lanzar `ValueError`. | Se agregó la validación `if a < 0: raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")`. |
| `kelvin_a_celsius` | `kelvin = -5` | **Erróneo:** Retornaba `-278.15` permitiendo valores bajo 0 K.<br>**Esperado:** Lanzar `ValueError`. | Se añadió la validación `if kelvin < 0: raise ValueError("Los grados Kelvin no pueden ser negativos")`. |
| `kilometros_a_millas` | `kilometros = 1.60934` | **Erróneo:** Multiplicaba dando `2.59`.<br>**Esperado:** Dividir dando `1.00`. | Se corrigió el operador matemático reemplazando la multiplicación (`*`) por división (`/`). |

---

## 4. Cobertura de Código

### Reporte de Salida (`pytest-cov`)

```text
---------- coverage: platform linux, python 3.13.5-final-0 ----------
Name                 Stmts   Miss  Cover   Missing
--------------------------------------------------
src/calculadora.py      14      0   100%
src/conversor.py        42      0   100%
src/descuentos.py        8      0   100%
--------------------------------------------------
TOTAL                   64      0   100%
```
## 5. Lectura de los resultados: 
Se logró alcanzar una cobertura del 100% en los tres módulos analizados (calculadora.py, conversor.py y descuentos.py). Esto indica que durante la ejecución del conjunto de 15 pruebas unitarias, todas las líneas de código, declaraciones y bifurcaciones condicionales (if/else) fueron ejecutadas al menos una vez, validando tanto los caminos de éxito como el lanzamiento de excepciones.

Las capturas de pantalla de la ejecución de las pruebas unitarias (errores iniciales en rojo, 15 pruebas pasadas en verde y reporte de cobertura del 100%) se encuentran adjuntas en el documento:
* [Evidencias de las pruebas.docx](./Evidencias%20de%20las%20pruebas.docx)

  
## 6. Reflexion 
¿Qué NO mide la cobertura de código?
La cobertura de código únicamente mide el porcentaje de líneas que fueron ejecutadas durante la corrida de los tests, pero no garantiza la calidad ni la corrección lógica del software. Un módulo puede tener un 100% de cobertura y aún así contener bugs de lógica, no considerar casos de borde complejos, pasar por alto requerimientos de negocio o no evaluar adecuadamente el rendimiento y la seguridad del sistema.

## 7. Aprendizaje
A través de este taller comprendí la importancia del desarrollo guiado por pruebas y el rol crítico que juegan las pruebas unitarias dentro del ciclo DevOps. Aprendí a identificar excepciones no controladas y errores sutiles de lógica matemática, así como la importancia de estructurar correctamente las aserciones para prevenir que errores de código lleguen a entornos de producción.
