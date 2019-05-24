from rest_framework import serializers
from risk import models


class FieldTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FieldType
        fields = ('id', 'name')


class FieldSerializer(serializers.ModelSerializer):
    field_type_id = serializers.IntegerField()

    class Meta:
        model = models.Field
        fields = ('id', 'label', 'value', 'field_type_id')
        extra_kwargs = {'field_type_id': {
            'write_only'}}


class FieldReadSerializer(serializers.ModelSerializer):
    fieldType = FieldTypeSerializer()

    class Meta:
        model = models.Field
        fields = ('id', 'label', 'value', 'fieldType')


class RiskTypeSerializer(serializers.ModelSerializer):
    fields = FieldReadSerializer(many=True, read_only=True)
    fields_write = FieldSerializer(many=True, write_only=True)

    class Meta:
        model = models.RiskType
        fields = ('id', 'name', 'description', 'fields', 'fields_write')

    def create(self, validated_data):
        fields_data = validated_data.pop('fields_write')
        riskType = models.RiskType.objects.create(**validated_data)
        for field_data in fields_data:
            field_type_id = field_data.pop('field_type_id')
            fieldType = models.FieldType.objects.get(
                pk=field_type_id)
            models.Field.objects.create(
                riskType=riskType, fieldType=fieldType, **field_data)
        return riskType
