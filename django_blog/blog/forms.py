from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Comment, Post
from django import forms
from taggit.forms import TagWidget


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commite = True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commite:
            user.save()
        return user




class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'tags': TagWidget(), 
        }

        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
