from cProfile import label
from django import forms
from django.forms import TextInput, EmailInput
from phonenumber_field.formfields import PhoneNumberField


class UserInfoForm(forms.Form):
    name = forms.CharField(label='Ism/Имя',
        widget=forms.TextInput(
        attrs={
            'placeholder': 'Jamshid',
            'style': 'width: 300px; height: 30px;  border-radius: 5px; font-size: 18px;  margin-bottom: 20px; padding-left: 10px; padding-right: 10px;'
        }))
    
    phone_number = PhoneNumberField(
        label='Telefon raqam/Телефон номер:',
        widget=forms.TextInput(attrs={
            'type':'tel', 
            'pattern':'+998[0-9]{2}[0-9]{3}[0-9]{2}[0-9]{2}', 
            'value':'+998', 
            'style': 'width: 300px; height: 30px;  border-radius: 5px; font-size: 18px; margin-bottom: 30px; padding-left: 10px; padding-right: 10px;'}))
