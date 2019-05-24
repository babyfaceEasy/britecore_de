from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import InsurerCreationForm, InsurerChangeForm
from .models import Insurer


class InsurerUserAdmin(UserAdmin):
    add_form = InsurerCreationForm
    form = InsurerChangeForm
    model = Insurer
    list_display = ['email',  'username', 'companyName']

# Register your models here.


admin.site.register(Insurer, InsurerUserAdmin)
