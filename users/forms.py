from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()

class RegisterForm(forms.ModelForm):
    """Registration form"""
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeed', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

    def clean_password2(self):
        if self.cleaned_data['password'] != self.cleaned_data['password2']:
            raise forms.ValidationError('Wrong password!')
        return self.cleaned_data['password2']