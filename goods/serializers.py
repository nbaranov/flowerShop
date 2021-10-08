from rest_framework import serializers


class ProductListCustomerSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    count = serializers.IntegerField()

    class Meta:
        read_only_fields = ["id", "title", "count"]
