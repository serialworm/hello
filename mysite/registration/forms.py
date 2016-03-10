from django.forms import ModelForm
from registration.models import User


class RegistrationForm(ModelForm):
    error_css_class = 'has-error'

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'address1',
            'address2',
            'city',
            'state',
            'zipcode',
            'country',
        ]
