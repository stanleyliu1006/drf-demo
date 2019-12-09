from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
import pytest
from django.conf import settings

pytestmark = pytest.mark.django_db

@pytest.fixture
def client(request):
    return APIClient()

class TestRoot:

  def test_get_request(self, client):
    response = client.get( reverse(settings.VERSION+':root') )
    assert response.status_code == 200

class TestHealthz:

  def test_get_request(self, client):
    response = client.get( reverse(settings.VERSION+':healthz') )
    assert response.status_code == 200