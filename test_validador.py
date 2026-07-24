#Persona 1 (Erick Froylan Pineda Aguillon)
import pytest
from validador import es_password_valida

def test_password_corta_devuelve_false():
    password_corta = "abc"
    resultado = es_password_valida(password_corta)   
    assert resultado is False
