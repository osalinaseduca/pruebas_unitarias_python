import pytest
from biblioteca import Libro, Biblioteca

@pytest.fixture
def biblioteca():
    biblioteca = Biblioteca()
    libro1 = Libro("El Señor de los Anillos", "J.R.R. Tolkien", 1954)
    libro2 = Libro("1984", "George Orwell", 1949)
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
    biblioteca.eliminar_libro("1984")
    assert len(biblioteca.libros) == 1  
    assert biblioteca.buscar_libro("1984") is None  

def test_eliminar_libro_inexistente(biblioteca):
    biblioteca.eliminar_libro("El Gran Gatsby")
    assert len(biblioteca.libros) == 2  

# Prueba para buscar libros
def test_buscar_libro(biblioteca):
    libro = biblioteca.buscar_libro("El Señor de los Anillos")
    assert libro is not None  
    assert libro.titulo == "El Señor de los Anillos"  

def test_buscar_libro_inexistente(biblioteca):
    libro = biblioteca.buscar_libro("El Gran Gatsby")
    assert libro is None  

# Prueba para listar libros
def test_listar_libros(biblioteca):
    lista_libros = biblioteca.listar_libros()
    assert len(lista_libros) == 2 
    assert "El Señor de los Anillos" in lista_libros  

# Pruebas para prestar libros
def test_prestar_libro(biblioteca):
    resultado = biblioteca.prestar_libro("El Señor de los Anillos")
    assert "Has pedido prestado el libro 'El Señor de los Anillos'" in resultado  
    assert biblioteca.buscar_libro("El Señor de los Anillos").prestado is True  
def test_prestar_libro_ya_prestado(biblioteca):
    # Prestarlo por segunda vez
    biblioteca.prestar_libro("El Señor de los Anillos")
    resultado = biblioteca.prestar_libro("El Señor de los Anillos")
    assert "ya está prestado" in resultado  

def test_prestar_libro_inexistente(biblioteca):
    resultado = biblioteca.prestar_libro("El Gran Gatsby")
    assert "no se encuentra en la biblioteca" in resultado  

# Pruebas para devolver libros
def test_devolver_libro(biblioteca):
    biblioteca.prestar_libro("El Señor de los Anillos")
    resultado = biblioteca.devolver_libro("El Señor de los Anillos")
    assert "Has devuelto el libro 'El Señor de los Anillos'" in resultado  
    assert biblioteca.buscar_libro("El Señor de los Anillos").prestado is False  

def test_devolver_libro_no_prestado(biblioteca):
    resultado = biblioteca.devolver_libro("El Señor de los Anillos")
    assert "no estaba prestado" in resultado  

def test_devolver_libro_inexistente(biblioteca):
    resultado = biblioteca.devolver_libro("El Gran Gatsby")
    assert "no se encuentra en la biblioteca" in resultado  

