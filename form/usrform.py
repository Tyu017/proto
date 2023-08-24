from django import forms
from django.forms import ModelForm
from .models import form



class usrform(ModelForm):
    class Meta:
        model = form
        fields = ('name','number','email','destination','budget','description')
        labels ={
            'name': 'Full Name*',
            'number':'Telephone*',
            'email':'Email*',
            'destination':'Choice of Destination*',
            'budget':'Trip Budget*',
            'description':'Add a Message',
        

        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':''}),
            'number':forms.TextInput(attrs={'class':'form-control','placeholder':''}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'','id':'exampleFormControlInput1'}),
            'destination':forms.TextInput(attrs={'class':'form-control','placeholder':''}),
            'budget':forms.TextInput(attrs={'class':'form-control','placeholder':''}),
            'description':forms.Textarea(attrs={'class':'form-control big','placeholder':''}),
        }