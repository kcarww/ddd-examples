from rest_framework import serializers

class CreateCustomerRequestSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255, allow_blank=False)
    street = serializers.CharField(max_length=255, allow_blank=False)
    city = serializers.CharField(max_length=255, allow_blank=False)
    state = serializers.CharField(max_length=255, allow_blank=False)
    zip_code = serializers.CharField(max_length=255, allow_blank=False)
    country = serializers.CharField(max_length=255, allow_blank=False)
    active = serializers.BooleanField(default=True)
    rewards_points = serializers.IntegerField(default=0)

class CreateCustomerResponseSerializer(serializers.Serializer):
    id = serializers.UUIDField()