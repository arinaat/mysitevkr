from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from users.models import User
from django import forms
#User = get_user_model()


#class UserCreationForm(UserCreationForm):
    #class Meta(UserCreationForm.Meta):
        #model = User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView




class UserLoginForm(forms.ModelForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'input', 'placeholder': 'Введите почту'}), max_length=60)
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input', 'placeholder': 'Введите пароль'}))

    class Meta:
        model = User
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Неверный пароль")


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input', 'placeholder': 'Введите логин'}), max_length=30)
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'input', 'placeholder': 'Введите email'}),  max_length=60)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input', 'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input', 'placeholder': 'Повторите пароль'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserProfileForm(UserCreationForm):
    image = forms.ImageField(widget=forms.FileInput())
    first_name = forms.CharField(max_length=30)
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input', 'placeholder': 'Введите логин'}), max_length=30)
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'input', 'placeholder': 'Введите email'}),  max_length=60)
    about_user = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ('image', 'first_name', 'username', 'email', 'about_user')


