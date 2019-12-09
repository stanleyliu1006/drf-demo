from apps.models import AddressModel
from apps.serializers import AddressSerializer
from rest_framework.test import APIClient
from rest_framework import status, serializers
from django.urls import reverse
from django.forms.models import model_to_dict
import pytest, json, datetime
from django.conf import settings

pytestmark = pytest.mark.django_db

@pytest.fixture
def serializer(request):
  return AddressSerializer

@pytest.fixture
def client(request):
    return APIClient()

@pytest.fixture
def address(request):
    address =  AddressModel.objects.create(
     first_name="Stanley",
     last_name="Liu",
     phone="0425 266 866")
    return address

class TestAddress:

  def test_return_instance(self,address):
    assert isinstance(address, AddressModel)
    assert address.__str__() == "{}".format(address.first_name+" "+address.last_name)

  def test_get_request(self, client):
    response = client.get( reverse(settings.VERSION+':addressList') )
    assert response.status_code == 200

  def test_post_request(self, client):
    success_data = {'first_name' : 'Jason', 'last_name': 'Piere', 'phone': '0426 781 881'}
    response = client.post( reverse(settings.VERSION+':addressList'), success_data)
    assert response.status_code == 201

    failed_data = {'middle_name' : 'Jason', 'last_name': 'Piere', 'mobile': '0426 781 881'}
    response = client.post( reverse(settings.VERSION+':addressList'), failed_data)
    assert response.status_code == 400

  def test_get_single_request(self, client, address):
    response = client.get(
            reverse(settings.VERSION+':addressDetail', kwargs={'pk': address.id}),
            format="json")
    result = json.loads(response.content)

    assert response.status_code == status.HTTP_200_OK
    origin_addr = model_to_dict(address)
    del origin_addr['created_at']

    assert result == origin_addr

  def test_delete_single_request(self, client, address):
    response = client.delete(
            reverse(settings.VERSION+':addressDetail',kwargs={'pk': address.id}),
            format="json")

    assert response.status_code == status.HTTP_204_NO_CONTENT

class TestAddressSerializers:

  def test_validation(self, serializer):
    with pytest.raises(serializers.ValidationError):
      assert serializer.validate_first_name(self, "34323")

    with pytest.raises(serializers.ValidationError):
      assert serializer.validate_last_name(self, "34323")

    with pytest.raises(serializers.ValidationError):
      assert serializer.validate_phone(self, "xyzuio")
