from django import forms
from .models import Profile
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        widgets = {
            'first_name' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : '이름'
                }
            ),

            'last_name' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : '이름'
                }
            ),
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('age', 'birth_date', 'self_introduce')
        widgets = {
            'age' : forms.NumberInput(
                attrs = {
                    'class' : 'form-control',
                }
            ),

            'birth_date' : forms.DateInput(
                attrs = {
                    'class' : 'form-control',
                    'type' : 'date',
                }
            ),

            'self_introduce' : forms.Textarea(
                attrs = {
                    'class' : 'form-control',
                }
            ),
        }