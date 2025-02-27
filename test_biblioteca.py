import pytest
from biblioteca import Libro, Biblioteca

@pytest.fixture
def biblioteca():
    biblioteca = Biblioteca()
    libro1 = Libro("Harry Potter y la Piedra Filosofal", "J.K. Rowling", 1997)
    libro2 = Libro("Memorias de Idhún", "Laura Gallego García", 2004)
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    return biblioteca

# Prueba para agregar libros
def test_agregar_libro(biblioteca):
    libro3 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 1967)
    biblioteca.agregar_libro(libro3)
    assert len(biblioteca.libros) == 3 
    assert biblioteca.buscar_libro("Cien Años de Soledad") is not None 

# Prueba para eliminar libros
def test_eliminar_libro(biblioteca):
    biblioteca.eliminar_libro("Memorias de Idhún")
    assert len(biblioteca.libros) == 1  
    assert biblioteca.buscar_libro("Memorias de Idhún") is None  

def test_eliminar_libro_inexistente(biblioteca):
    biblioteca.eliminar_libro("El Gran Gatsby")
    assert len(biblioteca.libros) == 2  

# Prueba para buscar libros
def test_buscar_libro(biblioteca):
    libro = biblioteca.buscar_libro("Harry Potter y la Piedra Filosofal")
    assert libro is not None  
    assert libro.titulo == "Harry Potter y la Piedra Filosofal"  

def test_buscar_libro_inexistente(biblioteca):
    libro = biblioteca.buscar_libro("El Gran Gatsby")
    assert libro is None  

# Prueba para listar libros
def test_listar_libros(biblioteca):
    lista_libros = biblioteca.listar_libros()
    assert len(lista_libros) == 2 
    assert "Harry Potter y la Piedra Filosofal de J.K. Rowling (1997) - disponible" in lista_libros  
    assert "Memorias de Idhún de Laura Gallego García (2004) - disponible" in lista_libros  

# Pruebas para prestar libros
def test_prestar_libro(biblioteca):
    resultado = biblioteca.prestar_libro("Harry Potter y la Piedra Filosofal")
    assert "Has pedido prestado el libro 'Harry Potter y la Piedra Filosofal'" in resultado  
    assert biblioteca.buscar_libro("Harry Potter y la Piedra Filosofal").prestado is True  

def test_prestar_libro_ya_prestado(biblioteca):
    # Prestarlo por segunda vez
    biblioteca.prestar_libro("Harry Potter y la Piedra Filosofal")
    resultado = biblioteca.prestar_libro("Harry Potter y la Piedra Filosofal")
    assert "ya está prestado" in resultado  

def test_prestar_libro_inexistente(biblioteca):
    resultado = biblioteca.prestar_libro("El Gran Gatsby")
    assert "no se encuentra en la biblioteca" in resultado  

# Pruebas para devolver libros
def test_devolver_libro(biblioteca):
    biblioteca.prestar_libro("Harry Potter y la Piedra Filosofal")
    resultado = biblioteca.devolver_libro("Harry Potter y la Piedra Filosofal")
    assert "Has devuelto el libro 'Harry Potter y la Piedra Filosofal'" in resultado  
    assert biblioteca.buscar_libro("Harry Potter y la Piedra Filosofal").prestado is False  

def test_devolver_libro_no_prestado(biblioteca):
    resultado = biblioteca.devolver_libro("Harry Potter y la Piedra Filosofal")
    assert "no estaba prestado" in resultado  

def test_devolver_libro_inexistente(biblioteca):
    resultado = biblioteca.devolver_libro("El Gran Gatsby")
    assert "no se encuentra en la biblioteca" in resultado


