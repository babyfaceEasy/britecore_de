from django.db import models

# Create your models here.


class RiskType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True, max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class FieldType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Field(models.Model):
    label = models.CharField(max_length=255)
    value = models.TextField(blank=True, null=True)
    riskType = models.ForeignKey(
        RiskType, related_name='fields', on_delete=models.CASCADE)
    fieldType = models.ForeignKey(
        FieldType, related_name='fieldType', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.label


class EnumValues(models.Model):
    value = models.CharField(max_length=255)
    enumField = models.ForeignKey(
        Field, related_name="enumField", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
