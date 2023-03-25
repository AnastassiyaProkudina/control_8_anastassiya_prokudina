from django import forms
from django.contrib.auth import get_user_model


class LoginForm(forms.Form):
    username = forms.CharField(required=True, label="Логин")
    password = forms.CharField(
        required=True, label="Пароль", widget=forms.PasswordInput
    )


class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(
        label="Пароль", strip=False, required=True, widget=forms.PasswordInput
    )
    password_confirm = forms.CharField(
        label="Подтвердите пароль",
        strip=False,
        required=True,
        widget=forms.PasswordInput,
    )
    email = forms.EmailField(required=True, label="Email")

    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "first_name",
            "email",
            "password",
            "password_confirm",
        )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Пароли не совпадают!")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get("password"))
        # user.groups.add("user")
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ["first_name", "email"]
        labels = {"first_name": "Имя", "email": "Email"}
