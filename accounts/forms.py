from django.contrib.auth.forms import UserCreationForm as _UserForm


class UserCreationForm(_UserForm):

    class Meta(_UserForm.Meta):
        fields = ("username", "email")
