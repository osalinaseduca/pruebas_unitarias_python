import pytest
from cine import Pelicula

pelicula1 = Pelicula("Bridget Jones: Loca por él", 100, 8)
pelicula2 = Pelicula("Captain America: Brave New World", 50, 10)
pelicula3 = Pelicula("Paddington in Peru", 75, 9)


def test_vender_entradas_suficientes():
    resultado = pelicula1.vender_entradas(3)
    assert resultado=="Has comprado 3 entradas para Bridget Jones: Loca por él. Total: $24"

def test_vender_entradas_insuficientes():
    resultado = pelicula2.vender_entradas(51)
    assert resultado=="No hay suficientes asientos disponibles. Solo quedan 50 asientos."

def test_vender_entradas_cero():
    resultado = pelicula3.vender_entradas(0)
    assert resultado=="Has comprado 0 entradas para Paddington in Peru. Total: $0"