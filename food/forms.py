from django.forms import ModelForm
from .models import Booktable

class Booktableform (ModelForm):
    class Meta:
        model = Booktable
        fields = ['name', 'email', 'phone', 'date', 'time', 'guests', 'message']
        