from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from users.models import User
from django import forms
# User = get_user_model()


# class UserCreationForm(UserCreationForm):
# class Meta(UserCreationForm.Meta):
# model = User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView, FormView


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
        'class': 'input', 'placeholder': 'Введите email'}), max_length=60)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input', 'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input', 'placeholder': 'Повторите пароль'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')


# class SomeView(FormView):
#
#     def get_form_kwargs(self):
#         kwargs = super(SomeView, self).get_form_kwargs()
#         kwargs['request'] = self.request
#         return kwargs

class UserProfileForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={ 'id': 'file-input'}), required=False)
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input2'}), max_length=30)
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input2', 'readonly': True}), max_length=30)
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'input2', 'readonly': True}), max_length=60)
    about_user = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'input3', 'resizable': 'false'}), max_length=255)

    class Meta:
        model = User
        fields = ('first_name', 'username', 'email', 'about_user', 'image')

    # def __init__(self, *args, **kwargs):
    #     self.request = kwargs.pop("intanse")
    #     super(UserProfileForm, self).__init__(*args, **kwargs)
    #     user = kwargs.pop('data')
    #     print(user)
    #     print(user['username'])
    #     self.username = user['username']
    #     self.first_name = user['first_name']
    #     self.email = user['email']
    #     self.about_user = user['about_user']
    #     self.password = user['csrfmiddlewaretoken']
