from django import forms
from .models import Person

class Contactform(forms.Form):
    contact_name = forms.CharField(label = "Enter your name", required = True)
    contact_email = forms.EmailField(label = "Enter your E-mail", required = True)
    contact_text = forms.CharField(label = "Enter your Message here", required = True, widget = forms.Textarea)


class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = ['name', 'gender', 'email', 'birthday', 'photo', 'desc',]