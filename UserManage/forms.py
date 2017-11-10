from django import forms
from .models import M_USER

class UserForm(forms.ModelForm):

    class Meta:
        model = M_USER
        fields = ('user_name', 'is_active')
        widgets = {
            'user_name': forms.TextInput(attrs={'size': 40}),
            'is_active': forms.CheckboxInput(attrs={'default': True})
        }
