# -*- coding: utf-8 -*-
from django import forms
from .models import Details


class Detailsform(forms.ModelForm):
    class Meta:
        model=Details
        fields=['eid','ename','eemail','econtact']
