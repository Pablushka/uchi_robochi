import pytest
from .factories import RaspberryFactory, UserFactory

@pytest.mark.django_db(transaction=True)
def test_get_raspberry(django_client):
    response = django_client.get('/pi_commander/raspberry/')
    assert response.status_code == 200


@pytest.mark.django_db(transaction=True)
def test_get_raspberry_count(django_client):
    # u1 = UserFactory()
    r1= RaspberryFactory()
    r2 =RaspberryFactory(name='rasp4')
    response = django_client.get('/pi_commander/raspberry/')
    breakpoint()
    assert len(response.json()) == 2

# TODO: hacer el test de usuario repetido/ usuario con 2 raspb con el mismo nombre, crear mil millones de raspberries