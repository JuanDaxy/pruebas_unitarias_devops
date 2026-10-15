def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

def raiz_cuadrada(a):
    if a < 0:
        raise ValueError("No se puede calcular la raiz cuadrada de un numero negativo")
    return a ** 0.5

def promedio(lista):
    """Calcula el promedio de una lista de números."""
    if not lista:
        raise ValueError("La lista no puede estar vacía")
    return sum(lista) / len(lista)

def maximo(lista):
    """Encuentra el número máximo de una lista."""
    if not lista:
        raise ValueError("La lista no puede estar vacía")
    max_val = lista[0]
    for num in lista:
        if num > max_val:
            max_val = num
    return max_val

def minimo(lista):
    """Encuentra el número mínimo de una lista."""
    if not lista:
        raise ValueError("La lista no puede estar vacía")
    # BUG 2: No maneja correctamente la comparación inicial
    min_val = 0
    for num in lista:
        if num < min_val:
            min_val = num
    return min_val

def calcular_area_rectangulo(base, altura):
    """Calcula el área de un rectángulo."""
    if base < 0 or altura < 0:
        raise ValueError("La base y altura deben ser positivas")
    return base * altura

def calcular_perimetro_rectangulo(base, altura):
    """Calcula el perímetro de un rectángulo."""
    if base < 0 or altura < 0:
        raise ValueError("La base y altura deben ser positivas")
    return 2 * (base + altura)
