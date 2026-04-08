from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()

class RegisterForm(forms.ModelForm):
    """Registration form"""
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'password1',
            'placeholder': 'Password',
        })
    )

    password2 = forms.CharField(
        label='Repead',
        widget=forms.PasswordInput(attrs={
            'class': 'password2',
            'placeholder': 'Repeat Password',
        })
    )

    class Meta:
        model = User
        fields = ['username']

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'username',
                'placeholder': "Username"
            }),
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Wrong Password!')

        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])

        if commit:
            user.save()

        return user