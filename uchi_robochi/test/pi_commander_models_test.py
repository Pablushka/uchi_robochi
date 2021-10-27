import pytest
from . import factories
from pi_commander import models


@pytest.mark.django_db(transaction=True)
def test_create_raspberry():
    factories.RaspberryFactory()
    assert models.Raspberry.objects.count() is 1
