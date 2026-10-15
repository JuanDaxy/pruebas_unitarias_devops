# Informe de Pruebas Unitarias y Corrección de Bugs

## 1. Análisis de Módulos
* **Calculadora:** Se probaron operaciones básicas y límites matemáticos (ej. división por cero y raíces negativas).
* **Descuentos:** (Pendiente)
* **Conversor:** (Pendiente)

## 2. Bugs Encontrados y Corregidos
1. **Módulo Calculadora (`raiz_cuadrada`):** 
   - **Error:** La función no validaba entradas negativas, por lo que no lanzaba la excepción en la prueba.
   - **Solución:** Se agregó la validación `if a < 0: raise ValueError("...")` antes del cálculo.

## 3. Evidencias Clave
*(Las imágenes se adjuntarán al final)*
