from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Insurer


class InsurerCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Insurer
        fields = ('username', 'email')


class InsurerChangeForm(UserChangeForm):

    class Meta:
        model = Insurer
        fields = UserChangeForm.Meta.fields
