from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from accounts.models.user import User
from django import forms


class CustomUserCreationForm(forms.Form):
    """
    Creates the user with the mode and email as the
    additional form.
    """
    username = forms.CharField(
        label='Enter Username', min_length=4, max_length=150)
    email = forms.EmailField(label='Enter email')
    mode = forms.IntegerField(label='Enter mode')
    password1 = forms.CharField(
        label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirm password', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)

        if r.count():
            raise ValidationError("Email already exists")
        return email

    def clean_mode(self):
        mode = self.cleaned_data['mode']
        if mode < 0 or mode > 3:
            raise ValidationError("Mode invalid.")
        return mode

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")

        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['mode'],
            self.cleaned_data['password1'],
        )
        return user
