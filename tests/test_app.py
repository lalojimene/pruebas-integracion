from app import productos

def test_productos_cargados():
    assert len(productos) == 3
