from rest_framework import serializers

class ItemSerializer(serializers.Serializer):
    farmid = serializers.IntegerField()
    friutid = serializers.IntegerField()
    quantity = serializers.IntegerField()

    