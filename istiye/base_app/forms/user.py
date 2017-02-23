__author__ = 'Hakan Uyumaz'

import datetime

import pytz
from django import forms

from ..models import User
from ..utils import generate_token


class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'surname', 'email', 'password', ]

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.activation_key = generate_token()
        user.activation_expire_date = datetime.datetime.now(pytz.utc) + datetime.timedelta(2)
        user.is_active = False
        user.last_login = datetime.datetime.now(pytz.utc)
        if commit:
            user.save()
        return user