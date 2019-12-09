from rest_framework import serializers
from apps.models import AddressModel
import datetime, string, re
from django.utils import timezone
from drf_serializer_cache import SerializerCacheMixin

class AddressSerializer(SerializerCacheMixin, serializers.ModelSerializer):
    created_at = serializers.HiddenField(default=datetime.datetime.now(tz=timezone.utc))
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = AddressModel
        fields = ('id', 'first_name', 'last_name', 'phone', 'created_at')

    def validate_first_name(self, value):
        """Validate on first name field"""
        if not all(c in string.ascii_letters for c in value.lower().replace(" ", "")):
            raise serializers.ValidationError("First name is not valid, please enter again")
        return value

    def validate_last_name(self, value):
        """Validate on last name field"""
        if not all(c in string.ascii_letters for c in value.lower().replace(" ", "")):
            raise serializers.ValidationError("Last name is not valid, please enter again")
        return value

    def validate_phone(self, value):
        """Validate on phone field"""
        rule = re.compile(r'^(\+?\(61\)|\(\+?61\)|\+?61|\(0[1-9]\)|0[1-9])?( ?-?[0-9]){7,9}$')
        if rule.search(value.replace(" ", "")) is None:
            raise serializers.ValidationError("Phone number is not valid, please enter again")
        return value