from django import forms

from .models import Subscribe

# This form is for the subscribe option
class SubscribeForm(forms.ModelForm):
    first_name = forms.TextInput()
    last_name = forms.TextInput()
    email = forms.EmailInput()

    class Meta:
        model = Subscribe
        fields = ('first_name', 'last_name', 'email')

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'})  
        }