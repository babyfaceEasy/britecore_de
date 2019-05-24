from rest_framework import serializers
from .models import Insurer


class InsurerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurer
        fields = ('email', 'username',)
