import pytest
from src.calculadora import sumar, restar, multiplicar, dividir, raiz_cuadrada

def test_sumar_numeros_positivos():
    # Arrange
    a, b = 7, 5
    # Act
    resultado = sumar(a, b)
    # Assert
    assert resultado == 12

def test_restar_numeros_positivos():
    # Arrange
    a, b = 10, 4
    # Act
    resultado = restar(a, b)
    # Assert
    assert resultado == 6

def test_multiplicar_por_cero():
    # Arrange
    a, b = 8, 0
    # Act
    resultado = multiplicar(a, b)
    # Assert
    assert resultado == 0

def test_dividir_por_cero_lanza_excepcion():
    # Arrange
    a, b = 10, 0
    # Act & Assert
    with pytest.raises(ValueError):
        dividir(a, b)

def test_raiz_cuadrada_numero_negativo_lanza_excepcion():
    # Arrange
    numero = -9
    # Act & Assert
    with pytest.raises(ValueError):
        raiz_cuadrada(numero)
