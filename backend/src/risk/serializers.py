from rest_framework import serializers
from risk import models


class EnumValuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EnumValues
        fields = ('id', 'value')


class FieldTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FieldType
        fields = ('id', 'name')


class FieldSerializer(serializers.ModelSerializer):
    field_type_id = serializers.IntegerField()
    enum_values = EnumValuesSerializer(write_only=True,
                                       required=False, allow_null=True, many=True)

    class Meta:
        model = models.Field
        fields = ('id', 'label', 'field_type_id', 'enum_values')
        extra_kwargs = {'field_type_id': {
            'write_only'}}


class FieldReadSerializer(serializers.ModelSerializer):
    fieldType = FieldTypeSerializer()
    enum_values = EnumValuesSerializer(read_only=True, source='enumField',
                                       required=False, allow_null=True, many=True)

    class Meta:
        model = models.Field
        fields = ('id', 'label', 'fieldType', 'enum_values')


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
            enum_values_data = field_data.pop('enum_values', {})
            fieldType = models.FieldType.objects.get(
                pk=field_type_id)
            field = models.Field.objects.create(
                riskType=riskType, fieldType=fieldType, **field_data)
            # print(fieldType.name)
            if fieldType.name == "enum":
                print(field_data.keys())
                for enum_value in enum_values_data:
                    models.EnumValues.objects.create(
                        enumField=field, **enum_value)

        return riskType
