# Informe de Pruebas Unitarias y Corrección de Bugs

## 1. Análisis de Módulos
* **Calculadora:** Se diseñaron pruebas para validar operaciones aritméticas básicas y verificar que las funciones de límites matemáticos (como división por cero o raíces negativas) gestionen las excepciones adecuadamente.
* **Descuentos:** Se estructuraron casos para validar la correcta aplicación de porcentajes, montos finales y la gestión de errores ante porcentajes de descuento fuera del rango válido (0 a 100).
* **Conversor:** Se probaron conversiones entre distintas unidades físicas (temperatura, distancia, peso), enfocando las pruebas en detectar cálculos erróneos en las fórmulas y asegurar que valores físicamente imposibles (como Kelvin negativos) lancen excepciones.

## 2. Bugs Encontrados y Corregidos
1. **Módulo Calculadora (`raiz_cuadrada`):**
   - **Error:** No validaba números negativos, por lo que no lanzaba la excepción esperada.
   - **Solución:** Se agregó la validación `if a < 0: raise ValueError(...)` antes de realizar la operación matemática.

2. **Módulo Conversor (`kelvin_a_celsius`):**
   - **Error:** Permitía ingresar valores Kelvin por debajo del cero absoluto (-273.15 °C) sin validar la entrada.
   - **Solución:** Se agregó la validación `if kelvin < 0: raise ValueError(...)`.

3. **Módulo Conversor (`kilometros_a_millas`):**
   - **Error:** Tenía un error en la fórmula matemática, multiplicando en lugar de dividir por el factor de conversión 1.60934.
   - **Solución:** Se corrigió el operador multiplicativo `*` por el operador de división `/`.

## 3. Evidencias Clave
Las capturas de pantalla de la ejecución de las pruebas unitarias (errores iniciales en rojo, 15 pruebas pasadas en verde y reporte de cobertura del 100%) se encuentran adjuntas en el documento:
* [Evidencias de las pruebas.docx](./Evidencias%20de%20las%20pruebas.docx)
