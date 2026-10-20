from django import forms
from employees.models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        exclude = ['slug']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last name'
            }),
            'job_title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Job title'
            }),
            'email_address': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'email@domain.com'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '123456789'
            })
        }

        labels = {
            'first_name': 'First name',
            'last_name': 'Last name',

        }

        error_messages = {
            'first_name' : {
                'required': 'Please enter a valid first name'
            },
            'last_name': {
                'required': 'Please enter a valid last name'
            },

        }