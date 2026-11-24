from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Note, UserProfile

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content', 'color']
        widgets = {
            'color': forms.TextInput(attrs={'type': 'color', 'class': 'form-control form-control-color'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Note title...'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your note...', 'rows': 5}),
        }

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email address'}))
    profile_picture = forms.ImageField(required=True, widget=forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'profile_picture']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm Password'})