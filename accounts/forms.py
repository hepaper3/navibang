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

        fields = ('age', 'birth_date', 'gender', 'self_introduce', 'profile_img')

        GENDER_CHOICES=(
            ('female', '여자'),
            ('male', '남자')
        )

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

            'gender' : forms.Select(
                attrs = {
                    'class' : 'form-control',
                    'choices' : 'GENDER_CHOCIES',
                }
            ),

            'self_introduce' : forms.Textarea(
                attrs = {
                    'class' : 'form-control',
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['profile_img'].required = False
