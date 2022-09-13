from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from .models import Test, Hint, Link, Tutorial
from django.contrib.auth.models import User


class AddQuestionForm(ModelForm):
    class Meta:
        model = Test
        fields = "__all__"


class AddHintForm(ModelForm):
    class Meta:
        model = Hint
        fields = "__all__"


class AddLinkForm(ModelForm):
    class Meta:
        model = Link
        fields = "__all__"


class AddTutorialForm(ModelForm):
    class Meta:
        model = Tutorial
        fields = "__all__"


class NewUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=101)
    last_name = forms.CharField(max_length=101)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

