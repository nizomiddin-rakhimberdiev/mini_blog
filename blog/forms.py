from django import forms
from .models import CustomUser, Blog, Comment


class RegisterForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'password')


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'phone')


class CreateBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'image')


class EditBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'image')


class EditCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)