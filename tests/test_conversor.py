import pytest
from src.conversor import celsius_a_fahrenheit, metros_a_kilometros, libras_a_kilogramos, kelvin_a_celsius, kilometros_a_millas

def test_celsius_a_fahrenheit_cero_grados():
    # Arrange
    celsius = 0
    # Act
    resultado = celsius_a_fahrenheit(celsius)
    # Assert
    assert resultado == 32.0

def test_metros_a_kilometros_positivos():
    # Arrange
    metros = 5000
    # Act
    resultado = metros_a_kilometros(metros)
    # Assert
    assert resultado == 5.0

def test_libras_a_kilogramos_negativo_lanza_error():
    # Arrange
    libras = -10
    # Act & Assert
    with pytest.raises(ValueError):
        libras_a_kilogramos(libras)

def test_kelvin_negativo_lanza_error():
    # Arrange
    kelvin = -5
    # Act & Assert
    with pytest.raises(ValueError):
        kelvin_a_celsius(kelvin)

def test_kilometros_a_millas_valido():
    # Arrange
    kilometros = 1.60934
    # Act
    resultado = kilometros_a_millas(kilometros)
    # Assert
    assert round(resultado, 2) == 1.00
