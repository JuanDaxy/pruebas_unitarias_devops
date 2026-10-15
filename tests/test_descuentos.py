import pytest
from src.descuentos import aplicar_descuento

def test_aplicar_descuento_valido():
    # Arrange
    precio = 100.0
    porcentaje = 20.0
    # Act
    resultado = aplicar_descuento(precio, porcentaje)
    # Assert
    assert resultado == 80.0

def test_aplicar_descuento_cero_porcentaje():
    # Arrange
    precio = 50.0
    porcentaje = 0.0
    # Act
    resultado = aplicar_descuento(precio, porcentaje)
    # Assert
    assert resultado == 50.0

def test_aplicar_descuento_cien_porcentaje():
    # Arrange
    precio = 200.0
    porcentaje = 100.0
    # Act
    resultado = aplicar_descuento(precio, porcentaje)
    # Assert
    assert resultado == 0.0

def test_descuento_con_precio_negativo_lanza_error():
    # Arrange
    precio = -10.0
    porcentaje = 15.0
    # Act & Assert
    with pytest.raises(ValueError):
        aplicar_descuento(precio, porcentaje)

def test_descuento_mayor_a_cien_lanza_error():
    # Arrange
    precio = 100.0
    porcentaje = 150.0
    # Act & Assert
    with pytest.raises(ValueError):
        aplicar_descuento(precio, porcentaje)
