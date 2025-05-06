from django.forms import ModelForm
from .models import Booktable
from django import forms



class Booktableform (ModelForm):
    class Meta:
        model = Booktable
        fields = ['name', 'email', 'phone', 'date', 'time', 'guests', 'message']
        labels = {
            'name': '',
            'email': '',
            'phone': '',
            'date': '',
            'time': '',
            'guests': '',
            'message': '',
        }
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Name',
        'required': 'required'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email',
        'required': 'required'
    }))
    phone = forms.CharField(max_length=15, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Mobile',
        'required': 'required'
    }))
    date = forms.DateField(widget=forms.DateInput(attrs={
        'class': 'form-control datetimepicker-input mb-3 mb-sm-0',
        'placeholder': 'Date',
        'data-toggle': 'datetimepicker',
        'data-target': '#date'
        
    }))
    time = forms.TimeField(widget=forms.TextInput(attrs={
        'class': 'form-control datetimepicker-input',
        'placeholder': 'Time',
        'data-toggle': 'datetimepicker',
        'data-target': '#time'
    }))
    guests = forms.ChoiceField(choices=[(str(i), f"{i} Guest") for i in range(1, 11)], widget=forms.Select(attrs={
        'class': 'custom-select form-control'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Message',
        'style':"height: 100px",
        'rows': 4 ,
        'cols': 20
        
    }))
   
    
        