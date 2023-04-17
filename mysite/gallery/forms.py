from django import forms
from .models import Post, Images


class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=400)

    class Meta:
        model = Post
        fields = ('title',)


class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')

    class Meta:
        model = Images
        fields = ('image',)

