from django import forms
from .models import Post
from .models import connect
from .models import relation
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm




class PostForm(forms.ModelForm):



    class Meta:
            model=Post
            fields=['post','privacy',]


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)


    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.is_superuser = True

        if commit:
            user.save()
        return user


class connectform(forms.ModelForm):



    class Meta:
                model=connect
                fields=['user1']

class relationform(forms.ModelForm):


    class Meta:
                model=relation
                fields=['flag']
