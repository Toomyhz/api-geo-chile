def test_get_regiones(client):
    response = client.get('/api/regiones/')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert all('tipo' in region and region['tipo'] == 'region' for region in data)

def test_get_region(client):
    response = client.get('/api/regiones/15/')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data,dict)
    assert data['tipo'] == 'region' and data['nombre'] == 'De Arica y Parinacota'

def test_get_region_error_codigo(client):
    response = client.get('/api/regiones/150/')
    assert response.status_code == 400
    data = response.get_json()
    assert isinstance(data,dict)
    assert data['error'] == 'Código inválido'

def test_get_region_error_no_encontrada(client):
    response = client.get('/api/regiones/19/')
    assert response.status_code == 404
    data = response.get_json()
    assert isinstance(data,dict)
    assert data['error'] == 'Región no encontrada'

def test_get_provincias_por_region(client):
    response = client.get('/api/regiones/15/provincias/')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data,list)
    assert data[0]['tipo'] == 'provincia'

def test_get_provincias_por_region_error_codigo(client):
    response = client.get('/api/regiones/150/provincias/')
    assert response.status_code == 400
    data = response.get_json()
    assert isinstance(data,dict)
    assert data['error'] == 'Código inválido'


def test_get_provincias(client):
    response = client.get('/api/provincias/')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert all('tipo' in provincia and provincia['tipo'] == 'provincia' for provincia in data)

def test_get_provincia(client):
    response = client.get('/api/provincias/136/')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data,dict)
    assert data['tipo'] == 'provincia' and data['nombre'] == 'Talagante'

def test_get_provincia_error_codigo(client):
    response = client.get('/api/provincias/02/')
    assert response.status_code == 400
    data = response.get_json()
    assert isinstance(data,dict)
    assert data['error'] == 'Código inválido'

def test_get_provincia_error_no_encontrada(client):
    response = client.get('/api/provincias/930/')
    assert response.status_code == 404
    data = response.get_json()
    assert isinstance(data,dict)
    assert data['error'] == 'Provincia no encontrada'

def test_get_comunas_por_provincia(client):
    response = client.get("/api/provincias/136/comunas/")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data,list)
    assert data[1]['tipo'] == "comuna" and data[1]["nombre"] == "El Monte"

def test_get_comunas_por_provincia_error_codigo(client):
    response = client.get('/api/provincias/02/comunas/')
    assert response.status_code == 400
    data = response.get_json()
    assert isinstance(data,dict)
    assert data['error'] == 'Código inválido'

def test_get_comunas_por_provincia_error_no_encontrada(client):
    response = client.get('/api/provincias/930/comunas/')
    assert response.status_code == 404
    data = response.get_json()
    assert isinstance(data,dict)
    assert data['error'] == 'Provincia no encontrada'

def test_get_comunas(client):
    response = client.get("/api/comunas/")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data,list)

def test_get_comuna(client):
    response = client.get('/api/comunas/13404/')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data,dict)
    assert data['tipo'] == 'comuna' and data['nombre'] == 'Paine'

def test_get_comuna_error_codigo(client):
    response = client.get('/api/comunas/02/')
    assert response.status_code == 400
    data = response.get_json()
    assert isinstance(data,dict)
    assert data['error'] == 'Código inválido'

def test_get_comuna_error_no_encontrada(client):
    response = client.get('/api/comunas/93002/')
    assert response.status_code == 404
    data = response.get_json()
    assert isinstance(data,dict)
    assert data['error'] == 'Comuna no encontrada'