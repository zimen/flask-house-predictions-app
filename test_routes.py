import pytest
from application import app

@pytest.fixture
def form_test():
    return {
        'Year_Built': 2015,
        'Total_Bsmt_SF': 50,
        'Frst_Flr_SF': 50,
        'Gr_Liv_Area': 50,
        'Garage_Area': 50,
        'Overall_Qual': 50,
        'Full_Bath': 4,
        'Exter_Qual': 'Ex',
        'Kitchen_Qual': 'TA',
        'Neighborhood': 'NAmes'
    }
    
@pytest.fixture
def client():
    app.config.update({'TESTING': True})
    with app.test_client() as client:
        yield client
        
def test_home(client):
    response = client.get('/')
    print(response.data)
    assert response.status_code == 200
    assert "Welcome" in str(response.data)
    
def test_login( client):
    response = client.get('/login')
    assert response.status_code == 200
    
def test_auth(client):
    response = client.post('/login', json={'email': 'ayoub1@gmail.com', 'password': '1234'}, follow_redirects=True)
    assert response.status_code == 200

def test_index(client):
    response = client.get('/predictions/', follow_redirects=True)
    assert response.status_code == 200
    assert "Prediction" in str(response.data)
    
def test_prediction(form_test: dict, client):
    response = client.post('/predictions/predict', data=form_test, follow_redirects=True)
    print(response.__dict__)
    print(response.data)
    assert response.status_code == 200
    assert " $" in str(response.data)
    
