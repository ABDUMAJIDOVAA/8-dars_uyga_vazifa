from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Post, Category



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'category', 'published')

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Maxsulot nomi",
                'style': 'margin-top: 10px;'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Maxsulot matni',
                'style': 'margin-top: 10px;'
            }),
            'category': forms.Select(attrs={
                'class': 'form-select',
                'style': 'margin-top: 10px;'
            }),
            'published': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'style': 'margin-top: 10px;',
                'id': 'test'
            })
        }



class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title',)



class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))



class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Parol'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Parolni takrorlang'
    }))

    class Meta:
        model = User
        fields = ('username', 'email')

